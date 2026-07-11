from pathlib import Path

from ysf.knowledge.service import (
    build_knowledge,
)


def test_build_knowledge_in_repository() -> None:
    repository_root = Path.cwd().parents[1]

    result = build_knowledge(
        repository_root
    )

    assert result.successful
    assert (
        result.data["documentCount"]
        > 0
    )
    assert (
        repository_root
        / "knowledge/catalog/summary.json"
    ).is_file()
