import json
import shutil
from collections import Counter
from pathlib import Path

import yaml

from ysf.index.service import build_indexes
from ysf.knowledge.service import (
    build_knowledge,
)


def _fresh_docs_repository(tmp_path: Path) -> Path:
    source_root = Path.cwd().parents[1]
    repository_root = tmp_path / "repository"
    shutil.copytree(source_root / "docs", repository_root / "docs")
    shutil.copytree(source_root / "knowledge", repository_root / "knowledge")
    return repository_root


def _summary(repository_root: Path) -> dict[str, object]:
    payload = json.loads(
        (repository_root / "knowledge/catalog/summary.json").read_text(encoding="utf-8")
    )
    assert isinstance(payload, dict)
    return payload


def _current_markdown_paths(repository_root: Path) -> tuple[str, ...]:
    docs_root = repository_root / "docs"
    return tuple(
        sorted(
            path.relative_to(repository_root).as_posix()
            for path in docs_root.rglob("*.md")
            if path.is_file()
        )
    )


def _current_document_codes(repository_root: Path) -> tuple[str, ...]:
    codes: list[str] = []
    for relative in _current_markdown_paths(repository_root):
        text = (repository_root / relative).read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            continue
        metadata = yaml.safe_load(text[4:].split("\n---\n", 1)[0])
        if isinstance(metadata, dict) and isinstance(metadata.get("document_code"), str):
            codes.append(metadata["document_code"])
    return tuple(codes)


def _current_knowledge_record_count(repository_root: Path) -> int:
    allowed = {".json", ".md", ".yaml", ".yml"}
    return sum(
        1
        for path in (repository_root / "knowledge").rglob("*")
        if path.is_file() and path.name != ".gitkeep" and path.suffix.lower() in allowed
    )


def _assert_current_document_boundary(repository_root: Path) -> int:
    paths = _current_markdown_paths(repository_root)
    codes = _current_document_codes(repository_root)
    duplicates = sum(count - 1 for count in Counter(codes).values() if count > 1)
    assert len(paths) == 125
    assert len(codes) == 123
    assert duplicates == 0
    return len(paths)


def test_build_knowledge_uses_current_docs_without_tracked_index(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
    expected_documents = _assert_current_document_boundary(repository_root)

    result = build_knowledge(repository_root)

    assert result.successful
    assert result.data == {
        "documentCount": expected_documents,
        "capabilityCount": 8,
        "integrationCount": 0,
        "relationshipCount": 48,
        "outputs": result.data["outputs"],
    }
    assert not (repository_root / "factory/index/documents.json").exists()
    assert _summary(repository_root)["sourceIndex"] == "in-memory:docs/**/*.md"


def test_stale_or_poisoned_tracked_index_cannot_change_fresh_result(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
    expected_documents = _assert_current_document_boundary(repository_root)
    tracked = repository_root / "factory/index/documents.json"
    tracked.parent.mkdir(parents=True)
    tracked.write_text(
        json.dumps({"documentCount": 999, "documents": "poisoned stale input"}),
        encoding="utf-8",
    )

    first = build_knowledge(repository_root)
    tracked.write_text("not-json", encoding="utf-8")
    second = build_knowledge(repository_root)

    assert first.data["documentCount"] == second.data["documentCount"] == expected_documents
    assert first.data["relationshipCount"] == second.data["relationshipCount"] == 48
    assert _summary(repository_root)["sourceIndex"] == "in-memory:docs/**/*.md"


def test_synthetic_document_add_change_and_remove_refreshes_each_run(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
    expected_documents = _assert_current_document_boundary(repository_root)
    synthetic = repository_root / "docs/SYNTHETIC/SYNTHETIC-R2-001.md"
    synthetic.parent.mkdir(parents=True)
    synthetic.write_text(
        "\n".join(
            (
                "---",
                "document_code: SYNTHETIC-R2-001",
                "document_name: Synthetic R2 Document",
                "project: YSim v3",
                "document_set: SYNTHETIC",
                "version: 0.0.0",
                "status: DRAFT",
                "language: en",
                "---",
                "# Synthetic R2 Document",
                "",
            )
        ),
        encoding="utf-8",
    )

    added = build_knowledge(repository_root)
    assert added.data["documentCount"] == expected_documents + 1
    synthetic.write_text(
        synthetic.read_text(encoding="utf-8").replace(
            "# Synthetic R2 Document", "# Synthetic R2 Document Changed"
        ),
        encoding="utf-8",
    )
    build_knowledge(repository_root)
    documents = json.loads(
        (repository_root / "knowledge/catalog/documents.json").read_text(encoding="utf-8")
    )["documents"]
    matched = [item for item in documents if item["documentCode"] == "SYNTHETIC-R2-001"]
    assert [item["title"] for item in matched] == ["Synthetic R2 Document Changed"]
    synthetic.unlink()
    removed = build_knowledge(repository_root)
    assert removed.data["documentCount"] == expected_documents


def test_index_then_knowledge_bind_the_same_current_document_set(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
    expected_documents = _assert_current_document_boundary(repository_root)
    expected_knowledge_records = _current_knowledge_record_count(repository_root)

    index = build_indexes(repository_root)
    knowledge = build_knowledge(repository_root)

    assert index.data["documentCount"] == knowledge.data["documentCount"] == expected_documents
    assert index.data["knowledgeCount"] == expected_knowledge_records == 14
    assert knowledge.data["capabilityCount"] == 8
    assert knowledge.data["integrationCount"] == 0
    assert knowledge.data["relationshipCount"] == 48
    assert _summary(repository_root)["documentCount"] == expected_documents
