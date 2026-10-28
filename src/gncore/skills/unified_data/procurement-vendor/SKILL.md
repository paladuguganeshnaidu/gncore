---
name: procurement-vendor
description: "Prepare sourcing requirements, RFPs, vendor comparisons, due diligence, negotiations, and vendor lifecycle plans."
license: Apache-2.0 AND MIT
---

# GNCore Procurement and Vendor Management

## Select the work from the user's intent

Define the business need, mandatory requirements, evaluation weights, total-cost horizon, and decision owner before comparing offers. Consider integration, service quality, security, exit costs, and vendor concentration alongside price.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Apply the same criteria to every offer, verify quoted terms, show assumptions in total cost, and identify diligence gaps, contract dependencies, and exit obligations.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `procurement-requirements` | Translate a business need into measurable, vendor-neutral procurement requirements. |
| `procurement-rfp` | Prepare a fair request for proposal with scope, scoring, schedule, and response instructions. |
| `procurement-scorecard` | Score supplier proposals against published criteria with evidence and consistent normalization. |
| `procurement-total-cost` | Compare vendor options across implementation, usage, support, renewal, exit, and risk costs. |
| `procurement-due-diligence` | Coordinate risk-based supplier due diligence across security, privacy, finance, and continuity. |
| `procurement-negotiation` | Prepare negotiation priorities and fallback options within approved procurement authority. |
| `procurement-onboarding` | Coordinate supplier onboarding with least-privilege access, ownership, and required control evidence. |
| `procurement-performance` | Review vendor service against contracted outcomes, service levels, and corrective actions. |
| `procurement-renewal` | Make a renewal decision using value, risk, alternatives, usage, and notice deadlines. |
| `procurement-exit` | Plan a controlled supplier transition that protects service, data, access, and records. |

## Focused procedures

### Procurement Requirements (`procurement-requirements`)

Separate mandatory outcomes from preferences, define acceptance evidence, service levels, security/privacy needs, accessibility, support, and lifecycle cost. Avoid requirements that unfairly lock the process to one vendor.

### RFP Package (`procurement-rfp`)

Define eligibility, scope, response format, evaluation weights, questions period, decision authority, and conflicts process. Ensure each criterion is testable and consistently applied; route terms to procurement and counsel.

### Vendor Scorecard (`procurement-scorecard`)

Use the same rubric for each bidder, cite response evidence, separate evaluator judgment from facts, disclose conflicts, and record unanswered requirements. Do not adjust weights after viewing results without governance approval.

### Total Cost of Ownership (`procurement-total-cost`)

Normalize contract periods, units, volumes, currency, discount assumptions, implementation, integration, training, support, and exit costs. Show sensitivity and distinguish quoted amounts from estimated costs.

### Supplier Due Diligence (`procurement-due-diligence`)

Apply supplied policy, risk tier, evidence date, scope, reviewer, and unresolved issue. Do not accept attestations as proof of controls; escalate critical gaps and avoid collecting unnecessary personal data.

### Supplier Negotiation Plan (`procurement-negotiation`)

Rank business needs, service protections, commercial levers, alternatives, approval limits, and tradeable concessions. Do not accept terms or bind the organization; route redlines to authorized signers and counsel.

### Supplier Onboarding (`procurement-onboarding`)

Confirm business sponsor, approved scope, contract status, data access, security review, payment setup, integrations, and renewal owner. Do not grant production access before required approvals are documented.

### Supplier Performance Review (`procurement-performance`)

Reconcile source telemetry to contractual measures and reporting window, record exclusions and incidents, assess trend and customer impact, and track owner/date for each remediation.

### Vendor Renewal Review (`procurement-renewal`)

Verify notice windows and contract terms, adoption and realized value, service incidents, price changes, dependency and exit cost. Present renew, renegotiate, replace, or exit options with owners and deadlines.

### Supplier Exit Plan (`procurement-exit`)

Map data export and deletion, credentials, integrations, user migration, dependencies, service overlap, and acceptance evidence. Assign accountable owners, sequence reversible steps, and verify exit obligations with counsel.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [anthropics/knowledge-work-plugins / vendor-review](research/anthropics-knowledge-work-plugins-vendor-review/GUIDE.md): Apache-2.0.
- [suzheng/k2f / k2f-purchase-order](research/suzheng-k2f-k2f-purchase-order/GUIDE.md): Apache-2.0.
- [rampstackco/claude-skills / vendor-evaluation](research/rampstackco-claude-skills-vendor-evaluation/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / business-operations-skills](research/alirezarezvani-claude-skills-business-operations-skills/GUIDE.md): MIT.
- [alirezarezvani/claude-skills / knowledge-ops](research/alirezarezvani-claude-skills-knowledge-ops/GUIDE.md): MIT.
- [mims-harvard/tooluniverse / tooluniverse-chemical-sourcing](research/mims-harvard-tooluniverse-tooluniverse-chemical-sourcing/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
