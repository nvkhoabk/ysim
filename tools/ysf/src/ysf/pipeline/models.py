from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class StageResult:
    name: str
    order: int
    status: str
    duration_seconds: float
    message: str
    data: dict[str, Any] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        return self.status == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class PipelineResult:
    name: str
    status: str
    duration_seconds: float
    stages: list[StageResult] = field(default_factory=list)

    @property
    def successful(self) -> bool:
        return self.status == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "status": self.status,
            "durationSeconds": self.duration_seconds,
            "stageCount": len(self.stages),
            "stages": [
                stage.to_dict()
                for stage in self.stages
            ],
        }
