from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ysf.core.result import CommandResult
from ysf.execution.models import ExecutionMode
from ysf.execution.planner import plan_execution
from ysf.execution.providers.defaults import (
    create_default_provider_registry,
)
from ysf.execution.report import (
    write_execution_report,
)
from ysf.execution.runner import run_execution


class ExecutionServiceError(RuntimeError):
    """Raised when execution orchestration fails."""


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ExecutionServiceError(
            f"Required JSON file not found: {path}"
        )

    try:
        payload = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise ExecutionServiceError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(payload, dict):
        raise ExecutionServiceError(
            f"Expected JSON object in {path}"
        )

    return payload


def run_dry_execution(
    repository_root: Path,
    prompt_artifact_path: Path,
    provider: str | None = None,
    execution_id: str | None = None,
    output_directory: Path | None = None,
    mode: ExecutionMode = "dry-run",
) -> CommandResult:
    if mode != "dry-run":
        raise ExecutionServiceError(
            "Only dry-run mode is supported in Step 14E."
        )

    request, plan, plan_path = plan_execution(
        repository_root=repository_root,
        prompt_artifact_path=(
            prompt_artifact_path
        ),
        execution_id=execution_id,
        provider=provider,
        mode=mode,
    )

    registry = create_default_provider_registry()

    result = run_execution(
        request=request,
        plan=plan,
        provider_registry=registry,
    )

    resolved_output = (
        output_directory
        or Path(
            "factory/executions"
        )
        / request.sprint.lower()
        / request.task.lower()
    )

    report_json, report_markdown = (
        write_execution_report(
            repository_root=repository_root,
            request=request,
            plan=plan,
            result=result,
            output_directory=resolved_output,
        )
    )

    return CommandResult(
        command="run",
        status=result.status,
        message=result.message,
        data={
            "executionId": result.execution_id,
            "provider": result.provider,
            "mode": result.mode,
            "dryRun": result.dry_run,
            "providerInvoked": result.metadata.get(
                "providerInvoked",
                False,
            ),
            "modifiedFileCount": len(
                result.modified_files
            ),
            "modifiedFiles": (
                result.modified_files
            ),
            "planFile": plan_path.relative_to(
                repository_root
            ).as_posix(),
            "reportJson": report_json.relative_to(
                repository_root
            ).as_posix(),
            "reportMarkdown": (
                report_markdown.relative_to(
                    repository_root
                ).as_posix()
            ),
        },
    )
