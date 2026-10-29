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

## Deliver and verify

A firmware/state-machine change, pin/protocol/configuration contract, memory/timing budget and a host/device test plan.

Use host fixtures for state transitions, buffer limits, timeouts and wraparound; verify hardware-specific timing and peripheral behavior on the actual device before claiming hardware readiness.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Keep interrupt work bounded and nonblocking; use preallocated storage with an explicit ISR/task ownership and synchronization protocol. Define queue-full behavior, dropped-event visibility, timeout and watchdog recovery rather than only testing for overflow. Document timer width, modular elapsed-time assumptions and the maximum observation interval. Separate host arithmetic/concurrency simulations from measured target latency, memory and peripheral evidence.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `embedded-state-machine` | Firmware state machines. |
| `embedded-protocols` | Peripheral protocol integration. |
| `embedded-timing` | Timers and interrupt boundaries. |
| `embedded-memory` | Constrained memory and firmware builds. |

## Focused procedures

### Firmware state machines (`embedded-state-machine`)

Separate pure state transitions from peripheral effects. Define events, deadlines and valid states; make retries bounded and recovery explicit. Simulate event sequences, repeated inputs and reset without requiring a device.

### Peripheral protocol integration (`embedded-protocols`)

Verify board pins, voltage assumptions, bus configuration, frame format and timeout behavior against the actual hardware documentation. Isolate the transport behind a testable boundary and inject truncated, delayed and corrupt frames in host tests.

### Timers and interrupt boundaries (`embedded-timing`)

Define tick units, counter width, wraparound and interrupt/main-loop ownership. Keep interrupt work bounded and use wrap-safe elapsed-time comparisons. Test deadlines across counter rollover and report which timing claims still require hardware measurement.

### Constrained memory and firmware builds (`embedded-memory`)

Record flash/RAM limits, stack/heap use and linker configuration for the target. Prefer bounded buffers and deterministic allocation where required. Inspect map/build output and exercise maximum frames and reset paths; desktop simulation does not certify device memory headroom.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
