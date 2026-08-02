from __future__ import annotations

import sys

import pytest

from gncore import ExternalCliProvider, ProviderFactory, ProviderHealth
from gncore.providers.external import CliProviderConfig


def test_provider_factory_creates_supported_providers() -> None:
    factory = ProviderFactory()

    assert factory.create("mock").name == "mock"
    assert factory.create("codex").name == "codex"
    assert factory.create("claude-code").name == "claude-code"
    assert factory.create("gemini-cli").name == "gemini-cli"
    assert factory.create("opencode").name == "opencode"


def test_provider_factory_rejects_unknown_provider() -> None:
    with pytest.raises(ValueError, match="Unsupported provider"):
        ProviderFactory().create("unknown")


def test_external_cli_provider_runs_local_executable() -> None:
    provider = ExternalCliProvider(
        CliProviderConfig(
            name="python-echo",
            executable=sys.executable,
            args=("-c", "import sys; print(sys.stdin.read().upper())"),
        )
    )

    response = provider.run("hello")

    assert response.provider_name == "python-echo"
    assert response.content.strip() == "HELLO"


def test_mock_provider_health_stream_and_cancel() -> None:
    provider = ProviderFactory().create("mock")

    assert provider.health().health is ProviderHealth.AVAILABLE
    assert "Mock response" in "".join(provider.stream("hello"))
    provider.cancel()
