from pathlib import Path

from ysf.core.result import CommandResult
from ysf.pipeline.registry import StageRegistry
from ysf.pipeline.stage import PipelineStage


class LateStage(PipelineStage):
    name = "late"
    order = 20

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return CommandResult(
            command="late",
            status="PASS",
            message="Late stage passed.",
        )


class EarlyStage(PipelineStage):
    name = "early"
    order = 10

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return CommandResult(
            command="early",
            status="PASS",
            message="Early stage passed.",
        )


def test_registry_sorts_stages() -> None:
    registry = StageRegistry()
    registry.register(LateStage())
    registry.register(EarlyStage())

    names = [
        stage.name
        for stage in registry.stages()
    ]

    assert names == ["early", "late"]
