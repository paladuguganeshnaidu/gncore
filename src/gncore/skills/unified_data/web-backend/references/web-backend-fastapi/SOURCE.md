# Source and modifications

GNCore adaptation of [fastapi/fastapi / fastapi](https://github.com/fastapi/fastapi/blob/79cab5bed28b24d92c185d236feb33f5783dfeb3/fastapi/.agents/skills/fastapi/SKILL.md).

Revision: `79cab5bed28b24d92c185d236feb33f5783dfeb3`.

Upstream metadata:

```json
{
  "name": "fastapi",
  "description": "FastAPI best practices and conventions. Use when working with FastAPI APIs, Pydantic models, dependencies, streaming responses including Server-Sent Events (SSE), and serving frontend apps. Keeps FastAPI code clean and up to date with the latest features and patterns."
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
