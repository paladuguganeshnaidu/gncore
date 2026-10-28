---
name: devops
description: "Improve delivery workflows and Kubernetes operations with reproducible configuration, observability, and recovery."
license: Apache-2.0 AND MIT
---

# GNCore Devops

## Select the work from the user's intent

Inspect pipelines, environment boundaries, container definitions, cluster resources, secrets handling, and rollout practices. Prefer a scoped improvement that reduces an observed failure or feedback delay. Make readiness, resource, dependency, and rollback assumptions explicit.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Validate manifests and the relevant build or staging path. Check configuration drift, failure signals, rollout and rollback behavior, and secret exposure.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `devops` | Improve build and delivery workflows with reproducible steps, safe rollout, and actionable failure signals. |
| `kubernetes` | Author Kubernetes resources with least privilege, clear health behavior, and safe rollout settings. |

## Focused procedures

### DevOps Engineering (`devops`)

Inspect the current pipeline, environments, secrets, and rollback process. Make steps deterministic, least-privileged, and observable; cache only safe artifacts. Validate configuration and test a non-production path first. Do not deploy, rotate secrets, destroy resources, or change production workflows without explicit authorization. Report required credentials as names only, never values.

### Kubernetes Engineering (`kubernetes`)

Inspect cluster version, namespace, chart conventions, workload needs, and security policies. Set resource requests/limits, probes that reflect readiness, least-privilege service accounts, and safe rollout/rollback behavior. Keep secrets out of manifests. Validate manifests locally; do not apply to a live cluster or expose services publicly without explicit authorization.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [github/awesome-copilot / azure-devops-cli](research/github-awesome-copilot-azure-devops-cli/GUIDE.md): MIT.
- [jeffallan/claude-skills / devops-engineer](research/jeffallan-claude-skills-devops-engineer/GUIDE.md): MIT.
- [github/awesome-copilot / devops-rollout-plan](research/github-awesome-copilot-devops-rollout-plan/GUIDE.md): MIT.
- [forcedotcom/sf-skills / dx-devops-test-failures-analyze](research/forcedotcom-sf-skills-dx-devops-test-failures-analyze/GUIDE.md): Apache-2.0.
- [aws/agent-toolkit-for-aws / chatting-with-aws-devops-agent](research/aws-agent-toolkit-for-aws-chatting-with-aws-devops-agent/GUIDE.md): Apache-2.0.
- [aws/agent-toolkit-for-aws / setup-devops-agent](research/aws-agent-toolkit-for-aws-setup-devops-agent/GUIDE.md): Apache-2.0.
- [aws/agent-toolkit-for-aws / investigating-incidents-with-aws-devops-agent](research/aws-agent-toolkit-for-aws-investigating-incidents-with-aws-devops-agent/GUIDE.md): Apache-2.0.
- [aws/agent-toolkit-for-aws / coordinating-multi-space-devops-agent](research/aws-agent-toolkit-for-aws-coordinating-multi-space-devops-agent/GUIDE.md): Apache-2.0.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
