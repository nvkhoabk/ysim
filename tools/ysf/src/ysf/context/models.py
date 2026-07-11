from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ContextDocument:
    document_code: str
    path: str
    document_set: str
    version: str | None
    status: str | None
    characters: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "documentCode": self.document_code,
            "path": self.path,
            "documentSet": self.document_set,
            "version": self.version,
            "status": self.status,
            "characters": self.characters,
        }


@dataclass(frozen=True)
class ContextPackage:
    context_id: str
    source_manifest: str
    document_count: int
    character_count: int
    output: str
    documents: list[ContextDocument] = field(
        default_factory=list,
    )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schemaVersion": "1.1",
            "contextId": self.context_id,
            "sourceManifest": self.source_manifest,
            "documentCount": self.document_count,
            "characterCount": self.character_count,
            "documents": [
                document.to_dict()
                for document in self.documents
            ],
            "output": self.output,
        }
