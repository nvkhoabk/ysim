from __future__ import annotations

from ysf.execution.models import ExecutionPlan, ExecutionRequest, ExecutionResult

from .base import ExecutionProvider


class CodexProvider(
    ExecutionProvider,
):
    """
    Stub implementation.

    Real execution
    will be implemented
    in Step 14E.
    """

    name = "codex"

    version = "0.1"

    def validate(
        self,
    ) -> None:
        return

    def plan(
        self,
        request: ExecutionRequest,
    ) -> ExecutionPlan:
        raise NotImplementedError

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionResult:
        raise NotImplementedError
