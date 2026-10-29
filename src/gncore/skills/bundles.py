"""Shared reader for packaged skill entrypoints and portable resources."""

from functools import lru_cache
from importlib.resources import files
import json
import hashlib
from pathlib import PurePosixPath

from gncore.skills.models import SkillDefinition, SkillMetadata


@lru_cache(maxsize=None)
def bundle_manifest(directory: str) -> tuple[dict, ...]:
    root = files("gncore.skills").joinpath(directory)
    return tuple(json.loads(root.joinpath("manifest.json").read_text(encoding="utf-8")))


@lru_cache(maxsize=None)
def bundle_skills(directory: str, category: str) -> tuple[SkillDefinition, ...]:
    definitions = []
    for entry in bundle_manifest(directory):
        entrypoint = "GUIDE.md" if directory in {"frontend_data", "backend_data"} else "SKILL.md"
        raw = files("gncore.skills").joinpath(directory, entry["id"], entrypoint).read_bytes()
        if entry.get("entrypoint_sha256") and hashlib.sha256(raw).hexdigest() != entry["entrypoint_sha256"]:
            raise ValueError(f"skill entrypoint digest mismatch: {entry['id']}")
        document = raw.decode("utf-8")
        body = document.split("---", 2)[2].strip()
        if body.startswith("# "):
            body = body.partition("\n")[2].strip()
        definitions.append(SkillDefinition(
            metadata=SkillMetadata(
                skill_id=entry["id"], name=entry["title"],
                description=entry["description"], version=entry.get("version", "1.0.0"),
                category=entry.get("category", category), tags=tuple(entry["tags"]),
                license=entry.get("license", "MIT"),
            ),
            prompt=body,
        ))
    return tuple(definitions)


def bundle_resources(directory: str, skill_id: str) -> dict[str, bytes]:
    entry = next((item for item in bundle_manifest(directory) if item["id"] == skill_id), None)
    if entry is None:
        return {}
    root = files("gncore.skills").joinpath(directory, skill_id)
    result = {}
    for name in entry["resources"]:
        path = PurePosixPath(name)
        if not name or path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name:
            raise ValueError(f"unsafe skill resource path: {name}")
        content = root.joinpath(*path.parts).read_bytes()
        expected = entry.get("resource_sha256", {}).get(name)
        if directory == "unified_data" and (not expected or hashlib.sha256(content).hexdigest() != expected):
            raise ValueError(f"skill resource digest mismatch: {skill_id}/{name}")
        result[name] = content
    return result


def packaged_resources(skill_id: str) -> dict[str, bytes]:
    for directory in ("unified_data",):
        result = bundle_resources(directory, skill_id)
        if result:
            return result
    return {}
