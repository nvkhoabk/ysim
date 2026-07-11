from __future__ import annotations

from pathlib import Path
from time import perf_counter

from ysf.pipeline.models import (
    PipelineResult,
    StageResult,
)
from ysf.pipeline.registry import StageRegistry


class PipelineEngine:
    def __init__(
        self,
        registry: StageRegistry,
    ) -> None:
        self._registry = registry

    def run(
        self,
        repository_root: Path,
        stage_names: list[str] | None = None,
        fail_fast: bool = True,
    ) -> PipelineResult:
        pipeline_started = perf_counter()
        stage_results: list[StageResult] = []

        for stage in self._registry.select(stage_names):
            stage_started = perf_counter()

            try:
                command_result = stage.run(
                    repository_root
                )

                stage_result = StageResult(
                    name=stage.name,
                    order=stage.order,
                    status=command_result.status,
                    duration_seconds=round(
                        perf_counter() - stage_started,
                        6,
                    ),
                    message=command_result.message,
                    data=command_result.data,
                )
            except Exception as exc:
                stage_result = StageResult(
                    name=stage.name,
                    order=stage.order,
                    status="FAIL",
                    duration_seconds=round(
                        perf_counter() - stage_started,
                        6,
                    ),
                    message=str(exc),
                    data={
                        "exceptionType": (
                            type(exc).__name__
                        ),
                    },
                )

            stage_results.append(stage_result)

            if (
                fail_fast
                and not stage_result.successful
            ):
                break

        status = (
            "PASS"
            if all(
                result.successful
                for result in stage_results
            )
            else "FAIL"
        )

        return PipelineResult(
            name="default",
            status=status,
            duration_seconds=round(
                perf_counter() - pipeline_started,
                6,
            ),
            stages=stage_results,
        )
