import json
from pathlib import Path

from ysf.execution.workspace import (
    capture_workspace_snapshot,
    write_workspace_snapshot,
)


def test_capture_repository_workspace() -> None:
    repository_root = (
        Path.cwd().parents[1]
    )

    snapshot = capture_workspace_snapshot(
        repository_root
    )

    assert snapshot.repository_root == str(
        repository_root.resolve()
    )
    assert snapshot.branch
    assert snapshot.head_commit
    assert len(snapshot.head_commit) >= 7


def test_write_repository_workspace_snapshot(
    tmp_path: Path,
) -> None:
    repository_root = (
        Path.cwd().parents[1]
    )

    snapshot = capture_workspace_snapshot(
        repository_root
    )

    output = write_workspace_snapshot(
        repository_root=repository_root,
        snapshot=snapshot,
        output_path=tmp_path / "workspace.json",
    )

    payload = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    assert payload["branch"]
    assert payload["headCommit"]
    assert payload["snapshotHash"]
