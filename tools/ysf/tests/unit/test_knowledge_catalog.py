from ysf.knowledge.catalog import (
    build_named_catalog,
)
from ysf.knowledge.models import (
    KnowledgeDocument,
)


def test_build_named_catalog() -> None:
    document = KnowledgeDocument(
        id="BRD-01",
        path="docs/BRD/BRD-01.md",
        filename="BRD-01.md",
        document_set="BRD",
        layer="business",
        document_code="BRD-01",
        title="Product Catalog",
        version="2.1",
        status="FROZEN",
        generated_navigation=False,
        searchable_text="product catalog",
    )

    catalog, relationships = (
        build_named_catalog(
            documents=[document],
            patterns={
                "product-catalog": (
                    "product",
                ),
            },
            relationship_type=(
                "references-capability"
            ),
        )
    )

    assert len(catalog) == 1
    assert (
        catalog[0]["id"]
        == "product-catalog"
    )
    assert len(relationships) == 1
