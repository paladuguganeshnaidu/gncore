# Source and modifications

GNCore adaptation of [redis/agent-skills / redis-connections](https://github.com/redis/agent-skills/blob/a84871d065f398fed55e1633f66b66f731eb4e2b/skills/redis-connections/SKILL.md).

Revision: `a84871d065f398fed55e1633f66b66f731eb4e2b`.

Upstream metadata:

```json
{
  "name": "redis-connections",
  "description": "Redis client and connection guidance covering connection pooling, multiplexing, pipelining, client-side caching with RESP3, avoiding slow commands (KEYS, SMEMBERS, HGETALL), and tuning socket timeouts. Use when configuring a Redis client (redis-py, Jedis, Lettuce, NRedisStack), batching commands for throughput, eliminating per-request connection creation, iterating large keyspaces with SCAN, enabling client-side caching for read-heavy workloads, or setting connect and read timeouts.",
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
