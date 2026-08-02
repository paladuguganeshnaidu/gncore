from __future__ import annotations

import sys
from types import SimpleNamespace

import pytest

from gncore import ExternalCliProvider, ProviderFactory, ProviderHealth
from gncore.providers import credentials as credentials_module
from gncore.providers.catalog import provider_by_name
from gncore.providers.external import CliProviderConfig
from gncore.providers.credentials import CredentialStore


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


def test_provider_aliases_resolve_to_current_names() -> None:
    assert provider_by_name("copilot").name == "github-copilot-agent"
    assert provider_by_name("claude").name == "claude-code"
    assert provider_by_name("gemini").name == "gemini-cli"


def test_credential_store_round_trip_with_keyring(monkeypatch) -> None:
    storage: dict[tuple[str, str], str] = {}

    class FakePasswordDeleteError(Exception):
        pass

    fake_keyring = SimpleNamespace(
        set_password=lambda service, account, secret: storage.__setitem__((service, account), secret),
        get_password=lambda service, account: storage.get((service, account)),
        delete_password=lambda service, account: storage.pop((service, account)),
        errors=SimpleNamespace(PasswordDeleteError=FakePasswordDeleteError),
    )
    monkeypatch.setattr(credentials_module, "keyring", fake_keyring)

    store = CredentialStore("test-service")
    store.save("openai-api", "secret-token")

    assert store.get("openai-api") == "secret-token"

    store.delete("openai-api")
    assert store.get("openai-api") is None
