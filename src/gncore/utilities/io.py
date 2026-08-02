"""I/O helpers used across GNCore."""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
from typing import Any, Iterator


@contextmanager
def _temp_file(path: Path) -> Iterator[Path]:
    temp_path = path.with_name(f".{path.name}.tmp")
    try:
        yield temp_path
        temp_path.replace(path)
    finally:
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)


def atomic_write_text(path: Path, content: str, encoding: str = "utf-8") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with _temp_file(path) as temp_path:
        temp_path.write_text(content, encoding=encoding)


def write_json(path: Path, data: Any) -> None:
    atomic_write_text(path, json.dumps(data, indent=2, sort_keys=True) + "\n")


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))
