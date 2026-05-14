#!/usr/bin/env python3
"""
core/tool_registry.py
======================
Central registry for all evaluation tools.

Provides a unified interface for tool discovery and execution.
Tools are registered with their metadata (params, outputs, description)
and an executor function.

Usage:
    from core.tool_registry import registry
    tool = registry.get("docx_extract")
    result = tool.execute(input="...", output_dir="...")
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

logger = logging.getLogger(__name__)


class Tool(ABC):
    """Abstract base class for evaluation tools."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Unique tool identifier."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description."""
        pass

    @property
    @abstractmethod
    def category(self) -> str:
        """Tool category (extract, analyze, evaluate, etc.)."""
        pass

    @property
    @abstractmethod
    def params(self) -> Dict[str, str]:
        """Expected parameters with descriptions."""
        pass

    @property
    @abstractmethod
    def output(self) -> Dict[str, str]:
        """Expected output fields with descriptions."""
        pass

    @abstractmethod
    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """Execute the tool with given parameters."""
        pass

    def __repr__(self) -> str:
        return f"<Tool {self.name} ({self.category})>"


class ToolRegistry:
    """Registry for evaluation tools."""

    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        """Register a tool."""
        self._tools[tool.name] = tool
        logger.info("Registered tool: %s", tool.name)

    def get(self, name: str) -> Optional[Tool]:
        """Get a tool by name."""
        return self._tools.get(name)

    def list_all(self) -> List[Tool]:
        """List all registered tools."""
        return list(self._tools.values())

    def list_by_category(self, category: str) -> List[Tool]:
        """List tools by category."""
        return [t for t in self._tools.values() if t.category == category]

    def execute(self, name: str, **kwargs: Any) -> Dict[str, Any]:
        """Execute a tool by name."""
        tool = self.get(name)
        if not tool:
            raise ValueError(f"Tool '{name}' not found in registry")
        return tool.execute(**kwargs)


# Global registry instance
registry = ToolRegistry()


# ---------------------------------------------------------------------------
# Concrete Tool Implementations
# ---------------------------------------------------------------------------

class DocxExtractTool(Tool):
    @property
    def name(self) -> str: return "docx_extract"
    @property
    def description(self) -> str: return "Convert DOCX to Markdown with image extraction"
    @property
    def category(self) -> str: return "extract"
    @property
    def params(self) -> Dict[str, str]: return {"input": "DOCX path", "output_dir": "Output dir"}
    @property
    def output(self) -> Dict[str, str]: return {"contents_md": "Markdown path", "images": "Image count"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.extraction.docx_extract import extract_docx
        result = extract_docx(kwargs["input"], kwargs["output_dir"])
        return {"result": result}


class RubricImporterTool(Tool):
    @property
    def name(self) -> str: return "rubric_importer"
    @property
    def description(self) -> str: return "Import Markdown rubric to YAML config"
    @property
    def category(self) -> str: return "config"
    @property
    def params(self) -> Dict[str, str]: return {"input": "Rubric MD path", "output": "YAML config path"}
    @property
    def output(self) -> Dict[str, str]: return {"config_path": "YAML path"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.config.rubric_importer import import_rubric
        input_path = kwargs["input"]
        output_path = kwargs["output"]
        prompts_dir = str(Path(output_path).parent / "prompts")
        import_rubric(input_path, output_path, prompts_dir)
        # Fix prompt paths
        import yaml
        with open(output_path) as f:
            cfg = yaml.safe_load(f)
        rubric_id = Path(output_path).stem.replace("rubric_", "").replace("rubrica_", "")
        for criterion in cfg["rubric"]["criteria"]:
            criterion["prompt"] = f"{rubric_id}/" + criterion["prompt"]
        with open(output_path, "w") as f:
            yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True)
        return {"result": {"config_path": output_path}}


class ExtractObjectivesTool(Tool):
    @property
    def name(self) -> str: return "extract_objectives"
    @property
    def description(self) -> str: return "Extract objectives (OBJ-X) via LLM"
    @property
    def category(self) -> str: return "extract"
    @property
    def params(self) -> Dict[str, str]: return {"document": "Markdown path"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "Extracted objectives MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.extraction.objectives import extract_objectives
        from core.clients.dashscope_client import DashScopeClient
        doc = Path(kwargs["document"]).read_text(encoding="utf-8")
        result = extract_objectives(doc, client=DashScopeClient())
        return {"result": {"markdown": result}}


class ExtractRequirementsTool(Tool):
    @property
    def name(self) -> str: return "extract_requirements"
    @property
    def description(self) -> str: return "Extract IRQ/NFR via LLM"
    @property
    def category(self) -> str: return "extract"
    @property
    def params(self) -> Dict[str, str]: return {"document": "Markdown path"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "Extracted requirements MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.extraction.requirements import extract_requirements
        from core.clients.dashscope_client import DashScopeClient
        doc = Path(kwargs["document"]).read_text(encoding="utf-8")
        result = extract_requirements(doc, client=DashScopeClient())
        return {"result": {"markdown": result}}


class ExtractUseCasesTool(Tool):
    @property
    def name(self) -> str: return "extract_use_cases"
    @property
    def description(self) -> str: return "Extract use cases (CU-XXX) via LLM"
    @property
    def category(self) -> str: return "extract"
    @property
    def params(self) -> Dict[str, str]: return {"document": "Markdown path"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "Extracted use cases MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.extraction.use_cases import extract_use_cases
        from core.clients.dashscope_client import DashScopeClient
        doc = Path(kwargs["document"]).read_text(encoding="utf-8")
        result = extract_use_cases(doc, client=DashScopeClient())
        return {"result": {"markdown": result}}


class DetectOrphansTool(Tool):
    @property
    def name(self) -> str: return "detect_orphans"
    @property
    def description(self) -> str: return "Detect orphan requirements/objectives"
    @property
    def category(self) -> str: return "analyze"
    @property
    def params(self) -> Dict[str, str]: return {"objectives_md": "Objectives MD", "requirements_md": "Requirements MD"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "Orphan report MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.analysis.orphans import detect_orphans
        report = detect_orphans(kwargs["objectives_md"], kwargs["requirements_md"])
        return {"result": {"markdown": report.as_markdown()}}


class EvaluateSmartTool(Tool):
    @property
    def name(self) -> str: return "evaluate_smart"
    @property
    def description(self) -> str: return "Evaluate objectives against SMART criteria"
    @property
    def category(self) -> str: return "analyze"
    @property
    def params(self) -> Dict[str, str]: return {"objectives_md": "Objectives MD"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "SMART report MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.analysis.smart import evaluate_objectives_smart, smart_summary_markdown
        scores = evaluate_objectives_smart(kwargs["objectives_md"])
        return {"result": {"markdown": smart_summary_markdown(scores)}}


class ClassifyIso25010Tool(Tool):
    @property
    def name(self) -> str: return "classify_iso25010"
    @property
    def description(self) -> str: return "Classify NFRs against ISO 25010"
    @property
    def category(self) -> str: return "analyze"
    @property
    def params(self) -> Dict[str, str]: return {"requirements_md": "Requirements MD"}
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "ISO 25010 report MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.analysis.iso25010 import classify_requirements_iso25010
        report = classify_requirements_iso25010(kwargs["requirements_md"])
        return {"result": {"markdown": report.as_markdown()}}


class BuildContextTool(Tool):
    @property
    def name(self) -> str: return "build_context"
    @property
    def description(self) -> str: return "Build consolidated analysis context"
    @property
    def category(self) -> str: return "analyze"
    @property
    def params(self) -> Dict[str, str]: return {
        "objectives_md": "Objectives MD",
        "requirements_md": "Requirements MD",
        "use_cases_md": "Use cases MD",
        "orphans_report": "Orphans report",
        "smart_report": "SMART report",
        "iso_report": "ISO report"
    }
    @property
    def output(self) -> Dict[str, str]: return {"markdown": "Context MD"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        parts = []
        for key, val in kwargs.items():
            if val and Path(val).exists():
                parts.append(f"### {key}\n\n{Path(val).read_text(encoding='utf-8')}")
            elif val:
                parts.append(f"### {key}\n\n{val}")
        return {"result": {"markdown": "\n\n".join(parts)}}


class CriterionEvaluatorTool(Tool):
    @property
    def name(self) -> str: return "criterion_evaluator"
    @property
    def description(self) -> str: return "Evaluate criteria against rubric via LLM"
    @property
    def category(self) -> str: return "evaluate"
    @property
    def params(self) -> Dict[str, str]: return {
        "document": "Markdown path",
        "config": "YAML config path",
        "full": "Boolean: run full analysis",
        "context": "Optional context path",
        "output_dir": "Output dir"
    }
    @property
    def output(self) -> Dict[str, str]: return {"scores": "Scores dict", "output_dir": "Output dir"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.evaluation.criterion_evaluator import run_criterion_evaluation
        eval_params = {
            "document_path": kwargs["document"],
            "config_path": kwargs["config"],
            "output_dir": kwargs["output_dir"],
        }
        if kwargs.get("context"):
            eval_params["context_path"] = kwargs["context"]
        elif kwargs.get("full"):
            eval_params["full"] = True
        result = run_criterion_evaluation(**eval_params)
        return {"result": {"scores": result["scores"], "output_dir": kwargs["output_dir"]}}


class GraderTool(Tool):
    @property
    def name(self) -> str: return "grader"
    @property
    def description(self) -> str: return "Calculate weighted final grade"
    @property
    def category(self) -> str: return "grade"
    @property
    def params(self) -> Dict[str, str]: return {"scores": "Scores dict", "config": "YAML config path"}
    @property
    def output(self) -> Dict[str, str]: return {
        "weighted_final": "Final grade",
        "mean_xbar": "Mean score",
        "performance_level": "Performance label"
    }

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.grading.grader import RubricGrader
        grader = RubricGrader.from_config(kwargs["config"])
        grading = grader.grade({}, scores=kwargs["scores"])
        return {"result": grading.as_dict()}


class ReportGeneratorTool(Tool):
    @property
    def name(self) -> str: return "report_generator"
    @property
    def description(self) -> str: return "Generate final evaluation report"
    @property
    def category(self) -> str: return "report"
    @property
    def params(self) -> Dict[str, str]: return {
        "document": "Markdown path",
        "eval_dir": "Eval dir",
        "config": "YAML config path",
        "scores": "Scores path or dict",
        "output": "Report output path"
    }
    @property
    def output(self) -> Dict[str, str]: return {"report_path": "Report path"}

    def execute(self, **kwargs: Any) -> Dict[str, Any]:
        from core.evaluation.evaluator import run_report_generation
        run_report_generation(
            document_path=kwargs["document"],
            eval_dir=kwargs["eval_dir"],
            config_path=kwargs["config"],
            scores_path=kwargs.get("scores"),
            output_dir=str(Path(kwargs["output"]).parent),
        )
        return {"result": {"report_path": kwargs["output"]}}


# ---------------------------------------------------------------------------
# Auto-registration
# ---------------------------------------------------------------------------

def register_all_tools() -> None:
    """Register all built-in tools."""
    tools = [
        DocxExtractTool(),
        RubricImporterTool(),
        ExtractObjectivesTool(),
        ExtractRequirementsTool(),
        ExtractUseCasesTool(),
        DetectOrphansTool(),
        EvaluateSmartTool(),
        ClassifyIso25010Tool(),
        BuildContextTool(),
        CriterionEvaluatorTool(),
        GraderTool(),
        ReportGeneratorTool(),
    ]
    for tool in tools:
        registry.register(tool)


# Register tools on module import
register_all_tools()
