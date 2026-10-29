# Primary sources used to check technical findings

Checked 29 October 2026. These support review decisions; the reviewed responses are preserved separately.

- [PostgreSQL18 UPDATE](https://www.postgresql.org/docs/18/sql-update.html): command grammar and bounded-update patterns. The shown trailing `UPDATE ... LIMIT` is not supported.
- [PostgreSQL18 ALTER TABLE](https://www.postgresql.org/docs/18/sql-altertable.html): lock behavior, existing-index constraints and the constraint types that permit `NOT VALID`.
- [PostgreSQL18 Read Committed](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED): concurrent unique-key insertion visibility and waiting.
- [PostgreSQL18 ROLLBACK](https://www.postgresql.org/docs/18/sql-rollback.html): rolled-back changes are discarded.
- [OpenTelemetry Python propagation](https://opentelemetry.io/docs/languages/python/propagation/): supported context-injection and extraction APIs, distinct from the generated `trace.propagate` spelling.

The 30 published comparator entrypoints, exact source revisions, hashes and notices are recorded in `source-snapshots.json`. No external helper was executed. No database or production observability deployment was performed to validate these written proposals.
