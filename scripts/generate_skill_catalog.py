"""Generate primary categories and the complete compatibility workflow map."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gncore import __version__, builtin_skills, list_domains, list_workflows
from gncore.skills.unified import unified_manifest, workflow_aliases


def escape(value):
    return value.replace("|", "\\|").replace("\n", " ").strip()


def main():
    entries = unified_manifest()
    domains = list_domains()
    lines = ["# GNCore skill catalog", "", f"GNCore {__version__} contains **{len(entries)} developer category skills** and **{len(list_workflows())} active workflows**, organized into **{len(domains)} developer capability groups**.", "", "Install a category under `.agents/skills/`, then describe the outcome to a compatible host AI. Its single entrypoint selects the relevant workflows; supporting references are loaded only when needed.", "", "## Primary categories", "", "| Category | Skill ID | Workflows | Use it for |", "| --- | --- | --- | --- |"]
    for entry in entries:
        lines.append(f"| `{entry['category']}` | `{entry['id']}` | {len(entry['workflows'])} | {escape(entry['description'])} |")
    lines.extend(["", "## Developer domains", "", "| Domain | Category skills | Active workflows |", "| --- | --- | --- |"])
    for domain in domains:
        lines.append(f"| {escape(domain.name)} | {', '.join('`'+name+'`' for name in domain.skill_ids)} | {len(domain.workflow_ids)} |")
    lines.extend(["", "## Complete workflow map", "", "These IDs remain CLI/API compatibility aliases. Exporting aliases from one category produces one merged category folder. Primary category names take precedence over older generic names when they collide."])
    aliases = workflow_aliases()
    for entry in entries:
        lines.extend(["", f"### {entry['title']} (`{entry['id']}`)", "", "| Workflow ID | Resolves to | Workflow | Use it for |", "| --- | --- | --- | --- |"])
        for workflow in entry["workflows"]:
            lines.append(f"| `{workflow['id']}` | `{aliases[workflow['id']]}` | {escape(workflow['title'])} | {escape(workflow['description'])} |")
    lines.extend(["", "## Use", "", "```bash", "gncore export --specific web-frontend", "gncore export --skills web-backend code-build", "gncore export --all --output gncore-categories.zip", "gncore plan \"A premium hotel website, no animation\"", "```", "", "See [Source Research](SOURCE_RESEARCH.md), [Ownership](OWNERSHIP.md), and [Migration](../MIGRATION.md) for provenance, licensing, and compatibility details."])
    (ROOT / "docs/ALL_SKILLS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print(f"Catalog: {len(entries)} categories, {len(list_workflows())} workflows, {len(domains)} developer domains")


if __name__ == "__main__":
    main()
