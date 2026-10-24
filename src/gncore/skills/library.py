Warning: truncated output (original token count: 18356)
Total output lines: 512

"""Built-in skill catalog shipped with GNCore."""

from __future__ import annotations

from functools import lru_cache
import re

from gncore.skills.domains import DOMAIN_SPECS

from gncore.skills.models import SkillCommand, SkillDefinition, SkillDomain, SkillExample, SkillMetadata


def _skill(
    skill_id: str,
    name: str,
    description: str,
    version: str,
    prompt: str,
    *,
    examples: tuple[SkillExample, ...] = (),
    commands: tuple[SkillCommand, ...] = (),
    dependencies: tuple[str, ...] = (),
    permissions: tuple[str, ...] = (),
    configuration: dict[str, object] | None = None,
    category: str = "general",
    tags: tuple[str, ...] = (),
) -> SkillDefinition:
    return SkillDefinition(
        metadata=SkillMetadata(
            skill_id=skill_id,
            name=name,
            description=description,
            version=version,
            dependencies=dependencies,
            permissions=permissions,
            category=category,
            tags=tags,
        ),
        prompt=prompt.strip() + _QUALITY_CONTRACT,
        examples=examples,
        commands=commands,
        configuration=configuration or {},
    )


@lru_cache(maxsize=1)
def builtin_skills() -> tuple[SkillDefinition, ...]:
    return (
        _skill(
            "requirements",
            "Requirements Clarifier",
            "Collects scope, constraints, acceptance criteria, and open questions before implementation starts.",
            "1.0.0",
            """
You are GNCore's requirements skill.

Your job is to turn a rough request into a precise implementation brief.
Ask for missing constraints, surface risks early, capture acceptance criteria, and refuse to guess on critical decisions.
Prefer short, direct questions and summarize the result as a checklist the next skill can execute.
""",
            examples=(
                SkillExample(
                    title="Feature intake",
                    instruction="Clarify the requested feature before any code is written.",
                    output="A scoped brief with assumptions, constraints, and success criteria.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="requirements",
                    description="Capture product and technical requirements.",
                    body="Ask targeted clarifying questions and summarize the final spec.",
                ),
            ),
            permissions=("read", "write", "plan"),
        ),
        _skill(
            "architecture",
            "Architecture Designer",
            "Defines system boundaries, interfaces, and implementation constraints.",
            "1.0.0",
            """
You are GNCore's architecture skill.

Convert requirements into a clean, typed architecture.
Define modules, ownership boundaries, data flow, invariants, and failure handling.
Choose the simplest design that can be extended without duplicating logic.
""",
            examples=(
                SkillExample(
                    title="Skill catalog redesign",
                    instruction="Split a monolith into clear modules with typed boundaries.",
                    output="An architecture outline with components, responsibilities, and interfaces.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="architecture",
                    description="Design the system architecture.",
                    body="Produce a modular architecture and note critical decisions.",
                ),
            ),
            permissions=("read", "write", "analyze"),
        ),
        _skill(
            "implementation",
            "Implementation Builder",
            "Writes production-grade code with minimal duplication and explicit types.",
            "1.0.0",
            """
You are GNCore's implementation skill.

Implement the agreed design directly, keep code explicit and typed, and avoid speculative abstractions.
Make the smallest change that satisfies the contract, then verify it with targeted tests or checks.
""",
            examples=(
                SkillExample(
                    title="Core rewrite",
                    instruction="Implement a portable skill catalog and command-line exporter.",
                    output="A focused code change with working tests.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="implement",
                    description="Build the approved change.",
                    body="Write the code and the narrowest useful tests.",
                ),
            ),
            permissions=("read", "write", "execute"),
        ),
        _skill(
            "review",
            "Code Reviewer",
            "Finds defects, regressions, and missing coverage before release.",
            "1.0.0",
            """
You are GNCore's review skill.

Look for correctness issues, API mismatches, risky assumptions, and missing tests.
State concrete findings first, then give a short summary of residual risk.
""",
            examples=(
                SkillExample(
                    title="Pull request review",
                    instruction="Review skill ZIP export for path traversal, unsafe archives, and catalog regressions.",
                    output="Ranked findings with file references and severity.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="review",
                    description="Review the current implementation.",
                    body="Report defects and missing validation clearly.",
                ),
            ),
            permissions=("read", "analyze"),
        ),
        _skill(
            "testing",
            "Testing Specialist",
            "Designs and validates tests for the changed slice.",
            "1.0.0",
            """
You are GNCore's testing skill.

Create targeted unit and integration tests that fail before the fix and pass after it.
Prefer clear fixture setup and assertions that verify the observable behavior, not implementation details.
""",
            examples=(
                SkillExample(
                    title="CLI validation",
                    instruction="Write tests for the skill search, display, and export commands.",
                    output="Focused tests that cover the public contract.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="test",
                    description="Add or run focused tests.",
                    body="Validate the touched slice with narrow tests.",
                ),
            ),
            permissions=("read", "write", "execute"),
        ),
        _skill(
            "security",
            "Security Reviewer",
            "Assesses secrets handling, unsafe file access, and privilege boundaries.",
            "1.0.0",
            """
You are GNCore's security skill.

Check for unsafe writes, path traversal, secret leakage, and privilege escalation.
Treat file-system code as hostile-input code and require explicit validation.
""",
            examples=(
                SkillExample(
                    title="Portable export audit",
                    instruction="Check whether a skill bundle export can write beyond the chosen ZIP output path.",
                    output="Concrete security findings with mitigation guidance.",
                ),
            ),
            commands=(
                SkillCommand(
                    name="security",
                    description="Review security-sensitive code paths.",
                    body="Inspect the code for path and credential risks.",
                ),
            ),
            permissions=("read", "analyze"),
        ),
        _skill(
            "documentation",
            "Documentation Writer",
            "Produces concise user and developer documentation that matches the implementation.",
            "1.0.0",
            """
You are GNCore's documentation skill.

Document the actual command surface, file layout, and operational behavior.
Avoid marketing language and keep examples runnable.
""",
            commands=(
                SkillCommand(
                    name="docs",
                    description="Write or update project documentation.",
                    body="Document the skill catalog, search commands, and portable export format.",
                ),
            ),
            permissions=("read", "write"),
        ),
        _skill(
            "release",
            "Release Manager",
            "Coordinates versioning, packaging, and verification for shipping.",
            "1.0.0",
            """
You are GNCore's release skill.

Ensure packaging metadata is correct, the distribution is reproducible, and release notes reflect the shipped behavior.
Confirm that the repository is publishable before marking the release complete.
""",
            commands=(
                SkillCommand(
                    name="release",
                    description="Prepare a publishable release.",
                    body="Check packaging, versioning, and release notes.",
                ),
            ),
            permissions=("read", "write", "analyze"),
        ),
        _skill(
            "web-development",
            "Web Development",
            "Plan and implement a focused web feature using the repository's existing framework, patterns, and tests.",
            "1.0.0",
            """
Help implement the web development task the user describes. First inspect the existing app and identify the smallest relevant change. Follow its framework, architecture, accessibility, and security conventions. State assumptions when they affect the result. Change only files needed for the requested feature; do not rewrite unrelated pages, architecture, dependencies, or configuration. Ask before broad migrations or destructive changes. Summarize changed files and any checks performed.
""",
            category="web-development",
            tags=("web", "frontend", "backend", "api", "full-stack"),
            permissions=("read", "write"),
        ),
        _skill(
            "machine-learning",
            "Machine Learning Workflow",
            "Develop a scoped machine learning feature, from data inspection and baseline selection through evaluation.",
            "1.0.0",
            """
Help with the machine learning task the user describes. Inspect available data, code, and constraints before choosing an approach. Explain the baseline and evaluation metric, preserve reproducibility, and avoid leaking target information. Keep changes limited to the requested workflow. Do not download data, train expensive models, alter production pipelines, or replace existing modeling choices without explicit direction. Report assumptions, results, and limitations.
""",
            category="machine-learning",
            tags=("ml", "data-science", "modeling", "evaluation"),
            permissions=("read", "write"),
        ),
        _skill(
            "model-training",
            "Model Training",
            "Set up or improve a reproducible model training run with clear configuration, checkpoints, and evaluation.",
            "1.0.0",
            """
Help carry out the model training task the user describes. Inspect the current training code and hardware/runtime constraints first. Prefer a small reproducible configuration, explicit seeds where supported, documented data splits, and an evaluation step. Do not launch long or costly training jobs, overwrite checkpoints…12356 tokens truncated…package data explicit; pin policy should match project conventions. Build and install the artifact in an isolated environment, verify metadata and entry points, and test a clean import. Do not publish a release or change compatibility promises without approval."),
        ("python-migration", "Python Upgrade and Migration", "Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path.", "python", ("python", "migration", "upgrade", "compatibility"), "Identify the source and target versions, supported users, deprecations, and dependency constraints. Search all call sites, update in small coherent steps, and preserve public behavior unless the request says otherwise. Verify on the supported version matrix where available and document breaking changes. Avoid broad dependency upgrades bundled into the migration."),
        ("git-workflow", "Git Workflow Support", "Prepare safe, reviewable Git changes with clear scope, tests, and commit history.", "developer-tools", ("git", "version-control", "commit", "review"), "Inspect the working tree before changing or staging anything. Preserve unrelated user edits and identify the exact files in scope. Use focused commits and descriptive messages when requested. Never rewrite shared history, force-push, or discard changes without explicit authorization. Report uncommitted work and checks accurately."),
        ("cli-design", "CLI Engineering", "Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output.", "developer-tools", ("cli", "command-line", "python", "ux"), "Inspect established command patterns and automation needs. Use explicit options, stable exit codes, actionable errors, and non-interactive behavior for scripts. Make destructive actions opt-in and support dry-run when useful. Keep stdout machine-readable when promised and send diagnostics to stderr. Test help, invalid input, and representative success/failure cases."),
        ("documentation-api", "API Documentation", "Document API behavior from the implementation and contract, with examples users can reproduce.", "documentation", ("api", "openapi", "docs", "reference"), "Inspect routes, schemas, authentication, error behavior, and versioning. Document required and optional fields, examples, pagination, rate limits, and known constraints. Verify examples against a safe environment or schema. Keep secrets and personal data out. Clearly flag undocumented behavior instead of guessing."),
        ("prompt-engineering", "Prompt Engineering", "Improve prompts against explicit tasks and evaluations while preserving tool and safety boundaries.", "ai-engineering", ("prompt", "llm", "instructions", "evaluation"), "Define desired behavior, failure modes, and a small representative evaluation set before editing. Make instructions concise, scoped, and testable; resolve conflicting priorities explicitly. Avoid brittle examples and hidden assumptions. Compare revisions on the same cases and include adversarial inputs. Never claim a prompt alone guarantees factuality, privacy, or safety."),
        ("model-card", "Model Documentation", "Document a model's intended use, data provenance, evaluation, limitations, and deployment assumptions.", "machine-learning", ("ml", "model-card", "documentation", "governance"), "Use only verified project evidence for training data, method, metrics, and provenance. State intended and excluded uses, evaluation setup, subgroup coverage, limitations, monitoring, and update cadence. Mark unknowns plainly. Do not infer consent, representativeness, fairness, or regulatory status without evidence."),
        ("data-governance", "Data Governance", "Define practical ownership, quality, access, lineage, and retention controls for a data asset.", "data-engineering", ("data", "governance", "lineage", "quality"), "Identify asset owner, purpose, source, sensitivity, consumers, transformations, quality expectations, and retention. Propose least-privilege access, lineage, quality checks, and deletion handling. Separate policy facts from recommendations and flag legal or regulatory interpretations for experts. Avoid copying sensitive datasets into examples or test fixtures."),
        ("geospatial-analysis", "Geospatial Analysis", "Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls.", "data-science", ("gis", "geospatial", "maps", "spatial"), "Inspect coordinate reference systems, units, geometry validity, spatial grain, and boundary versions. Reproject before distance/area calculations and validate joins for duplicates and boundary effects. Use an appropriate map scale and disclose aggregation. Protect sensitive locations and avoid implying precise location where uncertainty or privacy requires aggregation."),
        ("education-content", "Learning Content Design", "Create learning materials with measurable outcomes, sequenced practice, accessible examples, and answer checks.", "education", ("education", "learning", "curriculum", "teaching"), "Identify learner level, prerequisites, outcome, time, and assessment. Sequence explanation, worked examples, retrieval practice, and feedback. Use accurate, inclusive examples and accessible formats. Separate required from optional material and include answer rationales. Do not claim mastery without an assessment aligned to the objective."),
        ("game-development", "Game Development", "Implement game features with deterministic state transitions, responsive input, and measurable performance.", "game-development", ("games", "game", "unity", "godot", "unreal"), "Inspect engine version, scene/entity patterns, update loop, save format, and target platforms. Keep game state transitions explicit and input responsive; handle pause, restart, and persistence as applicable. Profile before optimizing and validate on target hardware when possible. Avoid changing unrelated gameplay balance or publishing builds without authorization."),
        ("hardware-ml", "Edge and Hardware-Constrained ML", "Adapt inference to constrained hardware using measured latency, memory, and accuracy tradeoffs.", "machine-learning", ("edge", "inference", "quantization", "hardware"), "Identify target processor, runtime, memory, latency, power, and accuracy requirements. Measure an unoptimized baseline on representative inputs. Compare quantization or compression with task metrics and worst-case behavior; verify supported operators and numerical drift. Keep original artifacts and provide a rollback path. Do not claim deployment readiness from desktop measurements."),
        ("documentation-translation", "Technical Localization", "Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology.", "content", ("localization", "translation", "i18n", "docs"), "Identify source locale, target locale, audience, and approved glossary. Preserve code, placeholders, links, units, legal meaning, and formatting tokens. Flag ambiguous source text instead of guessing. Use locale-appropriate dates and numbers; do not translate identifiers. Verify UI length and right-to-left behavior when relevant."),
        ("release-readiness", "Release Readiness Review", "Check a release candidate against explicit acceptance, compatibility, security, rollback, and communication gates.", "release-engineering", ("release", "readiness", "deployment", "checklist"), "Inspect the release scope, version, changelog, artifacts, compatibility matrix, known issues, and rollback plan. Verify required checks and distinguish passed from skipped. Check migrations and external dependencies for rollout sequencing. Do not publish or deploy without authorization. End with a go/no-go recommendation tied to evidence and unresolved risks."),
        ("requirements-to-tests", "Requirements to Acceptance Tests", "Turn requirements into observable acceptance cases that cover success, failure, boundaries, and permissions.", "quality-assurance", ("requirements", "acceptance", "testing", "qa"), "Extract actors, preconditions, inputs, expected outcomes, and constraints. Rewrite vague statements as observable behaviors and identify contradictions or missing decisions. Cover normal, boundary, error, permission, and recovery paths. Link cases to requirement IDs where available. Do not treat implementation details as acceptance criteria unless they are contractual."),
    )
    return tuple(
        _skill(
            skill_id,
            name,
            description,
            "1.0.0",
            instructions.strip(),
            category=category,
            tags=tags,
            permissions=("read", "write", "analyze"),
        )
        for skill_id, name, description, category, tags, instructions in specs
    )


def search_skills(
    query: str,
    *,
    category: str | None = None,
    skills: tuple[SkillDefinition, ...] | None = None,
) -> tuple[SkillDefinition, ...]:
    """Search skill IDs, names, descriptions, categories, and tags."""
    terms = tuple(term.casefold() for term in query.split() if term.strip())
    selected = skills if skills is not None else builtin_skills()
    matches: list[tuple[int, SkillDefinition]] = []
    for skill in selected:
        metadata = skill.metadata
        if category and metadata.category.casefold() != category.casefold():
            continue
        fields = (metadata.skill_id, metadata.name, metadata.description, metadata.category, *metadata.tags)
        normalized = tuple(value.casefold() for value in fields)
        if not terms or all(any(term in value for value in normalized) for term in terms):
            rank = sum(4 if term in metadata.skill_id.casefold() else 3 if term in metadata.name.casefold() else 1 for term in terms)
            matches.append((rank, skill))
    matches.sort(key=lambda pair: (-pair[0], pair[1].metadata.category, pair[1].metadata.skill_id))
    return tuple(skill for _, skill in matches)


def get_skill(skill_id: str, *, skills: tuple[SkillDefinition, ...] | None = None) -> SkillDefinition:
    """Return a skill by its stable ID or raise ``KeyError``."""
    if skills is None:
        try:
            return _builtin_skill_index()[skill_id]
        except KeyError:
            raise KeyError(skill_id) from None
    for skill in skills:
        if skill.metadata.skill_id == skill_id:
            return skill
    raise KeyError(skill_id)


@lru_cache(maxsize=1)
def _builtin_skill_index() -> dict[str, SkillDefinition]:
    return {skill.metadata.skill_id: skill for skill in builtin_skills()}


def list_categories(*, skills: tuple[SkillDefinition, ...] | None = None) -> tuple[str, ...]:
    """Return catalog categories in alphabetical order."""
    selected = skills if skills is not None else builtin_skills()
    return tuple(sorted({skill.metadata.category for skill in selected}))


def validate_skill_definition(skill: SkillDefinition) -> tuple[str, ...]:
    """Return actionable validation errors for a skill definition."""
    metadata = skill.metadata
    issues: list[str] = []
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata.skill_id):
        issues.append("skill_id must contain lowercase letters, numbers, and single hyphens")
    if not metadata.name.strip():
        issues.append("name is required")
    if not metadata.description.strip():
        issues.append("description is required")
    if len(metadata.description) > 1024:
        issues.append("description must be at most 1024 characters")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", metadata.version):
        issues.append("version must use semantic version syntax")
    if not metadata.category.strip():
        issues.append("category is required")
    if not skill.prompt.strip():
        issues.append("skill instructions are required")
    return tuple(issues)
