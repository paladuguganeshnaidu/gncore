"""Executable GNCore CLI entry point."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from gncore.cli.app import main


if __name__ == "__main__":
    main()
