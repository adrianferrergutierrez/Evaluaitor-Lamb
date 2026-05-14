"""
core/meta_agent/tool_catalog.py
================================
Catalog of available tools for the meta-agent workflow generator.

Each tool entry defines:
- name: Unique identifier used in workflow JSON
- description: Human-readable description
- params: Expected parameters with types and descriptions
- output: Expected output fields
- category: Tool category (extract, analyze, evaluate, etc.)
"""

from __future__ import annotations

from typing import Any, Dict, List

TOOL_CATALOG: List[Dict[str, Any]] = [
    {
        "name": "docx_extract",
        "description": "Convert a DOCX document to Markdown with image extraction",
        "category": "extract",
        "params": {
            "input": "Path to the DOCX file",
            "output_dir": "Directory to write contents.md and img/"
        },
        "output": {
            "contents_md": "Path to the generated Markdown file",
            "images": "Number of images extracted"
        }
    },
    {
        "name": "rubric_importer",
        "description": "Import a Markdown rubric table into YAML config and prompts",
        "category": "config",
        "params": {
            "input": "Path to the rubric Markdown file",
            "output": "Path to write the YAML config"
        },
        "output": {
            "config_path": "Path to the generated YAML config"
        }
    },
    {
        "name": "extract_objectives",
        "description": "Extract project objectives (OBJ-X) from a document using LLM",
        "category": "extract",
        "params": {
            "document": "Path to the Markdown document"
        },
        "output": {
            "markdown": "Structured Markdown with extracted objectives"
        }
    },
    {
        "name": "extract_requirements",
        "description": "Extract information requirements (IRQ) and non-functional requirements (NFR) from a document using LLM",
        "category": "extract",
        "params": {
            "document": "Path to the Markdown document"
        },
        "output": {
            "markdown": "Structured Markdown with extracted IRQ and NFR"
        }
    },
    {
        "name": "extract_use_cases",
        "description": "Extract use cases (CU-XXX) from a document using LLM",
        "category": "extract",
        "params": {
            "document": "Path to the Markdown document"
        },
        "output": {
            "markdown": "Structured Markdown with extracted use cases"
        }
    },
    {
        "name": "detect_orphans",
        "description": "Detect orphan requirements and objectives (deterministic, no LLM)",
        "category": "analyze",
        "params": {
            "objectives_md": "Structured Markdown with objectives",
            "requirements_md": "Structured Markdown with requirements"
        },
        "output": {
            "markdown": "Orphan detection report in Markdown"
        }
    },
    {
        "name": "evaluate_smart",
        "description": "Evaluate objectives against SMART criteria (heuristic, no LLM)",
        "category": "analyze",
        "params": {
            "objectives_md": "Structured Markdown with objectives"
        },
        "output": {
            "markdown": "SMART evaluation report in Markdown"
        }
    },
    {
        "name": "classify_iso25010",
        "description": "Classify NFRs against ISO/IEC 25010 quality characteristics (deterministic, no LLM)",
        "category": "analyze",
        "params": {
            "requirements_md": "Structured Markdown with requirements"
        },
        "output": {
            "markdown": "ISO 25010 classification report in Markdown"
        }
    },
    {
        "name": "build_context",
        "description": "Build a consolidated analysis context from extraction and analysis results",
        "category": "analyze",
        "params": {
            "objectives_md": "Structured Markdown with objectives",
            "requirements_md": "Structured Markdown with requirements",
            "use_cases_md": "Structured Markdown with use cases",
            "orphans_report": "Orphan detection report",
            "smart_report": "SMART evaluation report",
            "iso_report": "ISO 25010 classification report"
        },
        "output": {
            "markdown": "Consolidated analysis context in Markdown"
        }
    },
    {
        "name": "criterion_evaluator",
        "description": "Evaluate document criteria against a rubric config using LLM. Supports --full mode for automatic context generation",
        "category": "evaluate",
        "params": {
            "document": "Path to the Markdown document",
            "config": "Path to the YAML rubric config",
            "full": "Boolean: run full extraction + analysis before evaluation",
            "context": "Optional path to pre-built analysis context",
            "output_dir": "Directory to write eval_*.md and scores.json"
        },
        "output": {
            "scores": "Dict of criterion_id -> score",
            "output_dir": "Path to the evaluation output directory"
        }
    },
    {
        "name": "grader",
        "description": "Calculate weighted final grade from scores (deterministic, no LLM)",
        "category": "grade",
        "params": {
            "scores": "Dict of criterion_id -> score",
            "config": "Path to the YAML rubric config"
        },
        "output": {
            "weighted_final": "Final weighted grade (0-10)",
            "mean_xbar": "Arithmetic mean of scores",
            "performance_level": "Performance label (Excelente/Bueno/Aceptable/Insuficiente)"
        }
    },
    {
        "name": "report_generator",
        "description": "Generate a consolidated evaluation report from pre-computed evaluations",
        "category": "report",
        "params": {
            "document": "Path to the original Markdown document",
            "eval_dir": "Directory containing eval_*.md files",
            "config": "Path to the YAML rubric config",
            "scores": "Dict of criterion_id -> score",
            "output": "Path to write the final report"
        },
        "output": {
            "report_path": "Path to the generated final report"
        }
    }
]


def get_tool_catalog() -> List[Dict[str, Any]]:
    """Return the full tool catalog."""
    return TOOL_CATALOG


def get_tool_by_name(name: str) -> Dict[str, Any] | None:
    """Return a tool entry by name, or None if not found."""
    for tool in TOOL_CATALOG:
        if tool["name"] == name:
            return tool
    return None


def get_tools_by_category(category: str) -> List[Dict[str, Any]]:
    """Return all tools in a given category."""
    return [t for t in TOOL_CATALOG if t["category"] == category]


def format_catalog_for_prompt() -> str:
    """Format the tool catalog as a Markdown string for LLM prompts."""
    lines = ["# Tool Catalog\n"]
    for tool in TOOL_CATALOG:
        lines.append(f"## {tool['name']} ({tool['category']})")
        lines.append(f"**Description:** {tool['description']}")
        lines.append(f"**Params:**")
        for param, desc in tool["params"].items():
            lines.append(f"  - `{param}`: {desc}")
        lines.append(f"**Output:**")
        for field, desc in tool["output"].items():
            lines.append(f"  - `{field}`: {desc}")
        lines.append("")
    return "\n".join(lines)
