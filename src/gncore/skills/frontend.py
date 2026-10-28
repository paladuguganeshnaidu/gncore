"""Load GNCore's attributed, resource-complete frontend skill collection."""

from functools import lru_cache
from importlib.resources import files
import json
from pathlib import PurePosixPath

from gncore.skills.models import SkillDefinition, SkillMetadata


LEGACY_FRONTEND_IDS = {
    "frontend-engineering": "web-front-design",
    "ui-minimalism": "web-front-minimalism",
    "ui-maximalism": "web-front-maximalism",
    "responsive-accessibility": "web-front-accessibility",
    "web-performance": "web-front-react",
    "web-testing": "web-front-testing",
}


@lru_cache(maxsize=1)
def frontend_manifest() -> tuple[dict, ...]:
    return tuple(json.loads(files("gncore.skills").joinpath("frontend_data/manifest.json").read_text(encoding="utf-8")))


@lru_cache(maxsize=1)
def frontend_skills() -> tuple[SkillDefinition, ...]:
    definitions = []
    for entry in frontend_manifest():
        root = files("gncore.skills").joinpath("frontend_data", entry["id"])
        document = root.joinpath("GUIDE.md").read_text(encoding="utf-8")
        body = document.split("---", 2)[2].strip()
        definitions.append(SkillDefinition(
            metadata=SkillMetadata(
                skill_id=entry["id"], name=entry["title"],
                description=entry["description"], version="1.0.0",
                category="web-frontend", tags=tuple(entry["tags"]),
            ),
            prompt=body,
        ))
    return tuple(definitions)


def frontend_resources(skill_id: str) -> dict[str, bytes]:
    """Return only the resources declared in the packaged manifest."""
    entry = next((item for item in frontend_manifest() if item["id"] == skill_id), None)
    if entry is None:
        return {}
    root = files("gncore.skills").joinpath("frontend_data", skill_id)
    result = {}
    for name in entry["resources"]:
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or "\\" in name or ":" in name:
            raise ValueError(f"unsafe frontend resource path: {name}")
        result[name] = root.joinpath(*path.parts).read_bytes()
    return result
