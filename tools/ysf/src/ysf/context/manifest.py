from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class ContextManifestError(RuntimeError):
    """Raised when a context manifest is invalid."""


def load_context_manifest(
    path: Path,
) -> dict[str, Any]:
    if not path.is_file():
        raise ContextManifestError(
            f"Context manifest not found: {path}"
        )

    try:
        data = yaml.safe_load(
            path.read_text(encoding="utf-8-sig")
        )
    except yaml.YAMLError as exc:
        raise ContextManifestError(
            f"Invalid YAML in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise ContextManifestError(
            f"Expected YAML object in {path}"
        )

    required_fields = (
        "context_id",
        "documents",
        "limits",
        "output",
    )

    missing = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing:
        raise ContextManifestError(
            "Missing context manifest fields: "
            + ", ".join(missing)
        )

    return data
