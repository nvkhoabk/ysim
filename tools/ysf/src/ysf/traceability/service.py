"""Command service for V3-R1 traceability validation and queries."""

from __future__ import annotations

from pathlib import Path

from ysf.core.result import CommandResult
from ysf.traceability.validator import validate_traceability_baseline


def run_traceability_validation(
    repository_root: Path,
    registry_path: Path | None = None,
    *,
    facet: str | None = None,
) -> CommandResult:
    summary = validate_traceability_baseline(
        repository_root, registry_path=registry_path, facet=facet
    )
    return CommandResult(
        command="traceability",
        status="PASS",
        message="V3-R1 corpus and traceability baseline is internally consistent.",
        data=summary,
    )
