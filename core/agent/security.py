"""
core/agent/security.py
=======================
Security scaffolding for the Agent.

Implements the "Allow-list" pattern described in the methodology.
Security decisions are made here, NEVER in the prompt.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Set

logger = logging.getLogger(__name__)


class SecurityPolicy:
    """Defines which tools are allowed and under what conditions."""

    def __init__(self, allowed_tools: Set[str] | None = None):
        # By default, allow all registered tools. 
        # In production, this would be a strict subset.
        self.allowed_tools = allowed_tools or set()
        self._blocked_tools: Set[str] = set()

    def allow(self, tool_name: str) -> None:
        """Explicitly allow a tool."""
        self.allowed_tools.add(tool_name)
        self._blocked_tools.discard(tool_name)
        logger.debug(f"Tool '{tool_name}' explicitly allowed.")

    def block(self, tool_name: str) -> None:
        """Explicitly block a tool."""
        self._blocked_tools.add(tool_name)
        self.allowed_tools.discard(tool_name)
        logger.warning(f"Tool '{tool_name}' explicitly blocked.")

    def check(self, tool_name: str, arguments: Dict[str, Any]) -> None:
        """
        Check if a tool call is allowed.
        
        Raises PermissionError if the tool is not allowed.
        This is the "Gatekeeper" of the agent loop.
        """
        if tool_name in self._blocked_tools:
            raise PermissionError(f"Tool '{tool_name}' is blocked by security policy.")
        
        if self.allowed_tools and tool_name not in self.allowed_tools:
            raise PermissionError(
                f"Tool '{tool_name}' is not in the allow-list. "
                f"Allowed: {self.allowed_tools}"
            )
        
        # Additional checks could go here:
        # - Argument validation (e.g., prevent path traversal)
        # - Rate limiting
        # - Resource quotas
        
        logger.debug(f"Security check passed for tool '{tool_name}'.")
