from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


class KnowledgeIndexError(RuntimeError):
    """Raised when the knowledge index cannot be generated."""


def build_knowledge_index(
    repository_root: Path,
) -> dict[str, Any]:
    knowledge_root = repository_root / "knowledge"

    if not knowledge_root.is_dir():
        raise KnowledgeIndexError(
            f"Knowledge directory not found: {knowledge_root}"
        )

    entries: list[dict[str, Any]] = []

    for path in sorted(knowledge_root.rglob("*")):
        if not path.is_file():
            continue

        if path.name == ".gitkeep":
            continue

        if path.suffix.lower() not in {
            ".md",
            ".yaml",
            ".yml",
            ".json",
        }:
            continue

        relative = path.relative_to(knowledge_root)

        category = (
            relative.parts[0]
            if len(relative.parts) > 1
            else "ROOT"
        )

        entries.append({
            "path": path.relative_to(repository_root).as_posix(),
            "filename": path.name,
            "extension": path.suffix.lstrip("."),
            "category": category,
        })

    return {
        "schemaVersion": "1.1",
        "generatedAt": datetime.now().astimezone().isoformat(),
        "repositoryRoot": ".",
        "knowledgeCount": len(entries),
        "entries": entries,
    }


def write_knowledge_index(
    repository_root: Path,
    payload: dict[str, Any],
) -> Path:
    output = repository_root / "factory/index/knowledge.json"
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
