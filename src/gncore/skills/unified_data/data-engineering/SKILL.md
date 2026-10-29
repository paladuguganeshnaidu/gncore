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

## Deliver and verify

A restartable pipeline or data design, schemas, quality contracts, lineage and a reconciled accepted/rejected-record report.

Check row counts and totals, duplicate/conflicting events, late arrivals, missing/invalid values, backfills and repeat runs. Keep source data and credentials out of example outputs.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

State record grain, event identity, business timezone and value constraints before aggregation. Identical replays, conflicting payloads and legitimate revisions need separate policies; keep-first deduplication must not silently hide corrections. Quarantine invalid rows with lineage, publish atomically/idempotently, and reconcile accepted, duplicate, rejected and emitted counts and amounts. Test late events, changed revisions and restart at publication boundaries.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `data-analysis` | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |
| `data-pipeline` | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `data-governance` | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |

## Focused procedures

### Data Analysis (`data-analysis`)

Translate the question into a measurable quantity and inspect the relevant columns and missingness. Show the denominator, filters, time window, and aggregation. Check duplicates and outliers where they affect the answer. Label estimates and caveats; never fabricate values or imply causation from correlation.

### Data Pipeline Engineering (`data-pipelines`)

Trace source-to-sink data flow and failure semantics. Define schema and validation at boundaries, make retries idempotent, handle late or duplicate records, and emit actionable logs without secrets or sensitive payloads. Preserve existing schedules and production destinations unless the request explicitly changes them.

### Data Pipeline Engineering (`data-pipeline`)

Trace source, ownership, freshness, volume, schema evolution, and retry semantics. Make stages idempotent, checkpoint safely, validate schemas and key quality invariants, and expose useful failure context. Protect credentials and sensitive data. Keep backfills bounded and never trigger production backfills or mutate source systems without authorization.

### Data Governance (`data-governance`)

Identify asset owner, purpose, source, sensitivity, consumers, transformations, quality expectations, and retention. Propose least-privilege access, lineage, quality checks, and deletion handling. Separate policy facts from recommendations and flag legal or regulatory interpretations for experts. Avoid copying sensitive datasets into examples or test fixtures.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
