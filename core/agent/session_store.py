"""
core/agent/session_store.py
============================
Session management for the Agent.

Stores conversation history as JSON files to allow multi-turn interactions
and stateless invocation (Turtle Pattern).
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class SessionStore:
    """Manages agent sessions stored as JSON files."""

    def __init__(self, store_dir: str = ".agent_sessions"):
        self.store_dir = Path(store_dir)
        self.store_dir.mkdir(parents=True, exist_ok=True)

    def _get_path(self, session_id: str) -> Path:
        return self.store_dir / f"{session_id}.json"

    def load(self, session_id: str) -> List[Dict[str, Any]]:
        """Load messages for a specific session."""
        path = self._get_path(session_id)
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save(self, session_id: str, messages: List[Dict[str, Any]]) -> None:
        """Persist messages for a specific session."""
        path = self._get_path(session_id)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        logger.debug(f"Session {session_id} saved to {path}")

    def list_sessions(self) -> List[str]:
        """List all available session IDs."""
        return [p.stem for p in self.store_dir.glob("*.json")]

    def delete(self, session_id: str) -> bool:
        """Delete a specific session."""
        path = self._get_path(session_id)
        if path.exists():
            path.unlink()
            return True
        return False
