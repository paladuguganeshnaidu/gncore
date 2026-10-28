---
name: software-engineering
description: "Design, implement, debug, review, refactor, migrate, and release scoped software changes."
license: MIT
---

# GNCore Software Engineering

## Select the work from the user's intent

Inspect the repository, relevant call paths, invariants, public contracts, and current tests. Choose architecture, feature work, review, debugging, refactoring, dependency, performance, migration, or release work based on the concrete task. Preserve unrelated changes and the chosen stack.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Verify observable behavior with relevant tests, type/build checks, or reproduction steps. Cover boundary, error, and permission cases that matter to the change.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `software-feature` | Deliver a scoped software feature using local conventions and verifiable acceptance criteria. |
| `software-architecture` | Compare architecture options against constraints, operations, reversibility, and lifecycle cost. |
| `software-code-review` | Review a code change for correctness, security, maintainability, and missing regression coverage. |
| `software-debugging` | Diagnose a software failure from reproducible evidence and verify the smallest safe fix. |
| `software-refactor` | Refactor a bounded code area while preserving its documented behavior and public contracts. |
| `software-api-contract` | Define and verify an API contract across request, response, errors, versioning, and consumers. |
| `software-dependency` | Assess and implement a dependency change with compatibility, security, and rollback evidence. |
| `software-performance` | Find a measured software bottleneck and optimize it without regressing correctness. |
| `software-migration` | Plan a staged migration with compatibility gates, data safety, and rollback criteria. |
| `software-release` | Prepare a software release with reproducible artifacts, verified changes, and rollback readiness. |

## Focused procedures

### Software Feature Delivery (`software-feature`)

Trace the feature through interfaces and data flow, define observable behavior, make the smallest coherent change, add boundary tests, and run targeted regressions. Preserve unrelated user work and report exact checks.

### Software Architecture Decision (`software-architecture`)

Capture context, quality attributes, constraints, alternatives, trade-offs, failure modes, and a decision owner. Prefer incremental reversible choices and validate assumptions with a small implementation where useful.

### Software Code Review (`software-code-review`)

Inspect the full diff and relevant callers, identify concrete reproducible findings with severity and file locations, and separate defects from preferences. Confirm fixes with targeted regression checks.

### Software Debugging (`software-debugging`)

Reproduce or isolate the failing condition, inspect logs and state, form testable hypotheses, and narrow the cause before editing. Add a regression test, fix the root cause, and rerun the failure and impacted checks.

### Safe Refactoring (`software-refactor`)

Capture behavior with tests or characterization, identify callers, make small mechanical steps, and run tests after each risky step. Avoid unrelated redesign and compare externally observable behavior before and after.

### Software API Contract (`software-api-contract`)

Inspect actual consumers, validate schemas and authorization boundaries, specify error semantics and compatibility, and test contract fixtures. Flag breaking behavior and provide a migration path.

### Dependency Change Review (`software-dependency`)

Check supported versions, changelog, transitive effects, license policy, lockfile behavior, and known vulnerabilities. Change only needed packages, run affected tests, and record rollback and compatibility results.

### Software Performance Optimization (`software-performance`)

Establish repeatable workload and baseline, profile the critical path, estimate impact and resource trade-offs, then change one bottleneck. Rerun correctness tests and comparable benchmarks; report uncertainty.

### Software Migration Plan (`software-migration`)

Inventory dependencies and consumers, define target and interim states, map changes and data movement, and stage by reversible boundaries. Test backward compatibility and rollback before production cutover.

### Software Release Candidate (`software-release`)

Check version, diff, changelog, build provenance, tests, dependency locks, supported platforms, migrations, and known issues. Separate passed, skipped, and blocked gates; do not publish without authorization.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [amirtaherkhani/nestjs-skills / nestjs-professional-software-engineering](research/amirtaherkhani-nestjs-skills-nestjs-professional-software-engineering/GUIDE.md): MIT.
- [emilkowalski/skills / emil-design-eng](research/emilkowalski-skills-emil-design-eng/GUIDE.md): MIT.
- [paramchoudhary/resumeskills / tech-resume-optimizer](research/paramchoudhary-resumeskills-tech-resume-optimizer/GUIDE.md): MIT.
- [wshobson/agents / anti-reversing-techniques](research/wshobson-agents-anti-reversing-techniques/GUIDE.md): MIT.
- [samber/developer-relations-skills / tech-employer-branding](research/samber-developer-relations-skills-tech-employer-branding/GUIDE.md): MIT.
- [softaworks/agent-toolkit / codex](research/softaworks-agent-toolkit-codex/GUIDE.md): MIT.
- [everyinc/compound-engineering-plugin / ce-plan](research/everyinc-compound-engineering-plugin-ce-plan/GUIDE.md): MIT.
- [everyinc/compound-engineering-plugin / lfg](research/everyinc-compound-engineering-plugin-lfg/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
