from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def build_master_catalog(
    document_index: dict[str, Any],
    knowledge_index: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schemaVersion": "1.1",
        "generatedAt": datetime.now().astimezone().isoformat(),
        "project": "YSim",
        "factoryVersion": "2.1",
        "sources": {
            "documentation": {
                "index": "factory/index/documents.json",
                "count": document_index["documentCount"],
            },
            "knowledge": {
                "index": "factory/index/knowledge.json",
                "count": knowledge_index["knowledgeCount"],
            },
        },
    }


def write_master_catalog(
    repository_root: Path,
    payload: dict[str, Any],
) -> Path:
    output = repository_root / "factory/index/catalog.json"
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
