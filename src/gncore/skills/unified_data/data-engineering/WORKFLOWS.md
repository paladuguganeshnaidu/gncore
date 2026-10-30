# GNCore Data Engineering: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### Data Analysis (`data-analysis`)

Translate the question into a measurable quantity and inspect the relevant columns and missingness. Show the denominator, filters, time window, and aggregation. Check duplicates and outliers where they affect the answer. Label estimates and caveats; never fabricate values or imply causation from correlation.

### Data Pipeline Engineering (`data-pipelines`)

Trace source-to-sink data flow and failure semantics. Define schema and validation at boundaries, make retries idempotent, handle late or duplicate records, and emit actionable logs without secrets or sensitive payloads. Preserve existing schedules and production destinations unless the request explicitly changes them.

### Data Pipeline Engineering (`data-pipeline`)

Trace source, ownership, freshness, volume, schema evolution, and retry semantics. Make stages idempotent, checkpoint safely, validate schemas and key quality invariants, and expose useful failure context. Protect credentials and sensitive data. Keep backfills bounded and never trigger production backfills or mutate source systems without authorization.

### Data Governance (`data-governance`)

Identify asset owner, purpose, source, sensitivity, consumers, transformations, quality expectations, and retention. Propose least-privilege access, lineage, quality checks, and deletion handling. Separate policy facts from recommendations and flag legal or regulatory interpretations for experts. Avoid copying sensitive datasets into examples or test fixtures.
