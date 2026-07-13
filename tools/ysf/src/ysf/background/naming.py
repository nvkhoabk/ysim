from __future__ import annotations

import re

QUEUE_PART_PATTERN = re.compile(
    r"^[a-z][a-z0-9-]*$"
)


class QueueNamingError(ValueError):
    """Raised when a queue name violates YSF naming rules."""


def _validate_part(
    label: str,
    value: str,
) -> None:
    if not QUEUE_PART_PATTERN.fullmatch(value):
        msg = (
            f"{label} must be lowercase kebab-case "
            "and start with a letter"
        )
        raise QueueNamingError(msg)


def queue_name(
    capability: str,
    purpose: str,
    environment: str = "local",
) -> str:
    _validate_part("capability", capability)
    _validate_part("purpose", purpose)
    _validate_part("environment", environment)

    return (
        "ysim"
        f":{environment}"
        f":{capability}"
        f":{purpose}"
    )
