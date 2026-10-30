---
name: data-science
description: "Analyze data, statistics and experiments with correct grain, reproducibility and honest uncertainty."
license: MIT
---

# GNCore Data Science

Version: 7.0.0

## Choose the work

Define the question, estimand, sampling/assignment mechanism, units and time period. Audit missingness and join fanout before interpreting patterns.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Reproducible analysis, queries or charts with source provenance, transformations, assumptions, units and decision-relevant uncertainty.

Reconcile aggregates to source rows, test a small known fixture, inspect assumptions and distinguish association from causation. Do not manufacture significance or unobserved results.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Define the estimand, population, observational unit and denominator before calculating a percentage. Reconcile joins and counts; unequal weighting alone is not Simpson's paradox. Inspect missingness, selection and plausible confounding, and separate descriptive association from a supported causal conclusion. Quantify uncertainty at the right independent unit. Do not quote a p-value or significance result that was not calculated and checked; preserve the exact calculation and its assumptions.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Reconcile the observational unit, assigned population, denominators and join cardinality before estimating effects; inspect attrition and post-treatment selection.
- Check quoted arithmetic and uncertainty at the independent unit; choose suitable projected or geodesic calculations for spatial quantities and distinguish inference from causal evidence.

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

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
