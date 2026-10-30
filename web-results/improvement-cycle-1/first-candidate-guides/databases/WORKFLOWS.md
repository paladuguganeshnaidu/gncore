# GNCore Databases and SQL: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Database Design (`database-design`)

Inspect the database engine, schema, constraints, data volume, and access patterns. Encode invariants with appropriate constraints and indexes; parameterize input. Make migrations reversible and consider locking, backfill, and compatibility. Never run destructive SQL or apply a migration to production without explicit authorization. Verify query plans or migration behavior with a safe local fixture when possible.

### Transaction and concurrency invariants (`db-transaction-invariants`)

Express the business invariant with keys/checks and the chosen isolation/locking strategy. Reproduce a two-writer conflict using an isolated database and show which operation retries or fails. Keep the transaction boundary around the complete invariant.

### Query plan and index analysis (`db-query-plans`)

Record schema, distribution, query parameters and an explain plan on representative fixtures. Identify scan/join/order costs and compare a targeted index using the same workload. Account for write amplification and avoid declaring an index useful from syntax alone.

### Expand/backfill/contract migration (`db-expand-contract`)

Inventory existing values and define explicit handling of unknown or colliding data. Add a compatible representation and coordinate old/new writers before and throughout a resumable bounded backfill; use reconciliation or a final catch-up to close concurrent-write gaps. Check the actual engine/version constraint and lock semantics, validate integrity, then switch readers and contract only after overlap is over. State the last reversible step, mapping/backup needs and forward recovery after destructive contraction; rehearse interruption and recovery without claiming unexecuted SQL.

### Backup restoration evidence (`db-backup-restore`)

Define recovery-point/time requirements and the backup's consistency boundary. Restore into an isolated instance and verify schema, row counts, critical queries and recovery steps. A successful backup command alone is not evidence of a working restore.
