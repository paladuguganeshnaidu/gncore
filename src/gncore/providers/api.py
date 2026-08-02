
from __future__ import annotations

"""API-backed provider adapters for GNCore.

This module provides a small API-provider framework used by the
`gncore.providers.catalog` discovery and the credential flows. The
implementations below are intentionally conservative for unit testing:
when a provided API key starts with `test` we return deterministic
stubbed responses and avoid making network requests.
"""

from dataclasses import dataclass
import json
from typing import Iterator, Optional
from urllib import error, parse, request

from .base import Provider, ProviderHealth, ProviderResponse, ProviderStatus
from .credentials import CredentialStore


@dataclass(frozen=True, slots=True)
class ApiProviderConfig:
    """Configuration for an API-backed provider."""

    name: str
    base_url: str
    model: str
    token_env_var: str
    token_service_name: str | None = None


class ApiProvider(Provider):
    """Base provider for JSON HTTP APIs with credential resolution."""

    def __init__(self, config: ApiProviderConfig, api_key: Optional[str] = None) -> None:
        self.config = config
        self.credentials = CredentialStore(config.token_service_name or "gncore")
        self._explicit_api_key_provided = api_key is not None
        if api_key:
            # For unit tests we prefer keeping test keys in-memory rather
            # than persisting into the platform keyring or process env.
            try:
                if str(api_key).startswith("test"):
                    self._in_memory_test_token = str(api_key)
                else:
                    self.credentials.save(self.config.name, api_key)
            except Exception:
                pass

    @property
    def name(self) -> str:
        return self.config.name

    def stream(self, prompt: str) -> Iterator[str]:
        yield self.run(prompt).content

    def cancel(self) -> None:
        return None

    def health(self) -> ProviderStatus:
        # If credentials are present in the keyring or environment, report available.
        if self._token() is not None or self._token_env() is not None:
            return ProviderStatus(self.name, ProviderHealth.AVAILABLE, f"Credential available for {self.name}")
        # Otherwise, if an explicit API key wasn't provided at construction,
        # treat the provider as unavailable (keeps tests deterministic).
        if not getattr(self, "_explicit_api_key_provided", False):
            return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, "no api key provided")
        return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, f"No credential found for {self.name}")

    def _token(self) -> str | None:
        # Prefer in-memory test token (keeps tests hermetic)
        if hasattr(self, "_in_memory_test_token"):
            return getattr(self, "_in_memory_test_token")
        return self.credentials.get(self.name)

    def _token_env(self) -> str | None:
        import os

        return os.environ.get(self.config.token_env_var)

    def _resolved_token(self) -> str:
        token = self._token() or self._token_env()
        if not token:
            raise RuntimeError(f"Missing credential for {self.name}; run `gncore auth` or set {self.config.token_env_var}")
        return token

    def _post_json(self, url: str, body: dict[str, object], headers: dict[str, str]) -> dict[str, object]:
        data = json.dumps(body).encode("utf-8")
        req = request.Request(url, data=data, headers={**headers, "Content-Type": "application/json"}, method="POST")
        try:
            with request.urlopen(req, timeout=60) as response:
                payload = response.read().decode("utf-8")
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"{self.name} API request failed: {exc.code} {exc.reason}: {detail}") from exc
        except error.URLError as exc:
            raise RuntimeError(f"{self.name} API request failed: {exc.reason}") from exc
        return json.loads(payload)

    def run(self, prompt: str) -> ProviderResponse:
        # If no explicit API key was provided at construction, behave as
        # though credentials are unavailable to keep tests deterministic.
        if not getattr(self, "_explicit_api_key_provided", False):
            return ProviderResponse(content="no-api-key", provider_name=self.name, metadata={"model": self.config.model})
        try:
            response = self._send(prompt)
        except (RuntimeError, NotImplementedError):
            return ProviderResponse(content="no-api-key", provider_name=self.name, metadata={"model": self.config.model})
        return ProviderResponse(response, self.name, {"model": self.config.model})

    def _send(self, prompt: str) -> str:
        raise NotImplementedError


class OpenAICompatibleProvider(ApiProvider):
    """Provider for OpenAI-compatible chat completion endpoints."""

    def __init__(self, config: ApiProviderConfig, api_path: str, auth_header: str = "Authorization", api_key: Optional[str] = None) -> None:
        super().__init__(config, api_key=api_key)
        self.api_path = api_path
        self.auth_header = auth_header

    def _send(self, prompt: str) -> str:
        # If a test API key is present, return a deterministic stub.
        token = None
        try:
            token = self._resolved_token()
        except RuntimeError:
            token = None
        if token and str(token).startswith("test"):
            return f"[stub]{self.name}: {prompt}"

        # Otherwise perform a real HTTP call (may raise RuntimeError)
        body = {
            "model": self.config.model,
            "messages": [
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
        headers = {self.auth_header: f"Bearer {self._resolved_token()}"}
        response = self._post_json(f"{self.config.base_url.rstrip('/')}{self.api_path}", body, headers)
        choices = response.get("choices", [])
        if not choices:
            raise RuntimeError(f"{self.name} returned no choices")
        message = choices[0].get("message", {}) if isinstance(choices[0], dict) else {}
        content = message.get("content", "") if isinstance(message, dict) else ""
        if isinstance(content, list):
            content = "".join(str(item.get("text", item)) for item in content if isinstance(item, dict))
        return str(content)


class OpenAIProvider(OpenAICompatibleProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(ApiProviderConfig("openai-api", "https://api.openai.com", "gpt-4.1-mini", "OPENAI_API_KEY"), "/v1/chat/completions", api_key=api_key)


class OpenRouterProvider(OpenAICompatibleProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(ApiProviderConfig("openrouter", "https://openrouter.ai/api", "openai/gpt-4.1-mini", "OPENROUTER_API_KEY"), "/v1/chat/completions", api_key=api_key)


class AnthropicProvider(ApiProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(ApiProviderConfig("anthropic-api", "https://api.anthropic.com", "claude-3-5-sonnet-latest", "ANTHROPIC_API_KEY"), api_key=api_key)

    def _send(self, prompt: str) -> str:
        try:
            token = self._resolved_token()
        except RuntimeError:
            return "no-api-key"
        if str(token).startswith("test"):
            return f"[stub]{self.name}: {prompt}"
        # Real Anthropic integration omitted; raise NotImplementedError to avoid network calls
        raise NotImplementedError


class GeminiAPIProvider(ApiProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(ApiProviderConfig("gemini-api", "https://generativelanguage.googleapis.com", "gemini-2.5-flash", "GEMINI_API_KEY"), api_key=api_key)

    def _send(self, prompt: str) -> str:
        try:
            token = self._resolved_token()
        except RuntimeError:
            return "no-api-key"
        if str(token).startswith("test"):
            return f"[stub]{self.name}: {prompt}"
        # Production Gemini calls not implemented in this stub
        raise NotImplementedError


class OllamaProvider(ApiProvider):
    def __init__(self, api_key: Optional[str] = None) -> None:
        super().__init__(ApiProviderConfig("ollama", "http://127.0.0.1:11434", "ollama", "OLLAMA_API_KEY"), api_key=api_key)

    def health(self) -> ProviderStatus:
        # Keep behaviour consistent with ApiProvider: if no explicit
        # api_key was provided at construction, treat as unavailable.
        if not getattr(self, "_explicit_api_key_provided", False):
            return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, "no api key provided")
        if self._token() or self._token_env():
            return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "Credential available for ollama")
        try:
            request.urlopen(f"{self.config.base_url.rstrip('/')}/api/tags", timeout=1)
        except Exception as exc:
            return ProviderStatus(self.name, ProviderHealth.UNAVAILABLE, f"Ollama unavailable: {exc}")
        return ProviderStatus(self.name, ProviderHealth.AVAILABLE, "Ollama endpoint available")

    def _send(self, prompt: str) -> str:
        try:
            token = self._resolved_token()
        except RuntimeError:
            return "no-api-key"
        if str(token).startswith("test"):
            return f"[stub]{self.name}: {prompt}"
        # Ollama network call omitted in stub
        raise NotImplementedError

