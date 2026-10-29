"""Developer-focused catalog discovery, migration aliases and validation."""

from functools import lru_cache
from importlib.resources import files
import json
import re

from gncore.skills.models import SkillDefinition, SkillDomain
from gncore.skills.unified import search_terms, unified_manifest, unified_skills, workflow_aliases


@lru_cache(maxsize=1)
def builtin_skills() -> tuple[SkillDefinition, ...]:
    return unified_skills()


@lru_cache(maxsize=1)
def migration_manifest() -> dict:
    return json.loads(files("gncore.skills").joinpath("migration.json").read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def category_aliases() -> dict[str, str]:
    aliases = {entry["id"]: entry["target"] for entry in migration_manifest()["categories"] if entry["target"]}
    aliases.update({"frontend-engineering": "web-frontend", "backend-api": "web-backend",
                    "backend-engineering": "web-backend", "code-engineering": "code-build"})
    aliases.update(migration_manifest().get("aliases", {}))
    return aliases


@lru_cache(maxsize=1)
def list_domains() -> tuple[SkillDomain, ...]:
    """Return developer capability groups, replacing the retired professional packs."""
    groups = {
        "web-and-apps": ("Web and Applications", ("web-frontend", "web-backend", "design-ux", "mobile-development", "game-development")),
        "ai-and-ml": ("AI and Machine Learning", ("machine-learning", "neural-networks", "deep-learning", "computer-vision", "natural-language-processing", "mlops", "ai-engineering")),
        "data": ("Data and Databases", ("data-engineering", "data-science", "databases")),
        "systems": ("Systems and Performance", ("systems-programming", "embedded-systems", "distributed-systems", "performance-engineering")),
        "delivery": ("Delivery and Reliability", ("cloud-devops-sre", "cybersecurity", "observability", "testing", "release-engineering")),
        "engineering": ("Developer Workflow", ("code-build", "python", "developer-tools", "documentation", "automation", "developer-research")),
    }
    return tuple(SkillDomain(domain_id=name, name=title, description=f"Developer capabilities for {title.lower()}.",
                             skill_ids=ids, workflow_ids=tuple(w["id"] for entry in unified_manifest() if entry["id"] in ids for w in entry["workflows"]))
                 for name, (title, ids) in groups.items())


def get_skill(skill_id: str, *, skills: tuple[SkillDefinition, ...] | None = None) -> SkillDefinition:
    selected = skills if skills is not None else builtin_skills()
    index = {skill.metadata.skill_id: skill for skill in selected}
    if skill_id in index:
        return index[skill_id]
    if skills is None:
        target = category_aliases().get(skill_id, workflow_aliases().get(skill_id, skill_id))
        # Pre-6 frontend/backend aliases are retained only when their target is active.
        old_aliases = {"frontend-engineering": "web-frontend", "backend-api": "web-backend"}
        target = old_aliases.get(target, target)
        if target in index:
            return index[target]
        retired = {w["id"] for w in migration_manifest()["workflows"] if w["target"] is None}
        retired.update(e["id"] for e in migration_manifest()["categories"] if e["target"] is None)
        if skill_id in retired:
            raise KeyError(f"{skill_id}: retired in the developer-focused catalog; see migration notes")
    raise KeyError(skill_id)


def list_categories(*, skills: tuple[SkillDefinition, ...] | None = None) -> tuple[str, ...]:
    return tuple(sorted({s.metadata.category for s in (skills if skills is not None else builtin_skills())}))


def search_skills(query: str, *, category: str | None = None, skills: tuple[SkillDefinition, ...] | None = None) -> tuple[SkillDefinition, ...]:
    terms = tuple(term.casefold() for term in query.split() if term.strip())
    matches = []
    normalized_category = category_aliases().get(category, category) if category else None
    for skill in (skills if skills is not None else builtin_skills()):
        metadata = skill.metadata
        if normalized_category and metadata.category.casefold() != normalized_category.casefold():
            continue
        fields = (metadata.skill_id, metadata.name, metadata.description, metadata.category, *metadata.tags, *search_terms(metadata.skill_id))
        if all(any(term in value.casefold() for value in fields) for term in terms):
            score = sum(4 if term in metadata.skill_id.casefold() else 3 if term in metadata.name.casefold() else 1 for term in terms)
            matches.append((score, skill))
    return tuple(skill for _, skill in sorted(matches, key=lambda pair: (-pair[0], pair[1].metadata.skill_id)))


def validate_skill_definition(skill: SkillDefinition) -> tuple[str, ...]:
    metadata, issues = skill.metadata, []
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata.skill_id):
        issues.append("skill_id must contain lowercase letters, numbers, and single hyphens")
    for label, text in (("name", metadata.name), ("description", metadata.description), ("category", metadata.category), ("instructions", skill.prompt)):
        if not text.strip():
            issues.append(f"{label} is required")
    if len(metadata.description) > 1024:
        issues.append("description must be at most 1024 characters")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:(?:a|b|rc)\d+|[-+][0-9A-Za-z.-]+)?", metadata.version):
        issues.append("version must be a release or prerelease version")
    return tuple(issues)
