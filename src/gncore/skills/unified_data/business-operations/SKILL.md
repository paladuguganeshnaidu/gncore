---
name: business-operations
description: "Improve operating processes, procedures, capacity, controls, quality, continuity, and automation."
license: MIT
---

# GNCore Business Operations

## Select the work from the user's intent

Map the actual flow of work, demand, service commitments, handoffs, and bottlenecks. Select process design, SOP, measurement, capacity, control, incident, vendor, continuity, or automation work. Improve the constraint without moving unaccounted work or risk downstream.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Use baseline cycle time, throughput, defects, or service outcomes. Validate exceptions, recovery paths, control ownership, and how the changed process will be measured.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `operations-process-map` | Map a business process from trigger to outcome and expose waste and control gaps. |
| `operations-sop` | Write an actionable SOP with prerequisites, steps, decision points, and recovery paths. |
| `operations-kpi` | Analyze operational KPIs against service outcomes, baselines, and capacity limits. |
| `operations-quality` | Reduce recurring service defects through root-cause analysis and controlled countermeasures. |
| `operations-capacity` | Forecast service capacity and queues with explicit demand, throughput, and uncertainty. |
| `operations-control` | Design practical controls that prevent or detect costly process failures. |
| `operations-incident` | Coordinate a non-technical operational incident and restore service with clear ownership. |
| `operations-vendor` | Review vendor delivery against service commitments, risks, dependencies, and corrective actions. |
| `operations-continuity` | Prepare a business continuity response for essential processes and credible disruption scenarios. |
| `operations-automation` | Assess whether an operational task is ready for safe automation and quantify its value. |

## Focused procedures

### Process Mapping (`operations-process-map`)

Identify actors, inputs, decisions, handoffs, systems, exceptions, wait time, and controls using observed evidence. Validate the map with process owners before redesigning it.

### Standard Operating Procedure (`operations-sop`)

Name the owner, scope, required access, safety constraints, expected output, and review cadence. Write steps in executable order, include exception handling, and test the procedure with a user unfamiliar with the process.

### Operations KPI Review (`operations-kpi`)

Verify source, definition, grain, freshness, target, and denominator. Investigate variation and leading indicators, segment material differences, and avoid ranking teams without adjusting for workload and case mix.

### Service Quality Improvement (`operations-quality`)

Define defect and baseline, stratify by process stage, confirm root cause with evidence, and test one countermeasure at a time. Monitor unintended effects and sustain only improvements that persist.

### Capacity and Queue Planning (`operations-capacity`)

Measure arrival rates, service times, backlog, variability, and staffing constraints. Model scenarios and service targets, identify bottlenecks, and disclose assumptions rather than relying on average utilization alone.

### Operational Control Design (`operations-control`)

Map risk to preventive and detective controls, accountable owner, evidence, frequency, exceptions, and remediation. Minimize duplicate checks and test whether the control catches realistic failures.

### Business Operations Incident (`operations-incident`)

Establish customer and business impact, scope, timeline, safe containment, communications owner, and recovery criterion. Preserve records and avoid unapproved external commitments or irreversible actions.

### Vendor Operations Review (`operations-vendor`)

Compare service evidence to contract and agreed measures, record exceptions, assess concentration and continuity risk, and agree owners and dates for remediation. Route contract interpretation to counsel.

### Business Continuity Plan (`operations-continuity`)

Identify critical services, impact tolerances, dependencies, alternate procedures, contacts, data recovery, and exercise cadence. Verify the plan with a tabletop; distinguish assumed capability from tested capability.

### Operations Automation Case (`operations-automation`)

Measure current volume, variation, exception rate, labor, error cost, and control obligations. Keep human review for ambiguous or high-impact cases, define fallback, and pilot against a measured baseline.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [samber/developer-relations-skills / developer-ecosystem-strategy](research/samber-developer-relations-skills-developer-ecosystem-strategy/GUIDE.md): MIT.
- [samber/dev-event-organizer-skills / business-event-formats](research/samber-dev-event-organizer-skills-business-event-formats/GUIDE.md): MIT.
- [jeffallan/claude-skills / legacy-modernizer](research/jeffallan-claude-skills-legacy-modernizer/GUIDE.md): MIT.
- [wondelai/skills / create-business](research/wondelai-skills-create-business/GUIDE.md): MIT.
- [wondelai/skills / grow-business](research/wondelai-skills-grow-business/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / business-growth-skills](research/alirezarezvani-claude-skills-business-growth-skills/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / business-operations-skills](research/alirezarezvani-claude-skills-business-operations-skills/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
