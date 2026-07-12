from __future__ import annotations


class PromptValidationError(RuntimeError):
    """Raised when a generated prompt is incomplete."""


REQUIRED_SECTIONS = (
    "# ROLE",
    "# EXECUTION ID",
    "# OBJECTIVE",
    "# REPOSITORY SNAPSHOT",
    "# SOURCE DOCUMENTS",
    "# CONTEXT",
    "# ALLOWED PATHS",
    "# PROTECTED PATHS",
    "# IMPLEMENTATION RULES",
    "# VALIDATION COMMANDS",
    "# REQUIRED OUTPUTS",
    "# COMPLETION CONDITIONS",
    "# STOP CONDITIONS",
)


def validate_prompt(
    content: str,
) -> None:
    missing = [
        section
        for section in REQUIRED_SECTIONS
        if section not in content
    ]

    if missing:
        raise PromptValidationError(
            "Missing prompt sections: "
            + ", ".join(missing)
        )

    if "{{" in content or "}}" in content:
        raise PromptValidationError(
            "Prompt contains unresolved placeholders."
        )

    if len(content.strip()) < 500:
        raise PromptValidationError(
            "Generated prompt is unexpectedly short."
        )
