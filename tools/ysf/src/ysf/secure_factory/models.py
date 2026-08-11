"""Typed records shared by the secure-factory controls."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


class FactoryFailure(RuntimeError):
    """A fail-closed result whose message is safe to place in evidence."""

    def __init__(
        self,
        code: str,
        message: str,
        *,
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.code = code
        self.safe_message = message
        self.details = details or {}


@dataclass(frozen=True)
class GateResult:
    """Machine-readable outcome for one secure-factory gate."""

    gate: str
    result: str
    message: str
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return self.result == "PASS"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class EnvironmentExpectation:
    """Exact identity expected by the approved S00 Contract."""

    repository: str
    checkout: Path
    branch: str
    head_commit: str
    head_tree: str
    wsl_distribution: str
    os_id: str
    os_version_id: str
    architecture: str
    python_version: str
    upstream: str = "NONE"


@dataclass(frozen=True)
class EnvironmentObservation:
    """Observed local implementation identity."""

    repository: str
    checkout: Path
    branch: str
    head_commit: str
    head_tree: str
    wsl_distribution: str
    os_id: str
    os_version_id: str
    architecture: str
    python_version: str
    upstream: str


@dataclass(frozen=True)
class FileDigest:
    """Digest-bound file metadata."""

    relative_path: str
    byte_size: int
    sha256: str

    def to_dict(self) -> dict[str, str | int]:
        return asdict(self)
