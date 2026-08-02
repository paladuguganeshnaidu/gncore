"""Secure credential storage helpers for GNCore."""

from __future__ import annotations

from dataclasses import dataclass
import os

try:
    import keyring
except Exception:  # pragma: no cover - dependency import guard
    keyring = None


class CredentialError(RuntimeError):
    """Raised when a provider credential cannot be stored or retrieved."""


@dataclass(frozen=True, slots=True)
class CredentialRecord:
    """A provider credential reference."""

    provider_name: str
    secret_name: str


class CredentialStore:
    """Store provider secrets in the platform credential store when available."""

    def __init__(self, service_name: str = "gncore") -> None:
        self.service_name = service_name

    def save(self, provider_name: str, secret: str, secret_name: str = "token") -> None:
        if keyring is None:
            raise CredentialError("keyring is unavailable; cannot store secrets securely on this system")
        keyring.set_password(self.service_name, self._account(provider_name, secret_name), secret)

    def get(self, provider_name: str, secret_name: str = "token") -> str | None:
        if keyring is not None:
            value = keyring.get_password(self.service_name, self._account(provider_name, secret_name))
            if value:
                return value
        env_name = self.env_name(provider_name, secret_name)
        return os.environ.get(env_name)

    def delete(self, provider_name: str, secret_name: str = "token") -> None:
        if keyring is None:
            return
        try:
            keyring.delete_password(self.service_name, self._account(provider_name, secret_name))
        except keyring.errors.PasswordDeleteError:
            return

    @staticmethod
    def env_name(provider_name: str, secret_name: str = "token") -> str:
        normalized = provider_name.upper().replace("-", "_").replace(" ", "_")
        return f"GNCORE_{normalized}_{secret_name.upper()}"

    @staticmethod
    def _account(provider_name: str, secret_name: str) -> str:
        return f"{provider_name}:{secret_name}"
