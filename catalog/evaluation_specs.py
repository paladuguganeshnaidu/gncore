"""Concrete developer evaluation requests; normal / vague / boundary for each category."""

# mode, request, supplied context, expected artifact
SCENARIOS = {
    "neural-networks": [
        ("nn-gradient-check", "Verify gradients for a tiny XOR neural network on CPU.", "Use the bundled 2-4-1 tanh/logit probe with seed 17. Compare all 17 parameter gradients by central finite difference; no external dataset or framework is needed.", "gradient-report.json"),
        ("nn-tensor-contracts", "Help me build my first neural network.", "Binary classification of two numeric features. Explain input, hidden, output and target shapes, choose a modest local baseline, and state assumptions. No GPU or dataset has been supplied.", "network-plan.md"),
        ("nn-loss-semantics", "Review why this binary training loss is suspicious.", "The model applies sigmoid, then passes probabilities into BCEWithLogitsLoss; targets have shape [8] and outputs [8,1]. Identify the two contract problems before claiming training success.", "loss-review.md"),
    ],
    "deep-learning": [
        ("dl-checkpoint-resume", "Design a resumable PyTorch training checkpoint.", "The run uses an optimizer, scheduler, precision scaler and shuffled input. Define the saved state and a tiny uninterrupted/resumed equivalence check; do not launch a hosted job.", "checkpoint-contract.md"),
        ("dl-transfer-learning", "Fine-tune this model for my dataset.", "Only the task is known: three-class image classification. Weights, labels, data rights and hardware are not provided. Prepare minimum intake and a bounded transfer-learning experiment without reporting metrics.", "fine-tuning-plan.md"),
        ("dl-gradient-accumulation", "Review this accumulation loop before scaling it.", "Microbatches contain 4,4,2 examples. Loss is averaged per microbatch and each is divided by 3 before backward. Desired behavior equals the mean over all 10 examples. Explain the weighting error and a check against an equivalent full batch.", "accumulation-review.md"),
    ],
    "computer-vision": [
        ("cv-geometric-transforms", "Specify a tested image/box resize transform.", "Image width/height 100x50, xyxy box [10,5,30,20], resize to 200x100. Expected box [20,10,60,40]. State interpolation rules for categorical masks separately.", "transform-contract.md"),
        ("cv-dataset-audit", "Help me train a vision model.", "Photographs may contain multiple images of the same subject; labels and provenance are not yet audited. Prepare a dataset and split audit before selecting an architecture.", "vision-audit.md"),
        ("cv-detection-metrics", "Review this detection score.", "Evaluation silently drops images with no annotations and excludes failed image loads. Report selection bias and define empty prediction/annotation handling; no raw prediction data is supplied.", "detection-review.md"),
    ],
    "natural-language-processing": [
        ("nlp-token-alignment", "Design a token/label alignment test.", "Text includes café and a split subword; tokenizer emits special tokens and offsets. Define ignored labels and a hand-labeled fixture; do not assume one token per word.", "alignment-test.md"),
        ("nlp-text-classification", "Classify our support messages.", "The only facts are English/Spanish messages and repeated users. Labels, consent and retention rules are unspecified. Propose a simple baseline and group-aware evaluation, without requesting actual private messages.", "text-baseline.md"),
        ("nlp-sequence-modeling", "Review masking in this sequence model.", "The decoder receives future target tokens without a causal mask, and padding contributes to average loss. Identify leakage and masking/reduction checks on a short sequence.", "mask-review.md"),
    ],
    "mlops": [
        ("mlops-artifact-contract", "Prepare a portable model bundle contract.", "A model consumes named numeric features with a fitted scaler. Specify weights/scaler/schema/version/hashes and a clean-load prediction fixture; no production deployment is authorized.", "model-bundle.md"),
        ("mlops-serving-contract", "Put my model behind an endpoint.", "The serialized model, dependencies and schema have not been supplied. Prepare the serving boundary and exact missing-artifact requests instead of inventing a working integration.", "serving-plan.md"),
        ("mlops-drift-monitoring", "Review this monitoring claim.", "A feature histogram shifted but no labels have arrived. The dashboard says accuracy fell 20%. Explain what is observable, what is unproven, and which delayed-label check is needed.", "drift-review.md"),
    ],
    "databases": [
        ("db-transaction-invariants", "Prevent duplicate slot reservations in SQLite.", "Bookings(tenant_id,slot_id,owner_id); one booking per tenant/slot. Specify unique constraints, a transactional insert and a local two-writer conflict test. Authentication context is supplied separately.", "booking-schema.sql"),
        ("db-query-plans", "Speed up my SQL query.", "No engine, schema, query, distribution or explain plan is supplied. Request the minimum missing inputs and define a reproducible plan/benchmark comparison; do not invent an index.", "query-investigation.md"),
        ("db-expand-contract", "Plan a required-column migration with unknown existing values.", "An existing table has rows with unknown region; old app versions ignore the new column. Do not fabricate regions or immediately enforce NOT NULL; define compatible stages and a policy decision.", "region-migration.md"),
    ],
    "systems-programming": [
        ("systems-ffi", "Specify a Rust/C FFI buffer interface.", "C caller supplies pointer and byte length and owns its input. Define zero-length/null behavior, result ownership and error codes without unwinding across the boundary.", "ffi-contract.md"),
        ("systems-ownership", "Build a native extension for this hot path.", "No profile or ABI target is supplied. Prepare a bounded investigation, ownership contract and benchmark requirements before proposing unsafe code or a language migration.", "native-plan.md"),
        ("systems-safe-arithmetic", "Review a buffer allocation for overflow.", "C code allocates count * sizeof(Item), then copies count elements. count is external. Describe overflow/range validation and minimum/maximum test cases before allocation.", "buffer-review.md"),
    ],
    "embedded-systems": [
        ("embedded-state-machine", "Design a bounded retry firmware state machine.", "States idle/waiting/done/fault; at most three transmissions; each wait times out after 100 ticks. Separate transport effects from pure state and include reset/duplicate-event checks.", "firmware-state.md"),
        ("embedded-protocols", "Connect a sensor to my board.", "MCU, board, voltage, sensor model and bus are unspecified. Prepare a minimal hardware intake and host-testable transport boundary; do not invent pin assignments.", "sensor-intake.md"),
        ("embedded-timing", "Fix a timeout that fails when the timer wraps.", "Unsigned 32-bit tick counter; start=4294967290, now=5, timeout=10. Correct elapsed count is 11 modulo 2^32. State the maximum safe interval assumption.", "timer-fix.md"),
    ],
    "performance-engineering": [
        ("perf-benchmark-design", "Design a reproducible parser benchmark.", "Compare the same 1000 small JSON inputs in two implementations on one machine. Include warmup, multiple repeats, output equivalence and raw timings; no measured results are supplied.", "benchmark-plan.md"),
        ("perf-memory-profile", "My service uses too much memory.", "No workload or profile is supplied. Separate retained memory, peak working set and allocation churn and define a minimal measurement plan before changing caches.", "memory-investigation.md"),
        ("perf-tail-latency", "Review this latency summary.", "Reported p99 excludes timeouts and failed requests; a closed-loop generator sends a new request only after the last completes. Explain the bias and a safe staging measurement plan.", "latency-review.md"),
    ],
    "observability": [
        ("obs-trace-context", "Trace one request through a background queue.", "HTTP handler enqueues work; worker calls a dependency. Specify correlation/parent context, controlled error spans and redaction tests; no hosted telemetry credentials supplied.", "trace-contract.md"),
        ("obs-metrics-alerts", "Add monitoring to this service.", "Service objectives and owner are unspecified. Propose a small user-impact-focused metric/alert set and identify those missing decisions instead of creating noisy per-error alerts.", "monitoring-plan.md"),
        ("obs-structured-events", "Review these proposed structured log fields.", "Fields include raw Authorization header, full email and per-request URL as a metric label. Identify privacy/cardinality problems and provide bounded replacements.", "telemetry-review.md"),
    ],
    "developer-research": [
        ("research-api-compatibility", "Investigate an API migration using primary documentation.", "A Python library changes from a synchronous to async client; actual versions and call sites must be inspected before recommending a migration. Deliver an evidence/reproduction plan, not invented compatibility claims.", "api-investigation.md"),
        ("research-technical-decision", "Which database should we choose?", "A single developer is building a local prototype with modest writes. Workload growth, deployment and operations budget are unspecified. Compare a bounded set of options against known constraints and flag material unknowns.", "database-decision.md"),
        ("research-paper-reproduction", "Assess this claimed paper reproduction.", "The experiment used a different dataset split and reports training accuracy instead of the paper's holdout F1. Identify what was reproduced and what is incomparable; no training job is authorized.", "reproduction-review.md"),
    ],
    "ai-engineering": [
        ("ai-tool-contracts", "Design a bounded tool-using support assistant.", "Read-only search tool and draft-response tool; no email send permission. Define schemas, iteration/time budgets, malformed-output and injection fixtures.", "agent-contract.md"),
        ("ai-retrieval-evaluation", "Add RAG to our docs.", "Corpus rights, freshness and access rules are unspecified. Prepare indexing/retrieval/evaluation boundaries and the minimum missing inputs without uploading documents.", "rag-plan.md"),
        ("ai-retrieval-evaluation", "Review an answer with unsupported citations.", "The answer cites a document that mentions the topic but does not support its numerical claim. Define a grounding failure case; citation presence alone must not pass.", "grounding-review.md"),
    ],
    "automation": [
        ("automation-resume", "Design an idempotent local file-processing automation.", "Three immutable input files; output one checksum per file. Crash may happen after writing output but before recording progress. Resume must not duplicate completed work.", "resume-plan.md"),
        ("workflow-automation", "Automate our repetitive workflow.", "Trigger, inputs, side effects and owner are missing. Prepare a small intake/state model and do not assume permission to send messages or create paid resources.", "automation-intake.md"),
        ("automation-resume", "Review this retry policy.", "A payment operation retries every exception without an idempotency key, maximum attempts or end-to-end deadline. Explain duplicate-side-effect risk and a bounded contract; no live calls.", "retry-review.md"),
    ],
    "cloud-devops-sre": [
        ("cloud-ci-cd", "Prepare a CI pipeline with meaningful failure artifacts.", "Python package, existing pytest suite and wheel build. Use least-privilege workflow permissions and keep publication separate from pull-request checks.", "ci-plan.md"),
        ("cloud-architecture", "Move this service to the cloud.", "Only workload fact: HTTP API with a relational database. Availability, traffic, recovery objectives and budget are unknown. Prepare architecture questions/options without deploying infrastructure.", "cloud-intake.md"),
        ("cloud-kubernetes", "Review this Kubernetes health configuration.", "Readiness and liveness both fail whenever a shared dependency is briefly unavailable. Explain restart amplification and distinguish readiness, liveness and startup behavior.", "health-review.md"),
    ],
    "cybersecurity": [
        ("cyber-threat-model", "Threat-model a tenant-scoped document API.", "Authenticated users should read only their tenant's documents. Document IDs come from the URL. Map trust boundaries, a cross-tenant abuse case and negative tests on a local fixture.", "threat-model.md"),
        ("cyber-secure-code", "Check whether my application is secure.", "No code, scope or deployment is supplied. Request the smallest relevant attack surface and prepare an evidence-led review plan rather than a security certification.", "security-scope.md"),
        ("cyber-vulnerability-triage", "Review a dependency scan with zero findings.", "The scanner did not recognize the lockfile and excluded a native dependency. Explain the coverage gap and missing evidence without claiming no vulnerabilities.", "dependency-review.md"),
    ],
    "data-science": [
        ("sql-analysis", "Prevent join fanout in this revenue analysis.", "Orders A=100,B=200 cents. A has two order_items; B has one. Sum order revenue once per order, not once per joined item. Include a known-result check of 300 cents.", "revenue-analysis.md"),
        ("statistics", "Analyze whether this change improved conversion.", "Only an overall before/after rate is supplied; denominators, assignment and time windows are missing. Define the estimand and minimum data needed before significance or causal claims.", "experiment-intake.md"),
        ("statistics", "Review this statistical claim.", "Twenty subgroup tests were run and the only p<0.05 result was reported as the planned primary outcome. Identify multiplicity/selection concerns and distinguish exploratory from confirmatory evidence.", "statistics-review.md"),
    ],
    "design-ux": [
        ("design-system-component", "Specify an accessible developer settings form.", "Fields: display name and notification toggle. Include save/invalid/saving/error/success states, focus behavior and narrow layouts using existing tokens.", "settings-spec.md"),
        ("design-user-flow", "Make our onboarding easier.", "Only the goal is known; existing flow and observed failure evidence are absent. Prepare a small assumption-labeled flow and targeted evidence requests instead of inventing user research.", "onboarding-flow.md"),
        ("design-accessibility", "Review an interaction that relies only on hover and red/green color.", "The primary action is hidden until mouse hover; error/success uses color without labels. Provide equivalent keyboard/touch and text/semantic feedback.", "interaction-review.md"),
    ],
    "developer-tools": [
        ("cli-design", "Specify a scriptable checksum CLI.", "Input paths may include spaces and Unicode; stdout must be JSON, diagnostics stderr, invalid input exit 2. No network access needed. Include failure and interruption behavior.", "cli-contract.md"),
        ("tooling-reproducible-env", "Set up our developer environment.", "No language/version/lockfiles supplied. Inspect existing project conventions and prepare minimal reproducible setup steps without installing unrelated global hooks.", "environment-plan.md"),
        ("cli-design", "Review a destructive CLI default.", "The default command recursively deletes a computed target before validating that it is inside the workspace. Prepare a preflight/dry-run/path-boundary fix with isolated tests.", "filesystem-review.md"),
    ],
    "documentation": [
        ("documentation-api", "Document this request contract.", "POST /items accepts name (required nonempty text) and optional count (nonnegative integer, default 0). Return 201, validation 400, unauthenticated 401 and forbidden 403. Do not invent pagination.", "items-api.md"),
        ("technical-writing", "Write docs for our library.", "The audience and public API are not supplied. Inspect actual entrypoints and prepare a focused quick-start outline with explicit missing prerequisites, without inventing functions.", "docs-outline.md"),
        ("documentation-translation", "Localize this technical instruction without breaking it.", "Translate prose while retaining identifier user_id, token {count}, command gncore export --all and literal URL paths. State locale assumptions and do not translate executable identifiers.", "localized-guide.md"),
    ],
    "mobile-development": [
        ("mobile-app", "Design an offline-capable mobile task list.", "Existing mobile framework is retained; tasks can be edited offline and synced later. Define loading, offline, conflict, denied-permission and restored-lifecycle states.", "mobile-state.md"),
        ("mobile-app", "Build me a mobile app.", "No framework, OS support or product flow specified. Choose a modest prototype assumption and identify only choices that block a correct implementation; do not submit to an app store.", "mobile-plan.md"),
        ("mobile-app", "Review a mobile permission flow.", "The app repeatedly requests a permanently denied permission and loses edited text when backgrounded. Define recovery/settings guidance and state persistence without assuming the user grants permission.", "lifecycle-review.md"),
    ],
    "python": [
        ("python-packaging", "Prepare a cleanly installable Python library.", "Use a src layout and the existing pyproject backend; include one JSON resource and a CLI. Verify import/resource/entrypoint behavior from a wheel outside the checkout.", "packaging-plan.md"),
        ("python-migration", "Upgrade our Python code.", "Source/target interpreter versions and dependencies are unspecified. Inspect support constraints and call sites before proposing the smallest compatibility migration.", "python-migration.md"),
        ("python-migration", "Review a compatibility claim based only on grammar parsing.", "The package parses with Python 3.10 grammar but calls a standard-library method introduced later. Separate syntax compatibility from actual runtime evidence and define supported-version checks.", "compatibility-review.md"),
    ],
    "release-engineering": [
        ("release-artifact-integrity", "Prepare a release candidate without publishing it.", "Synchronize code, metadata, docs and website version; build wheel/source, record checksums and test clean installation. GitHub/PyPI publication requires a later user approval.", "release-readiness.md"),
        ("release-readiness", "Release this project.", "Version scope, destinations and current remote state are unknown. Inspect artifacts/workflows and prepare a concrete approval-ready release plan without creating tags or uploading packages.", "release-plan.md"),
        ("release-artifact-integrity", "Review whether these release artifacts match.", "CI tested one wheel but the publish step rebuilds from a moving branch. Explain why tests do not cover the uploaded bytes and prepare a build-once/promotion check.", "artifact-review.md"),
    ],
    "testing": [
        ("unit-testing", "Test a percentage-discount function through public behavior.", "Contract: nonnegative price, percentage 0..100, total=price*(1-percent/100). Include zero/full/invalid/fractional cases and do not mirror an incorrect implementation.", "discount-tests.md"),
        ("requirements-to-tests", "Add tests to this service.", "No change, contract or existing suite is supplied. Inspect the highest-impact boundary and propose focused normal/error/regression cases without an arbitrary coverage target.", "test-plan.md"),
        ("test-automation", "Review a CI test job that always exits zero.", "The shell runs pytest || true and publishes a success badge even when assertions fail. Restore meaningful failure signaling and preserve failure logs; do not weaken tests.", "ci-test-review.md"),
    ],
    "distributed-systems": [
        ("dist-idempotency", "Specify a durable idempotent operation.", "A caller may retry after timeout. Same key/same payload replays the result; same key/different payload conflicts. Persist operation result and side effect in one consistency boundary.", "idempotency-contract.md"),
        ("dist-consistency", "Make our application distributed.", "Workload, invariants and availability/consistency requirements are unspecified. Identify the concrete scaling/failure problem before proposing queues, replicas or coordination services.", "distributed-intake.md"),
        ("dist-queues", "Review this message handler.", "The handler commits a database write then crashes before acknowledgment. Define replay behavior and deduplication/transaction boundaries; do not claim exactly-once from a successful happy-path test.", "queue-review.md"),
    ],
}
