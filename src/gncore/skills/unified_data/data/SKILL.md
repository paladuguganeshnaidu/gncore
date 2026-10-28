---
name: data
description: "Inspect, transform, analyze, and move data through reproducible pipelines with explicit contracts."
license: Apache-2.0 AND MIT
---

# GNCore Data

## Select the work from the user's intent

Identify the question, source schema, data grain, keys, units, missingness, and downstream consumers. Preserve raw inputs and define deterministic transformations, validation, lineage, scheduling, and recovery around the actual workload.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Check row counts, key uniqueness, schema drift, missing values, reconciliation, incremental behavior, and replay safety. Keep queries and transformations reproducible.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `data-analysis` | Answer data questions with reproducible calculations, clear definitions, and honest uncertainty. |
| `data-pipelines` | Build reliable, observable data pipelines with explicit schemas, retries, and idempotency. |

## Focused procedures

### Data Analysis (`data-analysis`)

Translate the question into a measurable quantity and inspect the relevant columns and missingness. Show the denominator, filters, time window, and aggregation. Check duplicates and outliers where they affect the answer. Label estimates and caveats; never fabricate values or imply causation from correlation.

### Data Pipeline Engineering (`data-pipelines`)

Trace source-to-sink data flow and failure semantics. Define schema and validation at boundaries, make retries idempotent, handle late or duplicate records, and emit actionable logs without secrets or sensitive payloads. Preserve existing schedules and production destinations unless the request explicitly changes them.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [vercel-labs/agent-browser / agent-browser](research/vercel-labs-agent-browser-agent-browser/GUIDE.md): Apache-2.0.
- [supabase/agent-skills / supabase-postgres-best-practices](research/supabase-agent-skills-supabase-postgres-best-practices/GUIDE.md): MIT.
- [microsoft/azure-skills / microsoft-foundry](research/microsoft-azure-skills-microsoft-foundry/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-storage](research/microsoft-azure-skills-azure-storage/GUIDE.md): MIT.
- [microsoft/azure-skills / azure-kusto](research/microsoft-azure-skills-azure-kusto/GUIDE.md): MIT.
- [prisma/skills / prisma-client-api](research/prisma-skills-prisma-client-api/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
