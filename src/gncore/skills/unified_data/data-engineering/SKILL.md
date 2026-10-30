---
name: data-engineering
description: "Build schema-aware, observable batch/streaming pipelines with restart, reconciliation and lineage."
license: MIT
---

# GNCore Data Engineering

Version: 7.0.0rc1

## Choose the work

Define row/event grain, ownership, keys, event versus processing time and schema evolution. Decide deduplication, quarantine and checkpoint policies before moving data.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A restartable pipeline or data design, schemas, quality contracts, lineage and a reconciled accepted/rejected-record report.

Check row counts and totals, duplicate/conflicting events, late arrivals, missing/invalid values, backfills and repeat runs. Keep source data and credentials out of example outputs.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

State record grain, event identity, business timezone and value constraints before aggregation. Identical replays, conflicting payloads and legitimate revisions need separate policies; keep-first deduplication must not silently hide corrections. Quarantine invalid rows with lineage, publish atomically/idempotently, and reconcile accepted, duplicate, rejected and emitted counts and amounts. Test late events, changed revisions and restart at publication boundaries.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Declare record grain, business time, constraints, revision ordering and tombstones; an older late update must not overwrite newer accepted state.
- Define watermark/finality and correction/retraction policy; publish idempotently and reconcile raw, duplicate, rejected, accepted and emitted counts/amounts after restart.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `data-analysis` | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |
| `data-pipeline` | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `data-governance` | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
