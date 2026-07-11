from ysf.context.selector import (
    select_documents,
)


def test_required_documents_are_preserved() -> None:
    documents = [
        {
            "path": "docs/Z/Z-01.md",
            "documentCode": "Z-01",
            "documentSet": "Z",
            "generatedNavigation": False,
        },
        {
            "path": "docs/A/A-01.md",
            "documentCode": "A-01",
            "documentSet": "A",
            "generatedNavigation": False,
        },
        {
            "path": "docs/A/A-02.md",
            "documentCode": "A-02",
            "documentSet": "A",
            "generatedNavigation": False,
        },
    ]

    manifest = {
        "documents": {
            "required": ["Z-01"],
        },
        "document_sets": {
            "include": ["A", "Z"],
        },
        "capabilities": [],
        "limits": {
            "max_documents": 2,
        },
    }

    selected = select_documents(
        documents=documents,
        capabilities_catalog={
            "capabilities": [],
        },
        manifest=manifest,
    )

    selected_codes = {
        document["documentCode"]
        for document in selected
    }

    assert "Z-01" in selected_codes
    assert len(selected) == 2
