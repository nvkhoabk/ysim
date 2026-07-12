from __future__ import annotations

import json
from pathlib import Path

from ysf.execution.models import (
    ExecutionPlan,
    ExecutionRequest,
    ExecutionResult,
)
from ysf.execution.workspace import snapshot_to_payload


class ExecutionReportError(RuntimeError):
    """Raised when execution reports cannot be written."""


def write_execution_report(
    repository_root: Path,
    request: ExecutionRequest,
    plan: ExecutionPlan,
    result: ExecutionResult,
    output_directory: Path,
) -> tuple[Path, Path]:
    resolved_output = (
        output_directory
        if output_directory.is_absolute()
        else repository_root / output_directory
    )

    resolved_output.mkdir(
        parents=True,
        exist_ok=True,
    )

    json_path = resolved_output / "report.json"
    markdown_path = resolved_output / "report.md"

    payload = {
        "schemaVersion": "1.0",
        "request": request.to_dict(),
        "plan": plan.to_dict(),
        "workspaceSnapshot": snapshot_to_payload(
            plan.workspace
        ),
        "result": result.to_dict(),
    }

    try:
        json_path.write_text(
            json.dumps(
                payload,
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

        markdown_path.write_text(
            "\n".join([
                "# YSF Execution Report",
                "",
                f"- Execution ID: `{result.execution_id}`",
                f"- Status: **{result.status}**",
                f"- Provider: `{result.provider}`",
                f"- Mode: `{result.mode}`",
                f"- Dry run: `{result.dry_run}`",
                f"- Prompt: `{plan.prompt_path}`",
                f"- Branch: `{plan.workspace.branch}`",
                f"- HEAD: `{plan.workspace.head_commit}`",
                (
                    "- Working tree clean: "
                    f"`{plan.workspace.working_tree_clean}`"
                ),
                f"- Started: `{result.started_at}`",
                f"- Finished: `{result.finished_at}`",
                "",
                "## Message",
                "",
                result.message,
                "",
                "## Modified Files",
                "",
                *(
                    [
                        f"- `{path}`"
                        for path in result.modified_files
                    ]
                    if result.modified_files
                    else ["- None"]
                ),
                "",
                "## Provider Output",
                "",
                "```text",
                result.stdout or "(empty)",
                "```",
                "",
                "## Errors",
                "",
                "```text",
                result.stderr or "(empty)",
                "```",
                "",
            ]),
            encoding="utf-8",
        )
    except OSError as exc:
        raise ExecutionReportError(
            f"Cannot write execution report: {exc}"
        ) from exc

    return json_path, markdown_path
