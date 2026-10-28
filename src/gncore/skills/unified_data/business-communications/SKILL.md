---
name: business-communications
description: "Draft and edit executive briefs, emails, updates, policies, reports, crisis messages, and localized business content."
license: Apache-2.0 AND MIT
---

# GNCore Business Communications

## Select the work from the user's intent

Identify audience, purpose, action, source facts, tone, channel, and sensitivity. Choose structure and level of detail around the reader's decision. Preserve the writer's intent, distinguish facts from proposals, and keep distribution separate from drafting.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify names, dates, figures, commitments, links, terminology, and tone. Ensure the requested action and owner are clear and translations preserve meaning.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `comms-executive-brief` | Create a concise decision brief with evidence, options, owner, and timing. |
| `comms-email` | Draft audience-appropriate business email with a clear next action. |
| `comms-stakeholder-update` | Report status, changes, blockers, decisions, and next steps. |
| `comms-policy` | Draft policy with scope, rules, owner, exceptions, and review cadence. |
| `comms-report` | Connect evidence to conclusions and actions in a structured report. |
| `comms-crisis` | Prepare a factual holding statement and update plan for an incident. |
| `comms-edit` | Edit writing for clarity, audience fit, accuracy, and consistent tone. |
| `comms-meeting` | Prepare agendas and decision-focused minutes with owners and follow-ups. |
| `comms-localization` | Adapt content to a locale while preserving meaning, policy, and usability. |
| `comms-quality` | Quality-check business communications before distribution. |

## Focused procedures

### Executive Brief (`comms-executive-brief`)

Lead with the decision, show verified evidence and assumptions, compare options/risks, name owner and deadline, and keep detail traceable.

### Business Email (`comms-email`)

State purpose early, include relevant context, clarify request and deadline, preserve facts, and remove unnecessary sensitive information.

### Stakeholder Update (`comms-stakeholder-update`)

Use dated facts, distinguish done/in progress/at risk, name owners/dates, identify decisions, and avoid unsupported confidence.

### Internal Policy Draft (`comms-policy`)

Identify authority and audience, define terms, make requirements testable, include escalation and version owner, and route legal/HR review.

### Business Report (`comms-report`)

Define question and scope, cite data, label methods and limits, separate observation from interpretation, assign recommendation owners.

### Crisis Communications (`comms-crisis`)

Use verified facts, state known/unknown, avoid speculation, identify authorized spokesperson and approval path, set next update time.

### Clarity and Tone Edit (`comms-edit`)

Preserve meaning, verify names/numbers against sources, remove ambiguity, retain requested voice, and list material edits.

### Meeting Brief and Minutes (`comms-meeting`)

Set outcomes/time boxes, separate decisions from discussion, capture action owners/dates, distinguish facts from open issues, share selectively.

### Business Content Localization (`comms-localization`)

Confirm locale/audience, preserve legal and product terms, adapt formats, flag uncertain claims, and require local expert review for high impact.

### Communications Quality Check (`comms-quality`)

Check audience, purpose, facts, names, dates, links, attachments, accessibility, confidentiality, approvals, and action; verify final artifact.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [anthropics/knowledge-work-plugins / process-doc](research/anthropics-knowledge-work-plugins-process-doc/GUIDE.md): Apache-2.0.
- [mbfinotti/revops-skills / revenue-kpi-framework](research/mbfinotti-revops-skills-revenue-kpi-framework/GUIDE.md): MIT.
- [forcedotcom/sf-skills / omnistudio-datapacks-deploy](research/forcedotcom-sf-skills-omnistudio-datapacks-deploy/GUIDE.md): Apache-2.0.
- [grafana/skills / reconciler-logic](research/grafana-skills-reconciler-logic/GUIDE.md): Apache-2.0.
- [phuryn/pm-skills / sql-queries](research/phuryn-pm-skills-sql-queries/GUIDE.md): MIT.
- [forcedotcom/sf-skills / deploying-omnistudio-datapacks](research/forcedotcom-sf-skills-deploying-omnistudio-datapacks/GUIDE.md): Apache-2.0.
- [wondelai/skills / create-app](research/wondelai-skills-create-app/GUIDE.md): MIT.
- [owl-listener/designer-skills / design-rationale](research/owl-listener-designer-skills-design-rationale/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
