"""User-requested backend and general coding skills, grouped by task."""

# Each workflow guides selection; detailed task-specific material stays in the
# pinned upstream skill rather than being copied into every entrypoint.
GROUPS = [
    ("requirements", "code", "Establish the requested outcome, current behavior, constraints, acceptance criteria, and unresolved architectural choices. Use repository evidence before proposing changes; produce the brief or decision artifact requested rather than automatically moving into implementation.", {
        "mattpocock/skills": "grill-me research prototype domain-modeling decision-mapping",
        "affaan-m/ecc": "search-first product-lens architecture-decision-records blueprint",
    }),
    ("architecture", "web-backend", "Trace request boundaries, domain rules, persistence, dependencies, and failure modes in the current system. Choose interfaces and ownership boundaries appropriate to the actual service and explain concrete tradeoffs before changing architecture.", {
        "affaan-m/ecc": "backend-patterns api-design hexagonal-architecture error-handling",
        "mattpocock/skills": "codebase-design improve-codebase-architecture",
    }),
    ("contracts", "web-backend", "Inspect producers, consumers, schemas, authentication, and compatibility requirements. Make validation, status codes, error envelopes, pagination, and idempotency explicit when relevant; verify implementation against the agreed contract.", {
        "affaan-m/ecc": "contract-first api-connector-builder",
        "trailofbits/skills": "spec-to-code-compliance",
    }),
    ("quality", "code", "Understand local conventions and the behavior that must survive the change. Identify concrete correctness, maintainability, or complexity problems, make a scoped improvement, and verify observable behavior; avoid cosmetic churn and speculative abstractions.", {
        "affaan-m/ecc": "coding-standards codebase-onboarding plankton-code-quality",
        "mattpocock/skills": "code-review request-refactor-plan",
        "trailofbits/skills": "code-improver code-maturity-assessor",
    }),
    ("testing", "code", "Select tests from the requested behavior and relevant failure risks. Reproduce a bug or demonstrate a meaningful failing case where appropriate, implement the change, and run focused regressions without weakening assertions or claiming unrun tests passed.", {
        "obra/superpowers": "test-driven-development",
        "affaan-m/ecc": "tdd-workflow e2e-testing ai-regression-testing module-regression",
        "trailofbits/skills": "property-based-testing coverage-analysis",
    }),
    ("debugging", "code", "Reproduce the reported behavior with the smallest useful case, collect evidence, and distinguish hypotheses from causes. Trace the failure through the actual system, make a focused fix, and verify the reproduction plus relevant regressions before reporting completion.", {
        "obra/superpowers": "systematic-debugging verification-before-completion",
        "mattpocock/skills": "diagnosing-bugs qa",
        "affaan-m/ecc": "verification-loop",
    }),
    ("security", "code", "Map relevant trust boundaries and attacker-controlled input in the requested code. Tie findings to reachable paths and impact, preserve authorization and secret handling, and verify mitigations locally without expanding into unauthorized live-target testing.", {
        "affaan-m/ecc": "security-review agent-security-hardening",
        "trailofbits/skills": "sharp-edges insecure-defaults differential-review",
    }),
    ("analysis", "code", "Check available tool versions and project language support, scope the scan, and inspect the rules or query pack before execution. Triage results against reachable code and report commands, evidence, false positives, and analysis limits rather than treating every alert as a confirmed vulnerability.", {
        "trailofbits/skills": "semgrep codeql sarif-parsing supply-chain-risk-auditor",
    }),
    ("persistence", "web-backend", "Inspect the schema, query patterns, consistency rules, and migration tooling. Preserve transaction and authorization boundaries; use representative query plans or migration checks and account for rollback, existing data, and concurrent writes.", {
        "supabase/agent-skills": "supabase-postgres-best-practices",
        "affaan-m/ecc": "postgres-patterns database-migrations",
    }),
    ("performance", "web-backend", "Establish a representative baseline and workload before optimizing. Identify the dominant latency, throughput, contention, or resource cost; change a measured bottleneck and compare under the same conditions while preserving correctness.", {
        "affaan-m/ecc": "benchmark benchmark-optimization-loop latency-critical-systems redis-patterns",
    }),
    ("delivery", "web-backend", "Inspect the build, runtime, configuration, dependency pinning, and current delivery workflow. Prepare reproducible changes and validate a local or staging path; preserve secret boundaries and distinguish a prepared rollout from an actual authorized deployment.", {
        "affaan-m/ecc": "deployment-patterns docker-patterns github-ops git-workflow",
    }),
    ("observability", "web-backend", "Trace existing logs, traces, metrics, error grouping, and incident context. Instrument useful boundaries with redaction and bounded cardinality; correlate observed failures to code and verify signals without inventing production access or outcomes.", {
        "getsentry/plugin-codex": "sentry-instrument sentry-debug-issue",
        "affaan-m/ecc": "production-audit",
    }),
    ("readiness", "code", "Evaluate the requested change against concrete acceptance checks, regression evidence, operating costs, and recovery plans. Report passed checks separately from unknowns; prepare a reviewable result without implying authorization to publish, deploy, or merge.", {
        "affaan-m/ecc": "delivery-gate cost-tracking",
        "trailofbits/skills": "post-patch-validation mutation-testing",
    }),
    ("investigation", "code", "Turn the actual question into a bounded investigation with primary sources and repository evidence. Separate findings, hypotheses, decisions, and proposed experiments; produce the requested product brief, specification, or actionable tickets without expanding the product scope.", {
        "affaan-m/ecc": "deep-research research-ops product-capability",
        "mattpocock/skills": "to-prd to-spec to-tickets",
    }),
    ("ai-systems", "web-backend", "Define model and tool boundaries, typed inputs, state ownership, failure handling, and evaluation cases. Bound retries, latency, and spending; preserve authorization around external actions and verify useful task outcomes rather than evaluating model prose alone.", {
        "affaan-m/ecc": "agentic-engineering mcp-server-patterns agent-eval cost-aware-llm-pipeline",
        "anthropics/skills": "mcp-builder",
        "cloudflare/skills": "agents-sdk building-ai-agent-on-cloudflare",
    }),
    ("execution", "code", "Use the requested plan or specification as the acceptance boundary, inspect the relevant code, and implement reviewable increments. Keep plans proportional to complexity, preserve user changes, and use additional agents only when supported and authorized for the current task.", {
        "obra/superpowers": "writing-plans executing-plans requesting-code-review receiving-code-review",
        "mattpocock/skills": "implement implement-spec",
    }),
    ("python", "web-backend", "Inspect Python, framework, validation, database, and test versions before choosing APIs. Implement typed boundaries and explicit error handling using the current project conventions; verify the requested behavior with framework-appropriate tests.", {
        "fastapi/fastapi": "fastapi",
        "affaan-m/ecc": "fastapi-patterns python-patterns python-testing django-patterns django-security django-tdd django-verification",
    }),
    ("stacks", "web-backend", "Identify the actual language and framework versions, request lifecycle, dependency injection, data access, and security conventions. Apply only the selected stack's task-specific guidance, preserve public contracts, and run the relevant compiler, type, or behavior checks.", {
        "affaan-m/ecc": "nestjs-patterns springboot-patterns springboot-security springboot-tdd springboot-verification golang-patterns golang-testing laravel-patterns laravel-security laravel-tdd laravel-verification",
    }),
    ("managed-data", "web-backend", "Inspect the actual database or cache topology, client lifecycle, access controls, query workload, and operational constraints. Verify consistency, expiry, isolation, and failure behavior with representative local cases; keep credentials and sensitive data out of logs.", {
        "supabase/agent-skills": "supabase",
        "redis/agent-skills": "redis-core redis-connections redis-security redis-observability redis-search redis-semantic-cache",
    }),
    ("platforms", "web-backend", "Inspect the selected platform's deployment configuration, runtime limits, bindings, and existing observability. Use version-compatible APIs, validate locally, and state which deployment or production checks remain unperformed.", {
        "vercel-labs/agent-skills": "vercel-optimize",
        "cloudflare/skills": "cloudflare workers-best-practices wrangler durable-objects workers-profiling",
    }),
    ("regressions", "code", "Exercise the relevant user journey or changed boundary, compare expected and actual behavior, and isolate any regression to a reproducible case. Prefer deterministic fixtures and observable outcomes over timing sleeps or implementation-mirroring assertions.", {
        "anthropics/skills": "webapp-testing",
        "trailofbits/skills": "regression-hunt",
    }),
    ("workflow", "code", "Choose a workflow proportional to the requested change. Explore unresolved product decisions when needed, isolate parallel changes safely, and finish with a concrete reviewable result. Repository setup changes and external branch actions must remain within the user's actual request.", {
        "obra/superpowers": "brainstorming using-git-worktrees subagent-driven-development finishing-a-development-branch",
        "mattpocock/skills": "setup-matt-pocock-skills",
    }),
]

RENAMES = {
    "systematic-debugging": "code-debugging",
    "coding-standards": "code-quality",
    "test-driven-development": "code-tdd",
    "backend-patterns": "web-backend-patterns",
    "fastapi": "web-backend-fastapi",
    "django-patterns": "web-backend-django",
    "docker-patterns": "web-backend-docker",
    "git-workflow": "code-git-workflow",
    "codebase-design": "code-architecture",
    "improve-codebase-architecture": "code-improve-architecture",
    "python-patterns": "code-python",
    "python-testing": "code-python-testing",
    "setup-matt-pocock-skills": "code-workflow-setup",
}


def requests():
    return [
        {"requested": name, "repository": repo, "id": RENAMES.get(name, f"{prefix}-{name}"), "group": group, "guidance": guidance}
        for group, prefix, guidance, sources in GROUPS
        for repo, names in sources.items()
        for name in names.split()
    ]
