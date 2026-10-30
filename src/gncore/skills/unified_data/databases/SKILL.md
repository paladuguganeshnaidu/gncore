---
name: databases
description: "Design relational schemas, SQL, transactions, indexes and reversible data migrations."
license: MIT
---

# GNCore Databases and SQL

Version: 7.0.0

## Choose the work

Derive integrity constraints and isolation requirements from actual operations. Choose indexes from access paths and measured plans, and plan expand/backfill/contract changes for mixed application versions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Schema/query/migration changes with explicit keys, invariants, locking assumptions, backfill policy and rollback limits.

Use a local database to test constraints, nulls, concurrent/lost updates, rollback and migration compatibility. Inspect query plans on representative data; never invent missing business data for a backfill.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Plan migration behavior for old and new writers as well as readers. Use additive expansion, explicit null/collision resolution, resumable bounded backfill and validated contraction. Check the actual engine/version rules for concurrent indexes, constraints, transaction restrictions and locks; concurrent does not mean lock-free. A populated column cannot be dropped as a harmless rollback. Identify the last reversible step, backup/mapping needs and forward-recovery plan before removing data or compatibility.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Coordinate old/new writers before and throughout resumable backfill, reconciliation and contraction; state the unknown-value policy and last reversible boundary.
- Verify engine/version lock and constraint semantics; EXPLAIN ANALYZE executes the statement. Retry the whole transaction when required without duplicating external effects.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `database-design` | Design safe relational data models, queries, and migrations that preserve integrity and performance. |
| `db-transaction-invariants` | Transaction and concurrency invariants. |
| `db-query-plans` | Query plan and index analysis. |
| `db-expand-contract` | Expand/backfill/contract migration. |
| `db-backup-restore` | Backup restoration evidence. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
