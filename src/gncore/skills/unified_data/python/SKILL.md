---
name: python
description: "Build, profile, package and migrate Python applications and libraries with reproducible environments."
license: MIT
---

# GNCore Python

Version: 7.0.0

## Choose the work

Inspect supported interpreters, public APIs, build backend and dependency conventions. Use async for actual asynchronous I/O, and profile before choosing optimization or native extensions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Typed maintainable modules, a stable public contract, appropriate packaging metadata and an environment/reproduction command.

Run regressions, clean imports and interpreter checks relevant to the changed behavior. For packaging/resources/distribution work, verify the built sdist and its wheel outside the checkout; ordinary Python fixes do not require release work.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Match the verification boundary to the change: ordinary Python behavior, concurrency and performance work do not automatically require a distribution build. When packaging or resources change, test the produced sdist and wheel in clean environments outside the checkout, including entrypoints and working-directory behavior.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- For ordinary fixes, preserve API/runtime behavior and run relevant regressions without imposing a package release workflow.
- For packaging/resources/distribution changes, build the wheel from the produced sdist, inspect metadata/resources/entrypoints and clean-install outside the checkout across supported interpreters and working directories.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `python-library` | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-packaging` | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-migration` | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
