# Security Policy

GNCore is an offline skill catalog and explicit ZIP exporter. It does not make network requests, execute skill prompts, or scan or modify AI application directories.

## Reporting a vulnerability

Use a private security disclosure channel for issues that could affect users. Include the affected version, command or API, operating system, reproduction steps, and any relevant output. Do not include credentials or personal data.

## Security expectations

- Catalog commands read bundled skill definitions only.
- Export writes only to the caller-selected ZIP path and includes catalog text files.
- Skill content must not contain secrets, credentials, deceptive claims, or unsafe instructions.
- Skill text is guidance for the host assistant; it does not grant permissions or guarantee that actions are safe.
