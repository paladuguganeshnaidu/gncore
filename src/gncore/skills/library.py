"""Built-in skill catalog shipped with GNCore."""

from __future__ import annotations

from functools import lru_cache

from gncore.core.models import SkillCommand, SkillDefinition, SkillExample, SkillMetadata


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
) -> SkillDefinition:
    return SkillDefinition(
        metadata=SkillMetadata(
            skill_id=skill_id,
            name=name,
            description=description,
            version=version,
            dependencies=dependencies,
            permissions=permissions,
        ),
        prompt=prompt.strip(),
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
                    title="Installer redesign",
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
                    instruction="Implement the new adapter-driven installer.",
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
                    instruction="Review the installer for regressions and unsafe file writes.",
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
                    instruction="Write tests for the activate and list commands.",
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
                    title="Installer audit",
                    instruction="Check whether backup and restore can overwrite arbitrary files.",
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
                    body="Document how the installer works and how to use it.",
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
    )
