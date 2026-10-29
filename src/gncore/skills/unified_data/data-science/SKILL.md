---
name: data-science
description: "Analyze data, statistics and experiments with correct grain, reproducibility and honest uncertainty."
license: MIT
---

# GNCore Data Science

Version: 7.0.0rc1

## Choose the work

Define the question, estimand, sampling/assignment mechanism, units and time period. Audit missingness and join fanout before interpreting patterns.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

## Deliver and verify

Reproducible analysis, queries or charts with source provenance, transformations, assumptions, units and decision-relevant uncertainty.

Reconcile aggregates to source rows, test a small known fixture, inspect assumptions and distinguish association from causation. Do not manufacture significance or unobserved results.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `product-analytics` | Define product metrics and event instrumentation that answer a decision without collecting unnecessary data. |
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
| `clean-data` | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. |
| `analyze` | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. |
| `sql-analysis` | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. |
| `data-visualization` | Create clear charts that faithfully represent the underlying data and its uncertainty. |
| `statistics` | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. |
| `ab-testing` | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. |
| `geospatial-analysis` | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. |

## Focused procedures

### Product Analytics (`product-analytics`)

Start with the decision and user outcome, then define event grain, actor, timestamp, properties, denominator, and exclusions. Check identity stitching, consent, retention, and duplicate events. Prefer a small event schema with stable names and versioning. Validate counts end to end and document known blind spots. Avoid collecting sensitive attributes without a clear, approved need.

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

### Clean a Dataset (`clean-data`)

Profile the raw data before changing it: schema, nulls, duplicate keys, invalid ranges, category variants, and suspicious distributions. Clarify what each row represents and preserve a read-only source. Apply only defensible rules, log affected rows and counts, and keep a reproducible script. Do not silently impute, discard outliers, deduplicate on an arbitrary field, or overwrite the original. Compare before/after summaries and flag ambiguous cases.

### Analyze Data (`analyze`)

Clarify the unit of analysis and question. Inspect data definitions, missingness, time coverage, and possible selection bias before calculating. Use suitable summaries and comparisons; show denominators and uncertainty when relevant. Separate association from causation and observed facts from interpretation. Keep queries or code reproducible, avoid exposing sensitive records, and state what the data cannot establish.

### SQL Analysis (`sql-analysis`)

Read table definitions and grain before joining. State the intended row grain, join keys, time zone, null behavior, and filters. Check for fanout and use explicit columns. Validate row counts, distinct keys, and edge cases against a small known sample. Avoid expensive full scans or writes on production systems unless explicitly authorized; explain assumptions and query cost risks.

### Data Visualization (`data-visualization`)

Match chart form to the question and data type. Label units, denominators, time range, and transformations; show missing data and uncertainty when material. Use honest axes and accessible color/labels. Validate plotted values against source aggregates and avoid implying causality from descriptive data. Keep dashboards focused on decisions and explain filters and refresh timing.

### Statistical Analysis (`statistics`)

Translate the question into an estimand and identify sampling and assignment mechanisms. Check assumptions, missingness, dependence, and multiple testing. Report effect size and uncertainty, not just a p-value. Distinguish exploratory findings from confirmatory analysis and association from causation. Do not imply a result is actionable without considering study design and practical impact.

### A/B Test Analysis (`ab-testing`)

Confirm randomization unit, exposure, experiment window, primary metric, guardrails, and stopping rule. Check sample-ratio mismatch, logging gaps, interference, and repeated peeking. Estimate effect with uncertainty and predeclared method; handle multiple comparisons explicitly. Report absolute and relative impact and segment findings as exploratory unless preplanned. Do not declare a winner from an underpowered or invalid test.

### Geospatial Analysis (`geospatial-analysis`)

Inspect coordinate reference systems, units, geometry validity, spatial grain, and boundary versions. Reproject before distance/area calculations and validate joins for duplicates and boundary effects. Use an appropriate map scale and disclose aggregation. Protect sensitive locations and avoid implying precise location where uncertainty or privacy requires aggregation.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
