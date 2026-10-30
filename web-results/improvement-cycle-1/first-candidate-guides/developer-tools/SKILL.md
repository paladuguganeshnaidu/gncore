---
name: developer-tools
description: "Build reliable CLIs, developer workflows, editor integrations and local tooling."
license: MIT
---

# GNCore Developer Tools

Version: 7.0.0rc1

## Choose the work

Preserve established commands, stdout contracts and exit codes. Keep interactive UX optional for automation; preview consequential filesystem changes before applying them.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A scriptable interface with actionable errors, documented inputs, stable output, and interruption/cleanup behavior.

Exercise help, malformed options, spaces/Unicode paths, noninteractive use, failure exits and interrupted writes using isolated fixtures.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Preflight repository ownership, dirty state, path/branch collisions and the intended base before creating workspaces or files. Use argument arrays or correctly quoted explicit paths rather than generated shell strings. Make partial creation and interruption recoverable: detect owned incomplete state, preserve unrelated edits, and explain safe retry/cleanup. Define exit codes and diagnostics that distinguish invalid input, conflicts and environmental failure; verify paths containing spaces and concurrent invocations.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- For repository/workspace changes, preflight ownership, dirty paths and collisions; journal only owned partial state and preserve intervening user work during recovery.
- Use explicit paths and argument arrays; handle option-like values at the invoked program's boundary. Define actionable exit behavior and verify spaces, Unicode and interruption.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cli-design` | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |
| `tooling-reproducible-env` | Reproducible developer environments. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
