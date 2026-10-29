# Source and modifications

GNCore adaptation of [getsentry/plugin-codex / sentry-debug-issue](https://github.com/getsentry/plugin-codex/blob/8832fafe9b061151b80c34e7752bc3553de9f68a/plugins/sentry/skills/sentry-debug-issue/SKILL.md).

Revision: `8832fafe9b061151b80c34e7752bc3553de9f68a`.

Upstream metadata:

```json
{
  "name": "sentry-debug-issue",
  "description": "Debug and fix a Sentry issue — find it (by link, ID, or search), pull full context (stack trace, breadcrumbs, trace, logs), optionally run Seer root-cause / autofix, apply the code fix, and resolve it via a `Fixes PROJECT-NAME-12A` commit/PR. Use when working a known error or hunting one down to fix.",
  "license": "Apache-2.0"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: See retained upstream notices and metadata. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
