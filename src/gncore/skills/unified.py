"""Adaptive category skills and compatibility aliases for their workflows."""

from functools import lru_cache
from importlib.resources import files
import json

from gncore.skills.bundles import bundle_manifest, bundle_skills
from gncore.skills.models import SkillMetadata
from gncore.version import __version__


def unified_manifest() -> tuple[dict, ...]:
    return bundle_manifest("unified_data")


def unified_skills():
    return bundle_skills("unified_data", "general")


@lru_cache(maxsize=1)
def workflow_aliases() -> dict[str, str]:
    aliases = {workflow["id"]: entry["id"] for entry in unified_manifest() for workflow in entry["workflows"]}
    primary_ids = {entry["id"] for entry in unified_manifest()}
    migration = json.loads(files("gncore.skills").joinpath("migration.json").read_text(encoding="utf-8"))
    overrides = {item["id"]: item["target"] for item in migration["categories"] if item["target"]}
    overrides.update(migration.get("aliases", {}))
    return {name: name if name in primary_ids else overrides.get(name, target) for name, target in aliases.items()}


@lru_cache(maxsize=None)
def list_workflows(category: str | None = None) -> tuple[SkillMetadata, ...]:
    return tuple(
        SkillMetadata(
            skill_id=workflow["id"], name=workflow["title"],
            description=workflow["description"], version=__version__,
            category=entry["category"], tags=(entry["id"], "workflow"),
            license=entry["license"],
        )
        for entry in unified_manifest()
        if category is None or entry["category"] == category
        for workflow in entry["workflows"]
    )


def search_terms(skill_id: str) -> tuple[str, ...]:
    entry = next((e for e in unified_manifest() if e["id"] == skill_id), None)
    if not entry:
        return ()
    return tuple(value for w in entry["workflows"] for value in (w["id"], w["title"], w["description"]))
