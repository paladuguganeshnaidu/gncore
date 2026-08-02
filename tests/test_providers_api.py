import pytest

from gncore.providers.api import (
    OpenAIProvider,
    AnthropicProvider,
    OpenRouterProvider,
    GeminiAPIProvider,
    OllamaProvider,
)


@pytest.mark.parametrize("provider_cls", [
    OpenAIProvider,
    AnthropicProvider,
    OpenRouterProvider,
    GeminiAPIProvider,
    OllamaProvider,
])
def test_provider_health_without_key(provider_cls, monkeypatch):
    # Clear common provider env vars to avoid picking up real credentials
    for env in ("OPENAI_API_KEY", "OPENROUTER_API_KEY", "ANTHROPIC_API_KEY", "GEMINI_API_KEY", "OLLAMA_API_KEY"):
        monkeypatch.delenv(env, raising=False)
    # Prevent real keyring values from affecting test results
    monkeypatch.setattr("gncore.providers.credentials.CredentialStore.get", lambda self, provider_name, secret_name="token": None)
    p = provider_cls(api_key=None)
    status = p.health()
    assert status.health.name == "UNAVAILABLE"
    resp = p.run("hello")
    assert "no-api-key" in resp.content


@pytest.mark.parametrize("provider_cls", [
    OpenAIProvider,
    AnthropicProvider,
    OpenRouterProvider,
    GeminiAPIProvider,
    OllamaProvider,
])
def test_provider_run_and_stream_with_key(provider_cls):
    p = provider_cls(api_key="test-key")
    status = p.health()
    assert status.health.name == "AVAILABLE"
    resp = p.run("hello world")
    assert p.name in resp.provider_name or resp.provider_name == p.name
    chunks = list(p.stream("hello world"))
    assert len(chunks) >= 1
    assert all(isinstance(c, str) for c in chunks)
