---
name: distributed-systems
description: "Design and implement concurrency, queues, replication and failure recovery across service boundaries."
license: MIT
---

# GNCore Distributed Systems

Version: 7.0.0rc1

## Choose the work

Specify consistency, ordering, delivery and idempotency requirements. Model partial failure, timeout ambiguity, retry amplification and ownership before choosing coordination mechanisms.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A protocol/state-machine or implementation with invariants, failure scenarios, bounded retries and recovery/operational behavior.

Use deterministic fixtures for duplicates, reordering, partition/recovery, crash points and stale writers. State where local simulation cannot establish real cluster behavior.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `dist-idempotency` | Idempotent operations. |
| `dist-queues` | Queue delivery and recovery. |
| `dist-consistency` | Consistency and stale writers. |
| `dist-timeouts` | Timeouts, backoff and retry budgets. |

## Focused procedures

### Idempotent operations (`dist-idempotency`)

Define the operation identity, key scope, retention and same-key/different-payload behavior. Persist result and side effect within the consistency boundary, and replay after simulated timeout/crash. Do not implement exactly-once claims with an in-memory duplicate set.

### Queue delivery and recovery (`dist-queues`)

State ordering, delivery guarantees, acknowledgment point and poison-message policy. Test duplicate/redelivered messages and a crash between side effect and acknowledgment. Bound retries and dead-letter handling without silently dropping work.

### Consistency and stale writers (`dist-consistency`)

Identify which reads/writes require linearizable, transactional or eventual behavior. Define version/fencing tokens and test a stale owner after lease expiry. Make unavailable versus stale responses explicit during partial failure.

### Timeouts, backoff and retry budgets (`dist-timeouts`)

Allocate an end-to-end deadline and propagate cancellation to dependencies. Retry only safe transient failures with bounded jitter/backoff and a shared budget. Simulate ambiguous timeout completion and prevent retry amplification across layers.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
