from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from ysf.core.result import CommandResult


class PipelineStage(ABC):
    name: str
    order: int

    @abstractmethod
    def run(
        self,
        repository_root: Path,
    ) -> CommandResult:
        """Execute the pipeline stage."""
