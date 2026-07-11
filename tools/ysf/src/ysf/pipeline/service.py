from __future__ import annotations

from pathlib import Path

from ysf.core.result import CommandResult
from ysf.pipeline.engine import (
    PipelineEngine,
)
from ysf.pipeline.registry import (
    StageRegistry,
)
from ysf.pipeline.stages import (
    ContextStage,
    IndexStage,
    KnowledgeStage,
)


def create_default_registry(
    repository_root: Path,
    context_manifest: Path | None = None,
) -> StageRegistry:
    registry = StageRegistry()

    registry.register(IndexStage())
    registry.register(KnowledgeStage())

    manifest = (
        context_manifest
        or repository_root
        / "factory/context-manifests/"
        "s00.yaml"
    )

    registry.register(
        ContextStage(manifest)
    )

    return registry


def run_pipeline(
    repository_root: Path,
    stage_names: list[str] | None = None,
    fail_fast: bool = True,
    context_manifest: Path | None = None,
) -> CommandResult:
    engine = PipelineEngine(
        create_default_registry(
            repository_root=(
                repository_root
            ),
            context_manifest=(
                context_manifest
            ),
        )
    )

    pipeline_result = engine.run(
        repository_root=repository_root,
        stage_names=stage_names,
        fail_fast=fail_fast,
    )

    return CommandResult(
        command="pipeline",
        status=pipeline_result.status,
        message=(
            "Pipeline completed successfully."
            if pipeline_result.successful
            else "Pipeline execution failed."
        ),
        data=pipeline_result.to_dict(),
    )
