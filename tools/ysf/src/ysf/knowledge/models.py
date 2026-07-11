from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class KnowledgeDocument:
    id: str
    path: str
    filename: str
    document_set: str
    layer: str
    document_code: str | None
    title: str | None
    version: str | None
    status: str | None
    generated_navigation: bool
    searchable_text: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "path": self.path,
            "filename": self.filename,
            "documentSet": self.document_set,
            "layer": self.layer,
            "documentCode": self.document_code,
            "title": self.title,
            "version": self.version,
            "status": self.status,
            "generatedNavigation": self.generated_navigation,
            "searchableText": self.searchable_text,
        }


@dataclass(frozen=True)
class KnowledgeRelationship:
    id: str
    source: str
    target: str
    relationship_type: str
    generation_source: str

    def to_dict(self) -> dict[str, str]:
        return {
            "id": self.id,
            "from": self.source,
            "to": self.target,
            "type": self.relationship_type,
            "source": self.generation_source,
        }
