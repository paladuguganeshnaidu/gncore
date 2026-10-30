# GNCore Developer Tools: focused procedures

Read the selected section and relevant linked source only. These are workflows within this skill; imported scripts remain inert until deliberately selected for an authorized task.

### CLI Engineering (`cli-design`)

Inspect established command patterns and automation needs. Use explicit options, stable exit codes, actionable errors, and non-interactive behavior for scripts. Make destructive actions opt-in and support dry-run when useful. Keep stdout machine-readable when promised and send diagnostics to stderr. Test help, invalid input, and representative success/failure cases.

### Reproducible developer environments (`tooling-reproducible-env`)

Inspect existing lockfiles, compiler/runtime versions and setup scripts. Pin the reproducibility boundary without adding an unrelated toolchain; verify a clean setup and document platform-specific requirements, cache assumptions and offline limits.
