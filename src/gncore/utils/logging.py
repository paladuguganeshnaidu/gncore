"""Logging configuration for GNCore project runs."""

from __future__ import annotations

import logging
from pathlib import Path


class LoggerFactory:
    """Create configured loggers for project-scoped logs."""

    def create(self, log_dir: Path, name: str = "gncore") -> logging.Logger:
        """Return a logger writing to .gncore/logs/gncore.log."""
        log_dir.mkdir(parents=True, exist_ok=True)
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        handler = logging.FileHandler(log_dir / "gncore.log", encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger.addHandler(handler)
        logger.propagate = False
        return logger
