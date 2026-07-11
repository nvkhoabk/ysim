from __future__ import annotations

from pathlib import Path

from ysf.core.result import CommandResult
from ysf.index.catalog import (
    build_master_catalog,
    write_master_catalog,
)
from ysf.index.documents import (
    build_document_index,
    write_document_index,
)
from ysf.index.knowledge import (
    build_knowledge_index,
    write_knowledge_index,
)


def build_indexes(repository_root: Path) -> CommandResult:
    document_index = build_document_index(repository_root)
    knowledge_index = build_knowledge_index(repository_root)

    document_output = write_document_index(
        repository_root,
        document_index,
    )
    knowledge_output = write_knowledge_index(
        repository_root,
        knowledge_index,
    )

    catalog = build_master_catalog(
        document_index=document_index,
        knowledge_index=knowledge_index,
    )

    catalog_output = write_master_catalog(
        repository_root,
        catalog,
    )

    return CommandResult(
        command="build-index",
        status="PASS",
        message="Factory indexes generated successfully.",
        data={
            "documentCount": document_index["documentCount"],
            "knowledgeCount": knowledge_index["knowledgeCount"],
            "outputs": [
                document_output.relative_to(
                    repository_root
                ).as_posix(),
                knowledge_output.relative_to(
                    repository_root
                ).as_posix(),
                catalog_output.relative_to(
                    repository_root
                ).as_posix(),
            ],
        },
    )
