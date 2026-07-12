from ysf.execution.models import (
    ExecutionPlan,
    ExecutionRequest,
    WorkspaceSnapshot,
)
from ysf.execution.providers import (
    CodexProvider,
    ProviderRegistry,
)
from ysf.execution.runner import run_execution


def test_dry_run_execution_passes() -> None:
    request = ExecutionRequest(
        execution_id="s00-t00-test",
        sprint="S00",
        task="T00",
        provider="codex",
        prompt_path="prompt.md",
        repository_root="/repo",
        mode="dry-run",
    )

    workspace = WorkspaceSnapshot(
        repository_root="/repo",
        branch="main",
        head_commit="abc123",
        working_tree_clean=True,
        status_lines=[],
        captured_at=(
            "2026-07-12T10:00:00+07:00"
        ),
    )

    plan = ExecutionPlan(
        execution_id="s00-t00-test",
        provider="codex",
        mode="dry-run",
        prompt_path="prompt.md",
        prompt_hash="abc",
        estimated_tokens=100,
        workspace=workspace,
    )

    registry = ProviderRegistry()
    registry.register(CodexProvider())

    result = run_execution(
        request=request,
        plan=plan,
        provider_registry=registry,
    )

    assert result.successful
    assert result.dry_run
    assert result.modified_files == []
    assert (
        result.metadata["providerInvoked"]
        is False
    )
