---
name: systems-programming
description: "Build Rust, C/C++ and native components with explicit ownership, ABI and resource lifetimes."
license: MIT
---

# GNCore Systems Programming

Version: 7.0.0

## Choose the work

Inspect compiler targets, ownership and FFI boundaries before changing low-level code. Specify pointer validity, aliasing, alignment and cleanup invariants; keep unsafe regions small and justified.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A bounded native component or patch with ownership/ABI documentation, failure behavior and reproducible build configuration.

Run compiler diagnostics and relevant sanitizers/property tests when available. Test empty/large inputs, resource cleanup, integer boundaries and FFI errors; label unrun target-platform checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Make the owner, storage stability, borrow/retention interval and destruction order explicit at every native/FFI boundary. Pair allocation and deallocation through a documented compatible ABI and enforce exactly-once destruction after the foreign user has finished. Specify null/length/NUL, error/unwind and allowed concurrency behavior. Inspect small unsafe boundaries and use appropriate native/sanitizer/stress checks; a plausible ownership sketch is not runtime memory-safety proof.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Specify stable storage, ownership, retention, matching allocation/deallocation and destruction after foreign callbacks become quiescent; define permitted concurrency.
- Distinguish enforceable null/length/alignment/handle/overflow checks from caller lifetime/provenance obligations; specify error/unwind behavior and use appropriate native/sanitizer/stress evidence without claiming pointer inspection proves safety.
- Write the actual ABI rules rather than saying to document them: whether null is permitted at zero length, required alignment and checked length arithmetic, who owns each allocation, caller lifetime obligations, and a specific failure/status convention that prevents unwinding across the boundary. Mark unspecified foreign guarantees as assumptions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `systems-ownership` | Ownership and resource lifetime. |
| `systems-ffi` | FFI and ABI boundaries. |
| `systems-safe-arithmetic` | Integer and buffer boundaries. |
| `systems-concurrency` | Native concurrency. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
