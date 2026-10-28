---
name: legal-compliance
description: "Organize legal intake, contract obligations, compliance evidence, policy gaps, and review materials."
license: Apache-2.0 AND MIT
---

# GNCore Legal and Compliance Support

## Select the work from the user's intent

Identify jurisdiction, parties, purpose, dates, controlling documents, and the requested administrative or analytical deliverable. Separate quoted provisions, interpretations, risk hypotheses, and proposed wording. Preserve privilege designations and route consequential legal conclusions to a qualified reviewer.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Cite the actual provision or authoritative rule supporting each material issue. Check version, effective date, defined terms, cross-references, and unresolved factual dependencies.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `legal-contract-intake` | Extract obligations, deadlines, and questions from a supplied contract for counsel review. |
| `legal-obligation-map` | Turn contract or policy text into traceable obligations, owners, dates, and evidence. |
| `legal-policy-gap` | Compare supplied controls or evidence against a named policy or framework requirement. |
| `legal-privacy-intake` | Structure a privacy review by mapping purpose, data, access, retention, and user impact. |
| `legal-regulatory-watch` | Summarize a supplied regulatory update and identify affected business processes for expert review. |
| `legal-incident-hold` | Organize a preservation checklist from authorized instructions without altering source records. |
| `legal-marketing-claims` | Trace public claims to substantiation and flag claims needing legal or regulatory review. |
| `legal-entity-records` | Organize entity governance records and upcoming filing or approval actions from supplied records. |
| `legal-dispute-chronology` | Build a source-linked chronology from supplied dispute materials for counsel review. |
| `legal-review-memo` | Draft a neutral issue-and-evidence memo for a qualified lawyer to review. |

## Focused procedures

### Contract Review Intake (`legal-contract-intake`)

Identify document version, parties, term, payment, termination, liability, data, and governing-law clauses with section references. Flag ambiguity as a question; do not determine enforceability or provide jurisdiction-specific advice.

### Obligation Tracker (`legal-obligation-map`)

Capture exact source clause, obligation, trigger, owner, due date, evidence, dependencies, and uncertainty. Preserve original wording where interpretation matters and route unclear duties to counsel.

### Compliance Gap Assessment (`legal-policy-gap`)

Use the exact provided version and requirement IDs, link each conclusion to evidence, and label not assessed versus unmet. Do not claim certification, legal compliance, or audit assurance from a desk review.

### Privacy Review Intake (`legal-privacy-intake`)

Trace data source, purpose, categories, recipients, access, storage, retention, deletion, and user rights. Minimize personal data and route legal bases and jurisdiction conclusions to qualified privacy counsel.

### Regulatory Change Brief (`legal-regulatory-watch`)

Verify source authority, publication and effective dates, jurisdiction, affected entities, and text version. Separate quoted requirements from operational interpretation and flag legal questions for counsel.

### Legal Hold Coordination Checklist (`legal-incident-hold`)

Record custodian scope, systems, date ranges, preservation owner, acknowledgments, and exceptions from the supplied legal direction. Do not delete, modify, or independently decide when a hold begins or ends.

### Marketing Claims Review (`legal-marketing-claims`)

Inventory exact claim, audience, channel, evidence, qualification, expiry, and owner. Distinguish substantiation gaps from legal conclusions and do not publish or approve claims.

### Corporate Records Checklist (`legal-entity-records`)

Identify entity, record type, jurisdiction, period, source, custodian, deadline, and required approver. Flag missing records and verify filing duties with the responsible professional.

### Dispute Chronology (`legal-dispute-chronology`)

Normalize dates and time zones, quote or summarize only necessary text, preserve source IDs, distinguish allegations from established facts, and note gaps or contradictory accounts. Protect privilege and confidentiality.

### Legal Review Memo Support (`legal-review-memo`)

State the question, jurisdiction if supplied, relevant source text, facts assumed, competing interpretations, missing evidence, and questions for counsel. Do not conclude legal rights or replace professional advice.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [travisjneuman/.claude / legal-compliance](research/travisjneuman-.claude-legal-compliance/GUIDE.md): MIT.
- [mbfinotti/sales-skills / cold-email-deliverability](research/mbfinotti-sales-skills-cold-email-deliverability/GUIDE.md): MIT.
- [anthropics/knowledge-work-plugins / meeting-briefing](research/anthropics-knowledge-work-plugins-meeting-briefing/GUIDE.md): Apache-2.0.
- [mbfinotti/partnerships-skills / affiliate-program-terms](research/mbfinotti-partnerships-skills-affiliate-program-terms/GUIDE.md): MIT.
- [samber/cc-skills / site-launch-checklist](research/samber-cc-skills-site-launch-checklist/GUIDE.md): MIT.
- [phuryn/pm-skills / privacy-policy](research/phuryn-pm-skills-privacy-policy/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
