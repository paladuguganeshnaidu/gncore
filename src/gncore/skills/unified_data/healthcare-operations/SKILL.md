---
name: healthcare-operations
description: "Support healthcare intake, scheduling, quality, capacity, privacy, policies, audits, and administrative improvement."
license: MIT
---

# GNCore Healthcare Operations

## Select the work from the user's intent

Keep the task within healthcare administration and operations. Identify service, patient-flow context, urgency, data sensitivity, staffing, and operational constraints. Use de-identified or minimum-necessary records; do not turn administrative analysis into diagnosis or treatment recommendations.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify counts, dates, workflow exceptions, access boundaries, policy sources, and service impacts. Escalate clinical questions to the appropriate clinical professional rather than inferring clinical advice.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `healthcare-intake` | Improve administrative intake completeness, routing, accessibility, and privacy. |
| `healthcare-scheduling` | Coordinate appointments using supplied policies and patient preferences. |
| `healthcare-operations-map` | Map administrative handoffs, delays, duplication, and ownership gaps. |
| `healthcare-quality` | Organize quality improvement with defined measures, owners, and review cycles. |
| `healthcare-privacy` | Review artifacts for privacy exposure and minimum-necessary handling. |
| `healthcare-policy` | Maintain operational policies with ownership, evidence, and review dates. |
| `healthcare-patient-comms` | Write clear non-clinical communications about administrative next steps. |
| `healthcare-audit` | Review administrative controls and remediation with an evidence trail. |
| `healthcare-capacity` | Model service capacity using operational data and explicit assumptions. |
| `healthcare-improvement` | Plan and assess a bounded operational improvement with safeguards. |

## Focused procedures

### Healthcare Intake (`healthcare-intake`)

Use approved forms, collect minimum necessary information, follow supplied escalation rules, and verify routing without clinical judgment.

### Healthcare Scheduling (`healthcare-scheduling`)

Respect visit types, accessibility, time zones, and approved rules. Do not infer urgency or give medical advice; escalate ambiguity.

### Healthcare Operations Map (`healthcare-operations-map`)

Use authorized process data, map roles and queues, and validate changes with clinical and operational owners.

### Healthcare Quality Operations (`healthcare-quality`)

Use approved measures, define denominator and exclusions, protect data, document baseline, and require qualified review before changing care.

### Healthcare Privacy Review (`healthcare-privacy`)

Follow supplied policy, avoid repeating sensitive details, flag uncertain disclosures, and route decisions to the privacy officer.

### Healthcare Policy Operations (`healthcare-policy`)

Use approved sources, identify jurisdiction and audience, distinguish requirements from advice, version documents, and route clinical/legal decisions to qualified reviewers.

### Patient Administrative Communications (`healthcare-patient-comms`)

Use verified logistics and approved scripts, accessible plain language, no treatment advice, and approved escalation instructions.

### Healthcare Operations Audit (`healthcare-audit`)

Use authorized scope, de-identify where possible, record sampling, distinguish evidence from assumptions, restrict data, and assign owners/dates.

### Healthcare Capacity Planning (`healthcare-capacity`)

Define demand, service time, coverage, constraints, and uncertainty; avoid patient-level inference and have operations validate safety.

### Healthcare Improvement Cycle (`healthcare-improvement`)

Set baseline, aim, intervention, balancing measures, approvals, and review date. Monitor unintended effects and follow supplied stop rules.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [kishorkukreja/awesome-supply-chain / clinical-trial-logistics](research/kishorkukreja-awesome-supply-chain-clinical-trial-logistics/GUIDE.md): MIT.
- [kishorkukreja/awesome-supply-chain / value-analysis](research/kishorkukreja-awesome-supply-chain-value-analysis/GUIDE.md): MIT.
- [jshsakura/awesome-opencode-skills / healthcare-admin](research/jshsakura-awesome-opencode-skills-healthcare-admin/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
