# Source and modifications

GNCore adaptation of [trailofbits/skills / codeql](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/static-analysis/skills/codeql/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "codeql",
  "description": "Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking analysis. Triggers on \"run codeql\", \"codeql scan\", \"build codeql database\", \"SAST scan\", \"taint analysis\", \"dataflow analysis\", or \"find vulnerabilities in this repo\". Covers Python, JavaScript/TypeScript, Go, Java/Kotlin, C/C++, C#, Ruby, and Swift. Supports \"run all\" (security-and-quality + security-experimental) and \"important only\" (high-precision) scan modes, and creates data extension models for project-specific sources and sinks. For fast single-file pattern matching, or when no build is available for a compiled language, use the semgrep skill; to parse SARIF that already exists rather than produce it, use the sarif-parsing skill.",
  "allowed-tools": "Bash Read Write Edit Glob Grep AskUserQuestion TaskCreate TaskList TaskUpdate TaskGet"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
