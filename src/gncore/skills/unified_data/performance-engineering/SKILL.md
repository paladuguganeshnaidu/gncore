---
name: performance-engineering
description: "Profile and optimize software using repeatable latency, throughput and memory measurements."
license: MIT
---

# GNCore Performance Engineering

Version: 7.0.0

## Choose the work

State the workload, hardware, warmup, concurrency and correctness contract. Find the dominant bottleneck before optimizing and compare identical conditions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A reproducible benchmark/profile, targeted change, correctness evidence and before/after distributions with limitations.

Check output equivalence, cold/warm behavior, tail latency, allocation and saturation. Do not extrapolate a microbenchmark into a production-capacity guarantee.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Verify equivalent outputs before timing. Keep raw distributions, errors and timeouts; compare matched inputs, environment, warmup, load and cold/warm conditions with repeated or interleaved trials. Report median and tails as well as mean, throughput and memory against a user-relevant operating objective. A tiny sample or warm function timing cannot support a universal speedup. State which measurements were actually collected and which follow-up experiments remain proposed. Recompute quoted statistics from the retained raw values with trusted arithmetic, and postpone rounding until after comparisons.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Verify equivalent outputs and time actual completion, including async/accelerator synchronization where needed; preserve every outcome and recompute quoted statistics from raw samples.
- Match environment, workload, concurrency, warmup and cold/warm conditions; report relevant tails, throughput and memory against the user's objective, including errors/timeouts and small-sample limitations.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `python-performance` | Profile Python hotspots and improve measured runtime or memory without changing semantics. |
| `perf-benchmark-design` | Comparable benchmark design. |
| `perf-memory-profile` | Memory and allocation diagnosis. |
| `perf-tail-latency` | Tail latency and saturation. |
| `perf-regression` | Performance regression review. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
