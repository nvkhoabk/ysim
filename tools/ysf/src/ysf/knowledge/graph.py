from __future__ import annotations

from typing import Any

from ysf.knowledge.models import (
    KnowledgeDocument,
    KnowledgeRelationship,
)


def build_graph_nodes(
    documents: list[KnowledgeDocument],
    capabilities: list[dict[str, Any]],
    integrations: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []

    for document in documents:
        nodes.append({
            "id": document.id,
            "type": "document",
            "label": (
                document.title
                or document.filename
            ),
            "path": document.path,
            "documentSet": document.document_set,
            "layer": document.layer,
        })

    for capability in capabilities:
        nodes.append({
            "id": capability["id"],
            "type": "capability",
            "label": capability["name"],
        })

    for integration in integrations:
        nodes.append({
            "id": integration["id"],
            "type": "integration",
            "label": integration["name"],
        })

    return nodes


def build_graph(
    documents: list[KnowledgeDocument],
    capabilities: list[dict[str, Any]],
    integrations: list[dict[str, Any]],
    relationships: list[KnowledgeRelationship],
) -> dict[str, Any]:
    nodes = build_graph_nodes(
        documents=documents,
        capabilities=capabilities,
        integrations=integrations,
    )

    edges = [
        relationship.to_dict()
        for relationship in relationships
    ]

    return {
        "nodeCount": len(nodes),
        "edgeCount": len(edges),
        "nodes": nodes,
        "edges": edges,
    }
