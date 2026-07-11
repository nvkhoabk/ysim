from __future__ import annotations

from collections import defaultdict
from typing import Any

from ysf.knowledge.models import (
    KnowledgeDocument,
    KnowledgeRelationship,
)
from ysf.knowledge.normalizer import stable_id


def find_matches(
    searchable_text: str,
    patterns: dict[str, tuple[str, ...]],
) -> list[str]:
    matches: list[str] = []

    for key, terms in patterns.items():
        if any(
            term in searchable_text
            for term in terms
        ):
            matches.append(key)

    return sorted(set(matches))


def build_named_catalog(
    documents: list[KnowledgeDocument],
    patterns: dict[str, tuple[str, ...]],
    relationship_type: str,
) -> tuple[
    list[dict[str, Any]],
    list[KnowledgeRelationship],
]:
    grouped: defaultdict[str, list[str]] = defaultdict(list)
    relationships: list[KnowledgeRelationship] = []

    for document in documents:
        if document.generated_navigation:
            continue

        matches = find_matches(
            document.searchable_text,
            patterns,
        )

        for item_id in matches:
            grouped[item_id].append(document.id)

            relationships.append(
                KnowledgeRelationship(
                    id=stable_id(
                        "rel",
                        document.id,
                        relationship_type,
                        item_id,
                    ),
                    source=document.id,
                    target=item_id,
                    relationship_type=relationship_type,
                    generation_source=(
                        "deterministic-title-matching"
                    ),
                )
            )

    catalog: list[dict[str, Any]] = []

    for item_id, document_ids in sorted(
        grouped.items()
    ):
        unique_ids = sorted(set(document_ids))

        catalog.append({
            "id": item_id,
            "name": item_id.replace(
                "-",
                " ",
            ).title(),
            "documentIds": unique_ids,
            "documentCount": len(unique_ids),
            "source": "deterministic-title-matching",
            "reviewStatus": "REQUIRES_HUMAN_REVIEW",
        })

    return catalog, relationships


def build_document_set_catalog(
    documents: list[KnowledgeDocument],
) -> list[dict[str, Any]]:
    grouped: defaultdict[
        str,
        list[KnowledgeDocument],
    ] = defaultdict(list)

    for document in documents:
        grouped[document.document_set].append(
            document
        )

    result: list[dict[str, Any]] = []

    for document_set, entries in sorted(
        grouped.items()
    ):
        result.append({
            "id": document_set,
            "layer": entries[0].layer,
            "documentCount": len(entries),
            "documentIds": sorted(
                document.id
                for document in entries
            ),
        })

    return result
