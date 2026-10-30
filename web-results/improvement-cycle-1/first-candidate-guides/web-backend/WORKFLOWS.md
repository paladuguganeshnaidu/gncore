# GNCore Web Backend: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### GNCore Patterns (`web-backend-patterns`)

Trace request, application/domain and persistence boundaries in the existing service. Keep business invariants independent of transport details, make failure ownership explicit and introduce a new layer only when it simplifies a real change. Verify one complete success and failure path through the chosen boundaries.

Technical reference: [attributed source guide](references/web-backend-patterns/UPSTREAM.md).

### GNCore Api Design (`web-backend-api-design`)

Specify resources, schemas, status/error codes, authorization, pagination and retry semantics from the consumer's task. Test invalid input, missing/forbidden resources and compatibility with current clients; do not let framework serialization defaults silently define a public contract.

Technical reference: [attributed source guide](references/web-backend-api-design/UPSTREAM.md).

### GNCore Hexagonal Architecture (`web-backend-hexagonal-architecture`)

Identify domain invariants and external dependencies, then define narrow ports around the dependencies that need substitution. Keep framework/ORM types in adapters, test the domain through ports and one real adapter integration, and avoid wrapping every internal function in an interface.

Technical reference: [attributed source guide](references/web-backend-hexagonal-architecture/UPSTREAM.md).

### GNCore Error Handling (`web-backend-error-handling`)

Classify validation, authorization, conflict, transient dependency and unexpected errors. Preserve diagnostic causes internally while returning stable public errors without secrets. Test exception-to-response mapping, transaction rollback and whether a retry can duplicate the side effect.

Technical reference: [attributed source guide](references/web-backend-error-handling/UPSTREAM.md).

### GNCore Contract First (`web-backend-contract-first`)

Write request/response and error examples before implementation, including absence, invalid values and authorization. Validate the schema and consumer expectations against existing versions, then implement and run contract tests so documentation and runtime behavior agree.

Technical reference: [attributed source guide](references/web-backend-contract-first/UPSTREAM.md).

### GNCore Api Connector Builder (`web-backend-api-connector-builder`)

Inspect the external API's authentication, pagination, rate limits and versioned schema. Implement a typed boundary with bounded retries only for safe operations, timeouts and redacted diagnostics. Replay recorded/synthetic success, malformed response, pagination and quota/error fixtures before a live call.

Technical reference: [attributed source guide](references/web-backend-api-connector-builder/UPSTREAM.md).

### GNCore Spec To Code Compliance (`web-backend-spec-to-code-compliance`)

Turn supplied normative requirements into traceable code paths and executable acceptance cases. Distinguish MUST behavior from optional guidance and missing specification. Report each mismatch with source location and observed behavior instead of treating a passing schema check as full compliance.

Technical reference: [attributed source guide](references/web-backend-spec-to-code-compliance/UPSTREAM.md).

### GNCore Supabase Postgres Best Practices (`web-backend-supabase-postgres-best-practices`)

Inspect Postgres access patterns and Supabase role/RLS boundaries. Parameterize queries, encode integrity in constraints and inspect plans before indexing. Verify authenticated and cross-tenant negative cases using the actual role model; a privileged service key must not stand in for user-policy testing.

Technical reference: [attributed source guide](references/web-backend-supabase-postgres-best-practices/UPSTREAM.md).

### GNCore Postgres Patterns (`web-backend-postgres-patterns`)

Choose transaction isolation, constraints and indexes from the invariant and workload. Reproduce null/uniqueness behavior, lock conflicts and the query plan in a local Postgres fixture. Keep connection lifetime and prepared-query behavior consistent with the selected driver/pool.

Technical reference: [attributed source guide](references/web-backend-postgres-patterns/UPSTREAM.md).

### GNCore Database Migrations (`web-backend-database-migrations`)

Use expand/backfill/validate/contract sequencing for mixed-version deployments. Make backfills bounded and restartable, state the policy for unknown values and rehearse lock/failure behavior. Separate a reversible schema change from data changes that cannot be automatically undone.

Technical reference: [attributed source guide](references/web-backend-database-migrations/UPSTREAM.md).

### GNCore Benchmark (`web-backend-benchmark`)

Define workload, environment, warmup, concurrency and success thresholds before measuring. Retain raw latency/error/throughput results and compare identical request/data conditions. Separate benchmark setup cost from the measured operation and avoid claiming production capacity from a local microbenchmark.

Technical reference: [attributed source guide](references/web-backend-benchmark/UPSTREAM.md).

### GNCore Benchmark Optimization Loop (`web-backend-benchmark-optimization-loop`)

Capture a reproducible baseline, profile the dominant cost, make one targeted change and compare both correctness and distributions on the same workload. Keep raw evidence and stop if improvement is within noise or a correctness/resource tradeoff is unacceptable.

Technical reference: [attributed source guide](references/web-backend-benchmark-optimization-loop/UPSTREAM.md).

### GNCore Latency Critical Systems (`web-backend-latency-critical-systems`)

Allocate an end-to-end latency budget and measure dependency, queue and serialization contributions, including tails and errors. Bound queues, deadlines and cancellation; test overload/recovery rather than optimizing only successful warm requests. Explain the conditions under which the target was measured.

Technical reference: [attributed source guide](references/web-backend-latency-critical-systems/UPSTREAM.md).

### GNCore Redis Patterns (`web-backend-redis-patterns`)

Choose Redis key structure, TTL, invalidation and atomicity from the cache/state contract. Define cache-miss and unavailable-cache behavior and test stale data, expiry, concurrent updates and hot-key effects. Do not turn a disposable cache into an undocumented source of truth.

Technical reference: [attributed source guide](references/web-backend-redis-patterns/UPSTREAM.md).

### GNCore Deployment Patterns (`web-backend-deployment-patterns`)

Prepare a staged rollout with version compatibility, meaningful health signals and rollback criteria. Validate configuration and migration order in a safe environment; keep code preparation, deployment execution and verified live traffic separate in the report.

Technical reference: [attributed source guide](references/web-backend-deployment-patterns/UPSTREAM.md).

### GNCore Docker (`web-backend-docker`)

Use the repository's supported base/runtime images, a minimal build context and a non-secret runtime configuration. Check multi-stage output, user/file permissions, health/startup/shutdown and resource limits. Build and run the image locally before claiming container readiness.

Technical reference: [attributed source guide](references/web-backend-docker/UPSTREAM.md).

### GNCore Github Ops (`web-backend-github-ops`)

Inspect workflow triggers, permissions, dependency/cache boundaries and required checks. Restrict credentials to the job that needs them and preserve actionable failure artifacts. Exercise the workflow commands locally and report remote CI separately; do not change branch rules or publish artifacts without scope authorization.

Technical reference: [attributed source guide](references/web-backend-github-ops/UPSTREAM.md).

### GNCore Production Audit (`web-backend-production-audit`)

Review an explicitly scoped service's configuration, dependency boundaries, resource/timeout controls, observability and recovery evidence. Link findings to reachable code/configuration and impact. Use read-only/local checks unless production access/actions are authorized; do not certify readiness from a checklist alone.

Technical reference: [attributed source guide](references/web-backend-production-audit/UPSTREAM.md).

### GNCore Agentic Engineering (`web-backend-agentic-engineering`)

Define the agent's task, allowed tools, state transitions and bounded execution budget. Validate tool arguments/results and isolate side effects from model suggestions. Test tool failure, hostile retrieved instructions, retry and budget exhaustion with fixtures before introducing live integrations.

Technical reference: [attributed source guide](references/web-backend-agentic-engineering/UPSTREAM.md).

### GNCore Mcp Server Patterns (`web-backend-mcp-server-patterns`)

Inspect the selected MCP protocol/SDK version and model resources, tools and prompts with explicit schemas and authorization. Keep transport/session lifecycle separate from domain behavior. Test invalid tool inputs, canceled requests and reconnect/cleanup paths with an available protocol client.

Technical reference: [attributed source guide](references/web-backend-mcp-server-patterns/UPSTREAM.md).

### GNCore Agent Eval (`web-backend-agent-eval`)

Build representative task and failure cases, define objective success and human-review rubrics, and record model/tool/configuration versions. Compare changes on the same cases and separate structure/trace validity from semantic task success. Mark unrun provider or subjective evaluations honestly.

Technical reference: [attributed source guide](references/web-backend-agent-eval/UPSTREAM.md).

### GNCore Cost Aware Llm Pipeline (`web-backend-cost-aware-llm-pipeline`)

Record per-request token/tool budgets, latency requirements and acceptable fallback behavior. Cache only with correct identity/freshness boundaries and route simpler work to appropriate models without weakening output validation. Measure actual provider usage when authorized; otherwise use explicit cost assumptions.

Technical reference: [attributed source guide](references/web-backend-cost-aware-llm-pipeline/UPSTREAM.md).

### GNCore Mcp Builder (`web-backend-mcp-builder`)

Start from the consumer operation, define small typed MCP tools and useful errors, and implement the selected SDK's lifecycle correctly. Verify schemas, authentication/authority propagation and a real local client round-trip. Publishing a server or exposing credentials is a separate authorized action.

Technical reference: [attributed source guide](references/web-backend-mcp-builder/UPSTREAM.md).

### GNCore Agents Sdk (`web-backend-agents-sdk`)

Confirm which Agents SDK and runtime the project actually uses. Implement explicit state/tool contracts, bounded orchestration and error handling with that version's APIs. Test deterministic tool boundaries and resume/cancellation before enabling hosted models or persistent external state.

Technical reference: [attributed source guide](references/web-backend-agents-sdk/UPSTREAM.md).

### GNCore Building Ai Agent On Cloudflare (`web-backend-building-ai-agent-on-cloudflare`)

Inspect the selected Workers and Agents SDK versions, Wrangler configuration, bindings, authentication, state storage, and model provider. Implement the requested agent interaction with typed tool inputs, bounded retries, cancellation, and durable state only where needed. Keep provider credentials in the platform secret mechanism. Verify a useful task, a tool error, and an unauthorized request locally; prepare deployment instructions without claiming a deployed service unless deployment was requested and verified.

### GNCore Fastapi (`web-backend-fastapi`)

Inspect the installed fastapi version and existing application conventions, especially typed request/response models, dependency overrides, generated OpenAPI and async I/O boundaries. Implement a complete scoped feature in the existing application without introducing an unrelated framework migration.

Technical reference: [attributed source guide](references/web-backend-fastapi/UPSTREAM.md).

### GNCore Fastapi Patterns (`web-backend-fastapi-patterns`)

Inspect the installed fastapi version and existing application conventions, especially typed request/response models, dependency overrides, generated OpenAPI and async I/O boundaries. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

Technical reference: [attributed source guide](references/web-backend-fastapi-patterns/UPSTREAM.md).

### GNCore Django (`web-backend-django`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Implement a complete scoped feature in the existing application without introducing an unrelated framework migration.

Technical reference: [attributed source guide](references/web-backend-django/UPSTREAM.md).

### GNCore Django Security (`web-backend-django-security`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

Technical reference: [attributed source guide](references/web-backend-django-security/UPSTREAM.md).

### GNCore Django Tdd (`web-backend-django-tdd`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

Technical reference: [attributed source guide](references/web-backend-django-tdd/UPSTREAM.md).

### GNCore Django Verification (`web-backend-django-verification`)

Inspect the installed django version and existing application conventions, especially ORM constraints/transactions, migrations, queryset ownership, middleware and server-side permissions. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

Technical reference: [attributed source guide](references/web-backend-django-verification/UPSTREAM.md).

### GNCore Nestjs Patterns (`web-backend-nestjs-patterns`)

Inspect the installed nestjs version and existing application conventions, especially module/provider boundaries, validated DTOs, guards, exception filters and application lifecycle. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

Technical reference: [attributed source guide](references/web-backend-nestjs-patterns/UPSTREAM.md).

### GNCore Springboot Patterns (`web-backend-springboot-patterns`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

Technical reference: [attributed source guide](references/web-backend-springboot-patterns/UPSTREAM.md).

### GNCore Springboot Security (`web-backend-springboot-security`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

Technical reference: [attributed source guide](references/web-backend-springboot-security/UPSTREAM.md).

### GNCore Springboot Tdd (`web-backend-springboot-tdd`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

Technical reference: [attributed source guide](references/web-backend-springboot-tdd/UPSTREAM.md).

### GNCore Springboot Verification (`web-backend-springboot-verification`)

Inspect the installed springboot version and existing application conventions, especially service/transaction boundaries, validated request DTOs, security filters and persistence integration. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

Technical reference: [attributed source guide](references/web-backend-springboot-verification/UPSTREAM.md).

### GNCore Golang Patterns (`web-backend-golang-patterns`)

Inspect the installed golang version and existing application conventions, especially context cancellation, error wrapping, goroutine lifetime, race checks and HTTP/database timeouts. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

Technical reference: [attributed source guide](references/web-backend-golang-patterns/UPSTREAM.md).

### GNCore Golang Testing (`web-backend-golang-testing`)

Inspect the installed golang version and existing application conventions, especially context cancellation, error wrapping, goroutine lifetime, race checks and HTTP/database timeouts. Use the native test tooling and a local/disposable fixture to exercise success, cancellation, invalid input and persistence failures.

Technical reference: [attributed source guide](references/web-backend-golang-testing/UPSTREAM.md).

### GNCore Laravel Patterns (`web-backend-laravel-patterns`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Apply the project's conventions to the requested feature, keeping transport, domain invariants and persistence responsibilities clear.

Technical reference: [attributed source guide](references/web-backend-laravel-patterns/UPSTREAM.md).

### GNCore Laravel Security (`web-backend-laravel-security`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Trace request identity and ownership through policy/guard checks, test cross-user access and inspect sensitive logging and configuration.

Technical reference: [attributed source guide](references/web-backend-laravel-security/UPSTREAM.md).

### GNCore Laravel Tdd (`web-backend-laravel-tdd`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Write an observable failing request/domain regression, implement the smallest correct path and then refactor with integration evidence.

Technical reference: [attributed source guide](references/web-backend-laravel-tdd/UPSTREAM.md).

### GNCore Laravel Verification (`web-backend-laravel-verification`)

Inspect the installed laravel version and existing application conventions, especially form validation, policies, Eloquent transactions, migrations, queues and lifecycle configuration. Run relevant tests, configuration/build checks and a local request round-trip; distinguish the prepared change from a deployed service.

Technical reference: [attributed source guide](references/web-backend-laravel-verification/UPSTREAM.md).

### GNCore Supabase (`web-backend-supabase`)

Inspect project/client versions, authenticated roles, RLS, schema migrations and privileged-key boundaries. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-supabase/UPSTREAM.md).

### GNCore Redis Core (`web-backend-redis-core`)

Inspect key types, TTLs, atomic commands, cache versus durable-state ownership and unavailable-cache behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-core/UPSTREAM.md).

### GNCore Redis Connections (`web-backend-redis-connections`)

Inspect client/pool limits, timeouts, reconnect behavior, TLS and cancellation during network failure. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-connections/UPSTREAM.md).

### GNCore Redis Security (`web-backend-redis-security`)

Inspect authentication/ACL command scope, key isolation, TLS and secret-free diagnostics. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-security/UPSTREAM.md).

### GNCore Redis Observability (`web-backend-redis-observability`)

Inspect latency, hit/miss and eviction metrics with low-cardinality labels and actionable saturation signals. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-observability/UPSTREAM.md).

### GNCore Redis Search (`web-backend-redis-search`)

Inspect index schema, query escaping, update/refresh behavior and relevance against a known document fixture. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-search/UPSTREAM.md).

### GNCore Redis Semantic Cache (`web-backend-redis-semantic-cache`)

Inspect embedding/version identity, tenant isolation, freshness, similarity threshold and false-hit evaluation. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-redis-semantic-cache/UPSTREAM.md).

### GNCore Vercel Optimize (`web-backend-vercel-optimize`)

Inspect actual framework/build output, client/server boundaries, bundle costs, caching and measured page behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-vercel-optimize/UPSTREAM.md).

### GNCore Cloudflare (`web-backend-cloudflare`)

Inspect Workers runtime limits, bindings, request/response lifecycle and selected deployment configuration. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-cloudflare/UPSTREAM.md).

### GNCore Workers Best Practices (`web-backend-workers-best-practices`)

Inspect runtime compatibility, async lifetime, binding usage, caching semantics and bounded resource consumption. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-workers-best-practices/UPSTREAM.md).

### GNCore Wrangler (`web-backend-wrangler`)

Inspect installed Wrangler version, configuration schema, environment/binding names and local versus production command effects. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-wrangler/UPSTREAM.md).

### GNCore Durable Objects (`web-backend-durable-objects`)

Inspect object identity/routing, serialized state operations, storage consistency, reconnect and eviction behavior. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-durable-objects/UPSTREAM.md).

### GNCore Workers Profiling (`web-backend-workers-profiling`)

Inspect representative workload, CPU/wall-time distinction, runtime limits and before/after profile evidence. Implement or investigate only the requested platform boundary, replay relevant success/failure cases with local fixtures and verify actual version-compatible behavior. Keep configuration preparation separate from live resource creation, deployment or production traffic changes.

Technical reference: [attributed source guide](references/web-backend-workers-profiling/UPSTREAM.md).

### GNCore Backend Workflow (`web-backend`)

Trace the request through routing, validation, authentication, domain rules, persistence, background work, and observability as applicable. Select only the matching stack and the specialist skills needed for the request. Implement the scoped service behavior and verify its success, failure, and permission paths. Use existing infrastructure and interfaces unless the user requests a change.

### GNCore Backend Code Quality (`web-backend-codequality`)

Inspect a representative request or job path before refactoring. Check validation at boundaries, authorization at sensitive operations, ownership of transactions and state, cancellation and timeout behavior, and error propagation. Prefer clear interfaces and explicit invariants over generic abstraction layers. Make a focused improvement and verify relevant observable behavior; use the code quality, review, contract, or stack workflow that addresses the actual problem.

### GNCore Backend Security (`web-backend-security`)

Trace untrusted input and identity through each sensitive operation. Check object-level authorization, injection-safe queries, output handling, session and CSRF controls where relevant, and redacted failures. Reproduce concrete issues locally and verify allowed and denied cases after fixing them. Distinguish a scoped review from a claim that the whole service is secure.

### Web Development (`web-development`)

Help implement the web development task the user describes. First inspect the existing app and identify the smallest relevant change. Follow its framework, architecture, accessibility, and security conventions. State assumptions when they affect the result. Change only files needed for the requested feature; do not rewrite unrelated pages, architecture, dependencies, or configuration. Ask before broad migrations or destructive changes. Summarize changed files and any checks performed.

### SEO Audit (`seo-audit`)

Inspect rendered HTML, indexability, canonical URLs, structured data, sitemap, redirects, and page performance. Fix concrete issues in the existing framework and preserve user-facing meaning. Validate structured data syntax and avoid keyword stuffing or fabricated claims. Search rankings cannot be guaranteed; distinguish technical checks from outcome estimates.
