import hashlib
import json
from pathlib import Path
from unittest.mock import patch

import pytest

from ysf.execution.models import (
    WorkspaceSnapshot,
)
from ysf.execution.planner import (
    ExecutionPlannerError,
    build_execution_request,
    create_execution_plan,
    default_plan_output,
    write_execution_plan,
)


def create_prompt_fixture(
    repository_root: Path,
) -> Path:
    prompt_directory = (
        repository_root
        / "factory/prompts/generated/s00/t00"
    )

    prompt_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    prompt_content = "# Prompt\n\nDry-run fixture.\n"

    prompt_file = (
        prompt_directory / "prompt.md"
    )

    prompt_file.write_text(
        prompt_content,
        encoding="utf-8",
    )

    prompt_hash = hashlib.sha256(
        prompt_content.encode("utf-8")
    ).hexdigest()

    prompt_artifact = {
        "sprint": "S00",
        "task": "T00",
        "provider": "codex",
        "promptFile": (
            "factory/prompts/generated/"
            "s00/t00/prompt.md"
        ),
        "promptHash": prompt_hash,
        "estimatedTokens": 100,
    }

    prompt_artifact_path = (
        prompt_directory / "prompt.json"
    )

    prompt_artifact_path.write_text(
        json.dumps(prompt_artifact),
        encoding="utf-8",
    )

    source_manifest_path = (
        repository_root
        / "factory/prompt-manifests/"
        "s00-t00.yaml"
    )

    source_manifest_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    source_manifest_path.write_text(
        "\n".join([
            'schema_version: "1.0"',
            "prompt:",
            "  id: s00-t00",
            "  sprint: S00",
            "  task: T00",
            "  provider: codex",
            "constraints:",
            "  allowed_paths:",
            "    - factory/",
            "  protected_paths:",
            "    - docs/",
            "validation:",
            "  commands:",
            "    - ysf verify",
        ]),
        encoding="utf-8",
    )

    artifact_manifest = {
        "sourceManifest": (
            "factory/prompt-manifests/"
            "s00-t00.yaml"
        )
    }

    (
        prompt_directory / "manifest.json"
    ).write_text(
        json.dumps(artifact_manifest),
        encoding="utf-8",
    )

    return prompt_artifact_path


def test_build_execution_request(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        create_prompt_fixture(tmp_path)
    )

    request = build_execution_request(
        repository_root=tmp_path,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="s00-t00-test",
        mode="dry-run",
    )

    assert request.execution_id == (
        "s00-t00-test"
    )
    assert request.sprint == "S00"
    assert request.task == "T00"
    assert request.provider == "codex"
    assert request.dry_run is True
    assert request.allowed_paths == [
        "factory/"
    ]
    assert request.protected_paths == [
        "docs/"
    ]


def test_create_execution_plan(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        create_prompt_fixture(tmp_path)
    )

    request = build_execution_request(
        repository_root=tmp_path,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="s00-t00-test",
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

    with patch(
        "ysf.execution.planner."
        "capture_workspace_snapshot",
        return_value=workspace,
    ):
        plan = create_execution_plan(
            repository_root=tmp_path,
            request=request,
            prompt_artifact_path=(
                prompt_artifact
            ),
        )

    assert plan.provider == "codex"
    assert plan.dry_run is True
    assert plan.estimated_tokens == 100
    assert plan.workspace.branch == "main"


def test_prompt_hash_mismatch_fails(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        create_prompt_fixture(tmp_path)
    )

    artifact = json.loads(
        prompt_artifact.read_text(
            encoding="utf-8"
        )
    )

    artifact["promptHash"] = "invalid"

    prompt_artifact.write_text(
        json.dumps(artifact),
        encoding="utf-8",
    )

    request = build_execution_request(
        repository_root=tmp_path,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="s00-t00-test",
    )

    with pytest.raises(
        ExecutionPlannerError
    ):
        create_execution_plan(
            repository_root=tmp_path,
            request=request,
            prompt_artifact_path=(
                prompt_artifact
            ),
        )


def test_write_execution_plan(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        create_prompt_fixture(tmp_path)
    )

    request = build_execution_request(
        repository_root=tmp_path,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="s00-t00-test",
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

    with patch(
        "ysf.execution.planner."
        "capture_workspace_snapshot",
        return_value=workspace,
    ):
        plan = create_execution_plan(
            repository_root=tmp_path,
            request=request,
            prompt_artifact_path=(
                prompt_artifact
            ),
        )

    output = write_execution_plan(
        repository_root=tmp_path,
        request=request,
        plan=plan,
        output_path=Path(
            "factory/executions/"
            "s00/t00/plan.json"
        ),
    )

    payload = json.loads(
        output.read_text(
            encoding="utf-8"
        )
    )

    assert payload["status"] == "PLANNED"
    assert (
        payload["request"]["executionId"]
        == "s00-t00-test"
    )
    assert (
        payload["plan"]["provider"]
        == "codex"
    )
    assert payload[
        "workspaceSnapshot"
    ]["snapshotHash"]


def test_default_plan_output(
    tmp_path: Path,
) -> None:
    prompt_artifact = (
        create_prompt_fixture(tmp_path)
    )

    request = build_execution_request(
        repository_root=tmp_path,
        prompt_artifact_path=(
            prompt_artifact
        ),
        execution_id="s00-t00-test",
    )

    assert default_plan_output(
        request
    ) == Path(
        "factory/executions/"
        "s00/t00/plan.json"
    )
