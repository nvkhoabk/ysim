from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


class PromptManifestError(RuntimeError):
    """Raised when a prompt manifest is missing or invalid."""


def load_prompt_manifest(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise PromptManifestError(
            f"Prompt manifest not found: {path}"
        )

    try:
        data = yaml.safe_load(
            path.read_text(encoding="utf-8-sig")
        )
    except yaml.YAMLError as exc:
        raise PromptManifestError(
            f"Invalid YAML in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise PromptManifestError(
            f"Expected YAML object in {path}"
        )

    required_sections = (
        "prompt",
        "objective",
        "context",
        "constraints",
        "validation",
        "completion",
        "output",
    )

    missing = [
        section
        for section in required_sections
        if section not in data
    ]

    if missing:
        raise PromptManifestError(
            "Missing prompt manifest sections: "
            + ", ".join(missing)
        )

    prompt = data.get("prompt")

    if not isinstance(prompt, dict):
        raise PromptManifestError(
            "prompt must be a mapping"
        )

    required_prompt_fields = (
        "id",
        "sprint",
        "task",
        "provider",
        "template",
    )

    missing_prompt_fields = [
        field
        for field in required_prompt_fields
        if not prompt.get(field)
    ]

    if missing_prompt_fields:
        raise PromptManifestError(
            "Missing prompt fields: "
            + ", ".join(missing_prompt_fields)
        )

    return data
