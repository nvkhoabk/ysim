from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from ysf.context.assembler import (
    assemble_context,
)
from ysf.context.manifest import (
    load_context_manifest,
)
from ysf.context.models import (
    ContextPackage,
)
from ysf.context.selector import (
    select_documents,
)
from ysf.core.result import CommandResult


class ContextBuildError(RuntimeError):
    """Raised when context generation fails."""


def read_json(
    path: Path,
) -> dict[str, Any]:
    if not path.is_file():
        raise ContextBuildError(
            f"Required JSON not found: {path}"
        )

    try:
        data = json.loads(
            path.read_text(
                encoding="utf-8",
            )
        )
    except json.JSONDecodeError as exc:
        raise ContextBuildError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise ContextBuildError(
            f"Expected JSON object in {path}"
        )

    return data


def build_context(
    repository_root: Path,
    manifest_path: Path,
) -> CommandResult:
    manifest = load_context_manifest(
        manifest_path
    )

    document_index = read_json(
        repository_root
        / "factory/index/documents.json"
    )

    capability_catalog = read_json(
        repository_root
        / "knowledge/catalog/"
        "capabilities.json"
    )

    documents = document_index.get(
        "documents",
        [],
    )

    if not isinstance(documents, list):
        raise ContextBuildError(
            "Document index does not "
            "contain a documents array."
        )

    selected = select_documents(
        documents=documents,
        capabilities_catalog=(
            capability_catalog
        ),
        manifest=manifest,
    )

    maximum_characters = int(
        manifest.get(
            "limits",
            {},
        ).get(
            "max_characters",
            250000,
        )
    )

    (
        context_text,
        included_documents,
        character_count,
    ) = assemble_context(
        repository_root=repository_root,
        selected_documents=selected,
        maximum_characters=(
            maximum_characters
        ),
    )

    context_id = str(
        manifest.get(
            "context_id",
            "unknown-context",
        )
    )

    output_directory = str(
        manifest.get(
            "output",
            {},
        ).get(
            "directory",
            (
                "factory/contexts/"
                f"generated/{context_id}"
            ),
        )
    )

    output_root = (
        repository_root
        / output_directory
    )

    output_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    context_markdown_path = (
        output_root / "context.md"
    )

    context_json_path = (
        output_root / "context.json"
    )

    readme_path = (
        output_root / "README.md"
    )

    context_markdown_path.write_text(
        context_text,
        encoding="utf-8",
    )

    package = ContextPackage(
        context_id=context_id,
        source_manifest=(
            manifest_path.relative_to(
                repository_root
            ).as_posix()
        ),
        document_count=len(
            included_documents
        ),
        character_count=character_count,
        documents=included_documents,
        output=(
            context_markdown_path
            .relative_to(
                repository_root
            )
            .as_posix()
        ),
    )

    context_json_path.write_text(
        json.dumps(
            {
                **package.to_dict(),
                "generatedAt": (
                    datetime.now()
                    .astimezone()
                    .isoformat()
                ),
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    readme_path.write_text(
        "\n".join(
            [
                (
                    "# Context Package — "
                    f"{context_id}"
                ),
                "",
                (
                    "- Documents: "
                    f"{package.document_count}"
                ),
                (
                    "- Characters: "
                    f"{package.character_count}"
                ),
                "",
                "## Files",
                "",
                "- `context.md`",
                "- `context.json`",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return CommandResult(
        command="build-context",
        status="PASS",
        message=(
            "Context package generated "
            "successfully."
        ),
        data={
            "contextId": context_id,
            "documentCount": (
                package.document_count
            ),
            "characterCount": (
                package.character_count
            ),
            "outputDirectory": (
                output_root.relative_to(
                    repository_root
                ).as_posix()
            ),
            "manifest": (
                manifest_path.relative_to(
                    repository_root
                ).as_posix()
            ),
        },
    )
