from __future__ import annotations

from pathlib import Path

from ysf.context.service import (
    build_context,
)
from ysf.core.result import CommandResult
from ysf.index.service import (
    build_indexes,
)
from ysf.knowledge.service import (
    build_knowledge,
)
from ysf.pipeline.stage import PipelineStage
from ysf.prompt.service import build_prompt


class IndexStage(PipelineStage):
    name = "index"
    order = 10

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_indexes(
            repository_root
        )


class KnowledgeStage(PipelineStage):
    name = "knowledge"
    order = 20

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_knowledge(
            repository_root
        )


class ContextStage(PipelineStage):
    name = "context"
    order = 30

    def __init__(
        self,
        manifest_path: Path,
    ) -> None:
        self._manifest_path = (
            manifest_path
        )

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_context(
            repository_root=repository_root,
            manifest_path=(
                self._manifest_path
            ),
        )


class PromptStage(PipelineStage):
    name = "prompt"
    order = 40

    def __init__(
        self,
        manifest_path: Path,
    ) -> None:
        self._manifest_path = (
            manifest_path
        )

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_prompt(
            repository_root=repository_root,
            manifest_path=self._manifest_path,
        )
