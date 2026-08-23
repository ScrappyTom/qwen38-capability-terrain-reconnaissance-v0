from __future__ import annotations

import http.client
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

from .canonical import canonical_json_bytes, sha256_bytes, write_canonical_json


class ProviderError(RuntimeError):
    pass


def get_json(url: str, *, timeout: int = 30) -> dict[str, Any]:
    with urllib.request.urlopen(url, timeout=timeout) as response:
        value = json.loads(response.read())
    if not isinstance(value, dict):
        raise ProviderError(f"non-object response from {url}")
    return value


def post_json_custodied(
    base_url: str,
    endpoint: str,
    payload: dict[str, Any],
    custody_root: Path,
    *,
    timeout: int = 900,
) -> tuple[bytes, dict[str, Any], dict[str, Any]]:
    custody_root.mkdir(parents=True, exist_ok=False)
    request_bytes = canonical_json_bytes(payload)
    (custody_root / "request.body.json").write_bytes(request_bytes)
    response_path = custody_root / "response.body.bin"
    response_path.write_bytes(b"")
    parsed = urllib.parse.urlparse(base_url)
    connection = http.client.HTTPConnection(parsed.hostname, parsed.port, timeout=timeout)
    started = time.perf_counter()
    status: int | None = None
    error: str | None = None
    try:
        connection.request(
            "POST",
            endpoint,
            body=request_bytes,
            headers={"Content-Type": "application/json"},
        )
        response = connection.getresponse()
        status = response.status
        with response_path.open("ab") as handle:
            while True:
                chunk = response.read(65_536)
                if not chunk:
                    break
                handle.write(chunk)
                handle.flush()
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    finally:
        connection.close()
    elapsed = time.perf_counter() - started
    raw = response_path.read_bytes()
    receipt = {
        "schema_version": "provider-attempt-receipt-v0",
        "endpoint": endpoint,
        "request_bytes": len(request_bytes),
        "request_sha256": sha256_bytes(request_bytes),
        "response_status": status,
        "response_bytes": len(raw),
        "response_sha256": sha256_bytes(raw),
        "elapsed_seconds": elapsed,
        "error": error,
    }
    write_canonical_json(custody_root / "receipt.json", receipt)
    if error is not None:
        raise ProviderError(error)
    if status != 200:
        raise ProviderError(f"provider HTTP status {status}")
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ProviderError(f"provider returned invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ProviderError("provider returned non-object JSON")
    return raw, value, receipt


class LiveTokenizer:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def _post(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        request = urllib.request.Request(self.base_url + endpoint, data=body, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=180) as response:
            value = json.loads(response.read())
        if not isinstance(value, dict):
            raise ProviderError(f"non-object response from {endpoint}")
        return value

    def render(self, messages: list[dict[str, str]]) -> str:
        value = self._post(
            "/apply-template",
            {
                "messages": messages,
                "add_generation_prompt": True,
                "chat_template_kwargs": {"enable_thinking": False, "preserve_thinking": False},
            },
        )
        prompt = value.get("prompt")
        if not isinstance(prompt, str):
            raise ProviderError("/apply-template did not return prompt")
        return prompt

    def count_text(self, content: str) -> int:
        value = self._post("/tokenize", {"content": content, "add_special": False, "parse_special": True})
        tokens = value.get("tokens")
        if not isinstance(tokens, list) or not all(isinstance(item, int) for item in tokens):
            raise ProviderError("/tokenize did not return token IDs")
        return len(tokens)

    def count_messages(self, messages: list[dict[str, str]]) -> tuple[int, str]:
        prompt = self.render(messages)
        return self.count_text(prompt), prompt


def completion_payload(messages: list[dict[str, str]], *, profile: dict[str, Any]) -> dict[str, Any]:
    return {
        "model": profile["model_alias"],
        "messages": messages,
        "max_tokens": profile["completion_allowance_tokens"],
        "temperature": profile["temperature"],
        "top_p": profile["top_p"],
        "top_k": profile["top_k"],
        "min_p": profile["min_p"],
        "presence_penalty": profile["presence_penalty"],
        "repeat_penalty": profile["repeat_penalty"],
        "seed": profile["seed"],
        "stream": False,
        "chat_template_kwargs": {"enable_thinking": False, "preserve_thinking": False},
        "response_format": {"type": "json_object"},
    }


def extract_completion(value: dict[str, Any]) -> tuple[str, dict[str, Any], str | None]:
    choices = value.get("choices")
    if not isinstance(choices, list) or not choices or not isinstance(choices[0], dict):
        raise ProviderError("completion lacks choices")
    message = choices[0].get("message")
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str):
        raise ProviderError("completion lacks assistant content")
    usage = value.get("usage") if isinstance(value.get("usage"), dict) else {}
    return content, usage, choices[0].get("finish_reason")
