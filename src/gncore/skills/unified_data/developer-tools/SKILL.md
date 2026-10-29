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

## Deliver and verify

A scriptable interface with actionable errors, documented inputs, stable output, and interruption/cleanup behavior.

Exercise help, malformed options, spaces/Unicode paths, noninteractive use, failure exits and interrupted writes using isolated fixtures.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cli-design` | Design command-line tools with predictable arguments, clear errors, safe defaults, and scriptable output. |
| `tooling-reproducible-env` | Reproducible developer environments. |

## Focused procedures

### CLI Engineering (`cli-design`)

Inspect established command patterns and automation needs. Use explicit options, stable exit codes, actionable errors, and non-interactive behavior for scripts. Make destructive actions opt-in and support dry-run when useful. Keep stdout machine-readable when promised and send diagnostics to stderr. Test help, invalid input, and representative success/failure cases.

### Reproducible developer environments (`tooling-reproducible-env`)

Inspect existing lockfiles, compiler/runtime versions and setup scripts. Pin the reproducibility boundary without adding an unrelated toolchain; verify a clean setup and document platform-specific requirements, cache assumptions and offline limits.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
