---
name: automation
description: "Design and implement reliable automations with explicit inputs, state, retries, ownership, and recovery."
license: Apache-2.0 AND MIT
---

# GNCore Automation

## Select the work from the user's intent

Map the existing manual workflow and choose a useful bounded automation. Define triggers, permissions, idempotency, error handling, rate limits, and human intervention points based on actual risk. Use supported tools and preserve the requested notification behavior.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Test normal, duplicate, delayed, partial-failure, and recovery cases. Verify that retries cannot repeat consequential side effects and that useful failures reach the right owner.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `workflow-automation` | Automate a repetitive workflow with bounded inputs, safe retries, idempotency, and clear human checkpoints. |

## Focused procedures

### Workflow Automation (`workflow-automation`)

Map triggers, inputs, side effects, failure modes, and owners before automating. Validate inputs, use least-privilege credentials, make retries idempotent, and log useful non-sensitive events. Add human review before irreversible or externally visible actions. Test on fixtures or a sandbox first; do not send messages, spend money, or mutate production data without authorization.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [vercel-labs/agent-browser / agent-browser](research/vercel-labs-agent-browser-agent-browser/GUIDE.md): Apache-2.0.
- [flowkit-labs/skills / reddit-automation](research/flowkit-labs-skills-reddit-automation/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
