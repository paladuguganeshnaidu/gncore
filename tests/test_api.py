import ngcore


def test_import():
    assert ngcore.__version__


def test_build():
    result = ngcore.build("Hello")

    assert "skill" in result
    assert "prompt" in result


def test_search():
    assert isinstance(
        ngcore.search("authentication"),
        list,
    )


def test_list():
    assert len(
        ngcore.list_skills()
    ) > 0
