# GNCore 7.0.0rc1 local test results

Recorded on 29 October 2026, Asia/Calcutta. Both VS Code and Antigravity IDE were launched with this GNCore workspace. The candidate remains unpublished.

| Check | Observed result |
| --- | --- |
| Active category integrity | 30/30 entrypoint hashes, resource hashes and exported entrypoints match |
| Catalog | 374 workflows; all 553 prior workflow IDs accounted for |
| Support resources | 1,630 files compared across source, clean wheel, export ZIP and actual project installation |
| Attribution preservation | 1,569 original reference files unchanged byte-for-byte |
| Project installation | 30 skills, 1,660 tracked files; inventory verification passes |
| Full tests, Windows Python 3.10.20 | 134 passed, 1 skipped |
| Full tests, Windows Python 3.12.13 | 134 passed, 1 skipped |
| Full tests, Windows Python 3.14 | 134 passed, 1 skipped |
| Supporting helper syntax | 73 Python helpers parsed; not all helper dependencies executed |
| Native skill format | 30 source and 30 installed entrypoints valid |
| Website graph | 41 HTML pages, 1,796 local references, 672 redirects; no checker issues |
| VS Code 1.143.1 | GNCore opens; native Skills panel reports 30 workspace skills; installed neural-network file reads correctly |
| Antigravity IDE 2.5.5 | GNCore opens; installed neural-network file reads correctly; user handled trust prompts |
| Agent execution in IDEs | Blocked; no agent-generated task outcome claimed |

The full-suite skip requires Windows symlink creation unavailable to this account. A later website/release test attempt hit the sandbox's default temporary-directory permission error. Its failed log is retained; the rerun using a workspace-local temporary directory passed both tests. This was an environment setup failure, not a silently removed check.

## Measurements across all 30 categories

The raw benchmark contains 1,950 timed samples: 30 rendering and 30 explicit-routing samples per category, plus five reads of each category's complete declared resource set. One excluded warm-up precedes each operation. Local timings include no model inference, IDE task execution or remote service latency. Filesystem caches and background activity were not controlled. Read [the methodology](README.md) before comparing timings.

The 90 authored prompts produced 37 category suggestions and 53 `needs-context` results. Of the 30 normal prompts, 18 selected the intended category, ten were unresolved and two selected a different category. Across all 90 prompts, 34 matched their scenario category. Underspecified and boundary cases do not have a universal selection oracle, so those labels are observations rather than pass/fail quality scores.

This exposes limited recall in the deterministic English keyword router. It is suitable as an explainable hint with explicit category override; the measurements do not justify claiming reliable natural-language task routing or successful agent task completion. These same authored cases are not a held-out evaluation set. Full artifact generation and human rubric review remain pending.

The seeded CPU XOR probe passed: loss fell from approximately 0.8306874 to 0.0012142 after 2,500 steps; maximum relative finite-difference gradient error was approximately 1.69e-8. This validates a tiny numerical fixture, not production model training.

## IDE evidence and remaining checks

VS Code's native Skills panel reports **Workspace: 30** and shows GNCore skill paths with a Loaded state. Its editor recognizes the installed file as a Skill and offers it as chat context. Copilot still requests sign-in or a configured model, so no model task was submitted. The unrelated user customization migration notice was left unchanged.

Antigravity's launcher and editor are separate applications; the editor was opened and the GNCore skill content observed. After the user handled workspace trust, its message input did not acquire a verifiable editable focus through the available automation. `set_value` left it empty; observed clicks and the agent-focus shortcut did not establish focus. No test prompt was submitted. Native discovery of all categories and agent execution are unverified in this IDE.

Exact IDE observations are in [ide-results.json](ide-results.json). [Prepared reasoning cases](ide-cases.json) contain prompts and rubrics for a future available agent session; they are explicitly unexecuted. Sanitized accessibility records and correctly targeted screenshots are in [ide-evidence](ide-evidence).

## Reusable outputs

- [All-category coverage chart](charts/category-coverage.png) and [SVG](charts/category-coverage.svg).
- [All-category latency chart](charts/local-latency.png) and [SVG](charts/local-latency.svg).
- [All-category routing observations](charts/category-routing.png) and [SVG](charts/category-routing.svg).
- [Routing and neural mechanics chart](charts/routing-and-neural-probe.png) and [SVG](charts/routing-and-neural-probe.svg).
- [Every raw sample and scenario outcome](benchmarks.json), [CSV](categories.csv), [logs](logs), [package comparison](package-verification.json), [catalog audit](catalog-audit.json) and [website graph check](website-check.json).

Publication to GitHub, PyPI and gncore.pages.dev remains pending the owner's approval and the remote CI checks described in the release plan.
