from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any

from ysf.index.metadata import (
    extract_title,
    is_navigation_document,
    parse_frontmatter,
)
from ysf.index.models import DocumentRecord


class DocumentIndexError(RuntimeError):
    """Raised when the document index cannot be generated."""


def document_set_for(path: Path, docs_root: Path) -> str:
    relative = path.relative_to(docs_root)

    if len(relative.parts) == 1:
        return "ROOT"

    return relative.parts[0]


def build_document_record(
    path: Path,
    repository_root: Path,
    docs_root: Path,
) -> DocumentRecord:
    metadata = parse_frontmatter(path)

    return DocumentRecord(
        path=path.relative_to(repository_root).as_posix(),
        filename=path.name,
        extension=path.suffix.lstrip("."),
        document_set=document_set_for(path, docs_root),
        document_code=metadata.get("document_code") or None,
        document_name=metadata.get("document_name") or None,
        title=extract_title(path),
        project=metadata.get("project") or None,
        version=metadata.get("version") or None,
        status=metadata.get("status") or None,
        language=metadata.get("language") or None,
        generated_navigation=is_navigation_document(
            path,
            repository_root,
        ),
    )


def build_document_index(
    repository_root: Path,
) -> dict[str, Any]:
    docs_root = repository_root / "docs"

    if not docs_root.is_dir():
        raise DocumentIndexError(
            f"Documentation directory not found: {docs_root}"
        )

    files = sorted(docs_root.rglob("*.md"))

    records = [
        build_document_record(
            path=path,
            repository_root=repository_root,
            docs_root=docs_root,
        )
        for path in files
    ]

    return {
        "schemaVersion": "1.2",
        "generatedAt": datetime.now().astimezone().isoformat(),
        "repositoryRoot": ".",
        "documentCount": len(records),
        "documents": [
            record.to_dict()
            for record in records
        ],
    }


def write_document_index(
    repository_root: Path,
    payload: dict[str, Any],
) -> Path:
    output = repository_root / "factory/index/documents.json"
    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )

    return output
