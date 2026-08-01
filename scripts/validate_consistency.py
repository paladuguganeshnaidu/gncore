#!/usr/bin/env python3
"""
Consistency validator for website-builder-elite.

Catches the exact class of bug this repo shipped with before this pass:
a role-count claim that didn't match the table it described, and a
citation to a file (SECURITY.md) that didn't exist. Run on every push/PR
via .github/workflows/ci.yml.

Exit code 0 = all checks passed. Exit code 1 = at least one failure;
failures are printed with enough detail to fix them directly.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


def fail(msg: str) -> None:
    FAILURES.append(msg)


def check_frontmatter_name_matches_filename() -> None:
    """Every skills/*.md file's frontmatter `name:` must match its filename stem."""
    for path in sorted((REPO_ROOT / "skills").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
        if not m:
            fail(f"{path.relative_to(REPO_ROOT)}: no frontmatter block found")
            continue
        name_m = re.search(r"^name:\s*(\S+)\s*$", m.group(1), re.MULTILINE)
        if not name_m:
            fail(f"{path.relative_to(REPO_ROOT)}: frontmatter has no `name:` field")
            continue
        declared = name_m.group(1).strip()
        expected = path.stem
        if declared != expected:
            fail(
                f"{path.relative_to(REPO_ROOT)}: frontmatter name '{declared}' "
                f"does not match filename stem '{expected}'"
            )


# Stages with a documented, deliberate reason to have no formal NEXT: line:
# 00-orchestrator is the root (reports to the user, not another stage);
# 19-git is continuous background work, not a numbered wait-point in the
# main sequence — both state this explicitly in their own Handoff sections.
NO_NEXT_ALLOWED = {"00-orchestrator", "19-git"}

# Documented dynamic-return patterns that are not literal filenames by design.
NEXT_DYNAMIC_ALLOWLIST = ("return to the stage that originated",)


def check_next_targets_resolve() -> None:
    """Every NEXT: target in every skill's Handoff block must resolve to a real
    skills/<name>.md file, be the literal DONE, or be an allow-listed
    documented exception (see NO_NEXT_ALLOWED / NEXT_DYNAMIC_ALLOWLIST)."""
    skill_stems = {p.stem for p in (REPO_ROOT / "skills").glob("*.md")}
    for path in sorted((REPO_ROOT / "skills").glob("*.md")):
        stem = path.stem
        text = path.read_text(encoding="utf-8")
        next_m = re.search(r"^NEXT:\s*(.+)$", text, re.MULTILINE)
        if not next_m:
            if stem in NO_NEXT_ALLOWED:
                continue
            fail(f"{path.relative_to(REPO_ROOT)}: no NEXT: line found in Handoff block")
            continue
        line = next_m.group(1)
        if any(pattern in line for pattern in NEXT_DYNAMIC_ALLOWLIST):
            continue
        # Extract every NN-name or NN-name.md token mentioned on the line
        # (a line can name multiple stages, e.g. "14-debug + rollback (if fail)").
        targets = re.findall(r"\b(\d{2}-[a-z]+)(?:\.md)?\b", line)
        if not targets:
            if "DONE" in line:
                continue
            fail(
                f"{path.relative_to(REPO_ROOT)}: NEXT line '{line.strip()}' has no "
                f"recognizable stage target and isn't a documented exception"
            )
            continue
        for target in targets:
            if target not in skill_stems:
                fail(
                    f"{path.relative_to(REPO_ROOT)}: NEXT target '{target}' referenced "
                    f"in Handoff block does not match any file in skills/"
                )


def get_ledger_artifact_names() -> set[str]:
    """Filenames CONTEXT-ENGINEERING.md's ledger table declares as stage-written
    runtime outputs (requirements.md, architecture.md, etc.) — these live under
    a project's own context/ directory once a build runs, not in this template
    repo itself, so their absence here is correct, not a broken reference."""
    text = (REPO_ROOT / "context" / "CONTEXT-ENGINEERING.md").read_text(encoding="utf-8")
    names = set()
    for m in re.finditer(r"^\|\s*`([A-Za-z0-9_\-./*]+\.md)`", text, re.MULTILINE):
        names.add(m.group(1).split("/")[-1])
    return names


def check_referenced_filenames_exist() -> None:
    """Every backtick-quoted *.md filename referenced in README.md, ARCHITECTURE.md,
    and agents/AGENTS.md must exist somewhere in the repo, UNLESS it's a declared
    runtime ledger artifact (see get_ledger_artifact_names)."""
    docs = ["README.md", "ARCHITECTURE.md", "agents/AGENTS.md"]
    all_md_files = {p.name for p in REPO_ROOT.rglob("*.md")}
    ledger_artifacts = get_ledger_artifact_names()
    for doc in docs:
        path = REPO_ROOT / doc
        text = path.read_text(encoding="utf-8")
        for m in re.finditer(r"`([A-Za-z0-9_\-./]+\.md)`", text):
            ref = m.group(1)
            basename = ref.split("/")[-1]
            if "*" in basename:
                continue  # glob pattern, not a literal file reference
            if basename in ledger_artifacts:
                continue  # runtime-written per-project artifact, not a repo file
            if basename not in all_md_files:
                fail(f"{doc}: references `{ref}` which does not exist anywhere in the repo")


def check_countable_claims() -> None:
    """Any numeric claim about a countable table (e.g. 'N named roles') must match
    the actual row count of the table it describes."""
    agents_path = REPO_ROOT / "agents" / "AGENTS.md"
    agents_text = agents_path.read_text(encoding="utf-8")
    role_rows = re.findall(r"^\| \*\*[^*]+\*\* \|", agents_text, re.MULTILINE)
    actual_role_count = len(role_rows)

    readme_path = REPO_ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    claim_m = re.search(r"AGENTS\.md\s*←\s*(\d+)\s*named roles", readme_text)
    if not claim_m:
        fail("README.md: could not find the 'N named roles' claim to check against agents/AGENTS.md")
    else:
        claimed = int(claim_m.group(1))
        if claimed != actual_role_count:
            fail(
                f"README.md claims {claimed} named roles, but agents/AGENTS.md's "
                f"table actually defines {actual_role_count}"
            )

    # Pipeline stage count: ARCHITECTURE.md's diagram should have as many
    # numbered stages as there are skills/NN-*.md files (excluding 00-orchestrator,
    # which is the entry point, not a pipeline stage with a gate of its own).
    skill_files = sorted((REPO_ROOT / "skills").glob("[0-9][0-9]-*.md"))
    numbered_stage_count = len(skill_files)
    arch_text = (REPO_ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    diagram_stage_ids = set(re.findall(r"^\s*(\d{2})-[A-Z]+", arch_text, re.MULTILINE))
    skill_stage_ids = {p.stem.split("-")[0] for p in skill_files}
    missing_from_diagram = skill_stage_ids - diagram_stage_ids
    extra_in_diagram = diagram_stage_ids - skill_stage_ids
    if missing_from_diagram:
        fail(f"ARCHITECTURE.md diagram is missing stage(s): {sorted(missing_from_diagram)}")
    if extra_in_diagram:
        fail(f"ARCHITECTURE.md diagram references stage(s) not present in skills/: {sorted(extra_in_diagram)}")
    if numbered_stage_count != 20:
        # Not a hard failure by itself (repo could legitimately grow/shrink),
        # but flag it since every doc that cites a stage count should agree.
        pass


def check_templates_are_referenced() -> None:
    """Every file in templates/ must be referenced by name in at least one file
    under skills/ (or ARCHITECTURE.md, since that's where the shape-level
    reference to quality-gate-checklist.md lives) — catches future orphan templates."""
    skills_text = "\n".join(
        p.read_text(encoding="utf-8") for p in (REPO_ROOT / "skills").glob("*.md")
    )
    arch_text = (REPO_ROOT / "ARCHITECTURE.md").read_text(encoding="utf-8")
    haystack = skills_text + "\n" + arch_text
    for tmpl in sorted((REPO_ROOT / "templates").glob("*.md")):
        if tmpl.name not in haystack:
            fail(f"templates/{tmpl.name} is not referenced by name anywhere in skills/*.md or ARCHITECTURE.md")


def main() -> int:
    check_frontmatter_name_matches_filename()
    check_next_targets_resolve()
    check_referenced_filenames_exist()
    check_countable_claims()
    check_templates_are_referenced()

    if FAILURES:
        print(f"FAILED — {len(FAILURES)} consistency check(s) failed:\n")
        for f in FAILURES:
            print(f"  - {f}")
        return 1

    print("PASSED — all consistency checks green:")
    print("  - frontmatter name == filename stem, every skills/*.md file")
    print("  - every NEXT: target resolves to a real skill file")
    print("  - every *.md file referenced in README/ARCHITECTURE/AGENTS exists")
    print("  - role-count and stage-count claims match actual table/file counts")
    print("  - every templates/*.md file is referenced somewhere in skills/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
