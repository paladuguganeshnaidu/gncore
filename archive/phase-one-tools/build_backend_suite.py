"""Create portable GNCore backend/coding entrypoints with pinned attribution."""

from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
from urllib.parse import unquote

from backend_requests import requests

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "src/gncore/skills/backend_data"

DESCRIPTIONS = {
    "grill-me": "Clarify a coding or product request through focused questions that expose assumptions and missing decisions.",
    "research": "Investigate a technical question using repository evidence and relevant primary sources.",
    "prototype": "Build a scoped prototype that tests a specific technical or product assumption.",
    "domain-modeling": "Model domain concepts, invariants, ownership, and language before changing service boundaries.",
    "decision-mapping": "Map unresolved implementation decisions, dependencies, options, and evidence needed to choose.",
    "request-refactor-plan": "Plan a behavior-preserving refactor with explicit scope, sequencing, and regression checks.",
    "qa": "Validate a software change against acceptance criteria and reproduce observable regressions.",
    "to-prd": "Turn a product idea into a scoped requirements document with user outcomes and acceptance criteria.",
    "insecure-defaults": "Find unsafe configuration defaults and fail-open behavior in application code and deployment configuration.",
    "building-ai-agent-on-cloudflare": "Build a scoped AI agent on Cloudflare with explicit state, tool boundaries, bindings, and evaluation cases.",
    "brainstorming": "Explore unresolved software design choices and agree on a practical direction when the brief needs clarification.",
    "using-git-worktrees": "Isolate concurrent coding work in Git worktrees while preserving uncommitted changes and repository conventions.",
    "subagent-driven-development": "Coordinate authorized coding subagents on separable work with explicit interfaces and integration checks.",
    "finishing-a-development-branch": "Prepare a completed development branch for review, integration, or cleanup according to the user's chosen workflow.",
    "code-review": "Review a code diff for correctness, local coding standards, and alignment with its originating specification.",
    "setup-matt-pocock-skills": "Configure the requested coding workflow's repository context, issue-tracker references, and local skill conventions.",
    "code-improver": "Run a bounded review-and-fix loop over a specified code target with evidence and scope controls.",
    "verification-before-completion": "Verify the requested software outcome with fresh command output before reporting completion.",
    "test-driven-development": "Implement a behavior change through meaningful failing tests, a focused fix, and relevant regressions.",
    "supabase": "Implement or debug Supabase database, authentication, storage, and realtime features using current product documentation.",
    "fastapi": "Build FastAPI endpoints, Pydantic models, dependencies, and streaming responses using version-compatible APIs.",
    "search-first": "Search the existing codebase and relevant documentation before adding dependencies or implementing duplicate functionality.",
}

FALLBACKS = {
    "decision-mapping": "List decisions that materially affect the requested outcome. For each, record options, constraints, dependencies, reversibility, owner, and the evidence needed to choose. Resolve choices already implied by repository conventions; ask about only decisions that affect scope or correctness. Deliver a decision map and a concrete next implementation step, without treating every preference as a blocker.",
    "request-refactor-plan": "Inspect the current implementation, callers, and regression coverage. State the concrete maintainability problem and the observable behaviors that must remain unchanged. Propose a sequence of small changes with touched modules, compatibility boundaries, and checks for each step. Flag data migrations or API breaks explicitly. Deliver the requested plan; implement it only when implementation is within the user's request.",
    "qa": "Translate the feature brief or bug report into observable acceptance cases. Exercise the main journey and relevant permission, failure, empty, concurrency, or recovery cases. Record exact setup, inputs, commands, and outcomes. For a failure, isolate a reproducible case and distinguish implementation defects from environment limitations. Fix and retest when requested; report checks not performed rather than treating missing evidence as a pass.",
    "to-prd": "Describe the target users, current problem, desired outcome, scope, and explicit non-goals from the supplied context. Define functional behavior, key user journeys, constraints, dependencies, measurable acceptance criteria, and open decisions. Separate observed evidence from assumptions. Keep implementation details only where they constrain the product; avoid invented market claims, delivery estimates, or approvals.",
    "insecure-defaults": "Trace configuration values from defaults and environment parsing into sensitive operations. Look for development credentials, debug exposure, permissive origin or network rules, disabled verification, unchecked authorization, and fail-open error handling. Demonstrate the reachable unsafe condition in a local test where practical. Propose a secure default and an explicit opt-in for legitimate development cases; preserve a documented migration path and retest both allowed and denied behavior.",
    "building-ai-agent-on-cloudflare": "Inspect the selected Workers and Agents SDK versions, Wrangler configuration, bindings, authentication, state storage, and model provider. Implement the requested agent interaction with typed tool inputs, bounded retries, cancellation, and durable state only where needed. Keep provider credentials in the platform secret mechanism. Verify a useful task, a tool error, and an unauthorized request locally; prepare deployment instructions without claiming a deployed service unless deployment was requested and verified.",
}

EXTRAS = [
    ("code-build", "General Coding Workflow", "Plan, implement, debug, and verify a software task in its existing language and stack.", "Inspect the relevant source, current behavior, user request, and repository instructions. Choose the smallest useful set of coding skills for the task: requirements or architecture for unresolved design, the actual stack for implementation, and a suitable testing or debugging workflow for verification. Build the complete requested result, preserve unrelated work, and report concrete evidence. Do not load all installed skills for every task."),
    ("web-backend", "Backend Workflow", "Route a backend task to the appropriate architecture, API, database, stack, security, or operations workflow.", "Trace the request through routing, validation, authentication, domain rules, persistence, background work, and observability as applicable. Select only the matching stack and the specialist skills needed for the request. Implement the scoped service behavior and verify its success, failure, and permission paths. Use existing infrastructure and interfaces unless the user requests a change."),
    ("web-backend-codequality", "Backend Code Quality", "Improve backend correctness and maintainability across boundaries, data handling, concurrency, and error paths.", "Inspect a representative request or job path before refactoring. Check validation at boundaries, authorization at sensitive operations, ownership of transactions and state, cancellation and timeout behavior, and error propagation. Prefer clear interfaces and explicit invariants over generic abstraction layers. Make a focused improvement and verify relevant observable behavior; use the code quality, review, contract, or stack workflow that addresses the actual problem."),
    ("web-backend-security", "Backend Security", "Review and repair backend authentication, object authorization, input handling, session, and secret boundaries.", "Trace untrusted input and identity through each sensitive operation. Check object-level authorization, injection-safe queries, output handling, session and CSRF controls where relevant, and redacted failures. Reproduce concrete issues locally and verify allowed and denied cases after fixing them. Distinguish a scoped review from a claim that the whole service is secure."),
    ("web-backend-observability", "Backend Observability", "Design and verify useful service logs, traces, metrics, and alert signals with bounded overhead.", "Identify service entrypoints, external calls, background jobs, and meaningful failure boundaries. Reuse existing telemetry conventions, propagate correlation context, redact sensitive values, and bound label cardinality. Verify a representative success and failure path emits useful signals. Use Sentry-specific workflows only for Sentry projects; separate local verification from evidence from a connected production system."),
]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def should_copy(path):
    return not ({".git", "node_modules", "__pycache__", ".pytest_cache", "agents"} & set(path.parts)) and path.suffix not in {".pyc", ".pyo"}


def copy_tree(source, destination):
    for path in source.rglob("*"):
        relative = path.relative_to(source)
        if path.is_file() and not path.is_symlink() and should_copy(relative):
            # Source entrypoints become reference documents, not extra installed skills.
            if relative.name == "SKILL.md":
                relative = relative.with_name("UPSTREAM.md")
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)


def description_for(request, selected):
    name = request["requested"]
    if name in DESCRIPTIONS:
        return DESCRIPTIONS[name]
    text = re.sub(r"\s+", " ", str(selected["metadata"].get("description", ""))).strip()
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    if len(first) > 360:
        first = first[:357].rsplit(" ", 1)[0] + "..."
    return first or f"Apply {name.replace('-', ' ')} to the requested software task."


def support_files(record, selected, target):
    """Retain explicitly linked sibling plugin resources without escaping the repo."""
    staging = Path(selected["staged"])
    repo_container = staging.parents[1]
    checkout = next(p for p in repo_container.iterdir() if p.is_dir() and p.name != "installed")
    original_root = (checkout / selected["path"]).parent
    mapping = {}
    queue = list(original_root.rglob("*.md"))
    seen = set()
    while queue:
        document = queue.pop()
        if document in seen:
            continue
        seen.add(document)
        text = document.read_text(encoding="utf-8-sig", errors="replace")
        links = re.findall(r"\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)
        for link in links:
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith(("#", "/", "$")):
                continue
            name = unquote(link.split("#", 1)[0])
            if not name:
                continue
            source = (document.parent / name).resolve()
            if not source.is_relative_to(checkout.resolve()) or not source.exists() or source.is_relative_to(original_root.resolve()):
                continue
            external_paths = list(source.rglob("*")) if source.is_dir() else [source]
            for path in external_paths:
                if not path.is_file() or path.is_symlink() or not should_copy(path.relative_to(checkout)):
                    continue
                relative = Path("upstream-support") / path.relative_to(checkout)
                if relative.name == "SKILL.md":
                    relative = relative.with_name("UPSTREAM.md")
                destination = target / relative
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, destination)
                mapping[path.relative_to(checkout).as_posix()] = relative.as_posix()
                if path.suffix == ".md":
                    queue.append(path)
    if mapping:
        write(target / "RESOURCE_PATHS.json", json.dumps(mapping, indent=2))
    return mapping


def main():
    inventory = json.loads((ROOT / ".work/backend-import/inventory.json").read_text(encoding="utf-8"))
    if inventory["errors"]:
        raise SystemExit(f"Resolve import errors before building: {inventory['errors']}")
    sources = {r["repository"]: r for r in inventory["sources"]}
    entries = []
    for request in requests():
        record = sources[request["repository"]]
        selected = record["selected"].get(request["requested"])
        target = DESTINATION / request["id"]
        title = "GNCore " + request["id"].removeprefix("web-backend-").removeprefix("code-").replace("-", " ").title()
        entry = {**request, "title": title, "revision": record["revision"], "category": "backend-engineering" if request["id"].startswith("web-backend") else "code-engineering", "tags": [request["group"], request["requested"], "backend" if request["id"].startswith("web-backend") else "coding"]}
        if selected:
            copy_tree(Path(selected["staged"]), target)
            entry.update({"kind": "adapted", "source_path": selected["path"], "upstream_metadata": selected["metadata"], "description": description_for(request, selected)})
            entry["support_paths"] = support_files(record, selected, target)
            for index, (name, content) in enumerate(selected["notices"].items()):
                write(target / "notices" / f"{index + 1}-{Path(name).name}", content)
            # Trail of Bits publishes its collection under CC BY-SA 4.0.
            entry["license"] = "CC-BY-SA-4.0" if request["repository"] == "trailofbits/skills" else "See retained upstream notices and metadata"
            source_url = f"https://github.com/{request['repository']}/blob/{record['revision']}/{selected['path']}"
            write(target / "SOURCE.md", f"# Source and modifications\n\nGNCore adaptation of [{request['repository']} / {request['requested']}]({source_url}).\n\nRevision: `{record['revision']}`.\n\nUpstream metadata:\n\n```json\n{json.dumps(selected['metadata'], indent=2, ensure_ascii=False)}\n```\n\nModifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.\n\nUpstream notice origins: {', '.join(selected['notices']) or 'none supplied'}. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.\n\nAttribution and license: {entry['license']}. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.\n")
            references = "Read [UPSTREAM.md](UPSTREAM.md) for the relevant technical details, then load only the references needed for this task. The source document is reference material for this GNCore adaptation. Resolve relative resource paths from this installed skill folder; use `RESOURCE_PATHS.json` for relocated sibling files when present. Replace historical `.claude/skills/`, `${CLAUDE_SKILL_DIR}`, or plugin-root placeholders with the actual installed paths."
            technical = "Use the technical guidance within the user's actual scope. Upstream harness-specific tools, universal activation mandates, automatic commits, setup prompts, and mandatory approval sequences do not become requirements of this adaptation. Use an equivalent available host capability where it preserves the workflow; otherwise state the missing capability and complete independent work. Additional agents require support and authorization for the current task."
            detail = request["guidance"]
        else:
            entry.update({"kind": "original-replacement", "description": DESCRIPTIONS[request["requested"]], "license": "MIT", "reason": "Requested name absent from the verified source revision."})
            detail = FALLBACKS[request["requested"]]
            write(target / "SOURCE.md", f"# Original GNCore replacement\n\nCopyright (c) 2026 Ganesh Naidu. MIT license.\n\nThe requested `{request['requested']}` name was absent from `{request['repository']}` at `{record['revision']}`. This independently written workflow covers that requested capability; it is not an installation of the unavailable upstream skill.\n")
            shutil.copyfile(ROOT / "LICENSE", target / "LICENSE")
            references = "See [SOURCE.md](SOURCE.md) for the verified missing source name and the original replacement's license."
            technical = "Follow the actual request and available repository conventions; this workflow does not require an external plugin or a particular issue tracker."
        body = f"# {title}\n\n{detail}\n\n## Detailed guidance\n\n{references}\n\n## GNCore execution scope\n\n{technical}\n\nKeep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.\n\nSee [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices."
        license_field = "\nlicense: CC-BY-SA-4.0" if entry["license"] == "CC-BY-SA-4.0" else ""
        write(target / "GUIDE.md", f"---\nname: {entry['id']}\ndescription: {json.dumps(entry['description'], ensure_ascii=False)}{license_field}\n---\n\n{body}")
        entries.append(entry)
    for skill_id, title, description, body in EXTRAS:
        write(DESTINATION / skill_id / "GUIDE.md", f"---\nname: {skill_id}\ndescription: {json.dumps(description)}\n---\n\n# GNCore {title}\n\n{body}\n")
        entries.append({"id": skill_id, "title": f"GNCore {title}", "description": description, "kind": "original", "category": "backend-engineering" if skill_id.startswith("web-backend") else "code-engineering", "tags": ["coding", "backend" if skill_id.startswith("web-backend") else "workflow"], "license": "MIT"})
    for entry in entries:
        target = DESTINATION / entry["id"]
        entry["resources"] = sorted(p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file() and p.name != "SKILL.md" and should_copy(p.relative_to(target)))
    write(DESTINATION / "manifest.json", json.dumps(entries, indent=2, ensure_ascii=False))
    adapted = sum(e["kind"] == "adapted" for e in entries)
    missing = [e for e in entries if e["kind"] == "original-replacement"]
    docs = ["# Backend and general coding skills", "", f"GNCore adds **{len(entries)} workflows** for the 122 requested skills: {adapted} attributed adaptations, {len(missing)} original replacements for unavailable source names, and five original selection/quality/security/observability workflows.", "", "## Use the collection", "", "```bash", "gncore show web-backend-codequality", "gncore search code-debugging", "gncore export --skills code-build code-quality code-debugging web-backend-codequality", "```", "", "Install all backend and coding skills from this checkout for Codex:", "", "```bash", "npx skills add ./src/gncore/skills/backend_data --skill '*' --agent codex --yes --copy", "```", "", "Skills install under `.agents/skills/`. They provide instructions and resources, not the language runtimes, scanners, browsers, platform credentials, external plugins, or server infrastructure described in those instructions. Select the actual task's stack and workflows; installing the collection does not require loading all skills for every request.", "", "## Unavailable source names", "", "These names were absent from the recorded source revisions. Their GNCore entries are independently written replacements:", "", *[f"- `{e['requested']}` from `{e['repository']}` → `{e['id']}`" for e in missing], "", "## Source mapping", "", "| Requested skill | GNCore ID | Integration |", "| --- | --- | --- |"]
    for entry in entries:
        if "requested" in entry:
            url = f"https://github.com/{entry['repository']}/tree/{entry['revision']}"
            docs.append(f"| [{entry['requested']}]({url}) | `{entry['id']}` | {entry['kind']} |")
    docs.extend(["", "## Attribution and licensing", "", "Every adaptation retains its source entrypoint, supplied resources, notices, upstream metadata, and pinned revision. GNCore entrypoints rewrite discovery and scope for portable use. **Trail of Bits material and its GNCore adaptations retain CC BY-SA 4.0**, including attribution and share-alike terms; the rest retain their supplied MIT/Apache or other notices. Root package MIT licensing applies to GNCore code and its independent original workflows, not a blanket relicensing of bundled content.", "", "Some source workflows require a specific host tool, an authenticated Sentry connection, platform CLI, scanner, or optional companion skill. Use equivalent supported capabilities only when they preserve the task; report unavailable capabilities instead of claiming execution. Tool names in source references do not install those tools or expand authorization.", "", "## Maintenance and compatibility", "", "Edit `scripts/backend_requests.py` for requested sources, names, and routing, and `scripts/build_backend_suite.py` for GNCore entrypoint adaptations. `scripts/import_backend_sources.py` stages pinned archives with the bundled Codex installer; it needs GitHub access and the optional Python `skills` extra. Its per-source inventories record exact matches and missing names. Generic Skills CLI updates do not merge future upstream changes into authored adaptations; review and rebuild deliberately.", "", "The 40 frontend skills and 30 domain packs remain available. Overlapping legacy backend specialist IDs resolve through `src/gncore/skills/backend.py` to their new entrypoints; existing exports in other projects are not automatically removed.", "", "This collection remains unreleased. Complete the release review and choose the release version before tagging or publishing."])
    write(ROOT / "docs/BACKEND_SKILLS.md", "\n".join(docs))
    print(f"Built {len(entries)} skills: {adapted} adaptations, {len(missing)} original replacements, {len(EXTRAS)} original entrypoints.")
    print(f"Resources: {sum(len(e['resources']) for e in entries)}")


if __name__ == "__main__":
    main()
