from __future__ import annotations

from gncore.adapters import get_adapter_registry


def test_supported_adapter_registry_contains_all_targets() -> None:
    registry = get_adapter_registry()
    keys = [adapter.key for adapter in registry.adapters]
    assert keys == [
        "vscode-chat",
        "github-copilot-chat",
        "claude-desktop",
        "claude-code",
        "cursor",
        "windsurf",
        "continue-dev",
        "gemini-cli",
        "openai-codex-cli",
    ]