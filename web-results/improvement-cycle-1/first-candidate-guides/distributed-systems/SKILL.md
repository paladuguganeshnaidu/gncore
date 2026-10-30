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

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A protocol/state-machine or implementation with invariants, failure scenarios, bounded retries and recovery/operational behavior.

Use deterministic fixtures for duplicates, reordering, partition/recovery, crash points and stale writers. State where local simulation cannot establish real cluster behavior.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Write down the interleaving and commit boundaries before claiming serialization or exactly-once behavior. Use durable operation/payload identity and atomic state transitions; external lost replies require idempotency/status lookup or reconciliation. An expiring claim needs an ownership generation or fencing/CAS so an old worker cannot complete after takeover. Specify retry/retention limits and test crash, overlap, expiry and stale-owner schedules against the actual storage semantics.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Write the actual interleaving and transaction boundaries; enforce monotonically increasing ownership generations at the protected write, not only in the lease record.
- Scope deduplication to operation/payload identity and a replay-compatible retention policy; reconcile unknown outcomes and test expiry, stale owners, overlap and lost replies.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `dist-idempotency` | Idempotent operations. |
| `dist-queues` | Queue delivery and recovery. |
| `dist-consistency` | Consistency and stale writers. |
| `dist-timeouts` | Timeouts, backoff and retry budgets. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
