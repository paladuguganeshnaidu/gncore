---
name: cloud
description: "Evaluate cloud architecture and cost choices against workload, reliability, security, and operational constraints."
license: MIT
---

# GNCore Cloud

## Select the work from the user's intent

Inspect the actual provider, workload, data sensitivity, traffic shape, recovery objectives, team capacity, and budget. Compare managed and self-managed options by total operating burden, failure modes, scale, portability, and cost assumptions.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Validate architecture assumptions, trust boundaries, capacity estimates, recovery plans, and cost sensitivity. Mark estimates and avoid claiming compliance or deployed readiness without evidence.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cloud-architecture` | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | Find measurable cloud cost reductions while protecting reliability and workload correctness. |

## Focused procedures

### Cloud Architecture (`cloud-architecture`)

Inspect the current provider, workload, data classification, traffic, recovery targets, team skills, and budget. Prefer managed services only when their operational and cost tradeoffs fit. Define trust boundaries, failure modes, backup/restore, and observability. Do not create resources or expose endpoints without authorization. Mark estimates and assumptions; avoid claiming compliance without evidence.

### Cloud Cost Optimization (`cost-optimization`)

Use billing and utilization evidence with a stated period and scope. Separate idle waste, rightsizing, storage lifecycle, and architecture changes. Estimate savings and service risk; identify reversibility and validation. Avoid deleting resources, reducing capacity, or purchasing commitments without approval. Measure after a change and retain rollback options.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [microsoft/azure-skills / azure-cloud-migrate](research/microsoft-azure-skills-azure-cloud-migrate/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
