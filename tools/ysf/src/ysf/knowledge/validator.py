from __future__ import annotations

from ysf.knowledge.models import KnowledgeDocument


class KnowledgeValidationError(RuntimeError):
    """Raised when generated knowledge is invalid."""


def validate_documents(
    documents: list[KnowledgeDocument],
) -> None:
    invalid_paths = [
        document.path
        for document in documents
        if (
            not document.generated_navigation
            and not document.document_code
        )
    ]

    if invalid_paths:
        raise KnowledgeValidationError(
            "Governed documents without documentCode: "
            + ", ".join(invalid_paths)
        )


def validate_unique_ids(
    documents: list[KnowledgeDocument],
) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()

    for document in documents:
        if document.id in seen:
            duplicates.add(document.id)

        seen.add(document.id)

    if duplicates:
        raise KnowledgeValidationError(
            "Duplicate knowledge document IDs: "
            + ", ".join(sorted(duplicates))
        )
