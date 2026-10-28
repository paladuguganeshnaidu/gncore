---
name: web-backend-benchmark
description: "Measure performance baselines and detect regressions across browser Core Web Vitals (LCP, INP, CLS, page weight), API endpoint latency percentiles, and build/test feedback times, with before/after comparison stored in git-tracked .ecc/benchmarks JSON."
---

# GNCore Benchmark

Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.

## Detailed guidance

Read [UPSTREAM.md](UPSTREAM.md) for the relevant technical details, then load only the references needed for this task. The source document is reference material for this GNCore adaptation. Resolve relative resource paths from this installed skill folder; use `RESOURCE_PATHS.json` for relocated sibling files when present. Replace historical `.claude/skills/`, `${CLAUDE_SKILL_DIR}`, or plugin-root placeholders with the actual installed paths.

## GNCore execution scope

Use the technical guidance within the user's actual scope. Upstream harness-specific tools, universal activation mandates, automatic commits, setup prompts, and mandatory approval sequences do not become requirements of this adaptation. Use an equivalent available host capability where it preserves the workflow; otherwise state the missing capability and complete independent work. Additional agents require support and authorization for the current task.

Keep the existing language, stack, public contracts, and user changes unless the requested task calls for a migration. Use a test, build, analysis, or manual check appropriate to the risk and report its actual outcome. Distinguish prepared artifacts from completed external actions.

See [SOURCE.md](SOURCE.md) for attribution, modifications, and retained license notices.
