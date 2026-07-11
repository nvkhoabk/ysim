from pathlib import Path

from ysf.index.service import build_indexes


def test_build_indexes_in_repository() -> None:
    repository_root = Path.cwd().parents[1]

    result = build_indexes(repository_root)

    assert result.successful
    assert result.data["documentCount"] > 0
    assert (
        repository_root / "factory/index/documents.json"
    ).is_file()
