from __future__ import annotations

import argparse
import json
import sys

from ysf import __version__
from ysf.core.doctor import run_doctor
from ysf.core.repository import RepositoryError, find_repository_root
from ysf.index.service import build_indexes


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ysf",
        description="YSim Software Factory production toolchain",
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
        help="Print machine-readable JSON.",
    )

    build_index_parser = subparsers.add_parser(
        "build-index",
        help="Build documentation and knowledge indexes.",
    )

    build_index_parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()

    try:
        repository_root = find_repository_root()
    except RepositoryError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 4

    if args.command == "doctor":
        result = run_doctor(repository_root)

        if args.json:
            print(
                json.dumps(
                    result.to_dict(),
                    indent=2,
                    ensure_ascii=False,
                )
            )
        else:
            print(f"[{result.status}] {result.message}")

            for name, value in result.data["tools"].items():
                state = value if value is not None else "MISSING"
                print(f"  {name}: {state}")

            for name, value in result.data["paths"].items():
                print(f"  {name}: {'FOUND' if value else 'MISSING'}")

        return 0 if result.successful else 1

    if args.command == "build-index":
        result = build_indexes(repository_root)

        if args.json:
            print(
                json.dumps(
                    result.to_dict(),
                    indent=2,
                    ensure_ascii=False,
                )
            )
        else:
            print(f"[{result.status}] {result.message}")
            print(
                f"  documents: "
                f"{result.data['documentCount']}"
            )
            print(
                f"  knowledge: "
                f"{result.data['knowledgeCount']}"
            )

            for output in result.data["outputs"]:
                print(f"  output: {output}")

        return 0 if result.successful else 1

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
