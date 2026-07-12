from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

from ysf.execution.models import WorkspaceSnapshot


class WorkspaceSnapshotError(RuntimeError):
    """Raised when repository state cannot be captured."""


def run_git(
    repository_root: Path,
    arguments: list[str],
) -> str:
    process = subprocess.run(
        [
            "git",
            "-C",
            str(repository_root),
            *arguments,
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    if process.returncode != 0:
        message = (
            process.stderr.strip()
            or process.stdout.strip()
            or "Unknown Git error."
        )

        raise WorkspaceSnapshotError(
            f"Git command failed: "
            f"git {' '.join(arguments)}: {message}"
        )

    return process.stdout.strip()


def normalize_status_lines(
    status_output: str,
) -> list[str]:
    return [
        line.rstrip()
        for line in status_output.splitlines()
        if line.strip()
    ]


def build_snapshot_hash(
    payload: dict[str, Any],
) -> str:
    serialized = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )

    return hashlib.sha256(
        serialized.encode("utf-8")
    ).hexdigest()


def capture_workspace_snapshot(
    repository_root: Path,
) -> WorkspaceSnapshot:
    resolved_root = repository_root.resolve()

    if not (resolved_root / ".git").exists():
        raise WorkspaceSnapshotError(
            f"Not a Git repository: {resolved_root}"
        )

    branch = run_git(
        resolved_root,
        ["branch", "--show-current"],
    )

    head_commit = run_git(
        resolved_root,
        ["rev-parse", "HEAD"],
    )

    status_output = run_git(
        resolved_root,
        [
            "status",
            "--short",
            "--untracked-files=all",
        ],
    )

    status_lines = normalize_status_lines(
        status_output
    )

    captured_at = (
        datetime.now()
        .astimezone()
        .isoformat()
    )

    return WorkspaceSnapshot(
        repository_root=str(resolved_root),
        branch=branch or "(detached HEAD)",
        head_commit=head_commit,
        working_tree_clean=not status_lines,
        status_lines=status_lines,
        captured_at=captured_at,
    )


def snapshot_to_payload(
    snapshot: WorkspaceSnapshot,
) -> dict[str, Any]:
    base_payload = snapshot.to_dict()

    snapshot_hash = build_snapshot_hash(
        {
            "repositoryRoot": base_payload[
                "repositoryRoot"
            ],
            "branch": base_payload["branch"],
            "headCommit": base_payload[
                "headCommit"
            ],
            "workingTreeClean": base_payload[
                "workingTreeClean"
            ],
            "statusLines": base_payload[
                "statusLines"
            ],
        }
    )

    return {
        "schemaVersion": "1.0",
        **base_payload,
        "snapshotHash": snapshot_hash,
    }


def write_workspace_snapshot(
    repository_root: Path,
    snapshot: WorkspaceSnapshot,
    output_path: Path,
) -> Path:
    resolved_output = (
        output_path
        if output_path.is_absolute()
        else repository_root / output_path
    )

    resolved_output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    payload = snapshot_to_payload(snapshot)

    resolved_output.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    return resolved_output
