# Verified-mode E2E (scaffold)

This document explains how to run GNCore in Verified-mode end-to-end. Verified-mode is intended for controlled environments or CI where real provider credentials are available.

Providers and token environment variables
- OpenAI API: provider name `openai-api`, env var `OPENAI_API_KEY`
- OpenRouter: provider name `openrouter`, env var `OPENROUTER_API_KEY`
- Anthropic: provider name `anthropic-api`, env var `ANTHROPIC_API_KEY`
- Google Gemini: provider name `gemini-api`, env var `GEMINI_API_KEY`
- Ollama (local): provider name `ollama`, env var `OLLAMA_API_KEY` (optional for local socket)

Quick start (developer machine)
1. Install dependencies and activate your virtualenv (see `test-env` usage in this repo).
2. Ensure `git` is available on PATH.
3. Initialize a GNCore project (if not already):
```bash
python -m gncore.cli init --project .
```
4. Run the Verified-mode script with your provider and token:
```bash
python scripts/verified_mode_run.py --project . --provider openai-api --token-file /path/to/openai.token
```

CI usage
- Store provider tokens as repository secrets and write them to a file or pass via environment variable to the runner.
- Use the runner as part of a workflow step and fail the job if the runner exits non-zero.

Security notes
- Prefer storing credentials in the platform keyring via `gncore auth set <provider> <token>` or via your CI secret mechanism. The runner will call `GncoreRuntime.auth_set` to persist keys into the configured credential store.
- Avoid hardcoding tokens into scripts or source control.
