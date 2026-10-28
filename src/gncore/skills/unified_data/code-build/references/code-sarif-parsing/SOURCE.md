# Source and modifications

GNCore adaptation of [trailofbits/skills / sarif-parsing](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/static-analysis/skills/sarif-parsing/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "sarif-parsing",
  "description": "Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners. Triggers on \"parse sarif\", \"read scan results\", \"aggregate findings\", \"deduplicate alerts\", or \"process sarif output\". Handles filtering, deduplication, format conversion, and CI/CD integration of SARIF data. Does NOT run scans — use the Semgrep or CodeQL skills for that.",
  "allowed-tools": "Bash Read Glob Grep"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
