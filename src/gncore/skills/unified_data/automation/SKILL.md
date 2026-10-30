---
name: automation
description: "Implement restartable developer automations with bounded inputs, retries and observable failure recovery."
license: MIT
---

# GNCore Automation

Version: 7.0.0

## Choose the work

Define triggers, state, idempotency keys and allowed side effects. Model retryable versus permanent failures and choose a useful stopping condition.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

A runnable automation, configuration contract, state/retry policy, useful logs and recovery instructions.

Use fixtures for duplicate triggers, partial failures, invalid inputs, interrupted execution and resumed work. Do not infer permission for external messages or production writes from a local test.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Define durable operation identity before adding retries. Commit progress with the effect when one transactional boundary permits it; otherwise use an idempotent remote contract, ledger and reconciliation for unknown outcomes. Separate malformed/permanent failures from transient errors, cap retries with backoff and jitter, and leave a recoverable record. Test interruption immediately before and after the durable boundary, including replay of already accepted work.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Scope operation identity to the owner and payload; reject conflicting reuse and make overlapping triggers acquire atomic ownership.
- Fence stale owners at the effect's storage boundary; retain a bounded retry/quarantine record and verify crash/replay across the durable commit.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `workflow-automation` | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |
| `automation-resume` | Resume after partial execution. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
