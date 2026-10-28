---
name: data-science
description: "Clean and analyze data with reproducible SQL, statistics, experiments, visualizations, and spatial methods."
license: Apache-2.0 AND CC-BY-4.0 AND MIT
---

# GNCore Data Science

## Select the work from the user's intent

Define the unit of analysis, hypothesis or question, population, period, and decision. Inspect missingness, selection, duplicates, distributions, and measurement definitions. Choose descriptive, inferential, experimental, predictive, or spatial methods appropriate to the data.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Show denominators, uncertainty, assumptions, sensitivity, and limitations. Separate association from causation and use comparable groups or explicit identification assumptions for causal claims.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `clean-data` | Audit and clean a dataset with explicit, reversible rules for missing values, duplicates, types, and outliers. |
| `analyze` | Answer a data question with reproducible analysis, explicit assumptions, and evidence tied to the provided data. |
| `sql-analysis` | Write correct, reviewable SQL for analytics while guarding against join fanout and misleading aggregates. |
| `data-visualization` | Create clear charts that faithfully represent the underlying data and its uncertainty. |
| `statistics` | Choose and interpret statistical methods with assumptions, uncertainty, and practical effects stated clearly. |
| `ab-testing` | Analyze controlled experiments with valid assignment checks, predeclared metrics, and practical uncertainty. |
| `geospatial-analysis` | Analyze spatial data with explicit coordinate systems, units, geometry validity, and privacy controls. |

## Focused procedures

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

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [google/skills / google-cloud-solution-agentic-ai-data-science-workflow](research/google-skills-google-cloud-solution-agentic-ai-data-science-workflow/GUIDE.md): Apache-2.0.
- [personamanagmentlayer/pcl / data-science-expert](research/personamanagmentlayer-pcl-data-science-expert/GUIDE.md): Apache-2.0.
- [travisjneuman/.claude / data-science](research/travisjneuman-.claude-data-science/GUIDE.md): MIT.
- [microsoftdocs/agent-skills / azure-data-science-vm](research/microsoftdocs-agent-skills-azure-data-science-vm/GUIDE.md): CC-BY-4.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
