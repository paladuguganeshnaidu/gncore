---
name: systems-programming
description: "Build Rust, C/C++ and native components with explicit ownership, ABI and resource lifetimes."
license: MIT
---

# GNCore Systems Programming

Version: 7.0.0rc1

## Choose the work

Inspect compiler targets, ownership and FFI boundaries before changing low-level code. Specify pointer validity, aliasing, alignment and cleanup invariants; keep unsafe regions small and justified.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A bounded native component or patch with ownership/ABI documentation, failure behavior and reproducible build configuration.

Run compiler diagnostics and relevant sanitizers/property tests when available. Test empty/large inputs, resource cleanup, integer boundaries and FFI errors; label unrun target-platform checks.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `systems-ownership` | Ownership and resource lifetime. |
| `systems-ffi` | FFI and ABI boundaries. |
| `systems-safe-arithmetic` | Integer and buffer boundaries. |
| `systems-concurrency` | Native concurrency. |

## Focused procedures

### Ownership and resource lifetime (`systems-ownership`)

Map allocation, ownership transfer, borrowing and cleanup for each resource. Use RAII or language-native lifetime guarantees where possible; define cancellation/error cleanup and test repeated creation/destruction without leaks or use-after-free.

### FFI and ABI boundaries (`systems-ffi`)

Specify ABI, fixed-width types, layout/alignment, string length/encoding and ownership on both sides. Validate pointers/lengths and translate errors without unwinding across an incompatible boundary. Test zero-length buffers, invalid handles and cleanup from the caller's language.

### Integer and buffer boundaries (`systems-safe-arithmetic`)

State allowed numeric ranges and byte/element units. Check overflow before allocation/index arithmetic and validate buffer length before access. Exercise minimum/maximum values and malformed input with compiler/runtime checks enabled.

### Native concurrency (`systems-concurrency`)

Identify shared state, synchronization and the ownership of shutdown. Specify lock order and atomic memory-order requirements before choosing lock-free structures. Test cancellation, contention and race instrumentation where supported; explain the limits of stress tests.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
