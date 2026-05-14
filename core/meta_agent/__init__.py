"""
core/meta_agent
================
Meta-agent components for dynamic workflow generation and execution.
"""

from core.meta_agent.tool_catalog import get_tool_catalog, get_tool_by_name
from core.meta_agent.workflow_generator import generate_workflow

__all__ = [
    "get_tool_catalog",
    "get_tool_by_name",
    "generate_workflow",
]
