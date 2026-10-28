---
name: operations
description: "Investigate operational incidents and coordinate containment, recovery, communication, and follow-up from evidence."
license: Apache-2.0 AND MIT
---

# GNCore Operations

## Select the work from the user's intent

Establish impact, timeline, current state, known changes, ownership, and authorized response scope. Separate observations from hypotheses and choose reversible containment while investigating the cause. Maintain a clear incident record and recovery criterion.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify restoration with service evidence rather than a successful command alone. Record remaining exposure, customer impact, follow-up owners, and checks not yet completed.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `incident-response` | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

## Focused procedures

### Incident Response (`incident-response`)

Establish impact, timeline, scope, and current signals from available evidence. Prioritize reversible mitigations and state expected effects before action. Preserve logs and avoid destructive cleanup or speculative changes. Separate facts from hypotheses, assign verification steps, and document recovery criteria and follow-ups. Do not perform live production actions unless explicitly authorized.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [microsoft/azure-skills / azure-kubernetes](research/microsoft-azure-skills-azure-kubernetes/GUIDE.md): MIT.
- [prisma/skills / prisma-client-api](research/prisma-skills-prisma-client-api/GUIDE.md): MIT.
- [mattpocock/skills / git-guardrails-claude-code](research/mattpocock-skills-git-guardrails-claude-code/GUIDE.md): MIT.
- [mastra-ai/skills / mastra](research/mastra-ai-skills-mastra/GUIDE.md): Apache-2.0.
- [coreyhaines31/marketingskills / revops](research/coreyhaines31-marketingskills-revops/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
