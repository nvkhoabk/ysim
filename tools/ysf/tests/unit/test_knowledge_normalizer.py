from ysf.knowledge.normalizer import (
    normalize_document,
)


def test_normalize_document() -> None:
    document = normalize_document({
        "path": "docs/BRD/BRD-01.md",
        "filename": "BRD-01.md",
        "documentSet": "BRD",
        "documentCode": "BRD-01",
        "title": "Product Catalog",
        "version": "2.1",
        "status": "FROZEN",
        "generatedNavigation": False,
    })

    assert document.id == "BRD-01"
    assert document.layer == "business"
    assert "product catalog" in (
        document.searchable_text
    )
