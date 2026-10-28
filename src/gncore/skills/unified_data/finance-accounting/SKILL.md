---
name: finance-accounting
description: "Prepare financial models, reconciliations, budgets, forecasts, close support, and variance explanations."
license: MIT
---

# GNCore Finance and Accounting

## Select the work from the user's intent

Establish entity, period, currency, accounting definitions, and source of truth. Separate actuals, estimates, forecasts, and scenarios. Select budgeting, forecasting, variance, liquidity, unit economics, close, controls, investment cases, expenses, or reporting work.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Reconcile balances and source totals; check signs, formulas, units, dates, and scenario sensitivities. Identify accounting or tax judgments requiring qualified review rather than inventing a treatment.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `finance-budget` | Build a traceable budget from operational drivers, assumptions, owners, and approved targets. |
| `finance-forecast` | Update a rolling forecast from actuals and current business drivers without hiding variance. |
| `finance-variance` | Explain financial variance by volume, price, mix, timing, and one-time effects. |
| `finance-cashflow` | Model cash needs and runway using explicit receipts, obligations, and timing scenarios. |
| `finance-unit-economics` | Calculate unit economics with consistent cohort, cost allocation, and contribution assumptions. |
| `finance-month-close` | Coordinate a complete month-end close with reconciliations, owners, evidence, and review. |
| `finance-controls` | Review financial process controls for authorization, reconciliation, evidence, and segregation. |
| `finance-investment-case` | Build a decision-ready capital request with costs, benefits, alternatives, and sensitivity. |
| `finance-expense` | Assess expense submissions against supplied policy with consistent evidence and escalation. |
| `finance-report` | Review a financial report for arithmetic, consistency, labels, source traceability, and decision clarity. |

## Focused procedures

### Budget Build (`finance-budget`)

Reconcile opening baseline, volume and price drivers, headcount, timing, one-time costs, and scenario assumptions. Tie every material line to an owner and source; label pending decisions clearly.

### Rolling Forecast (`finance-forecast`)

Reconcile actuals to ledger, refresh operational drivers, explain variance and forecast changes, and retain prior snapshots. Show scenario ranges and separate expected outcomes from targets.

### Financial Variance Analysis (`finance-variance`)

Validate periods, account mapping, currency, and calculation. Bridge actual to plan or prior period, quantify material drivers, distinguish timing from structural change, and identify owner-approved actions.

### Cash Flow and Runway (`finance-cashflow`)

Reconcile cash balance and restricted funds, model collections, payroll, payables, financing, and downside timing. Show sensitivity and minimum-cash triggers; do not present a model as investment or solvency advice.

### Unit Economics (`finance-unit-economics`)

Define the unit and cohort, include variable acquisition, delivery, support, refund, and payment costs, and reconcile numerator and denominator. Show sensitivity and avoid treating allocated fixed costs as variable.

### Month-End Close Checklist (`finance-month-close`)

Use the organization's accounting policy and calendar. Track subledger close, accruals, reconciliations, review evidence, exceptions, and approvals. Never create or post unsupported journal entries.

### Financial Controls Review (`finance-controls`)

Map transaction risks to preventive and detective controls, control owner, frequency, evidence, reviewer, and exception follow-up. Do not claim audit effectiveness without operating evidence and appropriate assurance.

### Investment Business Case (`finance-investment-case`)

Separate cash flows from accounting effects, show timing and discount assumptions if used, include implementation and operating costs, compare alternatives, and quantify break-even conditions. Identify unverified benefits.

### Expense Policy Review (`finance-expense`)

Apply the provided policy and thresholds, verify receipt and business purpose, record exceptions neutrally, and protect personal information. Do not infer fraud or approve exceptions outside granted authority.

### Financial Report Review (`finance-report`)

Recalculate key totals, check period and unit consistency, reconcile against source statements, label non-GAAP measures, and surface uncertainty. Route accounting judgments and external reporting to authorized professionals.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [joellewis/finance_skills / performance-metrics](research/joellewis-finance-skills-performance-metrics/GUIDE.md): MIT.
- [samuelcastro/startup-skills / finance-accounting](research/samuelcastro-startup-skills-finance-accounting/GUIDE.md): MIT.
- [erphq/skills / finance-accounting-tech](research/erphq-skills-finance-accounting-tech/GUIDE.md): MIT.
- [peterbamuhigire/proposal-skills / accounting-finance-advisory](research/peterbamuhigire-proposal-skills-accounting-finance-advisory/GUIDE.md): MIT.
- [peterbamuhigire/chwezi-dev-engine / accounting-finance-controller](research/peterbamuhigire-chwezi-dev-engine-accounting-finance-controller/GUIDE.md): MIT.
- [peterbamuhigire/business-plan-skills / meta-accounting-finance-review](research/peterbamuhigire-business-plan-skills-meta-accounting-finance-review/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
