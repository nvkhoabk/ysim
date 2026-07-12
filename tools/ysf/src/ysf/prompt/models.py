from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class PromptArtifact:
    prompt_id: str
    sprint: str
    task: str
    provider: str
    template: str
    context_manifest: str
    context_content: str
    output_directory: str
    prompt_file: str
    prompt_hash: str
    character_count: int
    estimated_tokens: int
    source_documents: list[str] = field(default_factory=list)
    validation_commands: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "promptId": self.prompt_id,
            "sprint": self.sprint,
            "task": self.task,
            "provider": self.provider,
            "template": self.template,
            "contextManifest": self.context_manifest,
            "contextContent": self.context_content,
            "outputDirectory": self.output_directory,
            "promptFile": self.prompt_file,
            "promptHash": self.prompt_hash,
            "characterCount": self.character_count,
            "estimatedTokens": self.estimated_tokens,
            "sourceDocuments": self.source_documents,
            "validationCommands": self.validation_commands,
        }
