from pathlib import Path

from ysf.execution.stage import (
    ExecutionStage,
    ExecutionStageConfig,
)


def test_execution_stage_in_repository() -> None:
    repository_root = Path.cwd().parents[1]

    stage = ExecutionStage(
        ExecutionStageConfig(
            prompt_artifact=Path(
                "factory/prompts/generated/"
                "s00/t00/prompt.json"
            ),
            provider="codex",
            execution_id=(
                "s00-t00-stage-integration"
            ),
            output_directory=Path(
                "runtime/tmp/"
                "execution-stage-integration"
            ),
        )
    )

    result = stage.run(
        repository_root
    )

    assert result.successful
    assert result.command == "execution"
    assert result.data["providerInvoked"] is False
    assert result.data["modifiedFileCount"] == 0
    assert result.data["stageOrder"] == 50

    report_path = (
        repository_root
        / result.data["reportJson"]
    )

    assert report_path.is_file()
