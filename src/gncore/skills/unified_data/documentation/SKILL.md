---
name: documentation
description: "Write technical references, tutorials, API documentation and migration guides from verified software behavior."
license: MIT
---

# GNCore Documentation

Version: 7.0.0

## Choose the work

Identify the reader and task. Derive claims from code, schemas and observed commands; preserve identifiers, placeholders and supported version boundaries.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Task-oriented documentation with reproducible examples, prerequisites, error cases and migration or compatibility notes when needed.

Execute practical examples in an isolated environment, check local links and compare documented commands/schema fields with implementation. Mark examples that require unavailable services.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Derive examples from the real help/API contract, including prerequisites, changed defaults and compatibility boundaries. Make examples copyable without inventing flags or endpoints. Include a realistic failure and safe recovery route, such as an existing output collision, while preserving user data. Label untested examples explicitly and verify commands, links and migration behavior when execution is available.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Use only the supplied or verified API/help contract; label illustrative schema, status codes and assumptions instead of presenting invented fields as requirements.
- For procedural/migration guides, include compatible shell/platform examples and a recoverable failure path; preserve scope for narrow edits and distinguish unexecuted examples.
- Give a self-contained example a reader can copy. If the wire schema is incomplete, clearly label every assumption or supply a runnable offline mock/client example that preserves the known contract; do not imply unverified wire compatibility or leave the only example as non-runnable placeholder prose.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `documentation-translation` | Adapt technical content across languages while preserving product meaning, UI limits, and verified terminology. |
| `technical-writing` | Write accurate, task-oriented technical documentation with runnable examples and clear prerequisites. |
| `documentation-api` | Document API behavior from the implementation and contract, with examples users can reproduce. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
