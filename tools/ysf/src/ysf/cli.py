from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ysf import __version__
from ysf.context.service import build_context
from ysf.core.doctor import run_doctor
from ysf.core.repository import (
    RepositoryError,
    find_repository_root,
)
from ysf.core.result import CommandResult
from ysf.execution.service import run_dry_execution
from ysf.index.service import build_indexes
from ysf.knowledge.service import build_knowledge
from ysf.pipeline.service import run_pipeline
from ysf.prompt.service import build_prompt
from ysf.verification.service import run_verification


def print_result(
    result: CommandResult,
    as_json: bool,
) -> None:
    if as_json:
        print(
            json.dumps(
                result.to_dict(),
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    print(
        f"[{result.status}] "
        f"{result.message}"
    )

    if result.command == "doctor":
        tools = result.data.get("tools", {})
        paths = result.data.get("paths", {})

        for name, value in tools.items():
            state = (
                value
                if value is not None
                else "MISSING"
            )
            print(f"  {name}: {state}")

        for name, value in paths.items():
            state = (
                "FOUND"
                if value
                else "MISSING"
            )
            print(f"  {name}: {state}")

    elif result.command == "build-index":
        print(
            "  documents: "
            f"{result.data['documentCount']}"
        )
        print(
            "  knowledge: "
            f"{result.data['knowledgeCount']}"
        )

    elif result.command == "build-knowledge":
        print(
            "  documents: "
            f"{result.data['documentCount']}"
        )
        print(
            "  capabilities: "
            f"{result.data['capabilityCount']}"
        )
        print(
            "  integrations: "
            f"{result.data['integrationCount']}"
        )
        print(
            "  relationships: "
            f"{result.data['relationshipCount']}"
        )

    elif result.command == "pipeline":
        stages = result.data.get("stages", [])

        for stage in stages:
            print(
                f"  [{stage['status']}] "
                f"{stage['order']:02d} "
                f"{stage['name']} "
                f"({stage['duration_seconds']:.3f}s)"
            )

            if stage["status"] != "PASS":
                print(
                    f"    {stage['message']}"
                )

    elif result.command == "build-context":
        print(
            "  context: "
            f"{result.data['contextId']}"
        )
        print(
            "  documents: "
            f"{result.data['documentCount']}"
        )
        print(
            "  characters: "
            f"{result.data['characterCount']}"
        )
        print(
            "  output: "
            f"{result.data['outputDirectory']}"
        )

    elif result.command == "build-prompt":
        print(
            f"  prompt: "
            f"{result.data['promptId']}"
        )
        print(
            f"  provider: "
            f"{result.data['provider']}"
        )
        print(
            f"  characters: "
            f"{result.data['characterCount']}"
        )
        print(
            f"  estimated tokens: "
            f"{result.data['estimatedTokens']}"
        )
        print(
            f"  output: "
            f"{result.data['promptFile']}"
        )

    elif result.command == "verify":
        for check in result.data["checks"]:
            print(
                f"  [{check['status']}] "
                f"{check['name']}"
            )

        if result.data["failedChecks"]:
            print(
                "  failed: "
                + ", ".join(
                    result.data[
                        "failedChecks"
                    ]
                )
            )

    elif result.command == "run":
        print(
            "  execution: "
            f"{result.data['executionId']}"
        )
        print(
            "  provider: "
            f"{result.data['provider']}"
        )
        print(
            "  mode: "
            f"{result.data['mode']}"
        )
        print(
            "  provider invoked: "
            f"{result.data['providerInvoked']}"
        )
        print(
            "  modified files: "
            f"{result.data['modifiedFileCount']}"
        )
        print(
            "  report: "
            f"{result.data['reportJson']}"
        )


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ysf",
        description=(
            "YSim Software Factory "
            "production toolchain"
        ),
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    doctor_parser = subparsers.add_parser(
        "doctor",
        help="Validate the YSF environment.",
    )
    doctor_parser.add_argument(
        "--json",
        action="store_true",
    )

    build_index_parser = subparsers.add_parser(
        "build-index",
        help="Build Factory indexes.",
    )
    build_index_parser.add_argument(
        "--json",
        action="store_true",
    )

    build_knowledge_parser = (
        subparsers.add_parser(
            "build-knowledge",
            help="Build Knowledge catalogs.",
        )
    )
    build_knowledge_parser.add_argument(
        "--json",
        action="store_true",
    )

    build_context_parser = (
        subparsers.add_parser(
            "build-context",
            help="Build a Context Package.",
        )
    )

    build_context_parser.add_argument(
        "--manifest",
        default=(
            "factory/context-manifests/"
            "s00.yaml"
        ),
        help="Context manifest path.",
    )

    build_context_parser.add_argument(
        "--json",
        action="store_true",
    )

    build_prompt_parser = (
        subparsers.add_parser(
            "build-prompt",
            help="Build a Prompt Artifact.",
        )
    )

    build_prompt_parser.add_argument(
        "--manifest",
        default=(
            "factory/prompt-manifests/"
            "s00-t00.yaml"
        ),
    )

    build_prompt_parser.add_argument(
        "--json",
        action="store_true",
    )

    pipeline_parser = subparsers.add_parser(
        "pipeline",
        help="Run registered YSF stages.",
    )
    pipeline_parser.add_argument(
        "--json",
        action="store_true",
    )
    pipeline_parser.add_argument(
        "--stage",
        action="append",
        dest="stages",
        help=(
            "Run only the named stage. "
            "May be supplied multiple times."
        ),
    )
    pipeline_parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help=(
            "Continue remaining stages "
            "after a failure."
        ),
    )
    verify_parser = subparsers.add_parser(
        "verify",
        help="Run the complete YSF quality gate.",
    )

    verify_parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )

    run_parser = subparsers.add_parser(
        "run",
        help="Run an execution plan.",
    )

    run_parser.add_argument(
        "--prompt-artifact",
        default=(
            "factory/prompts/generated/"
            "s00/t00/prompt.json"
        ),
        help="Path to prompt.json.",
    )

    run_parser.add_argument(
        "--provider",
        default=None,
        help="Override the provider.",
    )

    run_parser.add_argument(
        "--execution-id",
        default=None,
        help="Optional execution ID.",
    )

    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help=(
            "Run without invoking an AI provider "
            "or modifying files."
        ),
    )

    run_parser.add_argument(
        "--json",
        action="store_true",
    )

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    try:
        repository_root = find_repository_root()

        result: CommandResult

        if args.command == "doctor":
            result = run_doctor(
                repository_root
            )

        elif args.command == "build-index":
            result = build_indexes(
                repository_root
            )

        elif args.command == "build-knowledge":
            result = build_knowledge(
                repository_root
            )

        elif args.command == "build-context":
            manifest_path = Path(
                args.manifest
            )

            if not manifest_path.is_absolute():
                manifest_path = (
                    repository_root
                    / manifest_path
                )

            result = build_context(
                repository_root=(
                    repository_root
                ),
                manifest_path=(
                    manifest_path
                ),
            )

        elif args.command == "build-prompt":
            manifest_path = Path(
                args.manifest
            )

            if not manifest_path.is_absolute():
                manifest_path = (
                    repository_root
                    / manifest_path
                )

            result = build_prompt(
                repository_root=repository_root,
                manifest_path=manifest_path,
            )

        elif args.command == "pipeline":
            result = run_pipeline(
                repository_root=repository_root,
                stage_names=args.stages,
                fail_fast=(
                    not args.continue_on_error
                ),
            )

        elif args.command == "verify":
            result = run_verification(
                repository_root
            )

        elif args.command == "run":
            if not args.dry_run:
                parser.error(
                    "Step 14E requires --dry-run."
                )
                return 2

            prompt_artifact_path = Path(
                args.prompt_artifact
            )

            if not prompt_artifact_path.is_absolute():
                prompt_artifact_path = (
                    repository_root
                    / prompt_artifact_path
                )

            result = run_dry_execution(
                repository_root=repository_root,
                prompt_artifact_path=(
                    prompt_artifact_path
                ),
                provider=args.provider,
                execution_id=(
                    args.execution_id
                ),
                mode="dry-run",
            )

        else:
            parser.error(
                f"Unsupported command: "
                f"{args.command}"
            )
            return 2

        print_result(
            result=result,
            as_json=args.json,
        )

        return (
            0
            if result.successful
            else 1
        )

    except RepositoryError as exc:
        print(
            f"ERROR: {exc}",
            file=sys.stderr,
        )
        return 4

    except Exception as exc:
        print(
            f"ERROR: {exc}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
