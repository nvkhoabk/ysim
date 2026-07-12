import pytest

from ysf.execution.models import (
    ExecutionPlan,
    WorkspaceSnapshot,
)
from ysf.execution.providers import (
    CodexProvider,
)
from ysf.execution.providers.exceptions import (
    ProviderValidationError,
)


def create_plan(
    mode: str = "dry-run",
) -> ExecutionPlan:

    workspace = WorkspaceSnapshot(
        repository_root="/repo",
        branch="main",
        head_commit="abc123",
        working_tree_clean=True,
        status_lines=[],
        captured_at="2026-07-12T10:00:00+07:00",
    )

    return ExecutionPlan(
        execution_id="test",
        provider="codex",
        mode=mode,
        prompt_path="prompt.md",
        prompt_hash="hash",
        estimated_tokens=100,
        workspace=workspace,
    )


def test_provider_name() -> None:

    provider = CodexProvider()

    assert provider.name == "codex"


def test_provider_validate() -> None:

    provider = CodexProvider()

    provider.validate()


def test_provider_plan_not_implemented() -> None:

    provider = CodexProvider()

    with pytest.raises(
        NotImplementedError,
    ):
        provider.plan(None)  # type: ignore[arg-type]


def test_provider_execute_dry_run() -> None:

    provider = CodexProvider()

    result = provider.execute(
        create_plan("dry-run")
    )

    assert result.successful

    assert result.dry_run

    assert (
        result.metadata["providerInvoked"]
        is False
    )


def test_provider_execute_apply_rejected() -> None:

    provider = CodexProvider()

    with pytest.raises(
        ProviderValidationError,
    ):
        provider.execute(
            create_plan("apply")
        )