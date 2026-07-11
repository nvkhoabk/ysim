from __future__ import annotations

import hashlib
from typing import Any

from ysf.knowledge.models import KnowledgeDocument
from ysf.knowledge.patterns import DOCUMENT_SET_LAYER


def stable_id(prefix: str, *parts: str) -> str:
    payload = "\x1f".join(parts).encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()[:16]
    return f"{prefix}-{digest}"


def normalize_document(
    raw: dict[str, Any],
) -> KnowledgeDocument:
    path = str(raw.get("path") or "").strip()
    filename = str(
        raw.get("filename") or path.rsplit("/", 1)[-1]
    ).strip()

    document_set = str(
        raw.get("documentSet") or "UNKNOWN"
    ).strip()

    code = raw.get("documentCode")
    title = raw.get("title")
    version = raw.get("version")
    status = raw.get("status")
    navigation = bool(
        raw.get("generatedNavigation", False)
    )

    normalized_code = (
        str(code).strip()
        if code is not None
        else None
    )

    normalized_title = (
        str(title).strip()
        if title is not None
        else None
    )

    searchable_text = " ".join(
        item
        for item in (
            normalized_code,
            normalized_title,
            filename,
            document_set,
        )
        if item
    ).lower()

    return KnowledgeDocument(
        id=normalized_code or stable_id("doc", path),
        path=path,
        filename=filename,
        document_set=document_set,
        layer=DOCUMENT_SET_LAYER.get(
            document_set,
            "other",
        ),
        document_code=normalized_code,
        title=normalized_title,
        version=(
            str(version).strip()
            if version is not None
            else None
        ),
        status=(
            str(status).strip()
            if status is not None
            else None
        ),
        generated_navigation=navigation,
        searchable_text=searchable_text,
    )
