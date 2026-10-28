# Source and modifications

GNCore adaptation of [trailofbits/skills / semgrep](https://github.com/trailofbits/skills/blob/bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3/plugins/static-analysis/skills/semgrep/SKILL.md).

Revision: `bf23bfb21f10a2a4b0406086d690dc8cb1b3ccf3`.

Upstream metadata:

```json
{
  "name": "semgrep",
  "description": "Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for explicit approval, then runs every approved ruleset through scripts/run-scans.sh, which batches the semgrep processes and writes scans.json, and merges the output to SARIF. Supports two scan modes, \"run all\" for full ruleset coverage and \"important only\" for security findings at medium-to-high confidence and impact. Uses Semgrep Pro for cross-file taint analysis when it is available. Use when asked to scan code for vulnerabilities, run a security audit with Semgrep, find bugs, or perform static analysis. For the same scan without the approval gate, use the /static-analysis:semgrep-scan workflow.",
  "allowed-tools": "Bash Read Glob AskUserQuestion TaskCreate TaskList TaskUpdate"
}
```

Modifications: GNCore name and focused entrypoint, progressive reference loading, portable path guidance, and host-neutral execution scope. The source entrypoint is retained as `UPSTREAM.md`; nested source entrypoints use the same reference filename to avoid installing unintended skills. Explicitly linked sibling resources are retained under `upstream-support/` and mapped in `RESOURCE_PATHS.json` when needed.

Upstream notice origins: LICENSE. Notices are retained in `notices/` and in their original locations inside copied skill folders where supplied. Frontmatter declarations can differ from repository-level notices; both are retained.

Attribution and license: CC-BY-SA-4.0. Original authors retain authorship of their contributions. Trail of Bits adaptations, including the GNCore entrypoint, are distributed under CC BY-SA 4.0, with attribution and modification disclosure; GNCore's MIT code license does not relicense these materials.
