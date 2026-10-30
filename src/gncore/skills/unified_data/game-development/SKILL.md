---
name: game-development
description: "Build playable game mechanics, simulation state, assets and measured runtime performance."
license: MIT
---

# GNCore Game Development

Version: 7.0.0rc1

## Choose the work

Preserve the requested mechanic within the existing engine and its enclosing gameplay loop. Separate simulation from rendering, make input/state transitions explicit and keep pause/restart behavior coherent without expanding a focused fix into a new game.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Playable mechanics with clear rules, input feedback, success/failure and restart states, plus asset/runtime assumptions.

Play through complete rounds, invalid input and reset. Test fixed-duration simulation at different frame rates and profile representative scenes before optimization claims.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Confirm the engine's movement API and units before introducing delta: some velocity APIs already integrate time. Separate action edges/input state from physics updates, validate direction/normalization and preserve intended mechanics. Bound pause/resume and large-timestep behavior instead of applying an uncontrolled jump. Compare displacement, collisions and action counts under different render and physics schedules; proposed engine tests are not measured gameplay results.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Preserve the requested mechanic and movement feel; respect engine units/time integration, input edges and physics ownership without expanding a small fix into a new game.
- Bound pause/hitch behavior and compare multiple schedules. Render-rate independence alone does not prove deterministic replay, which also depends on input/random/physics state.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `game-development` | Implement game features with deterministic state transitions, responsive input, and measurable performance. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
