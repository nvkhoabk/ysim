from pathlib import Path
from unittest.mock import patch

import pytest

from ysf.execution.workspace import (
    WorkspaceSnapshotError,
    build_snapshot_hash,
    capture_workspace_snapshot,
    normalize_status_lines,
    snapshot_to_payload,
    write_workspace_snapshot,
)


def test_normalize_status_lines() -> None:
    output = (
        " M tools/ysf/src/file.py\n"
        "?? factory/report.json\n"
        "\n"
    )

    result = normalize_status_lines(output)

    assert result == [
        " M tools/ysf/src/file.py",
        "?? factory/report.json",
    ]


def test_build_snapshot_hash_is_deterministic() -> None:
    payload = {
        "branch": "main",
        "headCommit": "abc123",
        "statusLines": [],
    }

    first = build_snapshot_hash(payload)
    second = build_snapshot_hash(payload)

    assert first == second
    assert len(first) == 64


def test_capture_clean_workspace(
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    with patch(
        "ysf.execution.workspace.run_git"
    ) as run_git_mock:
        run_git_mock.side_effect = [
            "main",
            "abc123",
            "",
        ]

        snapshot = capture_workspace_snapshot(
            tmp_path
        )

    assert snapshot.branch == "main"
    assert snapshot.head_commit == "abc123"
    assert snapshot.working_tree_clean is True
    assert snapshot.status_lines == []


def test_capture_dirty_workspace(
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    with patch(
        "ysf.execution.workspace.run_git"
    ) as run_git_mock:
        run_git_mock.side_effect = [
            "feature/test",
            "def456",
            " M file.py\n?? new.txt",
        ]

        snapshot = capture_workspace_snapshot(
            tmp_path
        )

    assert snapshot.branch == "feature/test"
    assert snapshot.working_tree_clean is False
    assert snapshot.status_lines == [
        " M file.py",
        "?? new.txt",
    ]


def test_capture_rejects_non_git_directory(
    tmp_path: Path,
) -> None:
    with pytest.raises(
        WorkspaceSnapshotError
    ):
        capture_workspace_snapshot(
            tmp_path
        )


def test_snapshot_payload_contains_hash(
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    with patch(
        "ysf.execution.workspace.run_git"
    ) as run_git_mock:
        run_git_mock.side_effect = [
            "main",
            "abc123",
            "",
        ]

        snapshot = capture_workspace_snapshot(
            tmp_path
        )

    payload = snapshot_to_payload(snapshot)

    assert payload["branch"] == "main"
    assert payload["snapshotHash"]
    assert len(payload["snapshotHash"]) == 64


def test_write_workspace_snapshot(
    tmp_path: Path,
) -> None:
    (tmp_path / ".git").mkdir()

    with patch(
        "ysf.execution.workspace.run_git"
    ) as run_git_mock:
        run_git_mock.side_effect = [
            "main",
            "abc123",
            "",
        ]

        snapshot = capture_workspace_snapshot(
            tmp_path
        )

    output = write_workspace_snapshot(
        repository_root=tmp_path,
        snapshot=snapshot,
        output_path=Path(
            "factory/executions/test/"
            "workspace.json"
        ),
    )

    assert output.is_file()

    content = output.read_text(
        encoding="utf-8"
    )

    assert '"branch": "main"' in content
    assert '"snapshotHash"' in content
