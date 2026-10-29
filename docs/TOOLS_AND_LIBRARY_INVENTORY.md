# GNCore tools, libraries and comparison sources

Checked 29 October 2026 using the project's actual metadata/evidence and upstream project pages. This is a curated inventory of established projects relevant to GNCore, not an exhaustive Internet list, a popularity leaderboard or a claim that each item is best. No star-count or adoption ranking was calculated.

**Used** means present in the recorded GNCore build/test/report workflow. **Proposed** means researched for a future optional integration, not installed or benchmarked in GNCore by this research. **Project choice** means a framework/library the skill may guide when it fits the user's project; it is not a dependency GNCore needs to run. Upstream capability descriptions are not GNCore performance results. Check selected versions, licenses and OS compatibility before adopting.

## Already used in GNCore's preparation

| Tool/library | Actual role | Status |
| --- | --- | --- |
| Python standard library | CLI/catalog, hashing, export archives, transaction journals and fixtures | Used; core runtime dependencies=[] |
| [pytest](https://github.com/pytest-dev/pytest) | Package regression suite and comparison-harness tests | Used; latest full Python 3.12 suite 148 passed,1 Windows symlink skip |
| [PyYAML](https://github.com/yaml/pyyaml) | Optional skill-format tooling | Declared optional dependency; not required for core runtime |
| [uv](https://github.com/astral-sh/uv) | Isolated environment dependency installation and artifact builds | Used during preparation |
| [Hatch/Hatchling](https://github.com/pypa/hatch) | Declared package build backend | Used for wheel/sdist builds |
| [Twine](https://github.com/pypa/twine) | Package metadata validation | Used; accepted wheel and sdist passed |
| [NumPy](https://numpy.org/) | Plot data arrays | Used in report generation |
| [Matplotlib](https://matplotlib.org/) | Four landscape sheets, each with six metric panels and a 30-category heatmap | Used; PNG/SVG/PDF outputs saved |
| [ReportLab](https://www.reportlab.com/) | Plain-language and technical PDF reports | Used |
| [PyMuPDF](https://pymupdf.readthedocs.io/) | Render PDF pages for visual inspection | Used |
| Git | Source history, candidate preservation and local website commits | Used; local commits are not publication |
| GitHub Actions | Configured cross-platform Python matrix and release workflow | Configured; hosted CI on the latest accepted commit has not been claimed as run |
| Original VS Code/Copilot | Saved synthetic development/holdout/follow-up answers | Used; Auto model selection is not a fixed model guarantee |
| Antigravity IDE | Separate saved synthetic answer block | Used; not pooled with VS Code as one model |
| In-app browser | Four actual development UI journeys | Used; remaining held-out and follow-up rendering unavailable |

## Evaluation, routing and observability candidates

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Prompt/agent evaluation and adversarial evaluation workflows | Proposed first orchestration option; provider costs and credentials remain separate |
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM application evaluation framework | Proposed alternative/complement where its metrics fit; do not duplicate every evaluation platform |
| [Ragas](https://github.com/vibrantlabsai/ragas) | LLM application evaluation | Proposed focused retrieval/grounding evaluation; not a substitute for executable coding checks |
| [Langfuse](https://github.com/langfuse/langfuse) | LLM traces and evaluation workflows | Proposed optional trace store; redact payloads and keep local export |
| [OpenTelemetry Python](https://github.com/open-telemetry/opentelemetry-python) | Telemetry API/SDK | Proposed interoperable traces and service metrics |
| [Sentence Transformers](https://github.com/huggingface/sentence-transformers) | Embeddings, retrieval and reranking | Proposed experiment for optional semantic category/reference selection, compared with lightweight lexical routing |
| [pgvector](https://github.com/pgvector/pgvector) | Vector similarity search in PostgreSQL | Optional hosted catalog/search extension only if scale warrants it; unnecessary for the current local 30-category router |

## Testing and code-quality candidates

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [Hypothesis](https://github.com/HypothesisWorks/hypothesis) | Property-based testing | Proposed exact-total, sorting, parser, numeric and recovery-boundary counterexamples |
| [mutmut](https://github.com/boxed/mutmut) | Mutation testing | Proposed test-strength checks, with equivalent mutants and valid baseline behavior reviewed |
| [Schemathesis](https://github.com/schemathesis/schemathesis) | Schema-driven API testing | Proposed backend contract fixtures |
| [Testcontainers Python](https://github.com/testcontainers/testcontainers-python) | Container-backed test environments | Proposed real PostgreSQL/service integration tests; requires compatible container runtime |
| [Ruff](https://github.com/astral-sh/ruff) | Python linting and formatting | Proposed focused checks on authored code; do not silently reformat retained third-party resources |
| [ty](https://github.com/astral-sh/ty) | Python type checking | Proposed compatibility trial before selecting it as a required check; type results are not runtime correctness |

## Frontend and design candidates

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [Playwright](https://github.com/microsoft/playwright) | Chromium/Firefox/WebKit web testing | Proposed repeatable frontend test profile; current in-app checks are a distinct recorded environment |
| [axe-core](https://github.com/dequelabs/axe-core) | Automated accessibility checks | Proposed alongside manual keyboard/focus checks; automatic checks cannot prove complete accessibility |
| [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Web audits and performance measurements | Proposed repeatable workload/device configuration; its score is not a visual-design score |
| [Storybook](https://github.com/storybookjs/storybook) | Component development/documentation/testing in isolation | Project choice and proposed component-state fixtures |
| [React](https://github.com/react/react) | Web/native interface library | Project choice; preserve an existing stack |
| [Next.js](https://github.com/vercel/next.js) | React application framework | Project choice when routing/rendering/server needs justify it |
| [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | Utility-first CSS | Project choice; not a requirement for good visual design |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | Customizable component source | Project choice; reused components still need project-specific validation |
| [Radix Primitives](https://github.com/radix-ui/primitives) | Accessible UI primitives | Project choice; integration can still introduce focus/label defects |

## Security and provenance candidates

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [Semgrep](https://github.com/semgrep/semgrep) | Static analysis and pattern rules | Proposed on suitable languages and authored/generated projects |
| [CodeQL](https://github.com/github/codeql) | Code analysis queries/libraries | Proposed deeper supported-language analysis; check CLI/license/CI eligibility separately |
| [Trivy](https://github.com/aquasecurity/trivy) | Vulnerability, configuration, secret and artifact scanning | Proposed container/dependency/configuration profile |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Secret detection | Proposed source/evidence leak checks; synthetic test values require reviewed handling |
| [Sigstore Python](https://github.com/sigstore/sigstore-python) | Python artifact signing/verification | Proposed provenance layer after CI/identity design; no artifact signing claimed today |

## Backend, data and performance project choices

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [FastAPI](https://github.com/fastapi/fastapi) | Python API framework | Project choice and API acceptance-track candidate |
| [Django](https://github.com/django/django) | Python web framework | Project choice when its integrated application facilities fit |
| [NestJS](https://github.com/nestjs/nest) | TypeScript/JavaScript server framework | Project choice for an existing or justified Node stack |
| [Pydantic](https://github.com/pydantic/pydantic) | Typed data validation | Project choice for API/result contracts; proposed evidence-schema experiment |
| [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) | Python database toolkit | Project choice; transaction correctness requires real storage tests |
| [Alembic](https://github.com/sqlalchemy/alembic) | SQLAlchemy migration tooling | Project choice; online migration/recovery still needs engine-aware planning |
| [Polars](https://github.com/pola-rs/polars) | DataFrame query engine | Project choice for schema/revision/reconciliation acceptance tasks |
| [DuckDB](https://github.com/duckdb/duckdb) | Analytical database | Project choice for local reproducible analytics |
| [Pandera](https://github.com/unionai-oss/pandera) | Statistical/tabular data validation | Proposed data-contract checks where the selected backend is supported |
| [Temporal Python SDK](https://github.com/temporalio/sdk-python) | Durable workflow SDK | Project choice for durable workflow acceptance tasks, not a mandatory service for every automation |
| [k6](https://github.com/grafana/k6) | Load testing | Proposed matched throughput/latency/error/memory-adjacent acceptance runs; memory needs separate instrumentation |

## ML, neural-network and deployment choices

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | Classical ML tools | Project choice for leakage-safe CPU baseline tasks |
| [PyTorch](https://github.com/pytorch/pytorch) | Tensor/neural-network framework | Project choice for gradient, numerical stability and checkpoint-resume tasks |
| [Transformers](https://github.com/huggingface/transformers) | Model definitions and training/inference tooling | Project choice for NLP/vision/multimodal tasks; model/data terms remain separate |
| [MLflow](https://github.com/mlflow/mlflow) | AI/ML experiment, evaluation and model workflows | Proposed experiment/artifact tracking option; choose intentionally against Langfuse overlap |
| [Optuna](https://github.com/optuna/optuna) | Hyperparameter optimization | Project choice with fixed validation protocol and bounded budget |
| [DVC](https://github.com/treeverse/dvc) | Data versioning and ML experiments | Proposed dataset/artifact lineage option; no hosted storage requirement implied |

## Mobile, games and native/embedded choices

| Project | What it supplies | GNCore use and status |
| --- | --- | --- |
| [React Native](https://github.com/react/react-native) | Native application framework | Project choice for lifecycle/offline/list acceptance tasks; desktop reasoning is not device testing |
| [Godot](https://github.com/godotengine/godot) | 2D/3D game engine | Project choice for deterministic movement/pause/input fixtures |
| [Zephyr](https://github.com/zephyrproject-rtos/zephyr) | Embedded RTOS | Project choice for ISR/ring/timer tests; physical timing requires target hardware |
| [Miri](https://github.com/rust-lang/miri) | Rust interpreter for detecting certain undefined behavior | Proposed supported Rust-boundary checks; not proof of all native/FFI safety |

## All 30 categories: proposed evidence track

| Category | Concrete future acceptance exercise | Appropriate tools from this inventory |
| --- | --- | --- |
| ai-engineering | Grounded answer, malicious retrieval, malformed/empty tool result | Promptfoo; optional Ragas/DeepEval |
| automation | Crash after effect, replay, bounded throttling | pytest/Hypothesis; Temporal only when relevant |
| cloud-devops-sre | Compatibility rollout and failure recovery in a test environment | Testcontainers, Trivy, OpenTelemetry |
| code-build | Real patch plus independent counterexamples | pytest, Hypothesis, Ruff |
| computer-vision | Annotation alignment and deployment-group split | PyTorch/Transformers, pytest |
| cybersecurity | Exploit-path repair plus safe-control false positives | Semgrep/CodeQL, Trivy, Gitleaks and executable fixtures |
| data-engineering | Late correction, publication interruption and reconciliation | Polars, Pandera, pytest |
| data-science | Join grain, denominators and uncertainty | DuckDB, NumPy, independent calculations |
| databases | Mixed-version writes, backfill, lock and recovery behavior | SQLAlchemy/Alembic where used, Testcontainers |
| deep-learning | Full-state checkpoint and controlled resume | PyTorch, MLflow, DVC where useful |
| design-ux | Keyboard/focus/error hierarchy and component states | Storybook, Playwright, axe-core |
| developer-research | Evidence/version disagreement and discriminating experiment | Versioned source fixtures, pytest, evidence schema |
| developer-tools | Dirty-path collision, preview and interrupted journal | pytest, Hypothesis, uv/Git fixtures |
| distributed-systems | Stale owner, overlap and lost reply | Testcontainers, Temporal where appropriate, pytest |
| documentation | Examples match actual help/API and recoverable errors | pytest, Schemathesis for relevant APIs |
| embedded-systems | Wrap arithmetic and ISR ownership, then measured timing | Zephyr, host fixtures; physical hardware separately |
| game-development | Multi-schedule displacement and one jump per press | Godot and deterministic fixtures |
| machine-learning | Point-in-time features, group split and baseline | scikit-learn, Optuna, MLflow |
| mlops | Compatible model/preprocessor bundle and rollback | MLflow, DVC, OpenTelemetry, k6 |
| mobile-development | Offline edits, process death and duplicate replay | React Native, device/emulator tests not yet selected |
| natural-language-processing | Label-preserving truncation and padding invariance | Transformers, PyTorch, pytest |
| neural-networks | Logit-space loss, finite differences and tiny-batch checks | PyTorch/NumPy, pytest/Hypothesis |
| observability | Queue context and sustained failure alert | OpenTelemetry; optional trace backend |
| performance-engineering | Equivalent outputs, matched load and full distributions | k6, NumPy/Matplotlib, separate process metrics |
| python | Wheel/sdist installs outside checkout and oldest-interpreter behavior | uv, Hatchling, Twine, pytest |
| release-engineering | Source/CI/artifact identity and destination verification | GitHub Actions, Twine, optional Sigstore |
| systems-programming | Stable FFI lifetime and destruction/concurrency | Miri where supported; native sanitizers still need selection |
| testing | Accept correct implementation and reject distinct mutants | pytest, Hypothesis, mutmut |
| web-backend | Tenant identity, payload mismatch and lost-commit reply | Schemathesis, Testcontainers, stack-specific framework |
| web-frontend | Complete responsive flow with invalid/valid states | Playwright, axe-core, Lighthouse; selected UI stack |

## Existing published-skill comparison inventory

These 14 repositories were already used as pinned references in the recorded pilot; they are not newly installed tools. The original snapshot file supplies exact commits and category mapping. Some specialize in one platform, so they are not interchangeable full-library competitors.

1. [Anthropic skills](https://github.com/anthropics/skills)
2. [Vercel agent skills](https://github.com/vercel-labs/agent-skills)
3. [Microsoft skills](https://github.com/microsoft/skills)
4. [Google skills](https://github.com/google/skills)
5. [Hugging Face skills](https://github.com/huggingface/skills)
6. [Trail of Bits skills](https://github.com/trailofbits/skills)
7. [Superpowers](https://github.com/obra/superpowers)
8. [Supabase agent skills](https://github.com/supabase/agent-skills)
9. [Cloudflare skills](https://github.com/cloudflare/skills)
10. [Temporal developer skill](https://github.com/temporalio/skill-temporal-developer)
11. [K-Dense scientific skills](https://github.com/K-Dense-AI/scientific-agent-skills)
12. [ECC](https://github.com/affaan-m/ecc)
13. [Zephyr agent skills](https://github.com/beriberikix/zephyr-agent-skills)
14. [Game-development agent skills](https://github.com/minhhoit/gamedev-agent-skills)

## Buying and adoption decisions

Keep the current core free of heavy framework dependencies. Put tooling in separate development/evaluation extras or explicit profiles. Start with one evaluation runner and one trace store, not several overlapping stacks. Keep credentials and hosted costs outside exported skills. Review licenses before bundling source or rules; upstream materials retain their owners and terms.

The upstream pages establish each project's stated purpose and current repository location. No comparative GNCore performance, freshness guarantee, security certification, license clearance or suitability for every project is inferred from appearing in this list. No proposed tool was installed or run as part of this inventory request.
