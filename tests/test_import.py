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
