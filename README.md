# GNCore

GNCore is a Python CLI for installing and managing reusable AI skills across coding assistants.

Project version: 3.0.0
Package name: gncore
License: MIT

## Why it exists

AI coding assistants use different locations and formats for prompts, skills, commands and configuration. GNCore provides a common skill representation plus application adapters for installation, validation, backup, restore and updates.

## Supported assistants

The current project documentation targets VS Code Chat, GitHub Copilot Chat, Claude Desktop, Claude Code, Cursor, Windsurf, Continue.dev, Gemini CLI and OpenAI Codex CLI.

## Core commands

- gncore activate
- gncore deactivate
- gncore update
- gncore doctor
- gncore list
- gncore install
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

The main engineering idea is adapter isolation: adding another assistant should not require rewriting the central skill model.

## Documentation

- docs/USAGE.md
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
