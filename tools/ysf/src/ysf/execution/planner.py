from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from ysf.execution.models import (
    ExecutionMode,
    ExecutionPlan,
    ExecutionRequest,
)
from ysf.execution.workspace import (
    capture_workspace_snapshot,
    snapshot_to_payload,
)


class ExecutionPlannerError(RuntimeError):
    """Raised when an execution plan cannot be created."""


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ExecutionPlannerError(
            f"Required JSON file not found: {path}"
        )

    try:
        payload = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise ExecutionPlannerError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(payload, dict):
        raise ExecutionPlannerError(
            f"Expected JSON object in {path}"
        )

    return payload


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ExecutionPlannerError(
            f"Required YAML file not found: {path}"
        )

    try:
        payload = yaml.safe_load(
            path.read_text(encoding="utf-8-sig")
        )
    except yaml.YAMLError as exc:
        raise ExecutionPlannerError(
            f"Invalid YAML in {path}: {exc}"
        ) from exc

    if not isinstance(payload, dict):
        raise ExecutionPlannerError(
            f"Expected YAML object in {path}"
        )

    return payload


def resolve_path(
    repository_root: Path,
    value: str,
) -> Path:
    path = Path(value)

    if path.is_absolute():
        return path.resolve()

    return (repository_root / path).resolve()


def relative_path(
    repository_root: Path,
    path: Path,
) -> str:
    try:
        return path.relative_to(
            repository_root
        ).as_posix()
    except ValueError as exc:
        raise ExecutionPlannerError(
            f"Path is outside repository: {path}"
        ) from exc


def calculate_file_hash(path: Path) -> str:
    if not path.is_file():
        raise ExecutionPlannerError(
            f"File not found: {path}"
        )

    return hashlib.sha256(
        path.read_bytes()
    ).hexdigest()


def normalize_string_list(
    value: Any,
    field_name: str,
) -> list[str]:
    if value is None:
        return []

    if not isinstance(value, list):
        raise ExecutionPlannerError(
            f"{field_name} must be a list"
        )

    return [
        str(item).strip()
        for item in value
        if str(item).strip()
    ]


def build_execution_request(
    repository_root: Path,
    prompt_artifact_path: Path,
    execution_id: str,
    provider: str | None = None,
    mode: ExecutionMode = "dry-run",
) -> ExecutionRequest:
    prompt_artifact = read_json(
        prompt_artifact_path
    )

    prompt_file_value = str(
        prompt_artifact.get(
            "promptFile",
            "",
        )
    ).strip()

    if not prompt_file_value:
        raise ExecutionPlannerError(
            "Prompt artifact does not define promptFile"
        )

    prompt_file = resolve_path(
        repository_root,
        prompt_file_value,
    )

    if not prompt_file.is_file():
        raise ExecutionPlannerError(
            f"Prompt file not found: {prompt_file}"
        )

    artifact_manifest_path = (
        prompt_artifact_path.parent
        / "manifest.json"
    )

    artifact_manifest = read_json(
        artifact_manifest_path
    )

    source_manifest_value = str(
        artifact_manifest.get(
            "sourceManifest",
            "",
        )
    ).strip()

    if not source_manifest_value:
        raise ExecutionPlannerError(
            "Prompt manifest artifact does not "
            "define sourceManifest"
        )

    source_manifest_path = resolve_path(
        repository_root,
        source_manifest_value,
    )

    source_manifest = read_yaml(
        source_manifest_path
    )

    prompt_configuration = source_manifest.get(
        "prompt",
        {},
    )

    if not isinstance(
        prompt_configuration,
        dict,
    ):
        raise ExecutionPlannerError(
            "prompt section must be a mapping"
        )

    constraints = source_manifest.get(
        "constraints",
        {},
    )

    if not isinstance(constraints, dict):
        raise ExecutionPlannerError(
            "constraints section must be a mapping"
        )

    validation = source_manifest.get(
        "validation",
        {},
    )

    if not isinstance(validation, dict):
        raise ExecutionPlannerError(
            "validation section must be a mapping"
        )

    sprint = str(
        prompt_artifact.get(
            "sprint",
            prompt_configuration.get(
                "sprint",
                "",
            ),
        )
    ).strip()

    task = str(
        prompt_artifact.get(
            "task",
            prompt_configuration.get(
                "task",
                "",
            ),
        )
    ).strip()

    resolved_provider = (
        provider
        or str(
            prompt_artifact.get(
                "provider",
                prompt_configuration.get(
                    "provider",
                    "",
                ),
            )
        ).strip()
    )

    if not sprint:
        raise ExecutionPlannerError(
            "Sprint is missing from prompt artifact"
        )

    if not task:
        raise ExecutionPlannerError(
            "Task is missing from prompt artifact"
        )

    if not resolved_provider:
        raise ExecutionPlannerError(
            "Execution provider is missing"
        )

    allowed_paths = normalize_string_list(
        constraints.get("allowed_paths"),
        "constraints.allowed_paths",
    )

    protected_paths = normalize_string_list(
        constraints.get("protected_paths"),
        "constraints.protected_paths",
    )

    validation_commands = (
        normalize_string_list(
            validation.get("commands"),
            "validation.commands",
        )
    )

    return ExecutionRequest(
        execution_id=execution_id,
        sprint=sprint,
        task=task,
        provider=resolved_provider,
        prompt_path=relative_path(
            repository_root,
            prompt_file,
        ),
        repository_root=str(
            repository_root.resolve()
        ),
        mode=mode,
        allowed_paths=allowed_paths,
        protected_paths=protected_paths,
        validation_commands=(
            validation_commands
        ),
    )


def create_execution_plan(
    repository_root: Path,
    request: ExecutionRequest,
    prompt_artifact_path: Path,
) -> ExecutionPlan:
    prompt_artifact = read_json(
        prompt_artifact_path
    )

    prompt_path = resolve_path(
        repository_root,
        request.prompt_path,
    )

    actual_hash = calculate_file_hash(
        prompt_path
    )

    expected_hash = str(
        prompt_artifact.get(
            "promptHash",
            "",
        )
    ).strip()

    if not expected_hash:
        raise ExecutionPlannerError(
            "Prompt artifact does not define promptHash"
        )

    if actual_hash != expected_hash:
        raise ExecutionPlannerError(
            "Prompt hash mismatch. "
            "Rebuild the Prompt Artifact before planning."
        )

    estimated_tokens_value = (
        prompt_artifact.get(
            "estimatedTokens",
            0,
        )
    )

    try:
        estimated_tokens = int(
            estimated_tokens_value
        )
    except (TypeError, ValueError) as exc:
        raise ExecutionPlannerError(
            "estimatedTokens must be an integer"
        ) from exc

    workspace = capture_workspace_snapshot(
        repository_root
    )

    return ExecutionPlan(
        execution_id=request.execution_id,
        provider=request.provider,
        mode=request.mode,
        prompt_path=request.prompt_path,
        prompt_hash=actual_hash,
        estimated_tokens=estimated_tokens,
        workspace=workspace,
        allowed_paths=request.allowed_paths,
        protected_paths=request.protected_paths,
        validation_commands=(
            request.validation_commands
        ),
    )


def write_execution_plan(
    repository_root: Path,
    request: ExecutionRequest,
    plan: ExecutionPlan,
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

    payload = {
        "schemaVersion": "1.0",
        "generatedAt": (
            datetime.now()
            .astimezone()
            .isoformat()
        ),
        "status": "PLANNED",
        "request": request.to_dict(),
        "plan": plan.to_dict(),
        "workspaceSnapshot": (
            snapshot_to_payload(
                plan.workspace
            )
        ),
    }

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


def default_execution_id(
    sprint: str,
    task: str,
) -> str:
    timestamp = (
        datetime.now()
        .astimezone()
        .strftime("%Y%m%d-%H%M%S")
    )

    return (
        f"{sprint.lower()}-"
        f"{task.lower()}-"
        f"{timestamp}"
    )


def default_plan_output(
    request: ExecutionRequest,
) -> Path:
    return Path(
        "factory/executions"
    ) / request.sprint.lower() / (
        request.task.lower()
    ) / "plan.json"


def plan_execution(
    repository_root: Path,
    prompt_artifact_path: Path,
    execution_id: str | None = None,
    provider: str | None = None,
    mode: ExecutionMode = "dry-run",
    output_path: Path | None = None,
) -> tuple[
    ExecutionRequest,
    ExecutionPlan,
    Path,
]:
    prompt_artifact = read_json(
        prompt_artifact_path
    )

    sprint = str(
        prompt_artifact.get(
            "sprint",
            "",
        )
    ).strip()

    task = str(
        prompt_artifact.get(
            "task",
            "",
        )
    ).strip()

    resolved_execution_id = (
        execution_id
        or default_execution_id(
            sprint=sprint,
            task=task,
        )
    )

    request = build_execution_request(
        repository_root=repository_root,
        prompt_artifact_path=(
            prompt_artifact_path
        ),
        execution_id=(
            resolved_execution_id
        ),
        provider=provider,
        mode=mode,
    )

    plan = create_execution_plan(
        repository_root=repository_root,
        request=request,
        prompt_artifact_path=(
            prompt_artifact_path
        ),
    )

    resolved_output = (
        output_path
        or default_plan_output(request)
    )

    written_path = write_execution_plan(
        repository_root=repository_root,
        request=request,
        plan=plan,
        output_path=resolved_output,
    )

    return request, plan, written_path
