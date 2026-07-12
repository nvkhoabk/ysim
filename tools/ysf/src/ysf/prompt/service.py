from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any

from ysf.core.result import CommandResult
from ysf.prompt.manifest import (
    load_prompt_manifest,
)
from ysf.prompt.models import PromptArtifact
from ysf.prompt.renderer import (
    render_template,
)
from ysf.prompt.repository import (
    build_repository_snapshot,
)
from ysf.prompt.validator import (
    validate_prompt,
)


class PromptBuildError(RuntimeError):
    """Raised when prompt generation cannot complete."""


def read_json(
    path: Path,
) -> dict[str, Any]:
    if not path.is_file():
        raise PromptBuildError(
            f"Required JSON not found: {path}"
        )

    try:
        data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise PromptBuildError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise PromptBuildError(
            f"Expected JSON object in {path}"
        )

    return data


def resolve_path(
    repository_root: Path,
    value: str,
) -> Path:
    path = Path(value)

    if path.is_absolute():
        return path

    return repository_root / path


def estimate_tokens(
    content: str,
) -> int:
    return max(
        1,
        round(len(content) / 4),
    )


def build_prompt(
    repository_root: Path,
    manifest_path: Path,
) -> CommandResult:
    manifest = load_prompt_manifest(
        manifest_path
    )

    prompt_config = manifest["prompt"]
    context_config = manifest["context"]
    output_config = manifest["output"]

    template_path = resolve_path(
        repository_root,
        str(prompt_config["template"]),
    )

    context_manifest_path = resolve_path(
        repository_root,
        str(context_config["manifest"]),
    )

    context_content_path = resolve_path(
        repository_root,
        str(context_config["content"]),
    )

    if not context_content_path.is_file():
        raise PromptBuildError(
            f"Context content not found: "
            f"{context_content_path}"
        )

    context_manifest = read_json(
        context_manifest_path
    )

    context_content = (
        context_content_path.read_text(
            encoding="utf-8-sig"
        )
    )

    source_documents = [
        (
            f"{document.get('documentCode')} "
            f"({document.get('path')})"
        )
        for document
        in context_manifest.get(
            "documents",
            [],
        )
    ]

    repository_snapshot = (
        build_repository_snapshot(
            repository_root=repository_root,
            configuration=manifest.get(
                "repository",
                {},
            ),
        )
    )

    constraints = manifest.get(
        "constraints",
        {},
    )

    validation = manifest.get(
        "validation",
        {},
    )

    completion = manifest.get(
        "completion",
        {},
    )

    values = {
        "prompt_id": prompt_config["id"],
        "sprint": prompt_config["sprint"],
        "task": prompt_config["task"],
        "provider": prompt_config["provider"],
        "objective": manifest["objective"],
        "repository_snapshot": repository_snapshot,
        "source_documents": source_documents,
        "context_content": context_content,
        "allowed_paths": constraints.get(
            "allowed_paths",
            [],
        ),
        "protected_paths": constraints.get(
            "protected_paths",
            [],
        ),
        "validation_commands": validation.get(
            "commands",
            [],
        ),
        "required_outputs": completion.get(
            "required_outputs",
            [],
        ),
    }

    prompt_content = render_template(
        template_path=template_path,
        values=values,
    )

    validate_prompt(prompt_content)

    output_directory = resolve_path(
        repository_root,
        str(output_config["directory"]),
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    prompt_path = (
        output_directory / "prompt.md"
    )

    prompt_json_path = (
        output_directory / "prompt.json"
    )

    manifest_json_path = (
        output_directory / "manifest.json"
    )

    prompt_path.write_text(
        prompt_content,
        encoding="utf-8",
    )

    prompt_hash = hashlib.sha256(
        prompt_content.encode("utf-8")
    ).hexdigest()

    artifact = PromptArtifact(
        prompt_id=str(prompt_config["id"]),
        sprint=str(prompt_config["sprint"]),
        task=str(prompt_config["task"]),
        provider=str(prompt_config["provider"]),
        template=template_path.relative_to(
            repository_root
        ).as_posix(),
        context_manifest=(
            context_manifest_path.relative_to(
                repository_root
            ).as_posix()
        ),
        context_content=(
            context_content_path.relative_to(
                repository_root
            ).as_posix()
        ),
        output_directory=(
            output_directory.relative_to(
                repository_root
            ).as_posix()
        ),
        prompt_file=prompt_path.relative_to(
            repository_root
        ).as_posix(),
        prompt_hash=prompt_hash,
        character_count=len(prompt_content),
        estimated_tokens=estimate_tokens(
            prompt_content
        ),
        source_documents=source_documents,
        validation_commands=[
            str(command)
            for command in validation.get(
                "commands",
                [],
            )
        ],
    )

    prompt_json_path.write_text(
        json.dumps(
            {
                "schemaVersion": "1.0",
                "generatedAt": (
                    datetime.now()
                    .astimezone()
                    .isoformat()
                ),
                **artifact.to_dict(),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    manifest_json_path.write_text(
        json.dumps(
            {
                "schemaVersion": "1.0",
                "sourceManifest": (
                    manifest_path.relative_to(
                        repository_root
                    ).as_posix()
                ),
                "promptId": artifact.prompt_id,
                "promptHash": artifact.prompt_hash,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    return CommandResult(
        command="build-prompt",
        status="PASS",
        message=(
            "Prompt artifact generated successfully."
        ),
        data={
            "promptId": artifact.prompt_id,
            "sprint": artifact.sprint,
            "task": artifact.task,
            "provider": artifact.provider,
            "characterCount": (
                artifact.character_count
            ),
            "estimatedTokens": (
                artifact.estimated_tokens
            ),
            "promptHash": artifact.prompt_hash,
            "outputDirectory": (
                artifact.output_directory
            ),
            "promptFile": artifact.prompt_file,
        },
    )
