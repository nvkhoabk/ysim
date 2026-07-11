from __future__ import annotations

from pathlib import Path

from ysf.core.result import CommandResult
from ysf.index.service import build_indexes
from ysf.knowledge.service import build_knowledge
from ysf.pipeline.stage import PipelineStage


class IndexStage(PipelineStage):
    name = "index"
    order = 10

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_indexes(repository_root)


class KnowledgeStage(PipelineStage):
    name = "knowledge"
    order = 20

    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        return build_knowledge(repository_root)
