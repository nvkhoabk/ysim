from __future__ import annotations

import re
from pathlib import Path
from typing import Any


class PromptRenderError(RuntimeError):
    """Raised when prompt rendering fails."""


PLACEHOLDER_PATTERN = re.compile(
    r"\{\{\s*([a-zA-Z0-9_]+)\s*\}\}"
)


def format_list(
    values: list[str],
) -> str:
    if not values:
        return "- None"

    return "\n".join(
        f"- {value}"
        for value in values
    )


def render_template(
    template_path: Path,
    values: dict[str, Any],
) -> str:
    if not template_path.is_file():
        raise PromptRenderError(
            f"Prompt template not found: {template_path}"
        )

    template = template_path.read_text(
        encoding="utf-8-sig"
    )

    missing: set[str] = set()

    def replace(
        match: re.Match[str],
    ) -> str:
        key = match.group(1)

        if key not in values:
            missing.add(key)
            return match.group(0)

        value = values[key]

        if isinstance(value, list):
            return format_list(
                [str(item) for item in value]
            )

        return str(value)

    rendered = PLACEHOLDER_PATTERN.sub(
        replace,
        template,
    )

    if missing:
        raise PromptRenderError(
            "Missing template values: "
            + ", ".join(sorted(missing))
        )

    remaining = PLACEHOLDER_PATTERN.findall(
        rendered
    )

    if remaining:
        raise PromptRenderError(
            "Unresolved template placeholders: "
            + ", ".join(sorted(set(remaining)))
        )

    return rendered.rstrip() + "\n"
