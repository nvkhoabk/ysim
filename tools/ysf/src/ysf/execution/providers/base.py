from __future__ import annotations

from abc import ABC, abstractmethod

from ysf.execution.models import ExecutionPlan, ExecutionRequest, ExecutionResult


class ExecutionProvider(ABC):

    name: str

    version: str = "1.0"

    @abstractmethod
    def validate(self) -> None:
        """
        Validate provider environment.
        """

    @abstractmethod
    def plan(
        self,
        request: ExecutionRequest,
    ) -> ExecutionPlan:
        """
        Convert request to execution plan.
        """

    @abstractmethod
    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionResult:
        """
        Execute plan.
        """
