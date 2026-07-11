from pathlib import Path

from ysf.index.documents import build_document_index


def test_build_document_index(tmp_path: Path) -> None:
    docs = tmp_path / "docs" / "TEST"
    docs.mkdir(parents=True)

    factory = tmp_path / "factory"
    factory.mkdir()

    document = docs / "TEST-01.md"

    document.write_text(
        "\n".join([
            "---",
            "document_code: TEST-01",
            "document_name: Test Document",
            "project: YSim v2.1",
            "document_set: Test",
            "version: 2.1",
            "status: FROZEN",
            "language: en-US",
            "---",
            "",
            "# Test Document",
        ]),
        encoding="utf-8",
    )

    index = build_document_index(tmp_path)

    assert index["documentCount"] == 1
    assert index["documents"][0]["documentCode"] == "TEST-01"
    assert index["documents"][0]["title"] == "Test Document"
