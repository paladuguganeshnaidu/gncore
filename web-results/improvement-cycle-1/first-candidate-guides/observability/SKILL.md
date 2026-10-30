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

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Instrumentation or a diagnostic report connecting requests, failures and dependencies, with useful dashboards/alerts and ownership.

Inject local success/failure/timeout cases, verify trace correlation, alert triggering and redaction, and explain sampling blind spots. Distinguish missing telemetry from an absent failure.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Carry or link trace context across queues, retries and asynchronous jobs. Bound metric cardinality with stable dimensions; put correlation IDs in redacted logs/traces instead of metric labels. Measure service outcomes, latency, throughput, queue age and failure/retry signals. Define sustained user-impact/SLO alerts with an owner, recovery condition and runbook. Exercise a controlled failure and inspect emitted telemetry; instrumented code alone does not prove an alert works.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Propagate or link queue context using the installed API; use bounded metric dimensions, redacted correlation and meaningful latency/error/throughput/queue signals.
- Define sustained SLO alerts with owner/recovery/runbook and exercise controlled failures. Bound exporter buffers and verify collector outages cannot block requests, exhaust memory or recurse into logging.

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

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
