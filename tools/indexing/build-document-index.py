#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from document_metadata import metadata_record


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    docs_root = repo_root / "docs"
    output_dir = repo_root / "factory" / "index"
    output_file = output_dir / "documents.json"

    output_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(docs_root.rglob("*.md"))

    documents = [
        metadata_record(
            path=path,
            repo_root=repo_root,
            docs_root=docs_root,
        )
        for path in files
    ]

    result = {
        "schemaVersion": "1.1",
        "generatedAt": datetime.now().astimezone().isoformat(),
        "repositoryRoot": ".",
        "documentCount": len(documents),
        "documents": documents,
    }

    output_file.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(
        f"Generated {output_file.relative_to(repo_root)} "
        f"with {len(documents)} document(s)."
    )


if __name__ == "__main__":
    main()
