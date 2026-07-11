from pathlib import Path

from ysf.core.result import CommandResult
from ysf.pipeline.engine import PipelineEngine
from ysf.pipeline.registry import StageRegistry
from ysf.pipeline.stage import PipelineStage


class PassingStage(PipelineStage):
    name = "passing"
    order = 10

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return CommandResult(
            command="passing",
            status="PASS",
            message="Passed.",
        )


class FailingStage(PipelineStage):
    name = "failing"
    order = 20

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        raise RuntimeError(
            "Expected test failure."
        )


def test_pipeline_passes(
    tmp_path: Path,
) -> None:
    registry = StageRegistry()
    registry.register(PassingStage())

    result = PipelineEngine(
        registry
    ).run(tmp_path)

    assert result.successful
    assert len(result.stages) == 1


def test_pipeline_fails_fast(
    tmp_path: Path,
) -> None:
    registry = StageRegistry()

    registry.register(PassingStage())
    registry.register(FailingStage())

    result = PipelineEngine(
        registry
    ).run(tmp_path)

    assert not result.successful

    # Passing chạy trước, Failing chạy sau
    assert len(result.stages) == 2

    assert result.stages[0].name == "passing"
    assert result.stages[0].successful

    assert result.stages[1].name == "failing"
    assert not result.stages[1].successful
   