"""Verified-mode E2E runner for GNCore projects.

This script scaffolds a verified execution run that requires explicit
provider credentials. It is intended to be run in a CI or a controlled
developer environment where real API keys are available.

Usage examples:
  python scripts/verified_mode_run.py --project . --provider openai-api --token ENV
  python scripts/verified_mode_run.py --project ./my-site --provider anthropic-api --token-file /secrets/anthropic.token

The script will persist provided tokens via the `GncoreRuntime.auth_set`
API (which uses the system keyring) or by setting the provider's token
environment variable when `--token-env` is used.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from gncore.runtime import GncoreRuntime, ProjectValidationError


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run GNCore in Verified E2E mode")
    p.add_argument("--project", default=".", help="Project directory (default: current directory)")
    p.add_argument("--provider", required=True, help="Provider name (e.g. openai-api, anthropic-api, openrouter, gemini-api, ollama)")
    p.add_argument("--token", help="Provider token value (will be stored in keyring)")
    p.add_argument("--token-env", help="Set provider token as an environment variable name (e.g. OPENAI_API_KEY)")
    p.add_argument("--token-file", help="Read token from a file and store it")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    project_dir = Path(args.project).resolve()
    runtime = GncoreRuntime()

    # Load or initialize project state
    if not (project_dir / ".gncore").exists():
        print(f"Initializing GNCore project in {project_dir}")
        runtime.init(project_dir)

    # Set provider and credentials
    provider_name = args.provider
    token_value = None
    if args.token_file:
        token_value = Path(args.token_file).read_text(encoding="utf-8").strip()
    elif args.token:
        token_value = args.token.strip()

    if token_value:
        print(f"Storing token for provider {provider_name} using runtime.auth_set")
        runtime.auth_set(provider_name, token_value)
    elif args.token_env:
        print(f"Setting environment variable {args.token_env} for provider {provider_name}")
        os.environ[args.token_env] = os.environ.get(args.token_env, "")

    # Select provider in project config
    try:
        print(f"Selecting provider {provider_name} for project {project_dir}")
        runtime.provider_select(project_dir, provider_name)
    except Exception as exc:
        print(f"Failed to select provider: {exc}")
        return 2

    # Run GNCore in verified mode (will raise ProjectValidationError on issues)
    try:
        print("Starting verified E2E run...")
        results = runtime.run(project_dir)
    except ProjectValidationError as exc:
        print(f"Project validation failed: {exc}")
        return 3
    except Exception as exc:
        print(f"Run failed: {exc}")
        return 4

    # Summarize results
    for r in results:
        print(f"stage={r.stage} provider={r.provider} output={r.output_file} success={r.success} duration={r.duration:.2f}s")
    print("Verified E2E run completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
