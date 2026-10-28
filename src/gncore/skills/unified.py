"""Adaptive category skills and compatibility aliases for their workflows."""

from functools import lru_cache

from gncore.skills.bundles import bundle_manifest, bundle_skills
from gncore.skills.models import SkillMetadata


def unified_manifest() -> tuple[dict, ...]:
    return bundle_manifest("unified_data")


def unified_skills():
    return bundle_skills("unified_data", "general")


@lru_cache(maxsize=1)
def workflow_aliases() -> dict[str, str]:
    aliases = {workflow["id"]: entry["id"] for entry in unified_manifest() for workflow in entry["workflows"]}
    primary_ids = {entry["id"] for entry in unified_manifest()}
    return {name: name if name in primary_ids else target for name, target in aliases.items()}


@lru_cache(maxsize=None)
def list_workflows(category: str | None = None) -> tuple[SkillMetadata, ...]:
    return tuple(
        SkillMetadata(
            skill_id=workflow["id"], name=workflow["title"],
            description=workflow["description"], version="6.0.0",
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
