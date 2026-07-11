from __future__ import annotations

from ysf.pipeline.stage import PipelineStage


class PipelineRegistryError(RuntimeError):
    """Raised when pipeline stage registration is invalid."""


class StageRegistry:
    def __init__(self) -> None:
        self._stages: dict[str, PipelineStage] = {}

    def register(
        self,
        stage: PipelineStage,
    ) -> None:
        if not stage.name:
            raise PipelineRegistryError(
                "Pipeline stage name cannot be empty."
            )

        if stage.name in self._stages:
            raise PipelineRegistryError(
                f"Duplicate pipeline stage: {stage.name}"
            )

        self._stages[stage.name] = stage

    def stages(self) -> list[PipelineStage]:
        return sorted(
            self._stages.values(),
            key=lambda stage: (
                stage.order,
                stage.name,
            ),
        )

    def select(
        self,
        names: list[str] | None = None,
    ) -> list[PipelineStage]:
        if not names:
            return self.stages()

        missing = [
            name
            for name in names
            if name not in self._stages
        ]

        if missing:
            raise PipelineRegistryError(
                "Unknown pipeline stage(s): "
                + ", ".join(missing)
            )

        selected_names = set(names)

        return [
            stage
            for stage in self.stages()
            if stage.name in selected_names
        ]
