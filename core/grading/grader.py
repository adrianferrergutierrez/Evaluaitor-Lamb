#!/usr/bin/env python3
"""
Deterministic grader.

Objetivo:
- Evitar errores por alucinación en agregaciones numéricas.
- Calcular media \bar{x} y una nota final ponderada (si hay pesos).

Uso:
  python core/grading/grader.py --scores 7 8.5 9
  python core/grading/grader.py --criteria-json core/grading/example_criteria.json

Salida:
- JSON por stdout con media y (si aplica) nota ponderada.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import List, Optional, Dict, Any


def mean(values: List[float]) -> float:
    if not values:
        raise ValueError("No scores provided")
    return sum(values) / len(values)


def weighted_score(items: List[Dict[str, Any]]) -> float:
    """
    items: [{ "name": str, "score": float, "weight": float }, ...]
    weights can sum to 1.0 or 100. We normalize.
    """
    if not items:
        raise ValueError("No criteria items provided")

    total_w = sum(float(i["weight"]) for i in items)
    if total_w <= 0:
        raise ValueError("Total weight must be > 0")

    return sum(float(i["score"]) * (float(i["weight"]) / total_w) for i in items)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scores", nargs="*", type=float, help="Raw scores to average")
    parser.add_argument("--criteria-json", type=str, help="Path to criteria JSON with scores and weights")
    args = parser.parse_args()

    result: Dict[str, Any] = {}

    if args.scores is not None and len(args.scores) > 0:
        result["mean_xbar"] = mean(args.scores)

    if args.criteria_json:
        with open(args.criteria_json, "r", encoding="utf-8") as f:
            payload = json.load(f)
        items = payload.get("criteria", [])
        result["weighted_final"] = weighted_score(items)

    if not result:
        raise SystemExit("Provide --scores or --criteria-json")

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
