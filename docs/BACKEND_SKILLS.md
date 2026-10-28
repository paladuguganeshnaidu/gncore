# Adaptive backend and coding skills

The earlier 127 backend and general coding workflows now form two primary entrypoints:

- `web-backend`: 61 service, architecture, API, persistence, stack, platform, delivery, security, and observability workflows.
- `code-build`: 66 language-independent requirements, design, implementation, debugging, review, testing, investigation, and verification workflows.

```bash
gncore export --skills web-backend code-build
```

```text
$web-backend Implement a booking API using this project's existing stack.
$code-build Investigate the failing tests, fix the cause, and verify the regression.
```

Each primary `SKILL.md` selects the relevant work from the request and contains its focused workflow procedures. It does not require executing all installed workflows or changing the chosen stack. Source guides, rules, helper scripts, and notices are supporting resources loaded only for a relevant task.

Earlier names such as `web-backend-codequality`, `web-backend-fastapi`, `code-quality`, and `code-debugging` remain CLI/API aliases. A fresh installation exposes the two category names for host-agent invocation.

Some source procedures depend on scanners, browser runtimes, platform CLIs, authenticated services, or a particular host capability. Exporting a skill does not install those dependencies or authorize external actions. The host should use an equivalent available capability when it preserves the task and report real limitations otherwise.

Attribution and applicable MIT, Apache, Creative Commons, and share-alike terms remain intact. See [Ownership](OWNERSHIP.md), [Migration](../MIGRATION.md), and [Catalog](ALL_SKILLS.md).
