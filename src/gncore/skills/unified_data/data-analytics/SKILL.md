---
name: data-analytics
description: "Answer business questions with reproducible data audits, SQL, metrics, cohorts, experiments, forecasts, and dashboards."
license: MIT
---

# GNCore Data Analytics and Intelligence

## Select the work from the user's intent

Define the question, unit of analysis, data grain, period, denominator, and decision to support. Select audit, query, visualization, metric design, cohort, experiment, forecast, insight, or data-contract work. Inspect missingness, duplication, joins, and selection effects before interpreting results.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Reconcile totals, validate joins and filters, show uncertainty and limitations, and preserve a reproducible query or calculation path.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `analytics-question` | Translate a business question into a measurable analysis plan and data requirements. |
| `analytics-data-audit` | Audit analytical data for missingness, duplication, validity, freshness, and grain. |
| `analytics-sql` | Write a traceable SQL analysis with correct grain, joins, time handling, and reconciliation. |
| `analytics-dashboard` | Design a dashboard around a recurring decision with clear metrics, filters, and data freshness. |
| `analytics-metric-tree` | Decompose a business outcome into leading drivers and measurable operational inputs. |
| `analytics-cohort` | Compare cohort behavior with consistent definitions, exposure windows, and censoring treatment. |
| `analytics-experiment` | Analyze an experiment with assignment, exposure, predeclared outcomes, and uncertainty checks. |
| `analytics-forecast` | Build a business forecast from history, drivers, scenarios, and out-of-sample checks. |
| `analytics-insight-brief` | Turn analysis into a concise decision brief with traceable evidence and caveats. |
| `analytics-data-contract` | Specify ownership, schema, quality, freshness, and change handling for an analytics dataset. |

## Focused procedures

### Analytics Question Plan (`analytics-question`)

Define decision, population, unit of analysis, outcome, comparison, time range, data sources, and limitations before querying. Identify causal language that the available design cannot support.

### Data Quality Audit (`analytics-data-audit`)

Profile schema, keys, nulls, ranges, category drift, late arrivals, and row grain. Report counts and affected segments, preserve raw data, and turn material defects into owned checks.

### Business SQL Analysis (`analytics-sql`)

Inspect source definitions, declare expected row grain, parameterize inputs, verify join cardinality, and reconcile totals to a trusted control. Avoid expensive or mutating production queries without authorization.

### Decision Dashboard (`analytics-dashboard`)

Name the audience and decision, define metrics and denominators, show time window and freshness, add useful breakdowns, and check accessibility. Remove charts that do not change a decision.

### Metric Tree (`analytics-metric-tree`)

Define the top outcome, decompose mathematically or causally only where evidence supports it, annotate owner and source for each metric, and distinguish controllable inputs from external factors.

### Cohort Analysis (`analytics-cohort`)

Specify cohort entry, event, observation window, time zone, exclusions, and incomplete follow-up. Check cohort comparability and report uncertainty and survivorship bias.

### Business Experiment Analysis (`analytics-experiment`)

Validate randomization, sample ratio, instrumentation, metric definition, duration, and stopping rule. Estimate effect with uncertainty and guardrails; do not declare success from post-hoc slicing.

### Business Forecast Analysis (`analytics-forecast`)

Check data coverage and structural changes, establish a simple baseline, use time-ordered validation, and compare scenarios. Explain forecast error and avoid false precision or unsupported causal narratives.

### Executive Analytics Brief (`analytics-insight-brief`)

Lead with the decision and finding, show key numbers with units and denominators, link to source and method, explain alternatives and limitations, and specify next actions and owners.

### Analytics Data Contract (`analytics-data-contract`)

Document grain, fields, types, allowed values, null semantics, primary keys, freshness SLA, owner, consumers, and compatibility policy. Define tests and an escalation route for breaking changes.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [microsoft/azure-skills / azure-kusto](research/microsoft-azure-skills-azure-kusto/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
