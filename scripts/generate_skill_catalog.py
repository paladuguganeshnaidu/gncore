"""Generate the public skill catalog from the authoritative built-in library."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gncore.skills import builtin_skills, list_domains  # noqa: E402


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main() -> None:
    skills = {skill.metadata.skill_id: skill for skill in builtin_skills()}
    domains = list_domains()
    lines = [
        "# GNCore Skill Catalog",
        "",
        f"GNCore 5.0.0 contains **{len(skills)} portable skills** across **{len(domains)} domain packs**. Each domain pack contains ten focused workflows.",
        "",
        "GNCore is a skill library and export tool. It does not detect, configure, install into, or orchestrate AI applications. Export standard `SKILL.md` folders and copy them to an assistant's documented skills directory, or use `gncore show <skill-id>` to inspect a skill.",
        "",
        "## Domain packs",
        "",
    ]
    domain_ids: set[str] = set()
    for domain in domains:
        lines.extend([f"### {domain.name} (`{domain.domain_id}`)", "", escape(domain.description), "", "| Skill ID | Slash name | Skill | Use it for |", "| --- | --- | --- | --- |"])
        for skill_id in domain.skill_ids:
            domain_ids.add(skill_id)
            metadata = skills[skill_id].metadata
            lines.append(f"| `{skill_id}` | `/{skill_id}` | {escape(metadata.name)} | {escape(metadata.description)} |")
        lines.append("")

    lines.extend(["## Additional specialist skills", "", "These complement the domain packs and are grouped by category.", ""])
    specialist = [skill for skill in skills.values() if skill.metadata.skill_id not in domain_ids]
    categories: dict[str, list] = {}
    for skill in specialist:
        categories.setdefault(skill.metadata.category, []).append(skill)
    for category, members in sorted(categories.items()):
        lines.extend([f"### {category}", "", "| Skill ID | Slash name | Skill | Use it for |", "| --- | --- | --- | --- |"])
        for skill in sorted(members, key=lambda item: item.metadata.skill_id):
            metadata = skill.metadata
            lines.append(f"| `{metadata.skill_id}` | `/{metadata.skill_id}` | {escape(metadata.name)} | {escape(metadata.description)} |")
        lines.append("")

    lines.extend([
        "## Use and export",
        "",
        "```bash",
        "gncore search \"clean data\"",
        "gncore show train",
        "gncore export --skills train evaluate --output ml-skills.zip",
        "gncore export --all --output all-gncore-skills.zip",
        "```",
        "",
        "Every skill guides an AI assistant through scoped, evidence-based work and asks it to report checks honestly. Skills are instructions, not executable agents; the host assistant supplies reasoning and tools.",
        "",
    ])
    output = ROOT / "docs" / "ALL_SKILLS.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote docs/ALL_SKILLS.md ({len(skills)} skills, {len(domains)} domains).")


if __name__ == "__main__":
    main()
