from ysf.execution.models import (
    ExecutionArtifact,
    ExecutionPlan,
    ExecutionRequest,
    ExecutionResult,
    WorkspaceSnapshot,
)


def test_execution_request_dry_run() -> None:
    request = ExecutionRequest(
        execution_id="s00-t00-001",
        sprint="S00",
        task="T00",
        provider="codex",
        prompt_path=(
            "factory/prompts/generated/"
            "s00/t00/prompt.md"
        ),
        repository_root="/workspace/ysim",
        mode="dry-run",
        allowed_paths=["factory/"],
        protected_paths=["docs/BRD/"],
        validation_commands=["ysf verify"],
    )

    payload = request.to_dict()

    assert request.dry_run is True
    assert payload["executionId"] == "s00-t00-001"
    assert payload["provider"] == "codex"
    assert payload["dryRun"] is True
    assert payload["allowedPaths"] == ["factory/"]


def test_execution_plan_serialization() -> None:
    workspace = WorkspaceSnapshot(
        repository_root="/workspace/ysim",
        branch="chore/s00-factory-commissioning",
        head_commit="abc123",
        working_tree_clean=True,
        status_lines=[],
        captured_at="2026-07-12T10:00:00+07:00",
    )

    plan = ExecutionPlan(
        execution_id="s00-t00-001",
        provider="codex",
        mode="dry-run",
        prompt_path="factory/prompts/prompt.md",
        prompt_hash="deadbeef",
        estimated_tokens=1200,
        workspace=workspace,
        allowed_paths=["factory/"],
        protected_paths=["docs/"],
        validation_commands=["ysf verify"],
    )

    payload = plan.to_dict()

    assert plan.dry_run is True
    assert payload["workspace"]["branch"] == (
        "chore/s00-factory-commissioning"
    )
    assert payload["estimatedTokens"] == 1200


def test_execution_result_success() -> None:
    result = ExecutionResult(
        execution_id="s00-t00-001",
        status="PASS",
        provider="codex",
        mode="dry-run",
        started_at="2026-07-12T10:00:00+07:00",
        finished_at="2026-07-12T10:00:01+07:00",
        duration_seconds=1.0,
        message="Dry run completed.",
        exit_code=0,
        artifacts=[
            ExecutionArtifact(
                artifact_type="plan",
                path="factory/executions/s00/t00/plan.json",
                description="Execution plan",
            )
        ],
    )

    payload = result.to_dict()

    assert result.successful is True
    assert result.dry_run is True
    assert payload["status"] == "PASS"
    assert payload["artifacts"][0]["artifact_type"] == "plan"


def test_execution_result_failure() -> None:
    result = ExecutionResult(
        execution_id="s00-t00-002",
        status="FAIL",
        provider="codex",
        mode="apply",
        started_at="2026-07-12T10:00:00+07:00",
        finished_at="2026-07-12T10:00:02+07:00",
        duration_seconds=2.0,
        message="Execution failed.",
        exit_code=1,
        stderr="Provider error",
    )

    assert result.successful is False
    assert result.dry_run is False
