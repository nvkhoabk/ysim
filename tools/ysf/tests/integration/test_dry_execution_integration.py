from pathlib import Path

from ysf.execution.service import (
    run_dry_execution,
)


def test_run_dry_execution_in_repository() -> None:
    repository_root = Path.cwd().parents[1]

    prompt_artifact = (
        repository_root
        / "factory/prompts/generated/"
        "s00/t00/prompt.json"
    )

    result = run_dry_execution(
        repository_root=repository_root,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="integration-dry-run",
        output_directory=Path(
            "runtime/tmp/ysf-integration-execution"
        ),
    )

    assert result.successful
    assert result.data["providerInvoked"] is False
    assert result.data["modifiedFileCount"] == 0

    assert (
        repository_root
        / result.data["reportJson"]
    ).is_file()
