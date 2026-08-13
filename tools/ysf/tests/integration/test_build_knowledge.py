import json
import shutil
from pathlib import Path

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


def test_build_knowledge_uses_current_docs_without_tracked_index(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)

    result = build_knowledge(repository_root)

    assert result.successful
    assert result.data == {
        "documentCount": 124,
        "capabilityCount": 8,
        "integrationCount": 0,
        "relationshipCount": 48,
        "outputs": result.data["outputs"],
    }
    assert not (repository_root / "factory/index/documents.json").exists()
    assert _summary(repository_root)["sourceIndex"] == "in-memory:docs/**/*.md"


def test_stale_or_poisoned_tracked_index_cannot_change_fresh_result(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
    tracked = repository_root / "factory/index/documents.json"
    tracked.parent.mkdir(parents=True)
    tracked.write_text(
        json.dumps({"documentCount": 999, "documents": "poisoned stale input"}),
        encoding="utf-8",
    )

    first = build_knowledge(repository_root)
    tracked.write_text("not-json", encoding="utf-8")
    second = build_knowledge(repository_root)

    assert first.data["documentCount"] == second.data["documentCount"] == 124
    assert first.data["relationshipCount"] == second.data["relationshipCount"] == 48
    assert _summary(repository_root)["sourceIndex"] == "in-memory:docs/**/*.md"


def test_synthetic_document_add_change_and_remove_refreshes_each_run(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)
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
    assert added.data["documentCount"] == 125
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
    assert removed.data["documentCount"] == 124


def test_index_then_knowledge_bind_the_same_current_document_set(tmp_path: Path) -> None:
    repository_root = _fresh_docs_repository(tmp_path)

    index = build_indexes(repository_root)
    knowledge = build_knowledge(repository_root)

    assert index.data["documentCount"] == knowledge.data["documentCount"] == 124
    assert index.data["knowledgeCount"] == 14
    assert knowledge.data["capabilityCount"] == 8
    assert knowledge.data["relationshipCount"] == 48
    assert _summary(repository_root)["documentCount"] == 124
