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
| Antigravity reasoning trials | Neural passed; frontend passed with caveats; backend needs revision |
| Copilot agent execution | Blocked by sign-in/model setup; no output claimed |

The full-suite skip requires Windows symlink creation unavailable to this account. A later website/release test attempt hit the sandbox's default temporary-directory permission error. Its failed log is retained; the rerun using a workspace-local temporary directory passed both tests. This was an environment setup failure, not a silently removed check.

## Measurements across all 30 categories

The raw benchmark contains 1,950 timed samples: 30 rendering and 30 explicit-routing samples per category, plus five reads of each category's complete declared resource set. One excluded warm-up precedes each operation. Local timings include no model inference, IDE task execution or remote service latency. Filesystem caches and background activity were not controlled. Read [the methodology](README.md) before comparing timings.

The 90 authored prompts produced 37 category suggestions and 53 `needs-context` results. Of the 30 normal prompts, 18 selected the intended category, ten were unresolved and two selected a different category. Across all 90 prompts, 34 matched their scenario category. Underspecified and boundary cases do not have a universal selection oracle, so those labels are observations rather than pass/fail quality scores.

This exposes limited recall in the deterministic English keyword router. It is suitable as an explainable hint with explicit category override; the measurements do not justify claiming reliable natural-language task routing or successful agent task completion. These same authored cases are not a held-out evaluation set. Full artifact generation and human rubric review remain pending.

The seeded CPU XOR probe passed: loss fell from approximately 0.8306874 to 0.0012142 after 2,500 steps; maximum relative finite-difference gradient error was approximately 1.69e-8. This validates a tiny numerical fixture, not production model training.

## IDE evidence and remaining checks

VS Code's native Skills panel reports **Workspace: 30** and shows GNCore skill paths with a Loaded state. Its editor recognizes the installed file as a Skill and offers it as chat context. Copilot still requests sign-in or a configured model, so no Copilot model task was submitted. The unrelated user customization migration notice was left unchanged.

Antigravity's launcher and editor are separate applications; the editor was opened and the GNCore skill content observed. The user handled workspace trust and helped focus the message field after automation difficulties. The selected model label was Gemini 3.8 Flash High. Three reasoning cases then completed in one conversation; frontend and backend were combined in the second message. Native discovery of all categories remains unverified because the trials explicitly referenced the installed skill files.

The [neural answer](ide-evidence/antigravity-neural-response.md) met its five scoped reasoning criteria: shapes, binary loss semantics, central finite differences, valid workflow IDs and honest runtime boundaries. Its proposed strict relative gradient tolerance still needs scale-aware numerical validation in a real implementation. The [review](ide-evidence/antigravity-neural-review.json) records that caveat.

The [frontend/backend answer](ide-evidence/antigravity-web-response.md) selected organic minimalism from the clinic brief and gave concrete keyboard and small-screen proposals. All eight cited workflow IDs exist. This is a design proposal; its claims of analytical validation do not establish a tested DOM, focus order or rendered touch geometry.

The backend answer **needs revision**. Its single-transaction claim protocol does not justify an unconditional immediate `409` for every concurrent duplicate; the competing insert can wait and then observe a completed result. It also sets `FAILED` before rolling back the same transaction, so that state would not be durable. This is a review of the proposed protocol against PostgreSQL's [Read Committed semantics](https://www.postgresql.org/docs/18/transaction-iso.html#XACT-READ-COMMITTED) and [rollback behavior](https://www.postgresql.org/docs/18/sql-rollback.html), rather than a PostgreSQL concurrency execution result. A [tiny SQLite transaction probe](ide-evidence/idempotency-rollback-probe.json) separately demonstrates the rollback issue, without claiming to reproduce PostgreSQL locking. The [detailed review](ide-evidence/antigravity-web-review.json) describes a consistent revision and needed tests.

Exact IDE observations are in [ide-results.json](ide-results.json). The [reasoning cases](ide-cases.json) contain the prompts, rubrics and execution status. These are three manual, unblinded reasoning reviews; they do not replace the 90 complete artifact-generation scenarios or constitute a general agent quality score. Sanitized accessibility records and correctly targeted screenshots are in [ide-evidence](ide-evidence). One preserved snapshot is explicitly marked stale: the accessibility bridge said Working after the completed answer was already visible. The actual answers were captured through the observed Copy response controls. Machine-local file links in the copied answers were normalized to repository-relative source links; prose and mathematics were retained.

## Reusable outputs

- [All-category coverage chart](charts/category-coverage.png) and [SVG](charts/category-coverage.svg).
- [All-category latency chart](charts/local-latency.png) and [SVG](charts/local-latency.svg).
- [All-category routing observations](charts/category-routing.png) and [SVG](charts/category-routing.svg).
- [Routing and neural mechanics chart](charts/routing-and-neural-probe.png) and [SVG](charts/routing-and-neural-probe.svg).
- [Every raw sample and scenario outcome](benchmarks.json), [CSV](categories.csv), [logs](logs), [package comparison](package-verification.json), [catalog audit](catalog-audit.json) and [website graph check](website-check.json).

Publication to GitHub, PyPI and gncore.pages.dev remains pending the owner's approval and the remote CI checks described in the release plan.
