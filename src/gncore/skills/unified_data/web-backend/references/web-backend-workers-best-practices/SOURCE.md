# Source and modifications

GNCore adaptation of [cloudflare/skills / workers-best-practices](https://github.com/cloudflare/skills/blob/49a31e0b3229ccdffe4944be9c61bc7481d1d432/skills/workers-best-practices/SKILL.md).

Revision: `49a31e0b3229ccdffe4944be9c61bc7481d1d432`.

Upstream metadata:

```json
{
  "name": "workers-best-practices",
  "description": "Cloudflare Workers best practices for production applications. Use when writing, reviewing, or configuring Workers."
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
