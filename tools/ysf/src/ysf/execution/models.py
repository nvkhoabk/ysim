from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

ExecutionStatus = Literal[
    "PLANNED",
    "RUNNING",
    "PASS",
    "FAIL",
    "BLOCKED",
    "CANCELLED",
]

ExecutionMode = Literal[
    "dry-run",
    "apply",
]


@dataclass(frozen=True)
class ExecutionRequest:
    execution_id: str
    sprint: str
    task: str
    provider: str
    prompt_path: str
    repository_root: str
    mode: ExecutionMode = "dry-run"
    allowed_paths: list[str] = field(default_factory=list)
    protected_paths: list[str] = field(default_factory=list)
    validation_commands: list[str] = field(default_factory=list)

    @property
    def dry_run(self) -> bool:
        return self.mode == "dry-run"

    def to_dict(self) -> dict[str, Any]:
        return {
            "executionId": self.execution_id,
            "sprint": self.sprint,
            "task": self.task,
            "provider": self.provider,
            "promptPath": self.prompt_path,
            "repositoryRoot": self.repository_root,
            "mode": self.mode,
            "dryRun": self.dry_run,
            "allowedPaths": self.allowed_paths,
            "protectedPaths": self.protected_paths,
            "validationCommands": self.validation_commands,
        }


@dataclass(frozen=True)
class WorkspaceSnapshot:
    repository_root: str
    branch: str
    head_commit: str
    working_tree_clean: bool
    status_lines: list[str] = field(default_factory=list)
    captured_at: str = ""

    def to_dict(self) -> dict[str, Any]:
        return {
            "repositoryRoot": self.repository_root,
            "branch": self.branch,
            "headCommit": self.head_commit,
            "workingTreeClean": self.working_tree_clean,
            "statusLines": self.status_lines,
            "capturedAt": self.captured_at,
        }


@dataclass(frozen=True)
class ExecutionPlan:
    execution_id: str
    provider: str
    mode: ExecutionMode
    prompt_path: str
    prompt_hash: str
    estimated_tokens: int
    workspace: WorkspaceSnapshot
    allowed_paths: list[str] = field(default_factory=list)
    protected_paths: list[str] = field(default_factory=list)
    validation_commands: list[str] = field(default_factory=list)

    @property
    def dry_run(self) -> bool:
        return self.mode == "dry-run"

    def to_dict(self) -> dict[str, Any]:
        return {
            "executionId": self.execution_id,
            "provider": self.provider,
            "mode": self.mode,
            "dryRun": self.dry_run,
            "promptPath": self.prompt_path,
            "promptHash": self.prompt_hash,
            "estimatedTokens": self.estimated_tokens,
            "workspace": self.workspace.to_dict(),
            "allowedPaths": self.allowed_paths,
            "protectedPaths": self.protected_paths,
            "validationCommands": self.validation_commands,
        }


@dataclass(frozen=True)
class ExecutionArtifact:
    artifact_type: str
    path: str
    description: str = ""

    def to_dict(self) -> dict[str, str]:
        return asdict(self)


@dataclass(frozen=True)
class ExecutionResult:
    execution_id: str
    status: ExecutionStatus
    provider: str
    mode: ExecutionMode
    started_at: str
    finished_at: str
    duration_seconds: float
    message: str
    exit_code: int | None = None
    stdout: str = ""
    stderr: str = ""
    modified_files: list[str] = field(default_factory=list)
    artifacts: list[ExecutionArtifact] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def successful(self) -> bool:
        return self.status == "PASS"

    @property
    def dry_run(self) -> bool:
        return self.mode == "dry-run"

    def to_dict(self) -> dict[str, Any]:
        return {
            "executionId": self.execution_id,
            "status": self.status,
            "provider": self.provider,
            "mode": self.mode,
            "dryRun": self.dry_run,
            "startedAt": self.started_at,
            "finishedAt": self.finished_at,
            "durationSeconds": self.duration_seconds,
            "message": self.message,
            "exitCode": self.exit_code,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "modifiedFiles": self.modified_files,
            "artifacts": [
                artifact.to_dict()
                for artifact in self.artifacts
            ],
            "metadata": self.metadata,
        }
