import json
from pathlib import Path

from ysf.execution.planner import (
    plan_execution,
)


def test_plan_execution_in_repository(
    tmp_path: Path,
) -> None:
    repository_root = (
        Path.cwd().parents[1]
    )

    prompt_artifact = (
        repository_root
        / "factory/prompts/generated/"
        "s00/t00/prompt.json"
    )

    output = (
        tmp_path / "plan.json"
    )

    request, plan, written_path = (
        plan_execution(
            repository_root=(
                repository_root
            ),
            prompt_artifact_path=(
                prompt_artifact
            ),
            execution_id=(
                "s00-t00-integration"
            ),
            mode="dry-run",
            output_path=output,
        )
    )

    payload = json.loads(
        written_path.read_text(
            encoding="utf-8"
        )
    )

    assert request.provider == "codex"
    assert plan.dry_run is True
    assert written_path == output
    assert payload["status"] == "PLANNED"
    assert payload["plan"]["promptHash"]
