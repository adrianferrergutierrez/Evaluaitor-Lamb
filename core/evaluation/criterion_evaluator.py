#!/usr/bin/env python3
"""
core/evaluation/criterion_evaluator.py
========================================
Evaluate document criteria using LLM prompts from YAML rubric config.

This module handles the **evaluation phase** — it loads criteria from a
YAML rubric config, runs each criterion prompt against the document,
extracts scores, and saves individual eval_*.md files.

It accepts optional structured context (from extraction/analysis phases)
to inject into the evaluation prompts via --{CONTEXTO}--.

Usage:
    # Criteria-only mode (document + YAML → eval_*.md + scores.json)
    python core/evaluation/criterion_evaluator.py \
        --document tests/test_arquitectura.md \
        --config configs/rubric_architecture.yaml \
        --output output/evaluacion_arquitectura/

    # With pre-built analysis context
    python core/evaluation/criterion_evaluator.py \
        --document tests/test_arquitectura.md \
        --config configs/rubric_architecture.yaml \
        --output output/evaluacion_arquitectura/ \
        --context output/analysis_context.md
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

load_dotenv()

from core.clients.dashscope_client import DashScopeClient
from core.config.config_manager import ConfigManager, CriterionConfig
from core.extraction.objectives import extract_objectives, parse_objective_ids
from core.extraction.requirements import extract_requirements, parse_requirement_ids
from core.extraction.use_cases import extract_use_cases, parse_use_case_ids
from core.analysis.orphans import detect_orphans
from core.analysis.smart import evaluate_objectives_smart, smart_summary_markdown
from core.analysis.iso25010 import classify_requirements_iso25010

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


def extract_detailed_scores(text: str) -> Dict[str, float]:
    """Extract per-sub-criterion scores from a markdown table."""
    scores: Dict[str, float] = {}
    table_pattern = re.compile(
        r"\|\s*(.+?)\s*\|.*?\|\s*(\d+\.?\d*)\s*/\s*10\s*\|"
    )
    for match in table_pattern.finditer(text):
        name = match.group(1).strip()
        value = float(match.group(2))
        if 0 <= value <= 10:
            scores[name] = value
    return scores


def find_images_in_document(document: str, doc_path: Path) -> List[Path]:
    """Extract image paths referenced in the markdown document."""
    img_refs = re.findall(r"!\[.*?\]\((.*?)\)", document)
    images: List[Path] = []
    for ref in img_refs:
        img_path = Path(ref)
        if not img_path.is_absolute():
            img_path = doc_path.parent / img_path
        if img_path.exists():
            images.append(img_path)
    return images


# ---------------------------------------------------------------------------
# Criterion evaluation
# ---------------------------------------------------------------------------

def evaluate_criterion(
    client: DashScopeClient,
    model: str,
    vision_model: str,
    prompt_template: str,
    document: str,
    doc_path: Path,
    criterion: CriterionConfig,
    options: Any,
    context_str: Optional[str] = None,
) -> str:
    """Evaluate a single criterion using the LLM, with optional vision and context."""
    prompt = prompt_template.replace("--{DOCUMENTO}--", document)

    # Inject analysis context
    if context_str:
        prompt = prompt.replace("--{CONTEXTO}--", context_str)
    else:
        prompt = prompt.replace("--{CONTEXTO}--", "No hay análisis previo disponible. Evalúa basándote únicamente en el documento.")

    # Inject vision if required
    if options.multimodal and criterion.requires_vision:
        images = find_images_in_document(document, doc_path)
        if images:
            img_descriptions = []
            for img in images:
                logger.info("Analyzing image with vision model: %s", img.name)
                desc = client.vision(
                    model=vision_model,
                    prompt="Describe this diagram in detail for software architecture evaluation.",
                    image_path=str(img),
                )
                img_descriptions.append(f"### {img.name}\n\n{desc}")
            images_text = "\n\n".join(img_descriptions)
            prompt = prompt.replace("--{IMAGENES}--", images_text)
        else:
            prompt = prompt.replace("--{IMAGENES}--", "No hay imágenes disponibles para este criterio.")
    else:
        prompt = prompt.replace("--{IMAGENES}--", "")

    logger.info("Evaluating criterion: %s", criterion.name)
    start = time.time()
    result = client.generate(
        model=model,
        prompt=prompt,
        temperature=0.1,
        max_tokens=4096,
    )
    elapsed = time.time() - start
    logger.info("Criterion %s evaluated in %.1fs", criterion.name, elapsed)

    return result


def build_context(
    document: str,
    client: DashScopeClient,
    model: str = "qwen3.6-plus",
) -> str:
    """Run full extraction + analysis pipeline and return context Markdown.

    Executes: objectives extraction, requirements extraction, use-case
    extraction, orphan detection, SMART evaluation, and ISO 25010
    classification.

    Parameters
    ----------
    document:
        Full Markdown document content.
    client:
        DashScopeClient instance for LLM calls.
    model:
        Model name to use for extractions.

    Returns
    -------
    str
        Markdown-formatted analysis context.
    """
    logger.info("Running full extraction pipeline...")

    objectives_md = extract_objectives(document, client=client, model=model)
    logger.info("Objectives extracted: %d chars", len(objectives_md))

    requirements_md = extract_requirements(document, client=client, model=model)
    logger.info("Requirements extracted: %d chars", len(requirements_md))

    use_cases_md = extract_use_cases(document, client=client, model=model)
    logger.info("Use cases extracted: %d chars", len(use_cases_md))

    orphans = detect_orphans(objectives_md, requirements_md)
    orphans_md = orphans.as_markdown()

    smart_scores = evaluate_objectives_smart(objectives_md)
    smart_md = smart_summary_markdown(smart_scores)

    iso_report = classify_requirements_iso25010(requirements_md)
    iso_md = iso_report.as_markdown()

    context_parts = [
        "### Objetivos Extraídos",
        objectives_md,
        "### Requisitos Extraídos",
        requirements_md,
        "### Casos de Uso Extraídos",
        use_cases_md,
        "### Detección de Huérfanos",
        orphans_md,
        "### Evaluación SMART",
        smart_md,
        "### Clasificación ISO/IEC 25010",
        iso_md,
    ]
    return "\n\n".join(context_parts)


def run_criterion_evaluation(
    document_path: str,
    config_path: str,
    output_dir: str,
    context_path: Optional[str] = None,
    full: bool = False,
) -> Dict[str, Any]:
    """Evaluate all criteria from a rubric config.

    Parameters
    ----------
    document_path:
        Path to the document to evaluate.
    config_path:
        Path to YAML rubric configuration.
    output_dir:
        Directory to write eval_*.md and scores.json.
    context_path:
        Optional path to a Markdown file containing analysis context
        (objectives, requirements, orphans, SMART, ISO 25010).
    full:
        If True, run the full extraction + analysis pipeline to build
        context automatically before evaluating criteria.

    Returns
    -------
    dict with scores, detailed_scores, and evaluation file paths.
    """
    manager = ConfigManager(config_path)
    cfg = manager.load()

    doc_path = Path(document_path)
    if not doc_path.exists():
        raise FileNotFoundError(f"Document not found: {doc_path}")
    document = doc_path.read_text(encoding="utf-8")

    client = DashScopeClient(region=cfg.provider.region if cfg.provider else "singapore")
    model = cfg.provider.text_model if cfg.provider else "qwen3.6-plus"
    vision_model = cfg.provider.vision_model if cfg.provider else "qwen-vl-max"

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    context_str = None
    if full:
        context_str = build_context(document, client, model)
        ctx_file = output_path / "analysis_context.md"
        ctx_file.write_text(context_str, encoding="utf-8")
        logger.info("Analysis context built and saved to %s", ctx_file)
    elif context_path:
        ctx_path = Path(context_path)
        if ctx_path.exists():
            context_str = ctx_path.read_text(encoding="utf-8")
            logger.info("Loaded analysis context from %s", context_path)
        else:
            logger.warning("Context file not found: %s", context_path)

    evaluations: Dict[str, str] = {}
    scores: Dict[str, float] = {}
    detailed_scores: Dict[str, Dict[str, float]] = {}

    print(f"\n{'='*60}")
    print(f"SE-Agentic-Evaluator v2.0 — Criterion Evaluation")
    print(f"Documento: {doc_path.name}")
    print(f"Rúbrica: {cfg.id} - {cfg.description}")
    print(f"Modelo: {model}")
    print(f"Criterios: {len(cfg.criteria)}")
    if full:
        print(f"Contexto: ✅ Generado automáticamente (--full)")
    elif context_str:
        print(f"Contexto: ✅ Inyectado desde {context_path}")
    else:
        print(f"Contexto: ❌ Sin análisis previo")
    print(f"{'='*60}\n")

    for criterion in cfg.criteria:
        print(f"[{len(evaluations)+1}/{len(cfg.criteria)}] Evaluando: {criterion.name}...")

        prompt_template = load_prompt(criterion.prompt)
        eval_text = evaluate_criterion(
            client, model, vision_model, prompt_template, document, doc_path,
            criterion, cfg.options, context_str
        )
        evaluations[criterion.id] = eval_text

        score = extract_score(eval_text)
        if score is not None:
            scores[criterion.id] = score
            print(f"  → Puntuación: {score}/10")
        else:
            print(f"  → ⚠️ No se pudo extraer puntuación (se asigna 0)")
            scores[criterion.id] = 0.0

        if cfg.options.detailed_scoring:
            sub_scores = extract_detailed_scores(eval_text)
            if sub_scores:
                detailed_scores[criterion.id] = sub_scores
                print(f"  → Sub-criterios: {', '.join(f'{k}={v}' for k, v in sub_scores.items())}")

        eval_file = output_path / f"eval_{criterion.id}.md"
        eval_file.write_text(eval_text, encoding="utf-8")

    scores_data = {"scores": scores}
    if detailed_scores:
        scores_data["detailed"] = detailed_scores

    scores_file = output_path / "scores.json"
    scores_file.write_text(
        json.dumps(scores_data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"\n✅ Evaluaciones guardadas en: {output_path}/")
    print(f"✅ Puntuaciones guardadas en: {scores_file}")

    return scores_data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Evaluate document criteria using YAML rubric config."
    )
    parser.add_argument("--document", type=str, required=True, help="Path to document to evaluate")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML rubric config")
    parser.add_argument("--output", type=str, required=True, help="Output directory for eval_*.md files")
    parser.add_argument(
        "--context", type=str, default=None,
        help="Path to a Markdown file with pre-built analysis context (objectives, orphans, SMART, etc.)"
    )
    parser.add_argument(
        "--full", action="store_true",
        help="Run full extraction + analysis pipeline before evaluating criteria"
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_criterion_evaluation(args.document, args.config, args.output, args.context, args.full)


if __name__ == "__main__":
    main()
