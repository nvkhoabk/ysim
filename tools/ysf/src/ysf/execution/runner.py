from __future__ import annotations

from time import perf_counter

from ysf.execution.models import (
    ExecutionPlan,
    ExecutionRequest,
    ExecutionResult,
)
from ysf.execution.providers.registry import ProviderRegistry


class ExecutionRunnerError(RuntimeError):
    """Raised when an execution cannot be run safely."""


def run_execution(
    request: ExecutionRequest,
    plan: ExecutionPlan,
    provider_registry: ProviderRegistry,
) -> ExecutionResult:
    if request.execution_id != plan.execution_id:
        raise ExecutionRunnerError(
            "Execution request and plan IDs do not match."
        )

    if request.provider != plan.provider:
        raise ExecutionRunnerError(
            "Execution request and plan providers do not match."
        )

    if request.mode != plan.mode:
        raise ExecutionRunnerError(
            "Execution request and plan modes do not match."
        )

    if not plan.dry_run:
        raise ExecutionRunnerError(
            "Apply execution is disabled in Step 14E."
        )

    provider = provider_registry.get(
        plan.provider
    )

    provider.validate()

    started = perf_counter()

    result = provider.execute(plan)

    duration = round(
        perf_counter() - started,
        6,
    )

    return ExecutionResult(
        execution_id=result.execution_id,
        status=result.status,
        provider=result.provider,
        mode=result.mode,
        started_at=result.started_at,
        finished_at=result.finished_at,
        duration_seconds=duration,
        message=result.message,
        exit_code=result.exit_code,
        stdout=result.stdout,
        stderr=result.stderr,
        modified_files=result.modified_files,
        artifacts=result.artifacts,
        metadata=result.metadata,
    )
