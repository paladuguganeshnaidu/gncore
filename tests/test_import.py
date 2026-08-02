import importlib
import os
import pathlib
import sys

import pytest

from ngcore import NgCore, Loader


def test_import_ngcore():
    core = NgCore()
    assert core.hello() == "Hello from gncore"


def test_loader_list_files(tmp_path):
    sample = tmp_path / "sample.txt"
    sample.write_text("hello")

    loader = Loader(tmp_path)
    files = loader.list_files()

    assert sample in files


def test_repository_root_does_not_shadow_package_import():
    repo_root = pathlib.Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(repo_root))
    try:
        imported = importlib.import_module("gncore")
    finally:
        sys.path.pop(0)

    assert imported.__file__ is not None
    assert "gncore.py" not in imported.__file__
