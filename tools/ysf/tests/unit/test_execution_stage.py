from pathlib import Path
from unittest.mock import patch

import pytest

from ysf.core.result import CommandResult
from ysf.execution.stage import (
    ExecutionStage,
    ExecutionStageConfig,
    ExecutionStageError,
)


def test_execution_stage_metadata() -> None:
    stage = ExecutionStage(
        ExecutionStageConfig(
            prompt_artifact=Path("prompt.json"),
        )
    )

    assert stage.name == "execution"
    assert stage.order == 50
    assert stage.config.provider == "codex"
    assert stage.config.dry_run is True


def test_execution_stage_rejects_apply_mode() -> None:
    with pytest.raises(
        ExecutionStageError,
        match="dry-run only",
    ):
        ExecutionStage(
            ExecutionStageConfig(
                prompt_artifact=Path("prompt.json"),
                dry_run=False,
            )
        )


def test_execution_stage_rejects_empty_provider() -> None:
    with pytest.raises(
        ExecutionStageError,
        match="provider cannot be empty",
    ):
        ExecutionStage(
            ExecutionStageConfig(
                prompt_artifact=Path("prompt.json"),
                provider="",
            )
        )


def test_execution_stage_rejects_missing_artifact(
    tmp_path: Path,
) -> None:
    stage = ExecutionStage(
        ExecutionStageConfig(
            prompt_artifact=Path(
                "factory/prompts/missing.json"
            ),
        )
    )

    with pytest.raises(
        ExecutionStageError,
        match="not found",
    ):
        stage.resolve_prompt_artifact(
            tmp_path
        )


def test_execution_stage_rejects_external_artifact(
    tmp_path: Path,
) -> None:
    repository_root = tmp_path / "repository"
    repository_root.mkdir()

    external_artifact = (
        tmp_path / "external-prompt.json"
    )
    external_artifact.write_text(
        "{}",
        encoding="utf-8",
    )

    stage = ExecutionStage(
        ExecutionStageConfig(
            prompt_artifact=external_artifact,
        )
    )

    with pytest.raises(
        ExecutionStageError,
        match="inside the repository",
    ):
        stage.resolve_prompt_artifact(
            repository_root
        )


def test_execution_stage_delegates_to_service(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        tmp_path
        / "factory/prompts/generated/"
        "s00/t00/prompt.json"
    )

    prompt_artifact.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    prompt_artifact.write_text(
        "{}",
        encoding="utf-8",
    )

    stage = ExecutionStage(
        ExecutionStageConfig(
            prompt_artifact=Path(
                "factory/prompts/generated/"
                "s00/t00/prompt.json"
            ),
            provider="codex",
            execution_id="s00-t00-stage-test",
            output_directory=Path(
                "runtime/tmp/stage-test"
            ),
        )
    )

    service_result = CommandResult(
        command="run",
        status="PASS",
        message="Dry run passed.",
        data={
            "executionId": "s00-t00-stage-test",
            "provider": "codex",
            "mode": "dry-run",
            "providerInvoked": False,
            "modifiedFileCount": 0,
        },
    )

    with patch(
        "ysf.execution.stage.run_dry_execution",
        return_value=service_result,
    ) as service_mock:
        result = stage.run(tmp_path)

    assert result.successful
    assert result.command == "execution"
    assert result.data["stageName"] == "execution"
    assert result.data["stageOrder"] == 50
    assert result.data["providerInvoked"] is False
    assert result.data["modifiedFileCount"] == 0

    service_mock.assert_called_once_with(
        repository_root=tmp_path.resolve(),
        prompt_artifact_path=(
            prompt_artifact.resolve()
        ),
        provider="codex",
        execution_id="s00-t00-stage-test",
        output_directory=Path(
            "runtime/tmp/stage-test"
        ),
        mode="dry-run",
    )
