---
name: observability
description: "Instrument and diagnose services using actionable logs, metrics, traces and service objectives."
license: Apache-2.0 AND CC-BY-SA-4.0 AND MIT
---

# GNCore Observability

Version: 7.0.0rc1

## Choose the work

Start from an operational question and propagation boundaries. Choose stable low-cardinality labels and sampling that retain diagnostic value without exposing sensitive payloads.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Instrumentation or a diagnostic report connecting requests, failures and dependencies, with useful dashboards/alerts and ownership.

Inject local success/failure/timeout cases, verify trace correlation, alert triggering and redaction, and explain sampling blind spots. Distinguish missing telemetry from an absent failure.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `web-backend-sentry-instrument` | Instrument an application with Sentry — detect the platform, install and initialize the SDK if needed, and wire up any signal — error monitoring, tracing/performance, logging, metrics, profiling, session replay, user feedback, cron check-ins, uptime monitors for the deployed app, and AI/LLM monitoring (agent runs, token cost, and conversations for... |
| `web-backend-sentry-debug-issue` | Debug and fix a Sentry issue — find it (by link, ID, or search), pull full context (stack trace, breadcrumbs, trace, logs), optionally run Seer root-cause / autofix, apply the code fix, and resolve it via a `Fixes PROJECT-NAME-12A` commit/PR. |
| `web-backend-observability` | Design and verify useful service logs, traces, metrics, and alert signals with bounded overhead. |
| `obs-structured-events` | Structured diagnostic events. |
| `obs-metrics-alerts` | Metrics and actionable alerts. |
| `obs-trace-context` | Trace propagation. |
| `obs-incident-diagnosis` | Evidence-led incident diagnosis. |

## Focused procedures

### GNCore Sentry Instrument (`web-backend-sentry-instrument`)

Identify framework and Sentry SDK versions, instrument relevant error/performance boundaries and propagate useful context without personal data or secrets. Trigger a controlled local error and verify capture/redaction using an authorized test sink. Keep sample rates and overhead explicit.

For relevant technical detail, read [the attributed source guide](references/web-backend-sentry-instrument/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

### GNCore Sentry Debug Issue (`web-backend-sentry-debug-issue`)

Use a supplied or authorized issue's stack, release, breadcrumbs and frequency to form a reproducible hypothesis. Trace the failing path in the matching revision, propose a bounded fix and regression, and distinguish a prepared fix from evidence that the live issue stopped recurring.

For relevant technical detail, read [the attributed source guide](references/web-backend-sentry-debug-issue/UPSTREAM.md). Resolve its paths from that folder, check tool availability, and retain its license terms. Do not run imported scripts automatically.

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

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
