#!/usr/bin/env python3
"""
Lily Pi — Enki AI Bridge
=========================
Lightweight client for communicating with the Enki AI engine.

Enki AI repo: https://github.com/Cassai2026/Enki

Supports:
  • Text / voice prompt queries
  • Multimodal vision queries (image + prompt)
  • Offline / fallback mode
  • Automatic retry with exponential back-off

Compatible with: Raspberry Pi 4/5, NVIDIA Jetson Nano/Orin
Python   : 3.9+
License  : AGPL-3.0
"""

from __future__ import annotations

import base64
import logging
import os
import time
from typing import Optional

import requests

log = logging.getLogger("lily-pi.enki-bridge")

# ---------------------------------------------------------------------------
# Defaults (override via environment variables)
# ---------------------------------------------------------------------------
DEFAULT_API_URL: str = os.getenv("ENKI_API_URL", "http://localhost:8080")
DEFAULT_TIMEOUT: int = int(os.getenv("ENKI_TIMEOUT", "5"))          # seconds
DEFAULT_MAX_RETRIES: int = int(os.getenv("ENKI_MAX_RETRIES", "3"))
DEFAULT_MODEL: str = os.getenv("ENKI_MODEL", "enki-base")


class EnkiBridgeError(Exception):
    """Raised when the Enki AI bridge encounters an unrecoverable error."""


class EnkiBridge:
    """
    Bridge between Lily Pi and the Enki AI engine.

    Parameters
    ----------
    api_url:
        Base URL of the Enki AI server (e.g. ``http://localhost:8080``).
    api_key:
        Optional API key for authentication (set ``ENKI_API_KEY`` env var).
    model:
        Enki model identifier to use for inference.
    timeout:
        HTTP request timeout in seconds.
    max_retries:
        Maximum number of retry attempts on transient failures.
    offline_fallback:
        Message to return when Enki is unreachable (instead of raising).

    Examples
    --------
    >>> bridge = EnkiBridge()
    >>> response = bridge.query("What hazards should I watch for at 60 km/h?")
    >>> print(response)
    """

    def __init__(
        self,
        api_url: str = DEFAULT_API_URL,
        api_key: Optional[str] = None,
        model: str = DEFAULT_MODEL,
        timeout: int = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        offline_fallback: Optional[str] = "[Enki offline]",
    ) -> None:
        self._api_url = api_url.rstrip("/")
        self._api_key = api_key or os.getenv("ENKI_API_KEY", "")
        self._model = model
        self._timeout = timeout
        self._max_retries = max_retries
        self._offline_fallback = offline_fallback

        self._session = requests.Session()
        if self._api_key:
            self._session.headers.update({"Authorization": f"Bearer {self._api_key}"})
        self._session.headers.update({"Content-Type": "application/json"})

        log.info("EnkiBridge initialised → %s (model=%s)", self._api_url, self._model)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def query(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Send a text prompt to Enki AI and return the response string.

        Parameters
        ----------
        prompt:
            The user / system prompt to send.
        context:
            Optional additional context prepended to the prompt.

        Returns
        -------
        str
            The AI-generated response text, or the offline fallback message.
        """
        full_prompt = f"{context}\n\n{prompt}" if context else prompt
        payload = {
            "model": self._model,
            "prompt": full_prompt,
            "stream": False,
        }
        response = self._post("/api/generate", payload)
        return response.get("response", "").strip()

    def vision_query(
        self,
        image_bytes: bytes,
        prompt: str,
        context: Optional[str] = None,
    ) -> str:
        """
        Send an image + text prompt to Enki AI for multimodal inference.

        Parameters
        ----------
        image_bytes:
            Raw image bytes (JPEG or PNG).
        prompt:
            Text prompt describing the vision task.
        context:
            Optional additional context.

        Returns
        -------
        str
            AI-generated description / answer.
        """
        full_prompt = f"{context}\n\n{prompt}" if context else prompt
        image_b64 = base64.b64encode(image_bytes).decode("utf-8")
        payload = {
            "model": self._model,
            "prompt": full_prompt,
            "images": [image_b64],
            "stream": False,
        }
        response = self._post("/api/generate", payload)
        return response.get("response", "").strip()

    def health_check(self) -> bool:
        """Return True if the Enki AI server is reachable."""
        try:
            resp = self._session.get(
                f"{self._api_url}/api/tags",
                timeout=self._timeout,
            )
            return resp.status_code == 200
        except requests.RequestException:
            return False

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _post(self, endpoint: str, payload: dict) -> dict:
        """POST *payload* to *endpoint* with retry / fallback logic."""
        url = f"{self._api_url}{endpoint}"
        last_exc: Optional[Exception] = None

        for attempt in range(1, self._max_retries + 1):
            try:
                resp = self._session.post(url, json=payload, timeout=self._timeout)
                resp.raise_for_status()
                return resp.json()
            except requests.RequestException as exc:
                last_exc = exc
                wait = 2 ** (attempt - 1)  # 1 s, 2 s, 4 s …
                log.warning(
                    "Enki request failed (attempt %d/%d): %s — retrying in %ds",
                    attempt,
                    self._max_retries,
                    exc,
                    wait,
                )
                time.sleep(wait)

        # All retries exhausted
        if self._offline_fallback is not None:
            log.error("Enki unreachable after %d retries — using fallback.", self._max_retries)
            return {"response": self._offline_fallback}

        raise EnkiBridgeError(
            f"Enki AI unreachable at {url} after {self._max_retries} retries."
        ) from last_exc


# ---------------------------------------------------------------------------
# Quick CLI test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys

    logging.basicConfig(level=logging.DEBUG)

    bridge = EnkiBridge()
    if not bridge.health_check():
        print("⚠️  Enki AI server not reachable — running with offline fallback.")

    test_prompt = " ".join(sys.argv[1:]) or "Hello from Lily Pi! What hazards should I watch for?"
    print("Prompt :", test_prompt)
    print("Response:", bridge.query(test_prompt))
