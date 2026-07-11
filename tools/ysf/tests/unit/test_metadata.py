from pathlib import Path

from ysf.index.metadata import parse_frontmatter


def test_parse_frontmatter(tmp_path: Path) -> None:
    document = tmp_path / "DOC-01.md"

    document.write_text(
        "\n".join([
            "---",
            "document_code: DOC-01",
            "version: 2.1",
            "status: FROZEN",
            "---",
            "",
            "# Document",
        ]),
        encoding="utf-8",
    )

    metadata = parse_frontmatter(document)

    assert metadata["document_code"] == "DOC-01"
    assert metadata["version"] == "2.1"
    assert metadata["status"] == "FROZEN"
