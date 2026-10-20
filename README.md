# GNCore

GNCore is a Python CLI and curated library for installing reusable AI agent skills into coding assistants.

Project version: 4.0.0
Package name: gncore
License: MIT

## Why it exists

AI coding assistants use different locations and formats for prompts, skills, commands and configuration. GNCore provides a common skill representation plus application adapters for installation, validation, backup, restore and updates.

## Supported assistants

The current project documentation targets VS Code Copilot, Codex, and Claude harnesses, Google Antigravity, Claude Code, Gemini CLI, and OpenAI Codex CLI. Generic adapters for Claude Desktop, Cursor, Windsurf, and Continue.dev remain available for managed bundles. Hosted ChatGPT Skills can be exported as ZIP files for upload in the ChatGPT Skills UI.

## Core commands

- gncore activate
- gncore deactivate
- gncore update
- gncore doctor
- gncore list
- gncore search
- gncore install
- gncore export
- gncore uninstall
- gncore backup
- gncore restore
- gncore validate
- gncore version

Useful first checks are gncore list apps, gncore validate --apps cursor and gncore doctor.

## Skill model

A skill can contain metadata, a description, system prompt, examples, commands, configuration, version, dependencies and permissions.

The core pipeline is:

Skill Definition → Validation / Manifest → Adapter Selection → Application Installation → Verification → Backup / Restore / Update.

The main engineering idea is adapter isolation: adding another assistant should not require rewriting the central skill model. Native skill adapters install standard `SKILL.md` folders. For example:

```bash
gncore search model training
gncore install train preprocess clean-data evaluate improve analyze --apps antigravity --scope workspace
```

Install focused workflows such as `/company-ceo`, `/train`, `/word-draft`, `/pdf-extract`, or `/ppt-create`, then describe the task. Each skill guides the assistant; it does not independently execute code. GNCore installs instructions for the assistant; it does not autonomously rewrite a project. The included skills demand evidence, scoped work, data-leakage controls, and honest reporting of checks and model results.

The catalog contains 403 skills: 103 established specialist workflows plus 30 curated domain packs with 10 focused slash-invoked workflows each. Packs cover company leadership and business functions; software, data, machine learning, cloud, security, quality, and design; Word, PDF, PowerPoint, and spreadsheets; research, education, healthcare operations, retail, communications, and supply chain. Run `gncore list domains`, `gncore list skills`, or `gncore search <terms>` to discover workflows. Every skill carries an evidence-based inspect → plan → implement → test → fix → retest → report loop with bounded stopping criteria and honest test reporting.

## Documentation

- docs/USAGE.md
- docs/ALL_SKILLS.md — all skills, use cases, slash names, and install examples
- ARCHITECTURE.md
- docs/DEVELOPER.md
- docs/API.md
- CONTRIBUTING.md
- docs/RELEASE.md
- SECURITY.md

## Project status

GNCore is a real Python package and CLI under active iteration. Adapter behavior can differ between assistant versions and operating systems, so support should always be verified with the installed build.

## License

MIT License. See LICENSE.

## Author

Paladugu Ganesh Naidu

Repository: https://github.com/paladuguganeshnaidu/gncore
