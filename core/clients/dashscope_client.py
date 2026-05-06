#!/usr/bin/env python3
"""
core/clients/dashscope_client.py
=================================
DashScope API client for Qwen models (Alibaba Cloud).

Uses the DashScope OpenAI-compatible endpoint to call Qwen models.
Supports text generation and vision (multimodal) models.
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

logger = logging.getLogger(__name__)

DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"


class DashScopeClient:
    """Client for DashScope API (Qwen models via Alibaba Cloud).

    Parameters
    ----------
    api_key:
        DashScope API key. If None, reads from DASHSCOPE_API_KEY env var.
    base_url:
        API base URL. Defaults to DashScope OpenAI-compatible endpoint.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
    ):
        self.api_key = api_key or os.environ.get("DASHSCOPE_API_KEY", "")
        self.base_url = (base_url or DASHSCOPE_BASE_URL).rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

    def _check_api_key(self) -> None:
        if not self.api_key:
            raise ValueError(
                "DashScope API key not set. "
                "Provide it via constructor or DASHSCOPE_API_KEY env var."
            )

    def generate(
        self,
        model: str,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.1,
        max_tokens: int = 4096,
        **kwargs: Any,
    ) -> str:
        """Generate text using a Qwen model.

        Parameters
        ----------
        model:
            Model name (e.g., "qwen-plus", "qwen-max", "qwen-turbo").
        prompt:
            User prompt text.
        system_prompt:
            Optional system message.
        temperature:
            Sampling temperature (lower = more deterministic).
        max_tokens:
            Maximum tokens in response.

        Returns
        -------
        str
            Generated text content.
        """
        self._check_api_key()

        messages: List[Dict[str, Any]] = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        payload: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            **kwargs,
        }

        url = f"{self.base_url}/chat/completions"
        response = self.session.post(url, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()

        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise ValueError(f"Empty response from DashScope model '{model}'")

        logger.info(
            "DashScope '%s': %d input tokens, %d output tokens",
            model,
            data.get("usage", {}).get("prompt_tokens", 0),
            data.get("usage", {}).get("completion_tokens", 0),
        )
        return content

    def vision(
        self,
        model: str,
        prompt: str,
        image_path: str | Path,
        system_prompt: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        """Analyze an image using a Qwen vision model.

        Parameters
        ----------
        model:
            Vision model name (e.g., "qwen-vl-plus", "qwen-vl-max").
        prompt:
            Text prompt describing what to analyze.
        image_path:
            Path to the image file.
        system_prompt:
            Optional system message.

        Returns
        -------
        str
            Generated description of the image.
        """
        self._check_api_key()

        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        # Encode image as base64 data URL
        import base64
        mime = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
        with open(image_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        data_url = f"data:{mime};base64,{b64}"

        messages: List[Dict[str, Any]] = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": data_url}},
                {"type": "text", "text": prompt},
            ],
        })

        payload: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "max_tokens": 2048,
            **kwargs,
        }

        url = f"{self.base_url}/chat/completions"
        response = self.session.post(url, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()

        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not content:
            raise ValueError(f"Empty response from DashScope vision model '{model}'")

        logger.info(
            "DashScope vision '%s': %d input tokens, %d output tokens",
            model,
            data.get("usage", {}).get("prompt_tokens", 0),
            data.get("usage", {}).get("completion_tokens", 0),
        )
        return content

    def check_connection(self) -> bool:
        """Verify that the API key is valid and the service is reachable.

        Returns
        -------
        bool
            True if connection is successful.
        """
        try:
            self._check_api_key()
            # Simple test call with minimal tokens
            self.generate(
                model="qwen-turbo",
                prompt="Respond with exactly: OK",
                max_tokens=10,
                temperature=0,
            )
            return True
        except Exception as exc:
            logger.error("DashScope connection check failed: %s", exc)
            return False

    def list_models(self) -> List[str]:
        """List available models (requires API key).

        Returns
        -------
        list
            List of model ID strings.
        """
        self._check_api_key()
        url = f"{self.base_url}/models"
        response = self.session.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        return [m.get("id", "") for m in data.get("data", [])]
