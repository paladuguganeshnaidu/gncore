from __future__ import annotations

from gncore import __version__, GncoreCli, get_adapter_registry


def test_public_api_exports() -> None:
    assert __version__ == "3.0.0"
    assert isinstance(GncoreCli(), GncoreCli)
    registry = get_adapter_registry()
    assert len(registry.adapters) == 9
