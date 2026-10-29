---
name: performance-engineering
description: "Profile and optimize software using repeatable latency, throughput and memory measurements."
license: MIT
---

# GNCore Performance Engineering

Version: 7.0.0rc1

## Choose the work

State the workload, hardware, warmup, concurrency and correctness contract. Find the dominant bottleneck before optimizing and compare identical conditions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A reproducible benchmark/profile, targeted change, correctness evidence and before/after distributions with limitations.

Check output equivalence, cold/warm behavior, tail latency, allocation and saturation. Do not extrapolate a microbenchmark into a production-capacity guarantee.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Verify equivalent outputs before timing. Keep raw distributions, errors and timeouts; compare matched inputs, environment, warmup, load and cold/warm conditions with repeated or interleaved trials. Report median and tails as well as mean, throughput and memory against a user-relevant operating objective. A tiny sample or warm function timing cannot support a universal speedup. State which measurements were actually collected and which follow-up experiments remain proposed.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `python-performance` | Profile Python hotspots and improve measured runtime or memory without changing semantics. |
| `perf-benchmark-design` | Comparable benchmark design. |
| `perf-memory-profile` | Memory and allocation diagnosis. |
| `perf-tail-latency` | Tail latency and saturation. |
| `perf-regression` | Performance regression review. |

## Focused procedures

### Python Performance (`python-performance`)

Measure a representative baseline before optimizing. Profile CPU and memory with available tools, identify the dominant hotspot, and optimize that path while preserving outputs and errors. Avoid clever micro-optimizations without evidence. Re-run the same workload and report hardware, input scale, and before/after measurements.

### Comparable benchmark design (`perf-benchmark-design`)

Specify representative input, machine/runtime versions, warmup, repeats and measurement boundaries. Separate setup from the measured operation and retain raw timings, not just a best run. Compare equivalent outputs and report dispersion and measurement noise.

### Memory and allocation diagnosis (`perf-memory-profile`)

Distinguish retained state, allocation rate and peak working set on the same workload. Identify the allocation/retention path before optimizing and verify object lifetime after the change. Report tool limitations and workload-dependent tradeoffs.

### Tail latency and saturation (`perf-tail-latency`)

Record load generation, concurrency, timeouts and latency percentiles, including failed requests. Ramp only an authorized local/staging target and identify the saturation knee. Avoid coordinated-omission or success-only summaries that hide slow/failed work.

### Performance regression review (`perf-regression`)

Reproduce baseline and candidate under matching conditions, check correctness first and compare distributions with a practical change threshold. Trace regressions to a measured path and retain the raw evidence; avoid brittle single-run timing assertions in unit tests.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
