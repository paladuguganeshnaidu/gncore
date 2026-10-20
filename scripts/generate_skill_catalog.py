"""Generate docs/ALL_SKILLS.md from the authoritative GNCore catalog."""

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
        "# GNCore Skill Catalog and Usage Guide",
        "",
        f"GNCore 4.0.0 includes **{len(skills)} skills** across **{len(domains)} domain packs**. Each domain pack has ten workflows. This page is generated from the built-in catalog; rerun `python scripts/generate_skill_catalog.py` after catalog changes.",
        "",
        "## How to use a skill",
        "",
        "1. Search by task: `gncore search \"clean data\"` or `gncore search CEO strategy`.",
        "2. Install the listed skill ID for your assistant and scope. Example: `gncore install company-ceo --apps vscode-codex --scope workspace`.",
        "3. In an assistant that supports native skill invocation, start the request with its slash name, such as `/company-ceo`, then describe the outcome, context, constraints, and acceptance checks.",
        "4. Review the assistant's changes and evidence. Skills guide the assistant; they do not execute independently or guarantee an outcome.",
        "",
        "Use `gncore list apps` to check target keys and `gncore doctor` / `gncore validate --apps <key>` to inspect an installation. Replace `vscode-codex` with a key from `gncore list apps`; use `--scope user` for user-wide installation.",
        "",
        "## Domain packs",
        "",
    ]
    domain_ids: set[str] = set()
    for domain in domains:
        lines.extend([f"### {domain.name} (`{domain.domain_id}`)", "", escape(domain.description), "", "| Skill ID | Slash name | Skill | Use it for | Install example |", "| --- | --- | --- | --- | --- |"] )
        for skill_id in domain.skill_ids:
            domain_ids.add(skill_id)
            skill = skills[skill_id]
            m = skill.metadata
            lines.append(f"| `{skill_id}` | `/{skill_id}` | {escape(m.name)} | {escape(m.description)} | `gncore install {skill_id} --apps vscode-codex --scope workspace` |")
        lines.append("")

    lines.extend(["## Additional specialist skills", "", "These skills complement the 30 domain packs and are grouped by their catalog category.", ""])
    specialist = [skill for skill in skills.values() if skill.metadata.skill_id not in domain_ids]
    categories: dict[str, list] = {}
    for skill in specialist:
        categories.setdefault(skill.metadata.category, []).append(skill)
    for category, members in sorted(categories.items()):
        lines.extend([f"### {category}", "", "| Skill ID | Slash name | Skill | Use it for | Install example |", "| --- | --- | --- | --- | --- |"] )
        for skill in sorted(members, key=lambda item: item.metadata.skill_id):
            m = skill.metadata
            skill_id = m.skill_id
            lines.append(f"| `{skill_id}` | `/{skill_id}` | {escape(m.name)} | {escape(m.description)} | `gncore install {skill_id} --apps vscode-codex --scope workspace` |")
        lines.append("")

    lines.extend(["## Other targets", "", "GNCore adapters currently include:", "", "- `vscode-chat` — VS Code Chat / Copilot skills", "- `vscode-codex` — VS Code Codex skills", "- `vscode-claude-code` — VS Code Claude Code skills", "- `antigravity` — Google Antigravity", "- `github-copilot-chat` — GitHub Copilot Chat", "- `claude-desktop` — Claude Desktop managed bundle", "- `claude-code` — Claude Code", "- `cursor` — Cursor managed bundle", "- `windsurf` — Windsurf managed bundle", "- `continue-dev` — Continue.dev managed bundle", "- `gemini-cli` — Gemini CLI skills", "- `openai-codex-cli` — OpenAI Codex CLI", "", "For hosted ChatGPT Skills, export one skill per ZIP and upload it in ChatGPT: `gncore export --app chatgpt --skills company-ceo --output company-ceo.zip`.", "", "Domain and specialist entries use the same shared inspect → plan → implement → test → fix → retest → report contract. The applicable checks depend on the task and the assistant's available tools; the assistant must report checks it did not run.", ""])
    output = ROOT / "docs" / "ALL_SKILLS.md"
    output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {output.relative_to(ROOT)} ({len(skills)} skills, {len(domains)} domains).")


if __name__ == "__main__":
    main()
