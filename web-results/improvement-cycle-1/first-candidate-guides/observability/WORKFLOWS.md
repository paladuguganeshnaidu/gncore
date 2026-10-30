# GNCore Observability: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### GNCore Sentry Instrument (`web-backend-sentry-instrument`)

Identify framework and Sentry SDK versions, instrument relevant error/performance boundaries and propagate useful context without personal data or secrets. Trigger a controlled local error and verify capture/redaction using an authorized test sink. Keep sample rates and overhead explicit.

Technical reference: [attributed source guide](references/web-backend-sentry-instrument/UPSTREAM.md).

### GNCore Sentry Debug Issue (`web-backend-sentry-debug-issue`)

Use a supplied or authorized issue's stack, release, breadcrumbs and frequency to form a reproducible hypothesis. Trace the failing path in the matching revision, propose a bounded fix and regression, and distinguish a prepared fix from evidence that the live issue stopped recurring.

Technical reference: [attributed source guide](references/web-backend-sentry-debug-issue/UPSTREAM.md).

### GNCore Backend Observability (`web-backend-observability`)

Identify service entrypoints, external calls, background jobs, and meaningful failure boundaries. Reuse existing telemetry conventions, propagate correlation context, redact sensitive values, and bound label cardinality. Verify a representative success and failure path emits useful signals. Use Sentry-specific workflows only for Sentry projects; separate local verification from evidence from a connected production system.

### Structured diagnostic events (`obs-structured-events`)

Emit stable event names, severity and correlation identifiers at meaningful boundaries. Redact credentials/personal payloads and bound field size/cardinality. Test the success and error event sequence using a local sink without making logs the source of truth for authorization.

### Metrics and actionable alerts (`obs-metrics-alerts`)

Choose counters, gauges and histograms from an operational question, with explicit units and bounded labels. Derive an alert from a user-impact condition, define an owner/runbook and test both trigger and recovery; do not alert on every individual request error.

### Trace propagation (`obs-trace-context`)

Propagate context across request, queue and background boundaries using the selected library's current APIs. Test parent/child relationships and failed dependency spans on a fixture. State sampling assumptions and do not record secret headers or full request bodies.

### Evidence-led incident diagnosis (`obs-incident-diagnosis`)

Build a timeline from correlated logs, metrics and traces; separate observed facts from hypotheses. Identify the smallest confirming probe and bounded mitigation with a rollback path. Preserve evidence and distinguish telemetry gaps from evidence that a component is healthy.
