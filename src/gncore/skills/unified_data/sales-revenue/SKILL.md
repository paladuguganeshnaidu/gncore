---
name: sales-revenue
description: "Research accounts, qualify opportunities, prepare sales conversations, proposals, forecasts, and renewals."
license: Apache-2.0 AND MIT
---

# GNCore Sales and Revenue

## Select the work from the user's intent

Use the customer's context, stage definitions, stakeholder roles, and verified interaction history. Select account planning, discovery, qualification, pipeline, forecasting, proposal, negotiation, objections, territory, or renewal work. Keep drafts and proposed CRM changes distinct from completed outreach or updates.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify account names, offer terms, stages, amounts, dates, and the next mutual action. Do not invent customer commitments, references, discounts, or forecast certainty.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `sales-account-plan` | Create an account plan based on customer outcomes, stakeholders, risks, and verified activity. |
| `sales-discovery` | Prepare neutral discovery questions that uncover customer needs, impact, constraints, and decision process. |
| `sales-qualification` | Assess opportunity fit and deal risk using transparent qualification evidence. |
| `sales-pipeline` | Inspect pipeline quality and next-step integrity to improve forecast and coaching. |
| `sales-forecast` | Build a revenue forecast with explicit assumptions, scenarios, and confidence. |
| `sales-proposal` | Draft a customer proposal tied to stated needs, outcomes, scope, assumptions, and evidence. |
| `sales-negotiation` | Prepare negotiation options and concession boundaries grounded in approved commercial policy. |
| `sales-objection` | Answer a sales objection with accurate evidence and a useful next question. |
| `sales-territory` | Balance account coverage and sales capacity across a territory using transparent criteria. |
| `sales-renewal` | Protect a renewal by connecting adoption, realized outcomes, risks, and agreed next value. |

## Focused procedures

### Strategic Account Plan (`sales-account-plan`)

Summarize customer goals, buying roles, current solution, value hypothesis, relationship evidence, competition, next milestones, and mutual actions. Mark unknown stakeholder views and avoid fabricating customer intent.

### Sales Discovery (`sales-discovery`)

Tailor questions to the prospect's context, quantify current impact without leading, identify users and approvers, and test urgency and alternatives. Capture direct statements separately from sales interpretation.

### Opportunity Qualification (`sales-qualification`)

Evaluate business problem, measurable impact, sponsor, decision process, timing, competition, implementation fit, and next customer-confirmed action. Identify disconfirming signals and do not inflate CRM confidence.

### Pipeline Review (`sales-pipeline`)

Review stage evidence, aging, amount provenance, buyer engagement, mutual plan, and next step. Flag stale or unsupported opportunities and distinguish pipeline coverage from forecast confidence.

### Revenue Forecast (`sales-forecast`)

Reconcile source opportunities and historical conversion, define cutoff and currency, model slippage and risk, and show base/upside/downside. Never present a scenario or quota target as a committed forecast.

### Customer Proposal (`sales-proposal`)

Use confirmed requirements, measurable outcomes, deliverables, exclusions, timeline assumptions, responsibilities, pricing source, and acceptance. Flag unsupported claims and route commercial or legal terms for approval.

### Commercial Negotiation Preparation (`sales-negotiation`)

Identify customer priorities, our walk-away conditions, value exchange, approval limits, and conditional concessions. Never invent authority, promise unapproved terms, or misrepresent alternatives.

### Customer Objection Response (`sales-objection`)

Clarify the concern, respond only with verified product or service evidence, acknowledge limits, and ask what would resolve the issue. Escalate roadmap, security, legal, or performance claims to an owner.

### Territory and Coverage Plan (`sales-territory`)

Use account potential evidence, segment, workload, geography, existing commitments, and representative capacity. Show assumptions and fairness checks; do not treat proxy data as certain buying intent.

### Renewal and Expansion Plan (`sales-renewal`)

Review usage and outcomes against the customer plan, open issues, stakeholders, renewal dates, and contract facts. Identify at-risk gaps honestly and agree an actionable recovery or expansion path.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [manojbajaj95/claude-gtm-plugin / sales-and-revenue-operations](research/manojbajaj95-claude-gtm-plugin-sales-and-revenue-operations/GUIDE.md): MIT.
- [coreyhaines31/marketingskills / revops](research/coreyhaines31-marketingskills-revops/GUIDE.md): MIT.
- [autonnel/autonnel-skills / landing-page-conversion-audit](research/autonnel-autonnel-skills-landing-page-conversion-audit/GUIDE.md): Apache-2.0.
- [mbfinotti/revops-skills / revenue-funnel](research/mbfinotti-revops-skills-revenue-funnel/GUIDE.md): MIT.
- [mbfinotti/revops-skills / revenue-leakage](research/mbfinotti-revops-skills-revenue-leakage/GUIDE.md): MIT.
- [mbfinotti/revops-skills / revenue-data-governance-strategy](research/mbfinotti-revops-skills-revenue-data-governance-strategy/GUIDE.md): MIT.
- [mbfinotti/revops-skills / pipeline-stage-definition-audit](research/mbfinotti-revops-skills-pipeline-stage-definition-audit/GUIDE.md): MIT.
- [mbfinotti/revops-skills / revops-radar](research/mbfinotti-revops-skills-revops-radar/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
