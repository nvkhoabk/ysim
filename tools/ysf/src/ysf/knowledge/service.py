from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

from ysf.core.result import CommandResult
from ysf.knowledge.catalog import (
    build_document_set_catalog,
    build_named_catalog,
)
from ysf.knowledge.graph import build_graph
from ysf.knowledge.models import KnowledgeDocument
from ysf.knowledge.normalizer import normalize_document
from ysf.knowledge.patterns import (
    CAPABILITY_PATTERNS,
    INTEGRATION_PATTERNS,
)
from ysf.knowledge.validator import (
    validate_documents,
    validate_unique_ids,
)


class KnowledgeBuildError(RuntimeError):
    """Raised when knowledge generation fails."""


def read_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise KnowledgeBuildError(
            f"Missing input file: {path}"
        )

    try:
        data = json.loads(
            path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as exc:
        raise KnowledgeBuildError(
            f"Invalid JSON in {path}: {exc}"
        ) from exc

    if not isinstance(data, dict):
        raise KnowledgeBuildError(
            f"Expected JSON object in {path}"
        )

    return data


def write_json(
    path: Path,
    payload: dict[str, Any],
) -> None:
    path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
        ) + "\n",
        encoding="utf-8",
    )


def build_knowledge(
    repository_root: Path,
) -> CommandResult:
    source_path = (
        repository_root
        / "factory/index/documents.json"
    )

    source = read_json(source_path)
    raw_documents = source.get("documents")

    if not isinstance(raw_documents, list):
        raise KnowledgeBuildError(
            "documents.json has no documents array"
        )

    documents: list[KnowledgeDocument] = [
        normalize_document(item)
        for item in raw_documents
        if isinstance(item, dict)
    ]

    validate_documents(documents)
    validate_unique_ids(documents)

    capabilities, capability_relationships = (
        build_named_catalog(
            documents=documents,
            patterns=CAPABILITY_PATTERNS,
            relationship_type=(
                "references-capability"
            ),
        )
    )

    integrations, integration_relationships = (
        build_named_catalog(
            documents=documents,
            patterns=INTEGRATION_PATTERNS,
            relationship_type=(
                "references-integration"
            ),
        )
    )

    relationships = sorted(
        (
            capability_relationships
            + integration_relationships
        ),
        key=lambda item: item.id,
    )

    document_sets = build_document_set_catalog(
        documents
    )

    graph = build_graph(
        documents=documents,
        capabilities=capabilities,
        integrations=integrations,
        relationships=relationships,
    )

    generated_at = (
        datetime.now()
        .astimezone()
        .isoformat()
    )

    knowledge_root = (
        repository_root / "knowledge"
    )

    normalized_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "documentCount": len(documents),
        "documents": [
            document.to_dict()
            for document in documents
        ],
    }

    documents_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "documentCount": len(documents),
        "documents": [
            {
                key: document.to_dict()[key]
                for key in (
                    "id",
                    "path",
                    "filename",
                    "documentSet",
                    "layer",
                    "documentCode",
                    "title",
                    "version",
                    "status",
                    "generatedNavigation",
                )
            }
            for document in documents
        ],
    }

    document_sets_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "documentSetCount": len(
            document_sets
        ),
        "documentSets": document_sets,
    }

    capabilities_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "capabilityCount": len(
            capabilities
        ),
        "capabilities": capabilities,
    }

    integrations_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "integrationCount": len(
            integrations
        ),
        "integrations": integrations,
    }

    relationships_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "relationshipCount": len(
            relationships
        ),
        "relationships": [
            relationship.to_dict()
            for relationship in relationships
        ],
    }

    graph_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        **graph,
    }

    counts_by_set = Counter(
        document.document_set
        for document in documents
    )

    summary_payload = {
        "schemaVersion": "1.1",
        "generatedAt": generated_at,
        "status": "PASS",
        "sourceIndex": (
            "factory/index/documents.json"
        ),
        "documentCount": len(documents),
        "documentSetCount": len(
            counts_by_set
        ),
        "capabilityCount": len(
            capabilities
        ),
        "integrationCount": len(
            integrations
        ),
        "relationshipCount": len(
            relationships
        ),
        "nullGovernedDocumentCodes": 0,
        "documentsBySet": dict(
            sorted(counts_by_set.items())
        ),
        "notes": [
            (
                "Capability and integration matches "
                "are deterministic heuristics."
            ),
            (
                "Heuristic relationships require "
                "human or AI review."
            ),
            (
                "docs/ remains the authoritative "
                "source."
            ),
        ],
    }

    outputs = {
        "normalized/documents.json": (
            normalized_payload
        ),
        "catalog/documents.json": (
            documents_payload
        ),
        "catalog/document-sets.json": (
            document_sets_payload
        ),
        "catalog/capabilities.json": (
            capabilities_payload
        ),
        "catalog/integrations.json": (
            integrations_payload
        ),
        "catalog/relationships.json": (
            relationships_payload
        ),
        "catalog/knowledge-graph.json": (
            graph_payload
        ),
        "catalog/summary.json": (
            summary_payload
        ),
    }

    output_paths: list[str] = []

    for relative_path, payload in outputs.items():
        output_path = (
            knowledge_root / relative_path
        )

        write_json(
            output_path,
            payload,
        )

        output_paths.append(
            output_path.relative_to(
                repository_root
            ).as_posix()
        )

    return CommandResult(
        command="build-knowledge",
        status="PASS",
        message=(
            "Knowledge catalogs generated "
            "successfully."
        ),
        data={
            "documentCount": len(documents),
            "capabilityCount": len(
                capabilities
            ),
            "integrationCount": len(
                integrations
            ),
            "relationshipCount": len(
                relationships
            ),
            "outputs": output_paths,
        },
    )
