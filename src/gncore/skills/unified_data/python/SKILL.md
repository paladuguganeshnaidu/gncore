---
name: python
description: "Build, profile, package and migrate Python applications and libraries with reproducible environments."
license: MIT
---

# GNCore Python

Version: 7.0.0rc1

## Choose the work

Inspect supported interpreters, public APIs, build backend and dependency conventions. Use async for actual asynchronous I/O, and profile before choosing optimization or native extensions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Typed maintainable modules, a stable public contract, appropriate packaging metadata and an environment/reproduction command.

Run meaningful tests, clean imports and relevant interpreter checks. Verify the built wheel instead of relying on an editable checkout.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `python-library` | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-packaging` | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-migration` | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |

## Focused procedures

### Python Library Engineering (`python-library`)

Inspect supported Python versions, packaging backend, and public imports. Keep public APIs small and backward-compatible unless a breaking change is requested. Use explicit types and focused modules, avoid import-time side effects, declare runtime dependencies accurately, and provide a minimal runnable example. Check wheel and source inclusion rules when packaging changes.

### Python Packaging (`python-packaging`)

Inspect the current build backend, Python support matrix, dependencies, and public API. Keep imports predictable and package data explicit; pin policy should match project conventions. Build and install the artifact in an isolated environment, verify metadata and entry points, and test a clean import. Do not publish a release or change compatibility promises without approval.

### Python Upgrade and Migration (`python-migration`)

Identify the source and target versions, supported users, deprecations, and dependency constraints. Search all call sites, update in small coherent steps, and preserve public behavior unless the request says otherwise. Verify on the supported version matrix where available and document breaking changes. Avoid broad dependency upgrades bundled into the migration.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
