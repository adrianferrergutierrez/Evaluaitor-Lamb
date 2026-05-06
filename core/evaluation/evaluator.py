#!/usr/bin/env python3
"""
core/evaluation/evaluator.py
==============================
Full document evaluation using DashScope API and YAML rubric config.

Usage:
    python core/evaluation/evaluator.py \
        --document tests/test_arquitectura.md \
        --config configs/rubric_architecture.yaml \
        --output output/evaluacion.md
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

load_dotenv()

from core.clients.dashscope_client import DashScopeClient
from core.config.config_manager import ConfigManager
from core.grading.grader import GradingResult, RubricGrader, mean, weighted_score

logger = logging.getLogger(__name__)

PROMPTS_DIR = Path(__file__).parents[2] / "prompts"


def load_prompt(prompt_filename: str) -> str:
    """Load a prompt template from the prompts directory."""
    prompt_path = PROMPTS_DIR / prompt_filename
    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")
    return prompt_path.read_text(encoding="utf-8")


def extract_score(text: str) -> Optional[float]:
    """Extract a score (X/10) from evaluation text."""
    patterns = [
        r"\*\*Puntuaci[oó]n:\*\*\s*(\d+\.?\d*)/10",
        r"Puntuaci[oó]n:\s*(\d+\.?\d*)/10",
        r"Nota:\s*(\d+\.?\d*)/10",
        r"(\d+\.?\d*)\s*/\s*10",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            value = float(match.group(1))
            if 0 <= value <= 10:
                return value
    return None


def evaluate_criterion(
    client: DashScopeClient,
    model: str,
    prompt_template: str,
    document: str,
    criterion_name: str,
) -> str:
    """Evaluate a single criterion using the LLM."""
    prompt = prompt_template.replace("--{DOCUMENTO}--", document)

    logger.info("Evaluating criterion: %s", criterion_name)
    start = time.time()
    result = client.generate(
        model=model,
        prompt=prompt,
        temperature=0.1,
        max_tokens=4096,
    )
    elapsed = time.time() - start
    logger.info("Criterion %s evaluated in %.1fs", criterion_name, elapsed)

    return result


def generate_final_report(
    client: DashScopeClient,
    model: str,
    document_path: str,
    evaluations: Dict[str, str],
    grading_result: GradingResult,
) -> str:
    """Generate the final evaluation report."""
    prompt_template = load_prompt("4_1_generacion_informe.md")
    document = Path(document_path).read_text(encoding="utf-8")

    evals_summary = "\n\n".join(
        f"### {criterion}\n\n{text}" for criterion, text in evaluations.items()
    )

    prompt = prompt_template.replace("--{DOCUMENTO}--", document)
    prompt = prompt.replace("--{EVALUACIONES}--", evals_summary)
    prompt = prompt.replace(
        "--{NOTA_FINAL}--",
        f"Ponderada: {grading_result.weighted_final}/10, Media: {grading_result.mean_xbar}/10",
    )

    return client.generate(
        model=model,
        prompt=prompt,
        temperature=0.1,
        max_tokens=4096,
    )


def run_evaluation(
    document_path: str,
    config_path: str,
    output_dir: str,
) -> Dict[str, Any]:
    """Run the full evaluation pipeline."""
    # Load config
    manager = ConfigManager(config_path)
    cfg = manager.load()

    # Load document
    doc_path = Path(document_path)
    if not doc_path.exists():
        raise FileNotFoundError(f"Document not found: {doc_path}")
    document = doc_path.read_text(encoding="utf-8")

    # Setup client
    provider = cfg.provider
    client = DashScopeClient(region=provider.region if provider else "singapore")
    model = provider.text_model if provider else "qwen3.6-plus"

    # Setup output
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Evaluate each criterion
    evaluations: Dict[str, str] = {}
    scores: Dict[str, float] = {}

    print(f"\n{'='*60}")
    print(f"SE-Agentic-Evaluator v2.0")
    print(f"Documento: {doc_path.name}")
    print(f"Rúbrica: {cfg.id} - {cfg.description}")
    print(f"Modelo: {model}")
    print(f"{'='*60}\n")

    for criterion in cfg.criteria:
        print(f"[{len(evaluations)+1}/{len(cfg.criteria)}] Evaluando: {criterion.name}...")

        prompt_template = load_prompt(criterion.prompt)
        eval_text = evaluate_criterion(client, model, prompt_template, document, criterion.name)
        evaluations[criterion.id] = eval_text

        score = extract_score(eval_text)
        if score is not None:
            scores[criterion.id] = score
            print(f"  → Puntuación: {score}/10")
        else:
            print(f"  → ⚠️ No se pudo extraer puntuación (se asigna 0)")
            scores[criterion.id] = 0.0

        # Save individual evaluation
        eval_file = output_path / f"eval_{criterion.id}.md"
        eval_file.write_text(eval_text, encoding="utf-8")

    # Calculate final grade
    print(f"\n{'='*60}")
    print("Calculando nota final...")

    grader = RubricGrader(
        weights=cfg.weights,
        labels=cfg.labels,
        evaluated_file=doc_path.name,
    )
    grading = grader.grade({}, scores=scores)

    print(f"Nota ponderada: {grading.weighted_final}/10")
    print(f"Media (x̄): {grading.mean_xbar}")
    print(f"Nivel: {grading.performance_level}")
    print(f"{'='*60}\n")

    # Print rubric table
    print(grading.rubric_table_markdown())

    # Generate final report
    print("\nGenerando informe final...")
    final_report = generate_final_report(client, model, document_path, evaluations, grading)

    # Save outputs
    report_file = output_path / "evaluacion_final.md"
    report_file.write_text(final_report, encoding="utf-8")

    scores_file = output_path / "scores.json"
    scores_file.write_text(
        json.dumps(grading.as_dict(), ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n✅ Informe guardado en: {report_file}")
    print(f"✅ Puntuaciones guardadas en: {scores_file}")

    return grading.as_dict()


def main() -> None:
    parser = argparse.ArgumentParser(description="Full document evaluation with DashScope API.")
    parser.add_argument("--document", type=str, required=True, help="Path to document to evaluate")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML rubric config")
    parser.add_argument("--output", type=str, default="output/evaluation", help="Output directory")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_evaluation(args.document, args.config, args.output)


if __name__ == "__main__":
    main()
