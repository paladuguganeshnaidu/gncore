# Source and modifications

GNCore adaptation of [redis/agent-skills / redis-security](https://github.com/redis/agent-skills/blob/a84871d065f398fed55e1633f66b66f731eb4e2b/skills/redis-security/SKILL.md).

Revision: `a84871d065f398fed55e1633f66b66f731eb4e2b`.

Upstream metadata:

```json
{
  "name": "redis-security",
  "description": "Redis security guidance covering authentication (requirepass and ACL users), TLS, ACL-based least-privilege access control, restricting network exposure via bind and protected-mode, firewall rules, and disabling dangerous commands. Use when deploying Redis to production, defining ACL users for an application, configuring TLS connections, locking down a Redis instance behind a firewall, or auditing a Redis deployment for security hardening.",
  "license": "MIT",
  "metadata": {
    "author": "Redis, Inc.",
    "version": "0.1.0"
  }
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
