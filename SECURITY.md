# Security Policy

GNCore writes files into application config directories and workspace locations. Report issues that could lead to unsafe path handling, unexpected overwrites, secret leakage, or permission escalation.

## Reporting a vulnerability

Use a private security disclosure channel for anything that could affect end users or their local files. Include:

- affected command
- operating system
- application target
- exact file path involved
- reproduction steps

## Security expectations

- All file writes must go through validated paths.
- Backup and restore must preserve application boundaries.
- Validators must fail closed when manifests are missing or inconsistent.
- No bundled skill may contain secrets or credentials.
