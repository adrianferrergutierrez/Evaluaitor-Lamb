#!/usr/bin/env python3
"""
core/clients/dashscope_client.py
=================================
DashScope API client for Qwen models (Alibaba Cloud).

Uses the DashScope OpenAI-compatible endpoint to call Qwen models.
Supports text generation and vision (multimodal) models.
"""

from __future__ import annotations

import json
import logging
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests

logger = logging.getLogger(__name__)

DASHSCOPE_ENDPOINTS = {
    "singapore": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
    "us": "https://dashscope-us.aliyuncs.com/compatible-mode/v1",
    "china": "https://dashscope.aliyuncs.com/compatible-mode/v1",
}

DEFAULT_MODEL = os.environ.get("DASHSCOPE_MODEL", "qwen3.5-plus")
DEFAULT_ENDPOINT = os.environ.get("DASHSCOPE_ENDPOINT", "singapore")

# Retry configuration for vision requests (addresses 400 errors in batch processing)
RETRY_CONFIG = {
    "max_retries": 3,
    "base_delay": 3.0,  # seconds (increased to handle rate limiting in batch processing)
    "max_delay": 60.0,  # seconds
    "backoff_factor": 2.0,  # exponential backoff multiplier
}
# Max payload size for vision requests (10 MB safety limit)
MAX_VISION_PAYLOAD_SIZE = 10 * 1024 * 1024


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
        region: Optional[str] = None,
    ):
        self.api_key = api_key or os.environ.get("DASHSCOPE_API_KEY", "")
        self.region = (region or os.environ.get("DASHSCOPE_REGION", "singapore")).lower()
        self.base_url = (
            base_url
            or DASHSCOPE_ENDPOINTS.get(self.region, DASHSCOPE_ENDPOINTS["singapore"])
        ).rstrip("/")
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

    def _post_with_retry(
        self,
        url: str,
        payload: Dict[str, Any],
        timeout: int = 120,
        max_retries: int = RETRY_CONFIG["max_retries"],
        base_delay: float = RETRY_CONFIG["base_delay"],
        max_delay: float = RETRY_CONFIG["max_delay"],
        backoff_factor: float = RETRY_CONFIG["backoff_factor"],
    ) -> requests.Response:
        """Send POST request with exponential backoff retry logic.
        
        Handles transient failures and rate limiting from DashScope API.
        
        Parameters
        ----------
        url : str
            API endpoint URL.
        payload : dict
            Request payload.
        timeout : int
            Request timeout in seconds.
        max_retries : int
            Maximum number of retry attempts.
        base_delay : float
            Initial delay in seconds before first retry.
        max_delay : float
            Maximum delay cap for retries.
        backoff_factor : float
            Multiplier for exponential backoff.
            
        Returns
        -------
        requests.Response
            Successful response object.
            
        Raises
        ------
        requests.exceptions.HTTPError
            If all retries exhausted or non-retryable error occurs.
        """
        payload_size = len(json.dumps(payload).encode("utf-8"))
        logger.debug(f"Payload size: {payload_size / 1024:.2f} KB")
        
        if payload_size > MAX_VISION_PAYLOAD_SIZE:
            raise ValueError(
                f"Payload size {payload_size / 1024 / 1024:.2f} MB exceeds limit "
                f"({MAX_VISION_PAYLOAD_SIZE / 1024 / 1024:.2f} MB). "
                "Image may be too large or corrupt."
            )
        
        delay = base_delay
        last_exception = None
        
        for attempt in range(max_retries + 1):
            try:
                # Create a new session for each request to avoid rate limit issues with persistent connections
                session = requests.Session()
                session.headers.update({
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                })
                response = session.post(url, json=payload, timeout=timeout)
                response.raise_for_status()
                
                if attempt > 0:
                    logger.info(f"Request succeeded after {attempt} retries")
                return response
                
            except requests.exceptions.HTTPError as e:
                last_exception = e
                error_code = e.response.status_code
                error_text = e.response.text  # Capture FULL error response
                
                # Determine if error is retryable
                retryable = error_code in (408, 429, 500, 502, 503, 504)
                
                if error_code == 400:
                    # 400 Bad Request - may be due to payload size/encoding issues
                    logger.error(
                        f"[Attempt {attempt + 1}/{max_retries + 1}] 400 Bad Request. "
                        f"Payload size: {payload_size / 1024:.2f} KB. "
                        f"Full API Response:\n{error_text}"
                    )
                    # Also log the request payload structure for debugging
                    logger.debug(f"Request payload keys: {list(payload.keys())}")
                    if 'messages' in payload:
                        logger.debug(f"Number of messages: {len(payload['messages'])}")
                        for i, msg in enumerate(payload['messages']):
                            logger.debug(f"Message {i} keys: {list(msg.keys())}")
                            if msg.get('content') and isinstance(msg['content'], list):
                                logger.debug(f"Message {i} content types: {[c.get('type') for c in msg['content']]}")
                    retryable = True  # Retry 400 as it might be transient
                elif error_code >= 500:
                    # 5xx errors are server-side, always retryable
                    logger.warning(
                        f"[Attempt {attempt + 1}/{max_retries + 1}] "
                        f"HTTP {error_code} (Server Error). "
                        f"Response: {error_text[:200]}"
                    )
                    retryable = True
                else:
                    logger.warning(
                        f"[Attempt {attempt + 1}/{max_retries + 1}] "
                        f"HTTP {error_code}: {error_text}"
                    )
                
                # Don't retry if this is the last attempt
                if attempt >= max_retries:
                    logger.error(f"Max retries ({max_retries}) exhausted. Raising error.")
                    raise
                
                # Don't retry if error is not retryable (unless it's a 400)
                if not retryable:
                    logger.error(f"Non-retryable error {error_code}. Not retrying.")
                    raise
                
                # Wait before retry with exponential backoff
                delay = min(max_delay, delay * backoff_factor)
                wait_time = delay + (0.1 * (attempt + 1))  # Add small jitter
                logger.info(
                    f"Retrying in {wait_time:.2f}s (attempt {attempt + 1}/{max_retries})"
                )
                time.sleep(wait_time)
                
            except requests.exceptions.Timeout as e:
                last_exception = e
                if attempt >= max_retries:
                    logger.error(f"Max retries ({max_retries}) exhausted. Timeout error.")
                    raise
                
                delay = min(max_delay, delay * backoff_factor)
                wait_time = delay + (0.1 * (attempt + 1))
                logger.warning(
                    f"Timeout on attempt {attempt + 1}/{max_retries}. "
                    f"Retrying in {wait_time:.2f}s"
                )
                time.sleep(wait_time)
                
            except requests.exceptions.RequestException as e:
                last_exception = e
                logger.error(f"Request failed: {e}")
                raise
        
        # This shouldn't be reached, but just in case
        if last_exception:
            raise last_exception
        raise RuntimeError("Unknown error in _post_with_retry")

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
        response = self._post_with_retry(url, payload, timeout=300, max_retries=2)
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
        
        Automatically compresses large images (>1 MB) to reduce payload size
        and avoid 400 errors.

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

        # Encode image as base64 data URL with validation
        import base64
        file_size = image_path.stat().st_size
        
        # Detect MIME type more accurately
        suffix = image_path.suffix.lower()
        mime = "image/png" if suffix == ".png" else "image/jpeg"
        
        logger.debug(f"Processing image: {image_path.name} ({file_size / 1024:.1f} KB), MIME: {mime}")
        
        # Compress large images to avoid 400 errors (try to import compress function)
        # This happens BEFORE encoding to base64
        try:
            from core.extraction.diagramlens_tool import compress_image_if_needed
            processed_path = compress_image_if_needed(image_path)
            if processed_path != image_path:
                logger.info(f"Image compressed for API call: {image_path.name}")
                image_path = processed_path
                file_size = image_path.stat().st_size
        except ImportError:
            logger.debug("Image compression not available (PIL not installed)")
        except Exception as e:
            logger.warning(f"Image compression failed, using original: {e}")
        
        # Warn if image is still very large (before encoding it gets bigger)
        if file_size > 2 * 1024 * 1024:  # 2MB
            logger.warning(
                f"Image {image_path.name} is still {file_size / 1024 / 1024:.1f} MB. "
                "This may cause 400 errors."
            )
        
        try:
            with open(image_path, "rb") as f:
                image_data = f.read()
                b64 = base64.b64encode(image_data).decode("utf-8")
        except Exception as e:
            logger.error(f"Failed to encode image {image_path.name}: {e}")
            raise ValueError(f"Cannot encode image: {e}")
        
        # DashScope format: Image as base64 embedded in message
        data_url = f"data:{mime};base64,{b64}"

        messages: List[Dict[str, Any]] = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        # Build multimodal message - DashScope expects specific format
        # Validate prompt is string and not None/empty
        if not prompt or not isinstance(prompt, str):
            logger.warning(f"Invalid prompt type: {type(prompt)}. Using default prompt.")
            prompt = "Describe this diagram in detail."
        
        # Sanitize prompt - remove any problematic characters
        prompt = prompt.strip()
        
        logger.debug(f"Prompt for image analysis: {prompt[:100]}...")
        logger.debug(f"Prompt type: {type(prompt).__name__}, length: {len(prompt)}")
        
        # DashScope OpenAI-compatible endpoint format for vision
        # The content field should be an array with text and image_url
        user_content = [
            {
                "type": "text",
                "text": prompt
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": data_url
                }
            }
        ]
        
        messages.append({
            "role": "user",
            "content": user_content,
        })

        payload: Dict[str, Any] = {
            "model": model,
            "messages": messages,
            "max_tokens": 2048,
            **kwargs,
        }

        url = f"{self.base_url}/chat/completions"
        # Vision requests get more retries due to batch processing challenges
        response = self._post_with_retry(url, payload, timeout=120, max_retries=3)
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
        
        # Add delay between vision requests to respect API rate limits during batch processing
        time.sleep(2)
        
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
