---
name: cloud-devops-sre
description: "Build delivery pipelines, cloud infrastructure, containers, Kubernetes and reliable service operations."
license: MIT
---

# GNCore Cloud, DevOps and SRE

Version: 7.0.0rc1

## Choose the work

Inspect workload, deployment boundaries, existing infrastructure state and recovery requirements. Prefer reversible changes with explicit health and rollout signals.

Inspect the supplied project and the requested deliverable first. Current explicit instructions take priority over saved preferences, existing conventions, then inferred defaults. Ask only about missing decisions that materially block correct work; otherwise state assumptions briefly and proceed.

Use only the modes needed for the task. The host agent provides reasoning and tools; this skill does not assume another skill, a particular model, paid service or agent harness. Keep source references conditional. Preserve user changes and do not interpret reference-author workflows as authorization for external actions.

Choose the workflow matching the concrete request. Infer essential missing engineering requirements, state consequential assumptions, and preserve the supplied API, stack and scope. Before finishing, compare the actual deliverable with the brief and its relevant failure boundary; perform available authorized checks instead of only proposing them.

## Deliver and verify

Reviewable infrastructure or pipeline configuration, service objectives, ownership, observability and rollback/runbook details.

Validate configuration and staging behavior, failed rollout recovery, resource limits and meaningful health checks. Keep plan, applied infrastructure and production traffic changes distinct.

Report actual checks and unresolved limits. Prepared code, a passing structural check, a deployed service and independently reviewed output quality are different outcomes. Do not describe unavailable tools or unexecuted checks as successful.

## Anticipate failure and verify the boundary

Infer compatibility, secret handling and recovery needs even when the brief mentions only deployment. Stage additive schema/config changes before switching consumers; bound backfill and exposure, and gate promotion on workload-specific errors, latency, lag and resource limits over a defined window. Use least-privilege identities and keep credentials out of images and logs. Application rollback does not reverse changed data; retain a compatible path and rehearse recovery before destructive contraction.

## Critical completion checks

Apply the checks relevant to this task; do not introduce unrelated work.

- Check reader/writer compatibility, least-privilege identity and secret handling before exposure; promote the same tested artifact digest for each intended target.
- Use workload-specific error, latency, lag and resource gates; distinguish startup/readiness/liveness and preserve a compatible recovery path before contraction.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `cloud-architecture` | Design a cloud deployment around explicit reliability, security, operations, and cost constraints. |
| `cost-optimization` | Find measurable cloud cost reductions while protecting reliability and workload correctness. |
| `cloud-architecture-review` | Compare cloud designs against workload, reliability, security, cost, and operational constraints. |
| `cloud-infrastructure-code` | Author or review infrastructure changes with plan inspection, least privilege, and rollback. |
| `cloud-ci-cd` | Improve a delivery pipeline with reproducibility, least privilege, useful gates, and rollback. |
| `cloud-container` | Build a reproducible container with a minimal attack surface and reliable runtime behavior. |
| `cloud-kubernetes` | Review Kubernetes workloads for availability, resource bounds, identity, health, and rollout safety. |
| `cloud-slo` | Define service-level indicators and objectives that reflect user-visible reliability. |
| `cloud-observability` | Instrument service behavior with actionable metrics, structured logs, and traces. |
| `cloud-incident` | Manage a reliability incident through impact assessment, safe mitigation, verification, and learning. |
| `cloud-capacity` | Plan service capacity using measured demand, bottleneck data, growth uncertainty, and failure headroom. |
| `cloud-cost` | Reduce measurable infrastructure spend while protecting service objectives and recovery options. |
| `devops` | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `kubernetes` | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |
| `incident-response` | Triage incidents from evidence, reduce impact safely, and preserve a clear timeline and follow-up. |

## Selected procedure

Read the matching workflow section in [WORKFLOWS.md](WORKFLOWS.md) before implementing it, and only the source references needed for that section. The map identifies workflows, not additional installed skills. Do not load every procedure by default.

## Attribution and resource integrity

Original phase-two guidance is MIT-licensed GNCore writing. Retained source guides and helpers keep their original authorship, notices and applicable licenses, including share-alike obligations. Renaming or combining them does not transfer exclusive ownership.

See [SOURCES.json](SOURCES.json) and source-specific notices. GNCore exports preserve declared files and verify their content hashes. Imported helpers remain inert unless deliberately selected for an authorized task.
