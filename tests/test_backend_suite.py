import json
from pathlib import Path

import pytest

from gncore import get_skill
from gncore.skills.bundles import bundle_resources, packaged_resources
from gncore.skills.unified import unified_manifest


def test_all_resources_remain_in_their_category_with_provenance():
    for entry in unified_manifest():
        resources = packaged_resources(entry["id"])
        assert set(resources) == set(entry["resources"])
        assert "SOURCES.json" in resources and "GNCORE-LICENSE" in resources
        assert not any("__pycache__" in name or name.endswith("/SKILL.md") for name in resources)
        sources = json.loads(resources["SOURCES.json"])
        assert sources["category"] == entry["category"]
        for source in entry["research_references"]:
            assert source["guide"] in resources
            folder = str(Path(source["guide"]).parent).replace("\\", "/")
            assert any(name.startswith(folder + "/notices/") for name in resources)


def test_sharealike_material_and_notices_survive_consolidation():
    for module in ("code-build", "web-backend"):
        assert "CC-BY-SA-4.0" in get_skill(module).metadata.license
        resources = packaged_resources(module)
        assert any(b"Attribution-ShareAlike 4.0" in data for name, data in resources.items() if "notices/" in name)
    resources = packaged_resources("code-build")
    assert "references/code-code-improver/RESOURCE_PATHS.json" in resources


@pytest.mark.parametrize("path", ["../outside", "/absolute", "C:/outside", "dir\\outside"])
def test_resource_reader_rejects_paths_outside_skill_root(monkeypatch, path):
    monkeypatch.setattr("gncore.skills.bundles.bundle_manifest", lambda _directory: ({"id": "test", "resources": [path]},))
    with pytest.raises(ValueError, match="unsafe skill resource path"):
        bundle_resources("unified_data", "test")


def test_source_tree_exposes_only_the_sixty_primary_skill_entrypoints():
    root = Path(__file__).resolve().parents[1] / "src/gncore/skills"
    entries = list(root.rglob("SKILL.md"))
    assert len(entries) == 60
    assert all("unified_data" in path.parts for path in entries)
