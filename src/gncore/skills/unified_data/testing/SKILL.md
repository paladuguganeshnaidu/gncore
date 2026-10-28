---
name: testing
description: "Design and run unit, integration, end-to-end, automation, and performance tests for important software behavior."
license: Apache-2.0 AND MIT
---

# GNCore Testing

## Select the work from the user's intent

Choose the test layer that can observe the requirement with the least unnecessary setup. Use representative fixtures, clear contracts, deterministic isolation, and behavior-based assertions. Include relevant boundaries, errors, permissions, concurrency, or recovery rather than aiming for a fixed test count.

Infer a useful working mode from the requested outcome, inputs, existing assets, audience, constraints, and current project context. An explicit format, theme, stack, or workflow takes priority. If enough is known to proceed, state material assumptions briefly and do the work. Ask only about missing decisions that materially block a correct result.

Use the workflow map below as capabilities within this one skill. Combine the modes that the actual task needs; do not run every mode, change the user's scope, or load every reference by default. The host agent supplies reasoning and tools; no particular model, connector, or extra skill is assumed.

## Execute and verify

1. Inspect the relevant inputs and existing conventions; preserve originals and unrelated user changes.
2. Define the requested artifact and observable acceptance checks. Scale the plan and review depth to the actual uncertainty and risk.
3. Produce the complete result using the selected mode guidance. Keep source facts, assumptions, estimates, interpretations, and proposals distinguishable.
4. Validate the artifact and fix observed failures. Rerun relevant checks after a fix, and stop rather than repeat an unchanged failing approach indefinitely.
5. Deliver the artifact or changes with actual evidence, important decisions, and remaining limitations. Do not claim unrun checks or unperformed external actions.

## Category quality criteria

Demonstrate useful failures where appropriate, run focused regressions after fixes, and preserve failure evidence. Do not hide flaky behavior, weaken assertions, or claim checks that were not run.

Use current primary documentation for version-sensitive APIs, rules, or consequential factual claims. Use supplied sources when available. References retain their authorship and license terms; their harness-specific tools, universal activation rules, and approval scripts do not replace the current user's request or host permissions.

## Workflow map

| Workflow | Use it for |
| --- | --- |
| `unit-testing` | Write fast, deterministic unit tests around public behavior and edge cases. |
| `integration-testing` | Verify interactions between real components while isolating external services and state. |
| `end-to-end-testing` | Validate critical user journeys across the running application with stable, accessible assertions. |
| `test-automation` | Create maintainable CI test workflows with clear triggers, artifacts, and failure signals. |
| `performance-testing` | Design controlled load tests that measure latency, throughput, and saturation safely. |

## Focused procedures

### Unit Testing (`unit-testing`)

Identify the contract and boundaries of one unit. Test normal, boundary, invalid, and regression cases with clear arrange/act/assert structure. Mock only external boundaries, not the behavior under test. Keep tests deterministic and assert meaningful outputs or side effects; never loosen assertions to silence a failure.

### Integration Testing (`integration-testing`)

Choose the smallest integration path that crosses the relevant boundary. Use isolated temporary state or disposable fixtures, cover failure and cleanup behavior, and keep credentials and production endpoints out of tests. Distinguish environment failures from product failures in the report.

### End-to-End Testing (`end-to-end-testing`)

Select journeys by user impact and risk. Assert user-visible outcomes and accessibility semantics, use unique test data and deterministic setup, and clean up created state. Prefer waiting on a real condition over fixed sleeps. Report browser, environment, and skipped coverage accurately.

### Test Automation Engineering (`test-automation`)

Inspect existing CI conventions and execution limits. Run the fastest useful checks early, parallelize only independent jobs, cache only safe reproducible artifacts, and preserve failure output. Do not make a check advisory or suppress errors merely to get a green pipeline.

### Performance and Load Testing (`performance-testing`)

Define workload, concurrency, duration, target environment, and success thresholds before running. Use a staging or explicitly approved target and ramp traffic gradually. Capture percentiles, errors, resource saturation, and test conditions. Do not stress production or claim capacity from an uncontrolled run.

## Additional reviewed references

These are optional technical references for relevant tasks, not a requirement to execute their workflows or install their host plugins.

- [anthropics/skills / webapp-testing](research/anthropics-skills-webapp-testing/GUIDE.md): Apache-2.0.
- [vercel-labs/agent-browser / agent-browser](research/vercel-labs-agent-browser-agent-browser/GUIDE.md): Apache-2.0.
- [mattpocock/skills / setup-pre-commit](research/mattpocock-skills-setup-pre-commit/GUIDE.md): MIT.
- [antibrow/anti-detect-browser-skills / anti-detect-browser](research/antibrow-anti-detect-browser-skills-anti-detect-browser/GUIDE.md): MIT.
- [coreyhaines31/marketingskills / ad-creative](research/coreyhaines31-marketingskills-ad-creative/GUIDE.md): MIT.

## Attribution and use

GNCore's new category guidance is authored for this library. Retained source guides, tools, and assets remain attributed to their original authors and keep their supplied licenses. Modified or combined material subject to share-alike terms remains under those terms. This skill does not claim exclusive ownership of third-party content.

See [SOURCES.json](SOURCES.json) for source identities, snapshot hashes or revisions, and license decisions. Read only the references relevant to the current task.
