"""Backward-compatible objects for the historical ngcore package."""

from __future__ import annotations

from pathlib import Path


class NgCore:
    """Compatibility facade retained for existing users."""

    def hello(self) -> str:
        """Return the legacy smoke-test message."""
        return "Hello from gncore"


class Loader:
    """Small filesystem loader retained for the previous public API."""

    def __init__(self, base_path: Path) -> None:
        """Create a loader for a directory."""
        self.base_path = base_path

    def list_files(self) -> list[Path]:
        """Return files directly inside the configured directory."""
        return sorted(path for path in self.base_path.iterdir() if path.is_file())
