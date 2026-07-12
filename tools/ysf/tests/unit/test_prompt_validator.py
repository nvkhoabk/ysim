import pytest

from ysf.prompt.validator import (
    PromptValidationError,
    validate_prompt,
)


def test_rejects_incomplete_prompt() -> None:
    with pytest.raises(
        PromptValidationError
    ):
        validate_prompt(
            "# ROLE\n\nIncomplete"
        )
