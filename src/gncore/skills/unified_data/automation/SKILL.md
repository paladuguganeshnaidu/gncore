---
name: automation
description: "Implement restartable developer automations with bounded inputs, retries and observable failure recovery."
license: MIT
---

# GNCore Automation

Version: 7.0.0rc1

## Choose the work

Define triggers, state, idempotency keys and allowed side effects. Model retryable versus permanent failures and choose a useful stopping condition.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

A runnable automation, configuration contract, state/retry policy, useful logs and recovery instructions.

Use fixtures for duplicate triggers, partial failures, invalid inputs, interrupted execution and resumed work. Do not infer permission for external messages or production writes from a local test.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `workflow-automation` | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |
| `automation-resume` | Resume after partial execution. |

## Focused procedures

### Workflow Automation (`workflow-automation`)

Map triggers, inputs, side effects, failure modes, and owners before automating. Validate inputs, use least-privilege credentials, make retries idempotent, and log useful non-sensitive events. Add human review before irreversible or externally visible actions. Test on fixtures or a sandbox first; do not send messages, spend money, or mutate production data without authorization.

### Resume after partial execution (`automation-resume`)

Record progress only after the operation's durable boundary and keep idempotency keys stable across retries. Inject failure after each meaningful side effect, resume against the same fixture and verify that no completed work is duplicated or silently skipped.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
