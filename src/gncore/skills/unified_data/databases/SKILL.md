---
name: databases
description: "Design relational schemas, SQL, transactions, indexes and reversible data migrations."
license: MIT
---

# GNCore Databases and SQL

Version: 7.0.0rc1

## Choose the work

Derive integrity constraints and isolation requirements from actual operations. Choose indexes from access paths and measured plans, and plan expand/backfill/contract changes for mixed application versions.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Schema/query/migration changes with explicit keys, invariants, locking assumptions, backfill policy and rollback limits.

Use a local database to test constraints, nulls, concurrent/lost updates, rollback and migration compatibility. Inspect query plans on representative data; never invent missing business data for a backfill.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `database-design` | Design safe relational data models, queries, and migrations that preserve integrity and performance. |
| `db-transaction-invariants` | Transaction and concurrency invariants. |
| `db-query-plans` | Query plan and index analysis. |
| `db-expand-contract` | Expand/backfill/contract migration. |
| `db-backup-restore` | Backup restoration evidence. |

## Focused procedures

### Database Design (`database-design`)

Inspect the database engine, schema, constraints, data volume, and access patterns. Encode invariants with appropriate constraints and indexes; parameterize input. Make migrations reversible and consider locking, backfill, and compatibility. Never run destructive SQL or apply a migration to production without explicit authorization. Verify query plans or migration behavior with a safe local fixture when possible.

### Transaction and concurrency invariants (`db-transaction-invariants`)

Express the business invariant with keys/checks and the chosen isolation/locking strategy. Reproduce a two-writer conflict using an isolated database and show which operation retries or fails. Keep the transaction boundary around the complete invariant.

### Query plan and index analysis (`db-query-plans`)

Record schema, distribution, query parameters and an explain plan on representative fixtures. Identify scan/join/order costs and compare a targeted index using the same workload. Account for write amplification and avoid declaring an index useful from syntax alone.

### Expand/backfill/contract migration (`db-expand-contract`)

Add compatible schema first, backfill in restartable bounded batches, verify integrity, then tighten constraints after old application versions are retired. State unknown-value policy and rollback limits; rehearse failure and lock behavior locally.

### Backup restoration evidence (`db-backup-restore`)

Define recovery-point/time requirements and the backup's consistency boundary. Restore into an isolated instance and verify schema, row counts, critical queries and recovery steps. A successful backup command alone is not evidence of a working restore.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
