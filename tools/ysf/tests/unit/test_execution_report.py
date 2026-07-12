import json
from pathlib import Path

from ysf.execution.models import (
    ExecutionPlan,
    ExecutionRequest,
    ExecutionResult,
    WorkspaceSnapshot,
)
from ysf.execution.report import (
    write_execution_report,
)


def test_write_execution_report(
    tmp_path: Path,
) -> None:
    request = ExecutionRequest(
        execution_id="test-run",
        sprint="S00",
        task="T00",
        provider="codex",
        prompt_path="prompt.md",
        repository_root=str(tmp_path),
    )

    workspace = WorkspaceSnapshot(
        repository_root=str(tmp_path),
        branch="main",
        head_commit="abc123",
        working_tree_clean=True,
        status_lines=[],
        captured_at=(
            "2026-07-12T10:00:00+07:00"
        ),
    )

    plan = ExecutionPlan(
        execution_id="test-run",
        provider="codex",
        mode="dry-run",
        prompt_path="prompt.md",
        prompt_hash="abc",
        estimated_tokens=10,
        workspace=workspace,
    )

    result = ExecutionResult(
        execution_id="test-run",
        status="PASS",
        provider="codex",
        mode="dry-run",
        started_at="start",
        finished_at="finish",
        duration_seconds=0.0,
        message="Dry run passed.",
        modified_files=[],
    )

    json_path, markdown_path = (
        write_execution_report(
            repository_root=tmp_path,
            request=request,
            plan=plan,
            result=result,
            output_directory=Path(
                "factory/executions/test"
            ),
        )
    )

    assert json_path.is_file()
    assert markdown_path.is_file()

    payload = json.loads(
        json_path.read_text(
            encoding="utf-8"
        )
    )

    assert payload["result"]["status"] == "PASS"
