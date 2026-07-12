from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ysf.core.result import CommandResult
from ysf.execution.service import run_dry_execution
from ysf.pipeline.stage import PipelineStage


class ExecutionStageError(RuntimeError):
    """Raised when the Execution Pipeline Stage is misconfigured."""


@dataclass(frozen=True)
class ExecutionStageConfig:
    """Configuration used by the dry-run Execution Pipeline Stage."""

    prompt_artifact: Path
    provider: str = "codex"
    execution_id: str | None = None
    output_directory: Path | None = None
    dry_run: bool = True

    def validate(self) -> None:
        if not str(self.prompt_artifact).strip():
            raise ExecutionStageError(
                "Execution stage prompt artifact cannot be empty."
            )

        if not self.provider.strip():
            raise ExecutionStageError(
                "Execution stage provider cannot be empty."
            )

        if not self.dry_run:
            raise ExecutionStageError(
                "Execution Stage supports dry-run only in YSF v0.1.0."
            )


class ExecutionStage(PipelineStage):
    """Pipeline adapter for the YSF dry-run Execution Service.

    This class contains no provider-specific execution logic. It only
    translates Pipeline execution into an Execution Service call.
    """

    name = "execution"
    order = 50

    def __init__(
        self,
        config: ExecutionStageConfig,
    ) -> None:
        config.validate()
        self._config = config

    @property
    def config(self) -> ExecutionStageConfig:
        return self._config

    def resolve_prompt_artifact(
        self,
        repository_root: Path,
    ) -> Path:
        path = self._config.prompt_artifact

        if not path.is_absolute():
            path = repository_root / path

        resolved_path = path.resolve()

        if not resolved_path.is_file():
            raise ExecutionStageError(
                "Execution stage prompt artifact not found: "
                f"{resolved_path}"
            )

        try:
            resolved_path.relative_to(
                repository_root.resolve()
            )
        except ValueError as exc:
            raise ExecutionStageError(
                "Execution stage prompt artifact must be "
                "inside the repository."
            ) from exc

        return resolved_path

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        resolved_root = repository_root.resolve()

        prompt_artifact = self.resolve_prompt_artifact(
            resolved_root
        )

        result = run_dry_execution(
            repository_root=resolved_root,
            prompt_artifact_path=prompt_artifact,
            provider=self._config.provider,
            execution_id=self._config.execution_id,
            output_directory=self._config.output_directory,
            mode="dry-run",
        )

        if not result.successful:
            return result

        return CommandResult(
            command=self.name,
            status="PASS",
            message=(
                "Execution pipeline stage completed in dry-run mode."
            ),
            data={
                **result.data,
                "stageName": self.name,
                "stageOrder": self.order,
            },
        )
