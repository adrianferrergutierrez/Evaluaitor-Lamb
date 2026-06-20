"""
core/clients/base.py
=================================
Abstract Base Class and common types for LLM Clients.
"""

from __future__ import annotations

import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

@dataclass
class ToolCall:
    """Represents a tool call requested by the LLM."""
    id: str
    name: str
    arguments: Dict[str, Any]

@dataclass
class ChatResponse:
    """Structured response from the LLM."""
    content: str
    tool_calls: List[ToolCall] = field(default_factory=list)

    def assistant_turn(self) -> Dict[str, Any]:
        """Format the response as an assistant message for the history."""
        msg = {"role": "assistant", "content": self.content}
        if self.tool_calls:
            msg["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {"name": tc.name, "arguments": json.dumps(tc.arguments)},
                }
                for tc in self.tool_calls
            ]
        return msg

class BaseLLMClient(ABC):
    """Abstract Base Class for LLM Clients."""
    
    @abstractmethod
    def chat(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        system: Optional[str] = None,
        model: str = "",
        temperature: float = 0.1,
        max_tokens: int = 4096,
    ) -> ChatResponse:
        """Chat with the LLM supporting function calling."""
        pass

    @abstractmethod
    def generate(
        self,
        model: str = "",
        prompt: str = "",
        system_prompt: Optional[str] = None,
        temperature: float = 0.1,
        max_tokens: int = 4096,
        **kwargs: Any,
    ) -> str:
        """Generate text using the LLM."""
        pass

    @abstractmethod
    def vision(
        self,
        model: str = "",
        prompt: str = "",
        image_path: Optional[str | Path] = None,
        system_prompt: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        """Analyze an image using a vision model."""
        pass

    @abstractmethod
    def check_connection(self) -> bool:
        """Verify API key and connectivity."""
        pass
