from __future__ import annotations

from typing import Any


class ContextSelectionError(RuntimeError):
    """Raised when context document selection fails."""


def select_documents(
    documents: list[dict[str, Any]],
    capabilities_catalog: dict[str, Any],
    manifest: dict[str, Any],
) -> list[dict[str, Any]]:
    included_sets = set(
        manifest.get(
            "document_sets",
            {},
        ).get(
            "include",
            [],
        )
    )

    required_codes = set(
        manifest.get(
            "documents",
            {},
        ).get(
            "required",
            [],
        )
    )

    capability_ids = set(
        manifest.get("capabilities", [])
    )

    capability_document_ids: set[str] = set()

    for capability in capabilities_catalog.get(
        "capabilities",
        [],
    ):
        if capability.get("id") in capability_ids:
            capability_document_ids.update(
                capability.get(
                    "documentIds",
                    [],
                )
            )

    selected_by_path: dict[
        str,
        dict[str, Any],
    ] = {}

    for document in documents:
        if document.get("generatedNavigation"):
            continue

        code = document.get("documentCode")
        document_id = (
            code
            or document.get("id")
        )
        document_set = document.get(
            "documentSet"
        )
        path = document.get("path")

        should_include = (
            code in required_codes
            or document_id
            in capability_document_ids
            or document_set in included_sets
        )

        if should_include and path:
            selected_by_path[path] = document

    selected = list(
        selected_by_path.values()
    )

    found_codes = {
        document.get("documentCode")
        for document in selected
        if document.get("documentCode")
    }

    missing_required = sorted(
        required_codes - found_codes
    )

    if missing_required:
        raise ContextSelectionError(
            "Missing required documents: "
            + ", ".join(missing_required)
        )

    selected.sort(
        key=lambda document: (
            str(
                document.get(
                    "documentSet",
                    "",
                )
            ),
            str(
                document.get(
                    "documentCode",
                )
                or document.get(
                    "filename",
                    "",
                )
            ),
        )
    )

    maximum_documents = int(
        manifest.get(
            "limits",
            {},
        ).get(
            "max_documents",
            30,
        )
    )

    required_documents = [
        document
        for document in selected
        if document.get(
            "documentCode"
        ) in required_codes
    ]

    optional_documents = [
        document
        for document in selected
        if document.get(
            "documentCode"
        ) not in required_codes
    ]

    if (
        len(required_documents)
        > maximum_documents
    ):
        raise ContextSelectionError(
            "Required document count exceeds "
            "max_documents: "
            f"{len(required_documents)} required, "
            f"limit is {maximum_documents}"
        )

    remaining_slots = (
        maximum_documents
        - len(required_documents)
    )

    result = (
        required_documents
        + optional_documents[
            :remaining_slots
        ]
    )

    return result
