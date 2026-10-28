---
name: data-engineering
description: "Design databases, data pipelines, and governance with explicit schemas, ownership, lineage, and quality controls."
license: Apache-2.0 AND MIT
---

# GNCore Data Engineering

## Select the work from the user's intent

Inspect access patterns, data contracts, change rate, consistency needs, sensitivity, retention, and operational scale. Choose schema, ingestion, transformations, orchestration, or governance controls to fit the actual consumers and recovery requirements.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify constraints, migrations, data-quality rules, lineage, access controls, retention behavior, and backfill or replay safety with representative inputs.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `database-design` | Design safe relational data models, queries, and migrations that preserve integrity and performance. |
| `data-pipeline` | Build observable, restartable pipelines with explicit schemas, idempotency, and data-quality checks. |
| `data-governance` | Define practical ownership, quality, access, lineage, and retention controls for a data asset. |

## Focused procedures

### Database Design (`database-design`)

Inspect the database engine, schema, constraints, data volume, and access patterns. Encode invariants with appropriate constraints and indexes; parameterize input. Make migrations reversible and consider locking, backfill, and compatibility. Never run destructive SQL or apply a migration to production without explicit authorization. Verify query plans or migration behavior with a safe local fixture when possible.

### Data Pipeline Engineering (`data-pipeline`)

Trace source, ownership, freshness, volume, schema evolution, and retry semantics. Make stages idempotent, checkpoint safely, validate schemas and key quality invariants, and expose useful failure context. Protect credentials and sensitive data. Keep backfills bounded and never trigger production backfills or mutate source systems without authorization.

### Data Governance (`data-governance`)

Identify asset owner, purpose, source, sensitivity, consumers, transformations, quality expectations, and retention. Propose least-privilege access, lineage, quality checks, and deletion handling. Separate policy facts from recommendations and flag legal or regulatory interpretations for experts. Avoid copying sensitive datasets into examples or test fixtures.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [wshobson/agents / dbt-transformation-patterns](research/wshobson-agents-dbt-transformation-patterns/GUIDE.md): MIT.
- [affaan-m/ecc / clickhouse-io](research/affaan-m-ecc-clickhouse-io/GUIDE.md): MIT.
- [affaan-m/ecc / mle-workflow](research/affaan-m-ecc-mle-workflow/GUIDE.md): MIT.
- [langchain-ai/langchain-skills / eval-engineering](research/langchain-ai-langchain-skills-eval-engineering/GUIDE.md): MIT.
- [wondelai/skills / release-it](research/wondelai-skills-release-it/GUIDE.md): MIT.
- [mastra-ai/mastra / react-best-practices](research/mastra-ai-mastra-react-best-practices/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
