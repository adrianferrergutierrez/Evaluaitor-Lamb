"""
core/meta_agent/tool_catalog.py
================================
Catalog of available tools for the meta-agent workflow generator.

Delegates to core.tool_registry for tool definitions.
"""

from __future__ import annotations

from typing import Any, Dict, List

from core.tool_registry import registry


def get_tool_catalog() -> List[Dict[str, Any]]:
    """Return the full tool catalog from the registry."""
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "category": tool.category,
            "params": tool.params,
            "output": tool.output,
        }
        for tool in registry.list_all()
    ]


def get_tool_by_name(name: str) -> Dict[str, Any] | None:
    """Return a tool entry by name, or None if not found."""
    tool = registry.get(name)
    if tool:
        return {
            "name": tool.name,
            "description": tool.description,
            "category": tool.category,
            "params": tool.params,
            "output": tool.output,
        }
    return None


def get_tools_by_category(category: str) -> List[Dict[str, Any]]:
    """Return all tools in a given category."""
    return [
        {
            "name": tool.name,
            "description": tool.description,
            "category": tool.category,
            "params": tool.params,
            "output": tool.output,
        }
        for tool in registry.list_by_category(category)
    ]


def format_catalog_for_prompt() -> str:
    """Format the tool catalog as a Markdown string for LLM prompts."""
    lines = ["# Tool Catalog\n"]
    for tool in registry.list_all():
        lines.append(f"## {tool.name} ({tool.category})")
        lines.append(f"**Description:** {tool.description}")
        lines.append(f"**Params:**")
        for param, desc in tool.params.items():
            lines.append(f"  - `{param}`: {desc}")
        lines.append(f"**Output:**")
        for field, desc in tool.output.items():
            lines.append(f"  - `{field}`: {desc}")
        lines.append("")
    return "\n".join(lines)
