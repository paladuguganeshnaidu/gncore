# GNCore next upgrade: capability, evidence and usability

Research date: 29 October 2026. Status: proposed work, not implemented or published by this plan. The tested 7.0.0rc1 candidate is recorded at a910935; these planning documents do not replace its accepted artifacts.

## Product direction

Make GNCore a portable engineering guide that selects a suitable workflow, notices important omissions in a brief, and helps the host agent produce verifiable results. Measure success by correct completed work, recovery behavior and user effort. More skill files, more instruction text or more dependencies are not success metrics.

GNCore remains a skill library and CLI. A hosted dashboard, agent execution service or IDE extension would be a separate optional product layer with its own requirements and evaluation. Do not imply the current package already executes an autonomous application.

## What already distinguishes this implementation

These are verified features of GNCore, not claims that no competitor offers them.

| Feature | Current evidence | Benefit | Limit |
| --- | --- | --- | --- |
| One category invocation with focused workflows | 30 entrypoints and 374 preserved workflows | Users describe an outcome without knowing every specialist skill name | Host must discover/load the skill; invocation alone does not prove compliance |
| Visual direction inferred from a brief | Frontend modes and direction-selection guidance | A user can request a credible technical site without naming a theme | Aesthetic quality is not established by keyword checks or the small UI pilot |
| Broad developer coverage | Web, Python, ML, neural networks, systems, embedded, delivery and research categories | Consistent entry format across different engineering tasks | Breadth is not evidence of equal depth in all 30 categories |
| Portable offline exports | CLI, wheel/sdist and complete skill ZIP verification | Usable without a mandatory model account or hosted registry | Host tools and project frameworks remain separate |
| No required runtime dependencies | pyproject.toml declares dependencies=[] | Small core integration surface | Optional tooling still has its own dependencies |
| Managed installation and recovery | Digest preflight, staging, journals, backups and customization preservation tests | Helps avoid overwriting customized skills | Windows synced-folder journal failure remains unresolved in one full run |
| Traceable source obligations | Resource hashes and source-specific notices retained | Reviewable provenance and redistribution terms | Combining or renaming material does not transfer exclusive ownership |
| Evidence alongside claims | 300 answers in 10 full IDE runs,6 adaptive answers, saved failures and plots | A reviewer can inspect the basis for a result | One unblinded evaluator, no repeated-trial/no-skill estimate |
| Original domain failure guidance | Additions to all 30 entrypoints, preserving existing procedures | Encourages recovery, contracts and validation even in short briefs | Written guidance must still be tested in actual outputs |

## Priority order and acceptance evidence

Acceptance targets below are proposals to declare before running new tests. A failed target blocks the corresponding claim; it does not authorize changing scores or deleting unfavorable cases.

| Priority | Upgrade | Why this comes next | Concrete acceptance evidence |
| --- | --- | --- | --- |
| P0 | Reproducible evaluation runner | Current batch conversations and manual copying confound comparisons | One independent task per fresh session; exact source/prompt/model/config identities; before/reference/revised/no-added-skill arms; preserved raw outputs; deterministic grading where possible; blinded review for subjective criteria |
| P0 | Close the Windows journal issue | Bounded retries did not eliminate a real sync-folder failure | Reproduce with a controlled file-lock fixture; distinguish ACL denial, sharing lock and sync interaction; prove bounded stop and usable prior journal; verify ordinary installs and interrupted recovery on Windows and other supported OSes |
| P0 | Restore measured UI coverage | Held-out and final pages still lack rendering evidence | Actual Chromium/Firefox/WebKit journeys where available;390px and wide layouts; keyboard focus, invalid input, confirmation and overflow checks; automated accessibility findings plus manual keyboard checks; unavailable environments remain unmeasured |
| P1 | Better category/workflow routing | Prior normal router corpus result is 18/30 | Expand to novel paraphrases, mixed tasks, exclusions and unsupported requests; publish top-1 accuracy, ambiguity/abstention precision and failures separately. Proposed goal:>=90% on a frozen held-out routing set, without forcing a category for unsupported work |
| P1 | Task contracts and omission handling | Some answers omit throughput, lifecycle cleanup, migration recovery or model provenance | A brief produces a small task-specific contract: output, constraints, critical failure modes and checks. It infers necessary engineering work, preserves explicit choices and asks only about consequential blockers. Verify on deliberately underspecified briefs |
| P1 | Real project acceptance tasks | Small pure functions cannot establish full application quality | Six initial projects cover frontend/backend, package, security repair, data pipeline, ML and native/lifecycle boundaries. Verify builds, runtime behavior, failure recovery and user-visible outcomes rather than only proposed plans |
| P1 | Selective reference loading | Huge merged instructions can obscure relevant rules | Keep a concise entrypoint and task-relevant references; compare against full-pack loading on identical tasks. Report useful task completion, context size and actually observed cost/time; preserve the no-extra-service core |
| P2 | Security and test-strength profiles | Seeded recall and repair correctness are different | Measure correct fixes, missed defects and safe-control false positives; property-based tests and deliberate mutants; static/dependency/secret scans appropriate to the project. No scanner result becomes an application-wide security certificate |
| P2 | Reproducible ML/NN tracks | Need leakage, checkpoint and numerical checks beyond prose | CPU baselines, dataset/split identity, training-only preprocessing, gradient/stability fixtures, resume comparison and model-serving parity. GPU results only when hardware tests actually execute |
| P2 | IDE compatibility evidence | Export success does not prove an agent read the skill | Fresh test workspaces, documented install path and discovery settings; observable evidence that the skill was loaded where exposed; identical requests across VS Code/Antigravity/other selected hosts. Account permissions handled by owner, never bypassed |
| P3 | Evidence dashboard and release provenance | CEOs need clarity; developers need reproducibility | Filter by category, host, task, source revision and metric; show numerator/denominator, coverage, failures and uncertainty. Pin exact accepted artifacts; prevent draft results from appearing as published availability |

## Suggested architecture

1. **Core catalog:** concise entrypoint, workflow map, declared resources, source/license manifests; keep portable exports and the current lightweight core.
2. **Task selection:** deterministic local signals first, explicit user choices first; optional semantic reranking only if it improves a frozen evaluation. Report ambiguous or unsupported requests honestly.
3. **Task contract:** host-readable requirements, inferred essential checks and explicit scope. A UI brief may need keyboard focus; it does not automatically need a database or payment service.
4. **Optional tool profiles:** web, API, Python, security, data/ML and native. Detect project compatibility, propose only relevant checks and retain host permissions. No automatic installation or execution of imported helpers.
5. **Evidence runner:** adapters for supported hosts/providers, isolated execution suitable for the code, reproducible fixtures and structured results. A Python AST allowlist is not a general sandbox.
6. **Reporting:** a common result schema with observed/proposed/unavailable states, raw evidence links and separate metrics for correctness, security, UI, resource use and cost.

Keep the single user-facing skill invocation while using progressive reference loading internally. Merging every guide into one enormous prompt should be an experimental comparison, not the default quality strategy.

## Measurement plan

- Compare GNCore before, published task-relevant reference, revised GNCore and no-added-skill on the **same tasks**, within each model/host block.
- Pin model versions where possible; otherwise record the uncertainty. Randomize run order and repeat independent tasks. Do not pool hosts into an intrinsic skill rating.
- Use development examples to improve guidance and keep a separate sealed evaluation set. Once a failure informs a change, its rerun is adaptive regression evidence, not unseen evaluation.
- Start with six representative categories and five distinct task briefs each. Three repeats, four conditions and two hosts imply 720 task responses. A 30-category expansion at the same design implies 3600. These are planning counts, not completed runs or guarantees of statistical power. Confirm provider budget and variance before scaling.
- Record actual latency and tokens only when observable; define concurrency, warm/cold state, caching and timeout treatment. Report cost per successfully accepted task as well as quality; unknown billing stays unavailable.
- Use code/API/browser assertions before model judges. Calibrate any judge against a blinded human subset; track disagreement. Repeated runs of one task do not replace task diversity.
- Give all categories minimum task coverage; do not hide a weak category behind a global average. Publish uncertainty at the independent task level using a justified paired/clustered analysis.
- Keep the 95% line as an ambition. Define severity-based release gates and report what passed. No universal score represents security, beauty, reliability and ML accuracy together.

## Optional instrumentation shortlist

Proposed first: [Promptfoo](https://github.com/promptfoo/promptfoo) for provider-neutral evaluation orchestration; [pytest](https://github.com/pytest-dev/pytest) and [Hypothesis](https://github.com/HypothesisWorks/hypothesis) for independent assertions; [Playwright](https://github.com/microsoft/playwright), [axe-core](https://github.com/dequelabs/axe-core) and [Lighthouse](https://github.com/GoogleChrome/lighthouse) for browser behavior, accessibility findings and performance audits.

Then evaluate [Schemathesis](https://github.com/schemathesis/schemathesis) and [Testcontainers](https://github.com/testcontainers/testcontainers-python) for API/database fixtures; [mutmut](https://github.com/boxed/mutmut) for test strength; [Semgrep](https://github.com/semgrep/semgrep), [CodeQL](https://github.com/github/codeql), [Trivy](https://github.com/aquasecurity/trivy) and [Gitleaks](https://github.com/gitleaks/gitleaks) for complementary security checks. Licensing, platform and project suitability must be checked before adoption.

Choose at most one primary trace/evaluation store initially: [Langfuse](https://github.com/langfuse/langfuse) for an LLM-oriented workflow or [MLflow](https://github.com/mlflow/mlflow) when ML experiment/artifact tracking is central. [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-python) can provide interoperable instrumentation. Hosted telemetry is opt-in, with payload redaction and explicit retention; local JSON evidence remains supported.

Do not install every tool in the inventory. These are candidates for particular jobs, not mandatory GNCore runtime dependencies. See [the full inventory](TOOLS_AND_LIBRARY_INVENTORY.md).

## Reference libraries to compare fairly

The existing pilot already mapped all 30 categories to 14 pinned source repositories. That complete category/source/revision list is in [source-snapshots.json](../web-results/comparison/source-snapshots.json).

For future comparisons, preserve their actual scope: [Anthropic skills](https://github.com/anthropics/skills), [Vercel skills](https://github.com/vercel-labs/agent-skills), [Microsoft skills](https://github.com/microsoft/skills), [Hugging Face skills](https://github.com/huggingface/skills), [Trail of Bits skills](https://github.com/trailofbits/skills) and [Superpowers](https://github.com/obra/superpowers) are relevant comparison sources. A narrower reference should not be penalized for a capability it never claims. Match tasks, setup, support files and execution opportunities before making a competitive statement.

## Release sequence

Keep this upgrade separate from the accepted 7.0.0rc1 release artifacts. First close P0 gaps and establish the evaluation schema; then route/contract improvements; then project acceptance tracks and optional instrumentation; finally refresh the dashboard and release evidence. Choose the next version after scope is implemented, not before.

No new dependencies were installed, no hosted benchmark calls were run, and no GitHub/PyPI/website publication was performed for this planning request. Existing reports remain the authoritative record of completed measurements.
