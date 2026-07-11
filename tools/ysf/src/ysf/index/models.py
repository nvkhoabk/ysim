from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DocumentRecord:
    path: str
    filename: str
    extension: str
    document_set: str
    document_code: str | None
    document_name: str | None
    title: str | None
    project: str | None
    version: str | None
    status: str | None
    language: str | None
    generated_navigation: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "filename": self.filename,
            "extension": self.extension,
            "documentSet": self.document_set,
            "documentCode": self.document_code,
            "documentName": self.document_name,
            "title": self.title,
            "project": self.project,
            "version": self.version,
            "status": self.status,
            "language": self.language,
            "generatedNavigation": self.generated_navigation,
        }
