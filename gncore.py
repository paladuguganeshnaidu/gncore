"""Compatibility launcher for the GNCore CLI.

The repository root contains a module named ``gncore.py`` that would otherwise
shadow the real ``gncore`` package when the project is imported directly from a
checkout. This shim ensures the CLI still runs from the repository root while
allowing ``import gncore`` to resolve to the packaged module under ``src/``.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_ROOT = ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


def main() -> None:
    """Run the packaged GNCore CLI entry point."""
    sys.modules.pop("gncore", None)
    importlib.import_module("gncore.cli.app").main()


if __name__ == "__main__":
    main()
