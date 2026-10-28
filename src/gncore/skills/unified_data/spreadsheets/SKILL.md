---
name: spreadsheets
description: "Build, audit, clean, analyze, visualize, forecast, and automate spreadsheets with correct formulas and readable models."
license: MIT
---

# GNCore Spreadsheets and Excel

## Select the work from the user's intent

Inspect workbook structure, inputs, formulas, units, dates, dependencies, and intended decisions. Separate inputs, assumptions, calculations, and outputs. Choose modeling, formula audit, cleaning, analysis, dashboard, pivot, forecasting, reconciliation, automation, or presentation work.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Recalculate with an appropriate engine when available, reconcile totals, inspect formula errors and edge cases, and render key sheets to check labels, widths, number formats, and chart readability.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `sheet-model` | Structure a spreadsheet model with clear inputs, calculations, outputs, and traceable assumptions. |
| `sheet-formula-audit` | Audit workbook formulas for broken references, inconsistencies, hard-codes, and calculation errors. |
| `sheet-clean` | Clean tabular spreadsheet data with explicit rules and before/after reconciliation. |
| `sheet-analysis` | Answer an analytical question from workbook data with transparent formulas and checks. |
| `sheet-dashboard` | Build a decision-focused spreadsheet dashboard with stable formulas, labels, filters, and accessible visuals. |
| `sheet-pivot` | Create or review pivot analyses with verified source range, grouping, aggregation, and filter behavior. |
| `sheet-forecast` | Build or audit a forecast workbook with driver-based assumptions, scenarios, and error checks. |
| `sheet-reconcile` | Reconcile two data sources with stable keys, exception categories, and totals control. |
| `sheet-automation` | Automate repetitive workbook transformations with idempotent runs and safe output handling. |
| `sheet-presentation` | Prepare a workbook for review or print with consistent formats, frozen headers, page setup, and clear labels. |

## Focused procedures

### Spreadsheet Model Design (`sheet-model`)

Separate inputs and formulas, document units and sources, use consistent time axes, avoid hard-coded values inside formulas, and test base/downside cases. Protect source data from accidental edits.

### Spreadsheet Formula Audit (`sheet-formula-audit`)

Inspect workbook sheets, named ranges, formula patterns, error cells, hidden regions, and external links. Trace key outputs to source cells and calculate independent spot checks.

### Spreadsheet Data Cleaning (`sheet-clean`)

Preserve the raw sheet, inspect headers, types, blanks, duplicates, units, and merged cells, apply documented transformations, and compare row counts and summary totals after cleaning.

### Spreadsheet Data Analysis (`sheet-analysis`)

Inspect grain, fields, data types, missing values, and workbook formulas before analysis. Use explicit filters and denominators, reconcile a sample to source rows, and state limitations.

### Spreadsheet Dashboard (`sheet-dashboard`)

Define audience and decisions, use a clean data table, validate KPI formulas, label periods and units, add clear filter state, and test refresh and empty-data behavior.

### Pivot Table Analysis (`sheet-pivot`)

Confirm each field's meaning and aggregation, expand the source range, check blanks and duplicates, and reconcile pivot totals to raw data. Document filters and refresh behavior.

### Spreadsheet Forecast Model (`sheet-forecast`)

Separate actuals and forecasts, document drivers and units, extend formulas consistently, model scenarios explicitly, and test sensitivity and historical backtests. Do not present the forecast as certainty.

### Spreadsheet Reconciliation (`sheet-reconcile`)

Normalize keys without changing source values, identify duplicates and unmatched rows, compare amounts with tolerances, categorize exceptions, and prove source and output totals reconcile.

### Spreadsheet Automation (`sheet-automation`)

Inspect workbook structure and formulas, preserve input, define deterministic transformations, validate output schema and formulas, and test on a copy. Do not enable macros or execute unknown embedded code.

### Spreadsheet Presentation Cleanup (`sheet-presentation`)

Apply consistent number/date formats, remove accidental clutter without deleting source content, set print areas and repeat headers, test page breaks, and verify the saved workbook opens cleanly.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [firecrawl/anydoc / convert-documents-to-markdown](research/firecrawl-anydoc-convert-documents-to-markdown/GUIDE.md): MIT.
- [claude-office-skills/skills / xlsx-manipulation](research/claude-office-skills-skills-xlsx-manipulation/GUIDE.md): MIT.
- [minimax-ai/skills / minimax-xlsx](research/minimax-ai-skills-minimax-xlsx/GUIDE.md): MIT.
- [davila7/claude-code-templates / excel-analysis](research/davila7-claude-code-templates-excel-analysis/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
