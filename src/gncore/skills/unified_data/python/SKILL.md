---
name: python
description: "Build, profile, package, and migrate Python libraries while preserving public APIs and supported runtimes."
license: Apache-2.0 AND MIT
---

# GNCore Python

## Select the work from the user's intent

Inspect Python versions, package layout, public interfaces, dependency policy, and tests. Choose library design, performance work, packaging, or migration based on the task. Use idiomatic types and resource handling; profile before optimizing and verify artifacts rather than only source imports.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Run relevant tests and build/type checks. Inspect wheel and source distributions, import from a clean installation, and verify supported-version assumptions.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `python-library` | Design maintainable Python packages with stable APIs, typing, packaging, and clear examples. |
| `python-performance` | Profile Python hotspots and improve measured runtime or memory without changing semantics. |
| `python-packaging` | Package a Python library with clear APIs, reproducible builds, supported versions, and clean installation behavior. |
| `python-migration` | Migrate Python code or dependencies in a controlled way with compatibility evidence and a rollback path. |

## Focused procedures

### Python Library Engineering (`python-library`)

Inspect supported Python versions, packaging backend, and public imports. Keep public APIs small and backward-compatible unless a breaking change is requested. Use explicit types and focused modules, avoid import-time side effects, declare runtime dependencies accurately, and provide a minimal runnable example. Check wheel and source inclusion rules when packaging changes.

### Python Performance (`python-performance`)

Measure a representative baseline before optimizing. Profile CPU and memory with available tools, identify the dominant hotspot, and optimize that path while preserving outputs and errors. Avoid clever micro-optimizations without evidence. Re-run the same workload and report hardware, input scale, and before/after measurements.

### Python Packaging (`python-packaging`)

Inspect the current build backend, Python support matrix, dependencies, and public API. Keep imports predictable and package data explicit; pin policy should match project conventions. Build and install the artifact in an isolated environment, verify metadata and entry points, and test a clean import. Do not publish a release or change compatibility promises without approval.

### Python Upgrade and Migration (`python-migration`)

Identify the source and target versions, supported users, deprecations, and dependency constraints. Search all call sites, update in small coherent steps, and preserve public behavior unless the request says otherwise. Verify on the supported version matrix where available and document breaking changes. Avoid broad dependency upgrades bundled into the migration.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [microsoft/azure-skills / python-appservice-deploy](research/microsoft-azure-skills-python-appservice-deploy/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-prepare](research/microsoft-azure-skills-azure-prepare/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-messaging](research/microsoft-azure-skills-azure-messaging/GUIDE.md): MIT.
- [anthropics/skills / mcp-builder](research/anthropics-skills-mcp-builder/GUIDE.md): Apache-2.0.
- [antibrow/anti-detect-browser-skills / anti-detect-browser](research/antibrow-anti-detect-browser-skills-anti-detect-browser/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
