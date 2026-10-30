---
name: embedded-systems
description: "Build firmware, peripheral interfaces and constrained-device software with explicit timing and hardware boundaries."
license: MIT
---

# GNCore Embedded Systems

Version: 7.0.0rc1

## Choose the work

Identify MCU/board, toolchain, memory map, interrupts and electrical/protocol assumptions. Separate pure state logic from hardware access and define timeout/watchdog behavior.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A firmware/state-machine change, pin/protocol/configuration contract, memory/timing budget and a host/device test plan.

Use host fixtures for state transitions, buffer limits, timeouts and wraparound; verify hardware-specific timing and peripheral behavior on the actual device before claiming hardware readiness.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Keep interrupt work bounded and nonblocking; use preallocated storage with an explicit ISR/task ownership and synchronization protocol. Define queue-full behavior, dropped-event visibility, timeout and watchdog recovery rather than only testing for overflow. Document timer width, modular elapsed-time assumptions and the maximum observation interval. Separate host arithmetic/concurrency simulations from measured target latency, memory and peripheral evidence.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Define bounded nonblocking ISR/task ownership and synchronization; volatile alone does not guarantee atomicity or ordering. Make overrun/drop/timeout state observable.
- State timer width, wrap comparison and observation/interval bounds; distinguish modular elapsed subtraction from signed deadline ordering and host fixtures from measured hardware timing.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `embedded-state-machine` | Firmware state machines. |
| `embedded-protocols` | Peripheral protocol integration. |
| `embedded-timing` | Timers and interrupt boundaries. |
| `embedded-memory` | Constrained memory and firmware builds. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
