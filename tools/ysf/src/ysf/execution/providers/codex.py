from __future__ import annotations

from datetime import datetime

from ysf.execution.models import (
    ExecutionArtifact,
    ExecutionPlan,
    ExecutionRequest,
    ExecutionResult,
)
from ysf.execution.providers.base import ExecutionProvider
from ysf.execution.providers.exceptions import (
    ProviderValidationError,
)


class CodexProvider(ExecutionProvider):
    """Codex execution provider.

    Step 14E supports dry-run only. Real Codex CLI execution will be
    implemented in a later step.
    """

    name = "codex"
    version = "0.2"

    def validate(self) -> None:
        """Validate the provider configuration.

        Codex CLI is intentionally not required for dry-run mode.
        """
        return

    def plan(
        self,
        request: ExecutionRequest,
    ) -> ExecutionPlan:
        raise NotImplementedError(
            "Planning is handled by the YSF Execution Planner."
        )

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionResult:
        if not plan.dry_run:
            raise ProviderValidationError(
                "Codex apply execution is disabled in Step 14E."
            )

        started_at = (
            datetime.now()
            .astimezone()
            .isoformat()
        )

        finished_at = (
            datetime.now()
            .astimezone()
            .isoformat()
        )

        return ExecutionResult(
            execution_id=plan.execution_id,
            status="PASS",
            provider=self.name,
            mode=plan.mode,
            started_at=started_at,
            finished_at=finished_at,
            duration_seconds=0.0,
            message=(
                "Codex dry-run completed. "
                "No provider process was started."
            ),
            exit_code=0,
            stdout=(
                "DRY RUN\n"
                "Provider: codex\n"
                f"Prompt: {plan.prompt_path}\n"
                "No files were modified.\n"
            ),
            stderr="",
            modified_files=[],
            artifacts=[
                ExecutionArtifact(
                    artifact_type="execution-plan",
                    path="plan.json",
                    description=(
                        "Validated dry-run execution plan."
                    ),
                )
            ],
            metadata={
                "providerVersion": self.version,
                "providerInvoked": False,
                "dryRun": True,
            },
        )
