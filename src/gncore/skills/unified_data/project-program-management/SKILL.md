---
name: project-program-management
description: "Plan, coordinate, recover, and close projects with explicit dependencies, capacity, and decisions."
license: MIT
---

# GNCore Project and Program Management

## Select the work from the user's intent

Establish scope, owner, milestones, dependencies, capacity, and the current baseline. Use a critical-path or dependency view when sequencing matters. For status work, explain variance and the next decision; for recovery, show what changes in scope, staffing, dates, or risk.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check dates, dependency order, resource conflicts, named owners, and milestone acceptance evidence. Label forecasts separately from commitments.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `project-charter` | Create a concise project charter with outcome, scope, ownership, constraints, and decision gates. |
| `project-plan` | Build an executable delivery plan with milestones, dependencies, owners, and evidence. |
| `project-status` | Produce a truthful project status update with progress, forecast, risks, and asks. |
| `project-risk-log` | Create and maintain actionable project risks, issues, assumptions, and dependencies. |
| `project-recovery` | Recover a troubled project by identifying root causes and rebaselining achievable outcomes. |
| `project-meeting` | Prepare a meeting agenda and decision record that uses participant time effectively. |
| `project-dependency` | Map and resolve cross-team dependencies before they become delivery blockers. |
| `project-capacity` | Match project demand to available skills, capacity, and protected operational work. |
| `project-retro` | Run a blameless retrospective that yields specific, owned process improvements. |
| `project-closure` | Close a project with accepted deliverables, operational ownership, records, and lessons. |

## Focused procedures

### Project Charter (`project-charter`)

Record sponsor, accountable lead, beneficiaries, success criteria, in-scope and excluded work, resources, constraints, risks, and governance. Resolve ambiguous authority and acceptance before execution begins.

### Delivery Plan (`project-plan`)

Decompose deliverables into verifiable milestones, estimate with ranges, identify dependencies and critical path, assign owners, and define completion evidence. Surface assumptions and contingency rather than hiding schedule uncertainty.

### Project Status Brief (`project-status`)

Compare actual progress to baseline using completed evidence, not activity. State schedule and scope variance, confidence, new risks, decisions needed, and next milestone; never convert an estimate into an achieved result.

### Project Risk Log (`project-risk-log`)

Write each item as a cause-event-impact statement with probability, impact, owner, response, trigger, and due date. Separate current issues from future risks and close items only with evidence.

### Project Recovery Plan (`project-recovery`)

Establish the true state, causes, remaining scope, capacity, dependencies, and stakeholder commitments. Present options with impacts, reset only with sponsor agreement, and define weekly recovery indicators and stop conditions.

### Decision Meeting Preparation (`project-meeting`)

Clarify the decision, decision maker, pre-read, options, evidence gaps, and time allocation. Capture decision, rationale, dissent, owner, due date, and revisit trigger; distinguish discussion from approval.

### Dependency Coordination (`project-dependency`)

Identify provider, consumer, contract, needed-by date, confidence, fallback, and escalation path for each dependency. Confirm ownership bilaterally and track changes to interfaces and dates.

### Capacity and Resource Plan (`project-capacity`)

Use realistic availability, leave, skills, context switching, and run-work data. Show demand versus capacity by period, expose trade-offs, and avoid treating people as interchangeable capacity units.

### Project Retrospective (`project-retro`)

Reconstruct outcomes and contributing conditions from evidence, include multiple perspectives, distinguish systemic causes from individual blame, and assign a small number of measurable experiments with owners and review dates.

### Project Closure and Handoff (`project-closure`)

Confirm acceptance, unresolved defects, support ownership, documentation, access, financial close, and records retention. Obtain explicit handoff acceptance and keep post-project work visible.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [alirezarezvani/claude-skills / senior-pm](research/alirezarezvani-claude-skills-senior-pm/GUIDE.md): MIT.
- [trae-community/trae-skills / wechat-mini-program-development](research/trae-community-trae-skills-wechat-mini-program-development/GUIDE.md): MIT.
- [cyberelf/agency-agents / project-management](research/cyberelf-agency-agents-project-management/GUIDE.md): MIT.
- [jimnguyendev/jimmy-skills / data-program-leadership](research/jimnguyendev-jimmy-skills-data-program-leadership/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
