from __future__ import annotations

from pathlib import Path

from ysf.core.result import CommandResult
from ysf.execution.stage import (
    ExecutionStage,
    ExecutionStageConfig,
)
from ysf.pipeline.engine import PipelineEngine
from ysf.pipeline.registry import StageRegistry
from ysf.pipeline.stages import (
    ContextStage,
    IndexStage,
    KnowledgeStage,
    PromptStage,
)


def create_default_registry(
    repository_root: Path,
    context_manifest: Path | None = None,
    prompt_manifest: Path | None = None,
    execution_prompt_artifact: Path | None = None,
    execution_id: str | None = None,
    execution_output_directory: Path | None = None,
) -> StageRegistry:
    """Create the default YSF pipeline registry.

    Default stage order:

    - 10: index
    - 20: knowledge
    - 30: context
    - 40: prompt
    - 50: execution

    The execution stage is restricted to dry-run mode.
    """

    registry = StageRegistry()

    registry.register(
        IndexStage()
    )

    registry.register(
        KnowledgeStage()
    )

    resolved_context_manifest = (
        context_manifest
        or repository_root
        / "factory/context-manifests/s00.yaml"
    )

    registry.register(
        ContextStage(
            resolved_context_manifest
        )
    )

    resolved_prompt_manifest = (
        prompt_manifest
        or repository_root
        / "factory/prompt-manifests/s00-t00.yaml"
    )

    registry.register(
        PromptStage(
            resolved_prompt_manifest
        )
    )

    resolved_execution_prompt = (
        execution_prompt_artifact
        or Path(
            "factory/prompts/generated/"
            "s00/t00/prompt.json"
        )
    )

    resolved_execution_output = (
        execution_output_directory
        or Path(
            "factory/executions/s00/t00"
        )
    )

    registry.register(
        ExecutionStage(
            ExecutionStageConfig(
                prompt_artifact=(
                    resolved_execution_prompt
                ),
                provider="codex",
                execution_id=(
                    execution_id
                    or "s00-t00-pipeline-dry-run"
                ),
                output_directory=(
                    resolved_execution_output
                ),
                dry_run=True,
            )
        )
    )

    return registry


def run_pipeline(
    repository_root: Path,
    stage_names: list[str] | None = None,
    fail_fast: bool = True,
    context_manifest: Path | None = None,
    prompt_manifest: Path | None = None,
    execution_prompt_artifact: Path | None = None,
    execution_id: str | None = None,
    execution_output_directory: Path | None = None,
) -> CommandResult:
    registry = create_default_registry(
        repository_root=repository_root,
        context_manifest=context_manifest,
        prompt_manifest=prompt_manifest,
        execution_prompt_artifact=(
            execution_prompt_artifact
        ),
        execution_id=execution_id,
        execution_output_directory=(
            execution_output_directory
        ),
    )

    engine = PipelineEngine(
        registry
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
