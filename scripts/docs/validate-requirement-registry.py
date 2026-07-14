#!/usr/bin/env python3
"""Build (with --write) and validate the BRD/UXF Phase-1 requirement registry."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/baselines/v2.3"
REGISTRY_DIR = BASE / "requirements"
SETS = {"BRD": ROOT / "docs/BRD", "UXF": ROOT / "docs/UXF"}
REGISTRY_PATHS = {
    "BRD": REGISTRY_DIR / "brd-requirements.json",
    "UXF": REGISTRY_DIR / "uxf-requirements.json",
}
SUMMARY_PATH = REGISTRY_DIR / "registry-summary.json"
INVENTORY_PATH = BASE / "BRD_UXF_INVENTORY.md"
REPORT_PATH = BASE / "REQUIREMENT_REGISTRY_REPORT.md"
QA_PATH = REGISTRY_DIR / "registry-qa.json"
QA_REPORT_PATH = BASE / "REQUIREMENT_REGISTRY_QA.md"
RECONCILIATION_PATH = REGISTRY_DIR / "registry-reconciliation.json"
RECONCILIATION_REPORT_PATH = BASE / "REQUIREMENT_REGISTRY_RECONCILIATION.md"
FRAMEWORK_DECISIONS_PATH = BASE / "FRAMEWORK_DECISIONS.md"
FREEZE_MANIFEST_PATH = REGISTRY_DIR / "registry-freeze-manifest.json"
FREEZE_CANDIDATE_PATH = BASE / "REQUIREMENT_REGISTRY_FREEZE_CANDIDATE.md"
PHASE_1C_REGISTRY_ARTIFACTS = {
    "docs/baselines/v2.3/BRD_UXF_INVENTORY.md": "SOURCE_INVENTORY_REPORT",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_QA.md": "QA_REPORT",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_RECONCILIATION.md": "RECONCILIATION_REPORT",
    "docs/baselines/v2.3/REQUIREMENT_REGISTRY_REPORT.md": "REGISTRY_REPORT",
    "docs/baselines/v2.3/requirements/brd-requirements.json": "BRD_REGISTRY",
    "docs/baselines/v2.3/requirements/registry-qa.json": "QA_DATA",
    "docs/baselines/v2.3/requirements/registry-reconciliation.json": "RECONCILIATION_LEDGER",
    "docs/baselines/v2.3/requirements/registry-summary.json": "REGISTRY_SUMMARY",
    "docs/baselines/v2.3/requirements/uxf-requirements.json": "UXF_REGISTRY",
}
PHASE_1C_VALIDATOR_ARTIFACTS = {
    "scripts/docs/validate-requirement-registry.py": "REGISTRY_VALIDATOR",
}
FREEZE_AGGREGATE_ALGORITHM = (
    "For source_documents, read canonical Git blob bytes from '<source_git_commit>:<relative_posix_path>' and hash those bytes with SHA-256. "
    "For registry_artifacts and validator_artifacts, hash raw artifact bytes with SHA-256. "
    "For each aggregate, sort entries lexicographically by relative POSIX path and SHA-256 the concatenated UTF-8 records "
    "'<path>\\0<lowercase_sha256>\\n'. source_aggregate_hash covers source_documents; "
    "registry_aggregate_hash covers registry_artifacts plus validator_artifacts."
)

SCOPE_VALUES = {"V2.3_ACTIVE", "FUTURE", "DEFERRED", "OUT_OF_SCOPE", "UNCLEAR"}
LIFECYCLE_VALUES = {"DRAFT", "FROZEN", "CURRENT", "DEPRECATED", "SUPERSEDED", "UNCLEAR"}
TYPE_VALUES = {"BUSINESS_DECISION", "DESIGN_PRINCIPLE", "BUSINESS_REQUIREMENT", "UX_REQUIREMENT"}
ACCEPTANCE_VALUES = {"DIRECT", "LINKED", "INFERRED_ONLY", "MISSING"}
SCOPE_BASIS_VALUES = {"SOURCE_EXPLICIT", "FRAMEWORK_DECISION", "BASELINE_INHERITANCE", "HUMAN_REVIEW_REQUIRED"}
REQUIRED_FIELDS = {
    "source_document", "source_anchor", "source_marker", "statement", "current_id",
    "temporary_key", "requirement_type", "scope_status", "lifecycle_status", "priority",
    "acceptance_present", "ambiguity", "duplicate_or_overlap", "referenced_requirements",
    "extraction_kind", "source_fingerprint", "acceptance_status", "acceptance_references",
    "scope_basis", "scope_evidence",
}
DOCUMENT_REQUIRED_FIELDS = {"path", "document_code", "title", "version", "status", "language", "requirement_ids", "requirement_count", "references"}

EXPLICIT_ID_RE = re.compile(
    r"^(?:BD-\d{2}-\d{3}|EP-\d{2}-\d{3}|UXF-\d{3}|"
    r"(?:BO|CAP|EVT|POL|SNP)-EP-\d{3}|(?:BO|CAP|EVT|POL|SNP)-[PR]\d{2}|EVT-C\d{2})$"
)
HEADING_RE = re.compile(r"^(#{2,4})\s+([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)(?:\s+(?:—|–|-)\s+.*)?\s*$")
NORMATIVE_RE = re.compile(
    r"\b(?:must|shall|required|mandatory|cannot|may\s+not|should|always|never|prohibited)\b|"
    r"\b(?:is|are)\s+required\b|(?:^|[-*]\s)(?:\w+\s+){0,2}Required\s*$|"
    r"\bonly\s+(?:be|use|allow|select|access|publish|read|write|create|modify|execute|run)\b|"
    r"bắt buộc|không được|không thể|không cho phép|chỉ được|chỉ có thể|"
    r"\bphải\b|\bcần\b|(?:mọi|hệ thống|platform|configuration|thao tác|tác vụ).{0,80}yêu cầu|"
    r"tuân thủ|\bluôn\b|\bduy nhất\b|không hỗ trợ",
    re.IGNORECASE,
)
AC_RE = re.compile(r"acceptance\s+criteria|acceptance\s*:|given\s+.+\s+when\s+.+\s+then", re.IGNORECASE | re.DOTALL)
REQ_REF_RE = re.compile(
    r"\b(?:BD-\d{2}-\d{3}|EP-\d{2}-\d{3}|UXF-\d{3}|"
    r"(?:BO|CAP|EVT|POL|SNP)-EP-\d{3}|(?:BO|CAP|EVT|POL|SNP)-[PR]\d{2}|EVT-C\d{2})\b"
)
FUTURE_RE = re.compile(r"\bfuture\b|phiên bản sau|post[_ -]?v?2\.3", re.IGNORECASE)
DEFERRED_RE = re.compile(r"\bdeferred\b|trì hoãn", re.IGNORECASE)
OUT_RE = re.compile(r"out[ _-]?of[ _-]?scope|được xem là ngoài phạm vi|ngoài phạm vi (?:phiên bản|version|v2\.3)|không hỗ trợ|not supported|not required for MVP", re.IGNORECASE)
UNCLEAR_RE = re.compile(r"\bTBD\b|to be (?:defined|decided)|open item|chưa xác định|chưa quyết định", re.IGNORECASE)
V23_EXCEPTION_RE = re.compile(
    r"recommendation engine|fraud(?:/risk)? engine|fraud detection|risk engine|approval engine|"
    r"visual store|landing builder|drag-and-drop",
    re.IGNORECASE,
)
ID_LIKE_RE = re.compile(r"\b(?:BD|EP|UXF|BO|CAP|EVT|POL|SNP)-[A-Z0-9]+(?:-[A-Z0-9]+){0,3}\b")
SEMANTIC_CANDIDATE_RE = re.compile(
    NORMATIVE_RE.pattern + r"|\bfuture\b|\bdeferred\b|out[ _-]?of[ _-]?scope|"
    r"phiên bản sau|không hỗ trợ|không thuộc phạm vi|chưa triển khai",
    re.IGNORECASE,
)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def frontmatter(lines: list[str]) -> dict[str, str]:
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"\'')
    return result


def source_files(doc_set: str) -> list[Path]:
    return sorted(path for path in SETS[doc_set].rglob("*") if path.is_file())


def explicit_spans(lines: list[str]) -> list[dict]:
    found = []
    for index, line in enumerate(lines):
        match = HEADING_RE.match(line.strip())
        if not match or not EXPLICIT_ID_RE.match(match.group(2)):
            continue
        end = index + 1
        while end < len(lines):
            stripped = lines[end].strip()
            if stripped == "---" or stripped.startswith("#"):
                break
            end += 1
        body_lines = lines[index + 1:end]
        while body_lines and not body_lines[0].strip():
            body_lines.pop(0)
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()
        statement = "\n".join(body_lines).strip()
        found.append({
            "start": index + 1,
            "end": max(index + 1, end),
            "current_id": match.group(2),
            "statement": statement,
            "marker": line,
            "kind": "EXPLICIT_ID",
        })
    return found


def heading_scope_hint(headings: list[tuple[int, str]], line_index: int) -> str | None:
    applicable = [text for position, text in headings if position < line_index]
    if not applicable:
        return None
    heading = applicable[-1]
    if re.search(r"out of scope", heading, re.IGNORECASE):
        return "OUT_OF_SCOPE"
    if re.search(r"deferred", heading, re.IGNORECASE):
        return "DEFERRED"
    if re.search(r"future|roadmap", heading, re.IGNORECASE):
        return "FUTURE"
    if re.search(r"in scope", heading, re.IGNORECASE):
        return "V2.3_ACTIVE"
    return None


def normative_blocks(lines: list[str], occupied: set[int]) -> list[dict]:
    blocks: list[dict] = []
    index = 0
    frontmatter_end = 0
    fenced: set[int] = set()
    fence_open = False
    for position, line in enumerate(lines):
        if line.strip().startswith("```"):
            fence_open = not fence_open
            fenced.add(position)
        elif fence_open:
            fenced.add(position)
    headings = [(position, line.lstrip("#").strip()) for position, line in enumerate(lines) if line.startswith("#")]
    if lines and lines[0].strip() == "---":
        for pos in range(1, len(lines)):
            if lines[pos].strip() == "---":
                frontmatter_end = pos + 1
                break

    def add(start: int, end: int, statement: str, scope_hint: str | None, marker_index: int | None = None) -> None:
        lowered = statement.lower()
        scoped = bool(scope_hint or FUTURE_RE.search(statement) or DEFERRED_RE.search(statement) or OUT_RE.search(statement))
        normative = bool(NORMATIVE_RE.search(statement))
        if re.search(r"required (?:properties|configuration)|missing required parameter", statement, re.IGNORECASE) and not re.search(r"\b(?:must|shall|mandatory|cannot|should|always|never|only|prohibited)\b|bắt buộc|không được|\bphải\b", statement, re.IGNORECASE):
            normative = False
        if lowered.startswith("điều này giúp đảm bảo") or lowered.startswith("để đảm bảo"):
            normative = False
        if scoped or normative:
            marker_at = start if marker_index is None else marker_index
            blocks.append({
                "start": start + 1,
                "end": end + 1,
                "current_id": None,
                "statement": statement.strip(),
                "marker": lines[marker_at],
                "kind": "NORMATIVE_BLOCK",
                "scope_hint": scope_hint,
            })

    while index < len(lines):
        if index < frontmatter_end or index in occupied or index in fenced:
            index += 1
            continue
        stripped = lines[index].strip()
        if not stripped or stripped == "---" or stripped.startswith("#"):
            index += 1
            continue
        scope_hint = heading_scope_hint(headings, index)

        # A table row is an independently classifiable statement. Header context is retained.
        if stripped.startswith("|"):
            table_start = index
            table_lines = []
            while index < len(lines) and lines[index].strip().startswith("|") and index not in occupied:
                table_lines.append((index, lines[index]))
                index += 1
            header = table_lines[0][1]
            for position, row in table_lines[1:]:
                if re.fullmatch(r"\s*\|?\s*:?-{3,}.*", row):
                    continue
                statement = f"{header}\n{row}"
                strong = re.search(r"\b(?:must|shall|mandatory|required)\b|bắt buộc|không được|\bphải\b", row, re.IGNORECASE)
                if scope_hint or FUTURE_RE.search(row) or DEFERRED_RE.search(row) or OUT_RE.search(row) or strong:
                    add(position, position, statement, scope_hint, marker_index=position)
            continue

        # Each list item is a separate requirement unless governed by a shared introduction below.
        if re.match(r"^(?:[-*]|\d+\.)\s+", stripped):
            start = index
            index += 1
            while index < len(lines):
                nxt = lines[index].strip()
                if not nxt or nxt == "---" or nxt.startswith("#") or nxt.startswith("|") or re.match(r"^(?:[-*]|\d+\.)\s+", nxt) or index in occupied:
                    break
                index += 1
            add(start, index - 1, "\n".join(lines[start:index]), scope_hint)
            continue

        # Plain Markdown paragraph.
        start = index
        index += 1
        while index < len(lines):
            nxt = lines[index].strip()
            if not nxt or nxt == "---" or nxt.startswith("#") or nxt.startswith("```") or nxt.startswith("|") or re.match(r"^(?:[-*]|\d+\.)\s+", nxt) or index in occupied:
                break
            index += 1
        text = "\n".join(lines[start:index]).strip()

        # Colon introductions transfer their normative/scope force to each following item.
        following = index
        while following < len(lines) and not lines[following].strip():
            following += 1
        intro_force = bool(scope_hint or NORMATIVE_RE.search(text) or FUTURE_RE.search(text) or DEFERRED_RE.search(text) or OUT_RE.search(text))
        if text.endswith(":") and following < len(lines) and intro_force and re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[following]):
            cursor = following
            while cursor < len(lines) and re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[cursor]):
                item_start = cursor
                cursor += 1
                while cursor < len(lines) and lines[cursor].strip() and not re.match(r"^\s*(?:[-*]|\d+\.)\s+", lines[cursor]) and not lines[cursor].startswith("#"):
                    cursor += 1
                statement = f"{text}\n\n" + "\n".join(lines[item_start:cursor]).strip()
                add(start, cursor - 1, statement, scope_hint, marker_index=start)
                while cursor < len(lines) and not lines[cursor].strip():
                    cursor += 1
            index = max(index, cursor)
            continue

        # Label/value pairs such as Authentication / Required or a named validation.
        if text.endswith(":") and following < len(lines) and following not in occupied and not lines[following].startswith("#"):
            value_end = following
            while value_end + 1 < len(lines) and lines[value_end + 1].strip() and not lines[value_end + 1].startswith("#"):
                value_end += 1
            combined = f"{text}\n\n" + "\n".join(lines[following:value_end + 1]).strip()
            if NORMATIVE_RE.search(combined) or scope_hint:
                add(start, value_end, combined, scope_hint, marker_index=start)
                index = max(index, value_end + 1)
                continue
        add(start, index - 1, text, scope_hint)
    return blocks


def discover(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    explicit = explicit_spans(lines)
    occupied = set()
    for item in explicit:
        occupied.update(range(item["start"] - 1, item["end"]))
    return sorted(explicit + normative_blocks(lines, occupied), key=lambda item: (item["start"], item["kind"]))


def nearest_heading(lines: list[str], line_number: int) -> str:
    for index in range(min(line_number - 1, len(lines) - 1), -1, -1):
        if lines[index].startswith("#"):
            return lines[index].lstrip("#").strip()
    return ""


def nearest_parent_heading(lines: list[str], line_number: int, own_key: str) -> str:
    for index in range(min(line_number - 2, len(lines) - 1), -1, -1):
        if not lines[index].startswith("#"):
            continue
        heading = lines[index].lstrip("#").strip()
        token = heading.split()[0] if heading.split() else ""
        if re.match(rf"^{re.escape(own_key)}(?:\s|$)", heading) or EXPLICIT_ID_RE.fullmatch(token):
            continue
        return heading
    return ""


def likely_false_positive(lines: list[str], line_number: int, statement: str) -> tuple[bool, str | None]:
    heading = nearest_heading(lines, line_number)
    lowered = statement.lower()
    if "this document should be read together with" in lowered:
        return True, "Reference-list instruction is documentation navigation, not a product requirement."
    if re.search(r"\b(?:architecture decisions applied|impact to future dip|references|traceability)\b", heading, re.IGNORECASE):
        return True, f"Source section '{heading}' is navigation/traceability material."
    if re.search(r"\bAI Implementation Guidelines\b", heading, re.IGNORECASE):
        return True, "Source section is an implementation guideline; requirement ownership/classification needs review."
    if re.match(r"^(?:ví dụ|example|for example)\b", statement.strip(), re.IGNORECASE):
        return True, "Example text may have been extracted as normative."
    return False, None


def acceptance_metadata(lines: list[str], item: dict) -> tuple[str, list[str]]:
    if AC_RE.search(item["statement"]):
        anchor = f"L{item['start']}" if item["start"] == item["end"] else f"L{item['start']}-L{item['end']}"
        return "DIRECT", [anchor]
    false_positive, _ = likely_false_positive(lines, item["start"], item["statement"])
    if false_positive:
        return "MISSING", []
    return "INFERRED_ONLY", []


def scope_provenance(doc_set: str, item: dict, scope: str, ambiguity: str | None) -> tuple[str, str]:
    anchor = f"L{item['start']}" if item["start"] == item["end"] else f"L{item['start']}-L{item['end']}"
    if scope == "UNCLEAR":
        return "HUMAN_REVIEW_REQUIRED", anchor
    if ambiguity and "promoted by FRAMEWORK_DECISIONS" in ambiguity:
        if re.search(r"visual store|landing builder|drag-and-drop", item["statement"], re.IGNORECASE):
            return "FRAMEWORK_DECISION", "UXD-11"
        return "FRAMEWORK_DECISION", "SD-03"
    if scope in {"FUTURE", "DEFERRED", "OUT_OF_SCOPE"} or item.get("scope_hint") == "V2.3_ACTIVE":
        return "SOURCE_EXPLICIT", anchor
    classification = "BRD ADOPTED" if doc_set == "BRD" else "UXF DRAFT_REVIEW"
    return "BASELINE_INHERITANCE", f"V23-DOCUMENT-BASELINE §4 ({classification})"


def lifecycle_for(status: str) -> str:
    normalized = status.strip().upper().replace(" ", "_")
    if normalized in LIFECYCLE_VALUES:
        return normalized
    if normalized in {"APPROVED", "ADOPTED"}:
        return "CURRENT"
    return "UNCLEAR"


def scope_for(statement: str, scope_hint: str | None = None) -> tuple[str, str | None]:
    signals = []
    if DEFERRED_RE.search(statement):
        signals.append("DEFERRED")
    if OUT_RE.search(statement):
        signals.append("OUT_OF_SCOPE")
    if FUTURE_RE.search(statement):
        signals.append("FUTURE")
    if UNCLEAR_RE.search(statement):
        signals.append("UNCLEAR")
    if scope_hint and scope_hint not in signals:
        signals.append(scope_hint)
    if V23_EXCEPTION_RE.search(statement) and any(value in signals for value in ("FUTURE", "DEFERRED", "OUT_OF_SCOPE")):
        return "V2.3_ACTIVE", "Scope is promoted by FRAMEWORK_DECISIONS.md SD-03/UXD-11 despite legacy wording."
    distinct = set(signals)
    if len(distinct) > 1:
        return "UNCLEAR", "Multiple scope signals occur in the same source statement: " + ", ".join(sorted(distinct)) + "."
    if signals:
        return signals[0], None
    if re.search(r"partner portal", statement, re.IGNORECASE):
        return "UNCLEAR", "Partner Portal is POST_V2.3 under SD-04, but this statement may bundle it with active channels."
    return "V2.3_ACTIVE", None


def requirement_type(doc_set: str, canonical_id: str | None) -> str:
    if doc_set == "UXF":
        return "UX_REQUIREMENT"
    if canonical_id and canonical_id.startswith("BD-"):
        return "BUSINESS_DECISION"
    if canonical_id and (canonical_id.startswith("EP-") or "-EP-" in canonical_id or re.match(r"^(?:BO|CAP|EVT|POL|SNP)-[PR]\d{2}$", canonical_id) or canonical_id.startswith("EVT-C")):
        return "DESIGN_PRINCIPLE"
    return "BUSINESS_REQUIREMENT"


def fingerprint(path: Path, item: dict) -> str:
    payload = f"{rel(path)}\0{item['start']}\0{item['end']}\0{item['kind']}\0{item['marker']}"
    return hashlib.sha256(payload.encode()).hexdigest()


def known_document_codes() -> set[str]:
    codes = set()
    for path in (ROOT / "docs").rglob("*.md"):
        meta = frontmatter(path.read_text(encoding="utf-8").splitlines())
        if meta.get("document_code"):
            codes.add(meta["document_code"])
    return codes


def document_references(path: Path, own_code: str, known_codes: set[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    references = {code for code in known_codes if code != own_code and re.search(rf"(?<![A-Z0-9-]){re.escape(code)}(?![A-Z0-9-])", text)}
    reference_sections = []
    active = False
    for line in text.splitlines():
        if line.startswith("# "):
            active = bool(re.search(r"references|traceability|architecture decisions applied", line, re.IGNORECASE))
        if active:
            reference_sections.append(line)
    reference_text = "\n".join(reference_sections)
    for code in re.findall(r"\b(?:AFD-\d{3}|(?:AAP|ABP|AFM|BRD|CAP|DIP|ECS|ESP|PCS|POL|ROP|SGP|UXF|YADF)-\d{2})\b", reference_text):
        if code != own_code:
            references.add(code)
    for doc_set in ("AAP", "ABP", "AFM", "BRD", "CAP", "DIP", "ECS", "ESP", "PCS", "POL", "ROP", "SGP", "UXF", "YADF"):
        if re.search(rf"(?<![A-Z0-9-]){doc_set}(?![A-Z0-9-])", reference_text):
            references.add(f"{doc_set} (document set)")
    return sorted(references)


def build_registry(doc_set: str, known_codes: set[str]) -> dict:
    documents = []
    requirements = []
    for path in source_files(doc_set):
        lines = path.read_text(encoding="utf-8").splitlines()
        meta = frontmatter(lines)
        required_meta = ("document_code", "document_name", "version", "status", "language")
        missing = [field for field in required_meta if not meta.get(field)]
        if missing:
            raise ValueError(f"{rel(path)} missing front matter: {', '.join(missing)}")
        discovered = discover(path)
        temporary_sequence = 0
        doc_requirements = []
        for item in discovered:
            if item["current_id"] is None:
                temporary_sequence += 1
                temporary_key = f"TMP-{meta['document_code']}-{temporary_sequence:03d}"
            else:
                temporary_key = None
            scope, scope_ambiguity = scope_for(item["statement"], item.get("scope_hint"))
            acceptance_status, acceptance_references = acceptance_metadata(lines, item)
            scope_basis, scope_evidence = scope_provenance(doc_set, item, scope, scope_ambiguity)
            req = {
                "source_document": rel(path),
                "source_anchor": f"L{item['start']}" if item["start"] == item["end"] else f"L{item['start']}-L{item['end']}",
                "source_marker": item["marker"],
                "statement": item["statement"],
                "current_id": item["current_id"],
                "temporary_key": temporary_key,
                "requirement_type": requirement_type(doc_set, item["current_id"]),
                "scope_status": scope,
                "lifecycle_status": lifecycle_for(meta["status"]),
                "priority": None,
                "acceptance_present": acceptance_status in {"DIRECT", "LINKED"},
                "acceptance_status": acceptance_status,
                "acceptance_references": acceptance_references,
                "ambiguity": scope_ambiguity,
                "scope_basis": scope_basis,
                "scope_evidence": scope_evidence,
                "duplicate_or_overlap": [],
                "referenced_requirements": [],
                "extraction_kind": item["kind"],
                "source_fingerprint": fingerprint(path, item),
            }
            requirements.append(req)
            doc_requirements.append(req)
        documents.append({
            "path": rel(path),
            "document_code": meta["document_code"],
            "title": meta["document_name"],
            "version": meta["version"],
            "status": meta["status"],
            "language": meta["language"],
            "requirement_ids": [req["current_id"] for req in doc_requirements if req["current_id"]],
            "requirement_count": len(doc_requirements),
            "references": document_references(path, meta["document_code"], known_codes),
        })
    identifiers = {req["current_id"] for req in requirements if req["current_id"]}
    for req in requirements:
        own = req["current_id"]
        refs = sorted(set(REQ_REF_RE.findall(req["statement"])) - ({own} if own else set()))
        req["referenced_requirements"] = refs
    normalized: defaultdict[str, list[dict]] = defaultdict(list)
    for req in requirements:
        norm = re.sub(r"\W+", " ", req["statement"].lower()).strip()
        if norm:
            normalized[norm].append(req)
    for group in normalized.values():
        if len(group) > 1:
            keys = [req["current_id"] or req["temporary_key"] for req in group]
            for req in group:
                own = req["current_id"] or req["temporary_key"]
                req["duplicate_or_overlap"] = [key for key in keys if key != own]
    return {
        "schema_version": "1.0",
        "phase": "Documentation Governance v2.3 Phase 1",
        "document_set": doc_set,
        "documents": documents,
        "requirements": requirements,
    }


def duplicate_values(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def dangling_source_references(registries: dict[str, dict], known_ids: set[str]) -> list[dict]:
    dangling = []
    for name in ("BRD", "UXF"):
        for document in registries[name]["documents"]:
            path = ROOT / document["path"]
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                for reference in REQ_REF_RE.findall(line):
                    if reference not in known_ids:
                        dangling.append({
                            "source_document": document["path"],
                            "source_anchor": f"L{line_number}",
                            "reference": reference,
                        })
    return dangling


def requirement_key(requirement: dict) -> str:
    return requirement["current_id"] or requirement["temporary_key"]


def normalize_statement(statement: str) -> str:
    return re.sub(r"\W+", " ", statement.lower()).strip()


def semantic_signature(statement: str) -> str:
    tokens = re.findall(r"[a-z0-9À-ỹ]+", statement.lower())
    ignored = {
        "must", "shall", "should", "always", "never", "required", "the", "a", "an", "be",
        "is", "are", "every", "each", "mọi", "phải", "luôn", "được", "không", "chỉ", "cần",
    }
    meaningful = sorted(set(token for token in tokens if token not in ignored and len(token) > 1))
    return " ".join(meaningful) if len(meaningful) >= 5 else ""


def overlap_classification(members: list[dict]) -> str:
    statements = [req["statement"].lower() for req in members]
    sources = {req["source_document"] for req in members}
    if any("this document should be read together with" in statement for statement in statements):
        return "LIKELY_FALSE_POSITIVE_NAVIGATION_DUPLICATE"
    if all(source.startswith("docs/UXF/") for source in sources) and len(sources) > 1:
        return "INTENTIONAL_SHARED_UX_STANDARD_CANDIDATE"
    if len(sources) == 1:
        return "POTENTIAL_ACCIDENTAL_SAME_SOURCE_DUPLICATE"
    return "POTENTIAL_ACCIDENTAL_CROSS_DOCUMENT_DUPLICATE"


def build_overlap_analysis(registries: dict[str, dict]) -> dict:
    requirements = [req for registry in registries.values() for req in registry["requirements"]]
    exact_map: defaultdict[tuple[str, str], list[dict]] = defaultdict(list)
    signature_map: defaultdict[tuple[str, str], list[dict]] = defaultdict(list)
    for req in requirements:
        applicability_scope = json.dumps(req.get("applicability_scope"), ensure_ascii=False, sort_keys=True)
        exact_map[(normalize_statement(req["statement"]), applicability_scope)].append(req)
        signature = semantic_signature(req["statement"])
        if signature:
            signature_map[(signature, applicability_scope)].append(req)
    groups = []
    exact_groups = []
    for members in exact_map.values():
        if len(members) < 2:
            continue
        keys = sorted(requirement_key(req) for req in members)
        exact_groups.append({"members": keys, "classification": overlap_classification(members)})
    exact_groups.sort(key=lambda group: group["members"])
    for index, group in enumerate(exact_groups, 1):
        groups.append({"group_id": f"OVL-EXACT-{index:03d}", "kind": "EXACT_DUPLICATE", **group})
    exact_member_sets = {tuple(group["members"]) for group in exact_groups}
    probable_groups = []
    for members in signature_map.values():
        keys = sorted({requirement_key(req) for req in members})
        if len(keys) < 2 or tuple(keys) in exact_member_sets:
            continue
        if len({normalize_statement(req["statement"]) for req in members}) < 2:
            continue
        probable_groups.append({"members": keys, "classification": overlap_classification(members)})
    unique_probable = {tuple(group["members"]): group for group in probable_groups}
    probable_groups = sorted(unique_probable.values(), key=lambda group: group["members"])
    for index, group in enumerate(probable_groups, 1):
        groups.append({"group_id": f"OVL-PROB-{index:03d}", "kind": "PROBABLE_SEMANTIC_OVERLAP", **group})
    pairs = set()
    for group in groups:
        members = group["members"]
        for left_index, left in enumerate(members):
            for right in members[left_index + 1:]:
                pairs.add(tuple(sorted((left, right))))
    pairs_list = [{"left": left, "right": right} for left, right in sorted(pairs)]
    endpoints = {value for pair in pairs for value in pair}
    return {
        "requirements_with_overlap": len(endpoints),
        "unique_overlap_pairs": len(pairs_list),
        "unique_overlap_groups": len(groups),
        "exact_duplicate_groups": len(exact_groups),
        "probable_semantic_overlap_groups": len(probable_groups),
        "pairs": pairs_list,
        "groups": groups,
    }


def independent_candidates(path: Path) -> list[dict]:
    lines = path.read_text(encoding="utf-8").splitlines()
    candidates = []
    seen = set()
    fenced = set()
    open_fence = False
    frontmatter_end = 0
    for position, line in enumerate(lines):
        if line.strip().startswith("```"):
            open_fence = not open_fence
            fenced.add(position)
        elif open_fence:
            fenced.add(position)
    if lines and lines[0].strip() == "---":
        for position in range(1, len(lines)):
            if lines[position].strip() == "---":
                frontmatter_end = position + 1
                break
    explicit_by_line = {item["start"]: item for item in explicit_spans(lines)}
    scope_hint = None
    normative_intro = False
    for index, line in enumerate(lines):
        stripped = line.strip()
        if index < frontmatter_end or index in fenced:
            continue
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            scope_hint = None
            if re.search(r"out of scope", heading, re.IGNORECASE):
                scope_hint = "OUT_OF_SCOPE"
            elif re.search(r"deferred", heading, re.IGNORECASE):
                scope_hint = "DEFERRED"
            elif re.search(r"future|roadmap", heading, re.IGNORECASE):
                scope_hint = "FUTURE"
            elif re.search(r"in scope", heading, re.IGNORECASE):
                scope_hint = "V2.3_ACTIVE"
            if index + 1 in explicit_by_line:
                item = explicit_by_line[index + 1]
                key = (index + 1, "EXPLICIT_ID")
                if key not in seen:
                    candidates.append({"source_anchor": f"L{index + 1}", "line": index + 1, "kind": "EXPLICIT_ID", "text": stripped})
                    seen.add(key)
            normative_intro = False
            continue
        if not stripped or stripped == "---":
            continue
        if stripped.startswith("|") and index + 1 < len(lines) and re.fullmatch(r"\s*\|?\s*:?-{3,}.*", lines[index + 1]):
            normative_intro = False
            continue
        is_list_or_table = bool(re.match(r"^(?:[-*>]|\d+\.|\|)", stripped))
        semantic = bool(SEMANTIC_CANDIDATE_RE.search(stripped))
        inherited = bool((scope_hint or normative_intro) and is_list_or_table and not re.fullmatch(r"\|?\s*:?-{3,}.*", stripped))
        if semantic or inherited:
            kind = "CALLOUT" if stripped.startswith(">") else "TABLE" if stripped.startswith("|") else "BULLET" if is_list_or_table else "PROSE"
            key = (index + 1, kind)
            if key not in seen:
                candidates.append({"source_anchor": f"L{index + 1}", "line": index + 1, "kind": kind, "text": stripped})
                seen.add(key)
        normative_intro = bool(stripped.endswith(":") and semantic)
    return candidates


def classification_findings(registries: dict[str, dict]) -> list[dict]:
    findings = []
    for registry in registries.values():
        for req in registry["requirements"]:
            path = ROOT / req["source_document"]
            lines = path.read_text(encoding="utf-8").splitlines()
            anchor = parse_anchor(req["source_anchor"])
            heading = nearest_heading(lines, anchor[0] if anchor else 1)
            if req["temporary_key"] and re.search(r"principle|governance|rule|policy|AI Implementation Guidelines", heading, re.IGNORECASE):
                findings.append({
                    "key": requirement_key(req),
                    "source_document": req["source_document"],
                    "source_anchor": req["source_anchor"],
                    "current_type": req["requirement_type"],
                    "finding": "TEMP_TYPE_POSITION_CONFUSION",
                    "evidence": f"Nearest source heading is '{heading}'; temporary-key status alone does not establish BUSINESS_REQUIREMENT/UX_REQUIREMENT semantics.",
                })
            if req["current_id"]:
                parent = nearest_parent_heading(lines, anchor[0] if anchor else 1, req["current_id"])
                position_consistent = True
                if req["current_id"].startswith("BD-"):
                    position_consistent = bool(re.search(r"business decisions", parent, re.IGNORECASE))
                elif req["requirement_type"] == "DESIGN_PRINCIPLE":
                    position_consistent = bool(re.search(r"principle|rule", parent, re.IGNORECASE))
                elif req["current_id"].startswith("UXF-"):
                    position_consistent = bool(re.search(r"principle", parent, re.IGNORECASE))
                if not position_consistent:
                    findings.append({
                        "key": requirement_key(req),
                        "source_document": req["source_document"],
                        "source_anchor": req["source_anchor"],
                        "current_type": req["requirement_type"],
                        "finding": "ID_PREFIX_POSITION_CONFUSION",
                        "evidence": f"Prefix-derived type is not confirmed by parent source heading '{parent}'.",
                    })
    return sorted(findings, key=lambda item: (item["key"], item["source_document"]))


def extraction_audit(registries: dict[str, dict]) -> tuple[list[dict], dict]:
    requirements_by_source: defaultdict[str, list[dict]] = defaultdict(list)
    for registry in registries.values():
        for req in registry["requirements"]:
            requirements_by_source[req["source_document"]].append(req)
    all_false_negatives = []
    per_file = []
    for name in ("BRD", "UXF"):
        for path in source_files(name):
            source = rel(path)
            reqs = requirements_by_source[source]
            candidates = independent_candidates(path)
            ranges = []
            for req in reqs:
                anchor = parse_anchor(req["source_anchor"])
                if anchor:
                    ranges.append((anchor[0], anchor[1], req))
            matched_candidate_count = 0
            false_negatives = []
            matched_keys = set()
            for candidate in candidates:
                matches = [req for start, end, req in ranges if start <= candidate["line"] <= end]
                if matches:
                    matched_candidate_count += 1
                    matched_keys.update(requirement_key(req) for req in matches)
                else:
                    finding = {"source_document": source, **candidate, "finding": "FALSE_NEGATIVE_CANDIDATE"}
                    false_negatives.append(finding)
                    all_false_negatives.append(finding)
            false_positives = []
            compounds = []
            normalized: defaultdict[str, list[str]] = defaultdict(list)
            lines = path.read_text(encoding="utf-8").splitlines()
            for req in reqs:
                key = requirement_key(req)
                anchor = parse_anchor(req["source_anchor"])
                likely, reason = likely_false_positive(lines, anchor[0] if anchor else 1, req["statement"])
                if key not in matched_keys or likely:
                    false_positives.append({
                        "key": key,
                        "source_anchor": req["source_anchor"],
                        "reason": reason or "Registry entry has no match in the independent semantic candidate scan.",
                    })
                bullet_count = len(re.findall(r"(?m)^\s*[-*]\s+", req["statement"]))
                modal_count = len(SEMANTIC_CANDIDATE_RE.findall(req["statement"]))
                if bullet_count >= 2 or modal_count >= 2:
                    compounds.append({
                        "key": key,
                        "source_anchor": req["source_anchor"],
                        "bullet_count": bullet_count,
                        "normative_signal_count": modal_count,
                        "finding": "COMPOUND_STATEMENT_CANDIDATE",
                    })
                normalized[normalize_statement(req["statement"])].append(key)
            same_source_duplicates = [
                {"members": sorted(keys), "finding": "SAME_SOURCE_DUPLICATE_EXTRACTION_CANDIDATE"}
                for keys in normalized.values() if len(keys) > 1
            ]
            same_source_duplicates.sort(key=lambda item: item["members"])
            per_file.append({
                "source_document": source,
                "document_set": name,
                "candidate_count": len(candidates),
                "matched_candidate_count": matched_candidate_count,
                "false_negative_candidate_count": len(false_negatives),
                "registry_requirement_count": len(reqs),
                "false_positive_candidate_count": len(false_positives),
                "compound_statement_candidate_count": len(compounds),
                "same_source_duplicate_group_count": len(same_source_duplicates),
                "false_negative_candidates": false_negatives,
                "false_positive_candidates": false_positives,
                "compound_statement_candidates": compounds,
                "same_source_duplicate_groups": same_source_duplicates,
            })
    totals = {
        "file_count": len(per_file),
        "candidate_count": sum(item["candidate_count"] for item in per_file),
        "matched_candidate_count": sum(item["matched_candidate_count"] for item in per_file),
        "false_negative_candidate_count": sum(item["false_negative_candidate_count"] for item in per_file),
        "registry_requirement_count": sum(item["registry_requirement_count"] for item in per_file),
        "false_positive_candidate_count": sum(item["false_positive_candidate_count"] for item in per_file),
        "compound_statement_candidate_count": sum(item["compound_statement_candidate_count"] for item in per_file),
        "same_source_duplicate_group_count": sum(item["same_source_duplicate_group_count"] for item in per_file),
    }
    return per_file, totals


def raw_reference_audit(registries: dict[str, dict]) -> dict:
    requirements = [req for registry in registries.values() for req in registry["requirements"]]
    canonical_ids = {req["current_id"] for req in requirements if req["current_id"]}
    aliases: set[str] = set()
    tombstones: set[str] = set()
    requirements_by_source: defaultdict[str, list[dict]] = defaultdict(list)
    for req in requirements:
        requirements_by_source[req["source_document"]].append(req)
    definitions = []
    valid_references = []
    dangling = []
    ambiguous: defaultdict[str, list[dict]] = defaultdict(list)
    unrecorded = []
    for name in ("BRD", "UXF"):
        for path in source_files(name):
            source = rel(path)
            lines = path.read_text(encoding="utf-8").splitlines()
            ranges = []
            for req in requirements_by_source[source]:
                anchor = parse_anchor(req["source_anchor"])
                if anchor:
                    ranges.append((anchor[0], anchor[1], req))
            for line_number, line in enumerate(lines, 1):
                for token in ID_LIKE_RE.findall(line):
                    occurrence = {"token": token, "source_document": source, "source_anchor": f"L{line_number}"}
                    is_definition = bool(re.match(rf"^\s*#{{2,4}}\s+{re.escape(token)}(?:\s|$)", line))
                    if token in canonical_ids:
                        if is_definition:
                            definitions.append(occurrence)
                            continue
                        valid_references.append(occurrence)
                        owners = [req for start, end, req in ranges if start <= line_number <= end]
                        if not owners or any(token not in req["referenced_requirements"] and token != req["current_id"] for req in owners):
                            unrecorded.append({**occurrence, "owning_registry_keys": sorted(requirement_key(req) for req in owners)})
                    elif token in aliases or token in tombstones:
                        valid_references.append({**occurrence, "resolution": "ALIAS_OR_TOMBSTONE"})
                    elif EXPLICIT_ID_RE.fullmatch(token):
                        dangling.append(occurrence)
                    else:
                        ambiguous[token].append({"source_document": source, "source_anchor": f"L{line_number}"})
    ambiguous_tokens = [
        {"token": token, "occurrence_count": len(occurrences), "occurrences": occurrences}
        for token, occurrences in sorted(ambiguous.items())
    ]
    return {
        "canonical_id_count": len(canonical_ids),
        "alias_count": len(aliases),
        "tombstone_count": len(tombstones),
        "definition_occurrence_count": len(definitions),
        "valid_reference_count": len(valid_references),
        "dangling_raw_reference_count": len(dangling),
        "ambiguous_id_like_token_count": len(ambiguous_tokens),
        "ambiguous_id_like_occurrence_count": sum(item["occurrence_count"] for item in ambiguous_tokens),
        "unrecorded_prose_reference_count": len(unrecorded),
        "definitions": definitions,
        "valid_references": valid_references,
        "dangling_raw_references": dangling,
        "ambiguous_id_like_tokens": ambiguous_tokens,
        "unrecorded_prose_references": unrecorded,
    }


def sample_review(requirement: dict, selected_for: list[str], registries: dict[str, dict], classification_keys: set[str], overlap_keys: set[str]) -> dict:
    key = requirement_key(requirement)
    source = ROOT / requirement["source_document"]
    lines = source.read_text(encoding="utf-8").splitlines()
    anchor = parse_anchor(requirement["source_anchor"])
    anchor_correct = bool(anchor and anchor[0] >= 1 and anchor[1] <= len(lines) and lines[anchor[0] - 1] == requirement["source_marker"])
    discovered = {fingerprint(source, item): item for item in discover(source)}
    item = discovered.get(requirement["source_fingerprint"])
    statement_complete = bool(item and item["statement"] == requirement["statement"])
    source_status = frontmatter(lines).get("status", "")
    lifecycle_reasonable = requirement["lifecycle_status"] == lifecycle_for(source_status)
    acceptance_reasonable = (
        requirement["acceptance_status"] in ACCEPTANCE_VALUES
        and requirement["acceptance_present"] == (requirement["acceptance_status"] in {"DIRECT", "LINKED"})
        and bool(requirement["acceptance_references"]) == (requirement["acceptance_status"] in {"DIRECT", "LINKED"})
    )
    scope_reasonable = (
        requirement["scope_basis"] in SCOPE_BASIS_VALUES
        and bool(requirement["scope_evidence"])
        and (requirement["scope_status"] != "UNCLEAR" or requirement["scope_basis"] == "HUMAN_REVIEW_REQUIRED")
        and (requirement["scope_status"] not in {"FUTURE", "DEFERRED", "OUT_OF_SCOPE"} or requirement["scope_basis"] == "SOURCE_EXPLICIT")
    )
    type_reasonable = key not in classification_keys
    ambiguity_overlap_reasonable = (not requirement["ambiguity"] or requirement["scope_basis"] in {"FRAMEWORK_DECISION", "HUMAN_REVIEW_REQUIRED"})
    if requirement["duplicate_or_overlap"] and key not in overlap_keys:
        ambiguity_overlap_reasonable = False
    checks = {
        "source_anchor_correct": anchor_correct,
        "statement_complete": statement_complete,
        "requirement_type_reasonable": type_reasonable,
        "scope_status_reasonable": scope_reasonable,
        "lifecycle_status_reasonable": lifecycle_reasonable,
        "acceptance_mapping_reasonable": acceptance_reasonable,
        "ambiguity_overlap_reasonable": ambiguity_overlap_reasonable,
    }
    notes = []
    if not type_reasonable:
        notes.append("Requirement type needs human review because source position suggests a different semantic class.")
    if requirement["acceptance_status"] == "INFERRED_ONLY":
        notes.append("Testability is inferred; no source acceptance criteria are recorded.")
    if requirement["acceptance_status"] == "MISSING":
        notes.append("No acceptance mapping; extraction may be navigation or implementation guidance.")
    if requirement["ambiguity"]:
        notes.append(requirement["ambiguity"])
    return {
        "key": key,
        "source_document": requirement["source_document"],
        "source_anchor": requirement["source_anchor"],
        "selected_for": sorted(selected_for),
        "checks": checks,
        "result": "PASS" if all(checks.values()) else "REVIEW",
        "notes": notes,
    }


def deterministic_sample(registries: dict[str, dict], overlap: dict, classification: list[dict]) -> dict:
    by_set = {name: registries[name]["requirements"] for name in ("BRD", "UXF")}
    def sorted_reqs(requirements: list[dict]) -> list[dict]:
        return sorted(requirements, key=lambda req: (requirement_key(req), req["source_document"]))
    selections = {
        "brd_existing_id": [requirement_key(req) for req in sorted_reqs([req for req in by_set["BRD"] if req["current_id"]])[:10]],
        "brd_temporary_key": [requirement_key(req) for req in sorted_reqs([req for req in by_set["BRD"] if req["temporary_key"]])[:10]],
        "uxf_existing_id": [requirement_key(req) for req in sorted_reqs([req for req in by_set["UXF"] if req["current_id"]])[:10]],
        "uxf_temporary_key": [requirement_key(req) for req in sorted_reqs([req for req in by_set["UXF"] if req["temporary_key"]])[:10]],
    }
    all_requirements = by_set["BRD"] + by_set["UXF"]
    selections["all_ambiguity"] = [requirement_key(req) for req in sorted_reqs([req for req in all_requirements if req["ambiguity"]])]
    selections["all_future"] = [requirement_key(req) for req in sorted_reqs([req for req in all_requirements if req["scope_status"] == "FUTURE"])]
    selections["all_deferred"] = [requirement_key(req) for req in sorted_reqs([req for req in all_requirements if req["scope_status"] == "DEFERRED"])]
    selections["all_out_of_scope"] = [requirement_key(req) for req in sorted_reqs([req for req in all_requirements if req["scope_status"] == "OUT_OF_SCOPE"])]
    overlap_groups = sorted(overlap["groups"], key=lambda group: group["group_id"])[:10]
    selections["representative_overlap_groups"] = [
        {"group_id": group["group_id"], "members": group["members"], "kind": group["kind"], "classification": group["classification"]}
        for group in overlap_groups
    ]
    selected_for: defaultdict[str, list[str]] = defaultdict(list)
    for category, values in selections.items():
        if category == "representative_overlap_groups":
            for group in values:
                for key in group["members"]:
                    selected_for[key].append(f"overlap:{group['group_id']}")
        else:
            for key in values:
                selected_for[key].append(category)
    by_key = {requirement_key(req): req for req in all_requirements}
    classification_keys = {item["key"] for item in classification}
    overlap_keys = {member for group in overlap["groups"] for member in group["members"]}
    reviews = [
        sample_review(by_key[key], categories, registries, classification_keys, overlap_keys)
        for key, categories in sorted(selected_for.items())
    ]
    return {
        "selection_method": "Sort by (requirement key, source path); take first 10 for four base strata; include all ambiguity and non-active scope entries; take first 10 overlap groups by group_id.",
        "selection": selections,
        "unique_requirement_count": len(reviews),
        "reviews": reviews,
    }


def build_qa(registries: dict[str, dict]) -> dict:
    per_file, extraction_totals = extraction_audit(registries)
    overlap = build_overlap_analysis(registries)
    raw_references = raw_reference_audit(registries)
    classification = classification_findings(registries)
    sample = deterministic_sample(registries, overlap, classification)
    acceptance = Counter()
    scope_basis = Counter()
    for registry in registries.values():
        for req in registry["requirements"]:
            acceptance[req["acceptance_status"]] += 1
            scope_basis[req["scope_basis"]] += 1
    existing_count = sum(req["current_id"] is not None for registry in registries.values() for req in registry["requirements"])
    classification_audit = {
        "existing_id_count": existing_count,
        "existing_id_position_confusion_count": sum(item["finding"] == "ID_PREFIX_POSITION_CONFUSION" for item in classification),
        "temporary_key_count": sum(req["temporary_key"] is not None for registry in registries.values() for req in registry["requirements"]),
        "temporary_position_confusion_count": sum(item["finding"] == "TEMP_TYPE_POSITION_CONFUSION" for item in classification),
        "rule": "Type must be confirmed by source meaning and section position; ID prefix and temporary-key status are only signals.",
    }
    human_decisions = []
    if extraction_totals["false_negative_candidate_count"]:
        human_decisions.append("Review all false-negative candidates before changing registry membership.")
    if extraction_totals["false_positive_candidate_count"]:
        human_decisions.append("Decide whether navigation, traceability, and AI implementation guideline entries remain requirements.")
    if extraction_totals["compound_statement_candidate_count"]:
        human_decisions.append("Decide which compound statements must be split during a later content-editing phase.")
    if classification:
        human_decisions.append("Resolve temporary-key classification confusion using source meaning and ownership, not TMP status.")
    if any(group["classification"].startswith("POTENTIAL_ACCIDENTAL") for group in overlap["groups"]):
        human_decisions.append("Classify potential accidental overlap groups; do not merge IDs automatically.")
    return {
        "schema_version": "1.0",
        "phase": "Documentation Governance v2.3 Phase 1B Semantic QA",
        "generated_on": date.today().isoformat(),
        "registry_requirement_count": sum(len(registry["requirements"]) for registry in registries.values()),
        "extraction_audit": {"totals": extraction_totals, "per_file": per_file},
        "deterministic_sample": sample,
        "acceptance_distribution": dict(sorted(acceptance.items())),
        "scope_provenance_distribution": dict(sorted(scope_basis.items())),
        "raw_reference_validation": raw_references,
        "overlap_normalization": overlap,
        "classification_audit": classification_audit,
        "classification_findings": classification,
        "human_decisions_required": human_decisions,
    }


def calculate_summary(registries: dict[str, dict]) -> dict:
    all_requirements = [req for registry in registries.values() for req in registry["requirements"]]
    ids = [req["current_id"] for req in all_requirements if req["current_id"]]
    temporary = [req["temporary_key"] for req in all_requirements if req["temporary_key"]]
    known_ids = set(ids)
    dangling = dangling_source_references(registries, known_ids)
    overlap = build_overlap_analysis(registries)
    def stats(registry: dict) -> dict:
        reqs = registry["requirements"]
        return {
            "file_count": len(registry["documents"]),
            "requirement_count": len(reqs),
            "with_id": sum(req["current_id"] is not None for req in reqs),
            "without_id": sum(req["temporary_key"] is not None for req in reqs),
            "missing_acceptance": sum(not req["acceptance_present"] for req in reqs),
            "unclear_scope": sum(req["scope_status"] == "UNCLEAR" for req in reqs),
        }
    return {
        "schema_version": "1.0",
        "generated_on": date.today().isoformat(),
        "sets": {name: stats(registries[name]) for name in ("BRD", "UXF")},
        "totals": {
            "file_count": sum(len(registry["documents"]) for registry in registries.values()),
            "requirement_count": len(all_requirements),
            "with_id": len(ids),
            "without_id": len(temporary),
            "duplicate_ids": len(duplicate_values(ids)),
            "duplicate_temporary_keys": len(duplicate_values(temporary)),
            "dangling_references": len(dangling),
            "missing_acceptance": sum(not req["acceptance_present"] for req in all_requirements),
            "unclear_scope": sum(req["scope_status"] == "UNCLEAR" for req in all_requirements),
            "ambiguous_requirements": sum(req["ambiguity"] is not None for req in all_requirements),
            "requirements_with_overlap": overlap["requirements_with_overlap"],
            "unique_overlap_pairs": overlap["unique_overlap_pairs"],
            "unique_overlap_groups": overlap["unique_overlap_groups"],
            "exact_duplicate_groups": overlap["exact_duplicate_groups"],
            "probable_semantic_overlap_groups": overlap["probable_semantic_overlap_groups"],
        },
        "duplicate_ids": duplicate_values(ids),
        "duplicate_temporary_keys": duplicate_values(temporary),
        "dangling_references": dangling,
        "by_scope_status": dict(sorted(Counter(req["scope_status"] for req in all_requirements).items())),
        "by_lifecycle_status": dict(sorted(Counter(req["lifecycle_status"] for req in all_requirements).items())),
        "by_requirement_type": dict(sorted(Counter(req["requirement_type"] for req in all_requirements).items())),
        "by_acceptance_status": dict(sorted(Counter(req["acceptance_status"] for req in all_requirements).items())),
        "by_scope_basis": dict(sorted(Counter(req["scope_basis"] for req in all_requirements).items())),
    }


def json_write(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def inventory_markdown(registries: dict[str, dict], summary: dict) -> str:
    rows = []
    for doc_set in ("BRD", "UXF"):
        for doc in registries[doc_set]["documents"]:
            ids = ", ".join(f"`{value}`" for value in doc["requirement_ids"]) or "—"
            refs = ", ".join(f"`{value}`" for value in doc["references"]) or "—"
            rows.append(
                f"| `{doc['path']}` | `{doc['document_code']}` | {doc['title']} | `{doc['version']}` | "
                f"`{doc['status']}` | `{doc['language']}` | {ids} | {doc['requirement_count']} | {refs} |"
            )
    return f"""# BRD/UXF Inventory — Documentation Governance v2.3 Phase 1

Generated from the source files and requirement registries. Counts are validated, not estimates.

## Exact totals

- BRD files: **{summary['sets']['BRD']['file_count']}**
- UXF files: **{summary['sets']['UXF']['file_count']}**
- BRD requirements: **{summary['sets']['BRD']['requirement_count']}**
- UXF requirements: **{summary['sets']['UXF']['requirement_count']}**

## Document inventory

| Path | Document code | Title | Version | Status | Language | Existing requirement IDs | Requirement count | Document references |
|---|---|---|---|---|---|---|---:|---|
{chr(10).join(rows)}

## Extraction boundary

An inventory requirement is either an explicit normative heading with a pre-existing ID, or a Markdown source block containing an explicit normative modal/prohibition in English or Vietnamese. No new canonical Requirement ID is assigned; unnumbered blocks use `TMP-{{document-code}}-{{sequence}}`.
"""


def report_markdown(registries: dict[str, dict], summary: dict) -> str:
    ambiguities = []
    overlaps = []
    for registry in registries.values():
        for req in registry["requirements"]:
            key = req["current_id"] or req["temporary_key"]
            if req["ambiguity"]:
                ambiguities.append(f"- `{key}` ({req['source_document']}:{req['source_anchor']}): {req['ambiguity']}")
            if req["duplicate_or_overlap"]:
                overlaps.append(f"- `{key}` overlaps exact normalized statement with {', '.join(f'`{item}`' for item in req['duplicate_or_overlap'])}.")
    totals = summary["totals"]
    return f"""# Requirement Registry Report — BRD/UXF Phase 1

## Validation totals

| Metric | BRD | UXF | Total |
|---|---:|---:|---:|
| Files | {summary['sets']['BRD']['file_count']} | {summary['sets']['UXF']['file_count']} | {totals['file_count']} |
| Requirements | {summary['sets']['BRD']['requirement_count']} | {summary['sets']['UXF']['requirement_count']} | {totals['requirement_count']} |
| With existing ID | {summary['sets']['BRD']['with_id']} | {summary['sets']['UXF']['with_id']} | {totals['with_id']} |
| Without ID / temporary key | {summary['sets']['BRD']['without_id']} | {summary['sets']['UXF']['without_id']} | {totals['without_id']} |
| Missing acceptance criteria | {summary['sets']['BRD']['missing_acceptance']} | {summary['sets']['UXF']['missing_acceptance']} | {totals['missing_acceptance']} |
| Scope `UNCLEAR` | {summary['sets']['BRD']['unclear_scope']} | {summary['sets']['UXF']['unclear_scope']} | {totals['unclear_scope']} |

- Duplicate existing IDs: **{totals['duplicate_ids']}**
- Duplicate temporary keys: **{totals['duplicate_temporary_keys']}**
- Dangling requirement references: **{totals['dangling_references']}**
- Requirements with recorded ambiguity: **{totals['ambiguous_requirements']}**
- Requirements with overlap: **{totals['requirements_with_overlap']}**
- Unique overlap pairs: **{totals['unique_overlap_pairs']}**
- Unique overlap groups: **{totals['unique_overlap_groups']}**
- Exact duplicate groups: **{totals['exact_duplicate_groups']}**
- Probable semantic overlap groups: **{totals['probable_semantic_overlap_groups']}**

## Classification distributions

- Scope: `{json.dumps(summary['by_scope_status'], ensure_ascii=False, sort_keys=True)}`
- Lifecycle: `{json.dumps(summary['by_lifecycle_status'], ensure_ascii=False, sort_keys=True)}`
- Requirement type: `{json.dumps(summary['by_requirement_type'], ensure_ascii=False, sort_keys=True)}`
- Acceptance: `{json.dumps(summary['by_acceptance_status'], ensure_ascii=False, sort_keys=True)}`
- Scope basis: `{json.dumps(summary['by_scope_basis'], ensure_ascii=False, sort_keys=True)}`

## Ambiguities

{chr(10).join(ambiguities) if ambiguities else 'None.'}

## Exact normalized duplicates/overlaps

{chr(10).join(overlaps) if overlaps else 'None.'}

## Registry interpretation

- `FROZEN` is retained as the source requirement lifecycle from the prior baseline; it is not represented as v2.3 approval.
- `DRAFT` is retained for UXF source requirements.
- `V2.3_ACTIVE` is the default for inherited requirements unless the source has an explicit future/deferred/out-of-scope signal or classification is uncertain.
- `acceptance_present` is true only when the requirement source block itself contains identifiable acceptance criteria; testability of a statement alone is not treated as documented acceptance criteria.
"""


def qa_markdown(qa: dict, summary: dict) -> str:
    extraction = qa["extraction_audit"]
    file_rows = []
    false_negatives = []
    false_positives = []
    compounds = []
    for item in extraction["per_file"]:
        file_rows.append(
            f"| `{item['source_document']}` | {item['candidate_count']} | {item['matched_candidate_count']} | "
            f"{item['registry_requirement_count']} | {item['false_negative_candidate_count']} | "
            f"{item['false_positive_candidate_count']} | {item['compound_statement_candidate_count']} | "
            f"{item['same_source_duplicate_group_count']} |"
        )
        false_negatives.extend(item["false_negative_candidates"])
        false_positives.extend({"source_document": item["source_document"], **finding} for finding in item["false_positive_candidates"])
        compounds.extend({"source_document": item["source_document"], **finding} for finding in item["compound_statement_candidates"])
    sample_rows = []
    for review in qa["deterministic_sample"]["reviews"]:
        failed = [name for name, passed in review["checks"].items() if not passed]
        sample_rows.append(
            f"| `{review['key']}` | `{review['source_document']}:{review['source_anchor']}` | "
            f"{', '.join(review['selected_for'])} | `{review['result']}` | {', '.join(failed) or '—'} |"
        )
    fn_lines = [
        f"- `{item['source_document']}:{item['source_anchor']}` `{item['kind']}` — {item['text']}"
        for item in false_negatives
    ]
    fp_lines = [
        f"- `{item['key']}` (`{item['source_document']}:{item['source_anchor']}`) — {item['reason']}"
        for item in false_positives
    ]
    compound_lines = [
        f"- `{item['key']}` (`{item['source_document']}:{item['source_anchor']}`): bullets={item['bullet_count']}, normative signals={item['normative_signal_count']}"
        for item in compounds
    ]
    raw = qa["raw_reference_validation"]
    ambiguous_lines = [
        f"- `{item['token']}`: {item['occurrence_count']} occurrence(s)"
        for item in raw["ambiguous_id_like_tokens"]
    ]
    overlap = qa["overlap_normalization"]
    overlap_sample = qa["deterministic_sample"]["selection"]["representative_overlap_groups"]
    overlap_lines = [
        f"- `{group['group_id']}` `{group['kind']}` `{group['classification']}`: {', '.join(f'`{member}`' for member in group['members'])}"
        for group in overlap_sample
    ]
    classification_lines = [
        f"- `{item['key']}` (`{item['source_document']}:{item['source_anchor']}`): {item['evidence']}"
        for item in qa["classification_findings"]
    ]
    human_lines = [f"- {item}" for item in qa["human_decisions_required"]]
    totals = extraction["totals"]
    return f"""# BRD/UXF Requirement Registry Semantic QA — Phase 1B

This audit preserves all **{qa['registry_requirement_count']}** registry statements and all existing canonical IDs/temporary keys. Findings are candidates for human review, not automatic registry membership changes.

## Extraction coverage by source file

| Source | Independent candidates | Matched candidates | Registry requirements | False-negative candidates | False-positive candidates | Compound candidates | Same-source duplicate groups |
|---|---:|---:|---:|---:|---:|---:|---:|
{chr(10).join(file_rows)}

Totals: candidates **{totals['candidate_count']}**, matched **{totals['matched_candidate_count']}**, false-negative candidates **{totals['false_negative_candidate_count']}**, false-positive candidates **{totals['false_positive_candidate_count']}**, compound candidates **{totals['compound_statement_candidate_count']}**.

## Deterministic sample audit

Selection is deterministic: `{qa['deterministic_sample']['selection_method']}`

Unique sampled requirements: **{qa['deterministic_sample']['unique_requirement_count']}**.

| Key | Source | Selected for | Result | Checks requiring review |
|---|---|---|---|---|
{chr(10).join(sample_rows)}

## False-negative candidates

{chr(10).join(fn_lines) if fn_lines else 'None.'}

## False-positive candidates

{chr(10).join(fp_lines) if fp_lines else 'None.'}

## Compound statement candidates

{chr(10).join(compound_lines) if compound_lines else 'None.'}

## Acceptance mapping

- Distribution: `{json.dumps(qa['acceptance_distribution'], ensure_ascii=False, sort_keys=True)}`
- `acceptance_present` is true only for `DIRECT` or `LINKED`.
- `INFERRED_ONLY` records testability without inventing acceptance criteria.

## Scope provenance

- Distribution: `{json.dumps(qa['scope_provenance_distribution'], ensure_ascii=False, sort_keys=True)}`
- Non-active source scope uses `SOURCE_EXPLICIT` with a source anchor.
- SD-03/UXD-11 promotions use `FRAMEWORK_DECISION` with the decision ID.
- Default inherited active scope uses `BASELINE_INHERITANCE`.

## Independent raw reference validation

- Canonical IDs: **{raw['canonical_id_count']}**
- Definitions: **{raw['definition_occurrence_count']}**
- Valid raw references excluding definitions: **{raw['valid_reference_count']}**
- Dangling raw references: **{raw['dangling_raw_reference_count']}**
- Ambiguous ID-like tokens: **{raw['ambiguous_id_like_token_count']}** unique / **{raw['ambiguous_id_like_occurrence_count']}** occurrences
- Prose references absent from `referenced_requirements`: **{raw['unrecorded_prose_reference_count']}**

Ambiguous ID-like token inventory:

{chr(10).join(ambiguous_lines) if ambiguous_lines else 'None.'}

## Normalized overlap metrics

- Requirements with overlap: **{overlap['requirements_with_overlap']}**
- Unique pairs: **{overlap['unique_overlap_pairs']}**
- Unique groups: **{overlap['unique_overlap_groups']}**
- Exact duplicate groups: **{overlap['exact_duplicate_groups']}**
- Probable semantic overlap groups: **{overlap['probable_semantic_overlap_groups']}**

Deterministic representative groups:

{chr(10).join(overlap_lines) if overlap_lines else 'None.'}

Intentional shared UX candidates and potential accidental duplicates remain separate classifications; no IDs are merged or removed.

## Classification findings

The audit does not accept TMP status or an ID prefix alone as semantic proof of type. Findings below identify temporary entries whose source position conflicts with the current broad type.

- Existing-ID entries reviewed by position rule: **{qa['classification_audit']['existing_id_count']}**
- Existing-ID position confusion findings: **{qa['classification_audit']['existing_id_position_confusion_count']}**
- Temporary-key entries reviewed: **{qa['classification_audit']['temporary_key_count']}**
- Temporary-key position confusion findings: **{qa['classification_audit']['temporary_position_confusion_count']}**

{chr(10).join(classification_lines) if classification_lines else 'None.'}

## Human decisions required

{chr(10).join(human_lines) if human_lines else 'None.'}

Full occurrence-level evidence, all overlap groups/pairs, all samples and all per-file findings are in `requirements/registry-qa.json`.
"""


def write_artifacts() -> None:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    codes = known_document_codes()
    registries = {name: build_registry(name, codes) for name in ("BRD", "UXF")}
    summary = calculate_summary(registries)
    qa = build_qa(registries)
    for name, path in REGISTRY_PATHS.items():
        json_write(path, registries[name])
    json_write(SUMMARY_PATH, summary)
    INVENTORY_PATH.write_text(inventory_markdown(registries, summary), encoding="utf-8")
    REPORT_PATH.write_text(report_markdown(registries, summary), encoding="utf-8")
    json_write(QA_PATH, qa)
    QA_REPORT_PATH.write_text(qa_markdown(qa, summary), encoding="utf-8")


def parse_anchor(anchor: str) -> tuple[int, int] | None:
    match = re.fullmatch(r"L(\d+)(?:-L(\d+))?", anchor)
    if not match:
        return None
    start = int(match.group(1))
    return start, int(match.group(2) or start)


def validate() -> list[str]:
    errors = []
    registries = {}
    for name, path in REGISTRY_PATHS.items():
        try:
            registries[name] = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid or missing JSON {rel(path)}: {exc}")
    try:
        summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid or missing JSON {rel(SUMMARY_PATH)}: {exc}")
        summary = None
    try:
        qa = json.loads(QA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid or missing JSON {rel(QA_PATH)}: {exc}")
        qa = None
    if len(registries) != 2:
        return errors
    all_ids = []
    all_tmp = []
    for name, registry in registries.items():
        if registry.get("document_set") != name or not isinstance(registry.get("documents"), list) or not isinstance(registry.get("requirements"), list):
            errors.append(f"{name} registry has invalid top-level schema")
            continue
        if registry.get("schema_version") != "1.0" or not registry.get("phase"):
            errors.append(f"{name} registry has invalid schema_version/phase")
        physical = [rel(path) for path in source_files(name)]
        registered = [doc.get("path") for doc in registry["documents"]]
        if physical != registered:
            errors.append(f"{name} file coverage mismatch: physical={physical}, registered={registered}")
        document_paths = set(registered)
        expected_fingerprints = {fingerprint(path, item) for path in source_files(name) for item in discover(path)}
        actual_fingerprints = set()
        per_doc_counts = Counter()
        document_by_path = {}
        for doc in registry["documents"]:
            missing_doc_fields = DOCUMENT_REQUIRED_FIELDS - set(doc)
            if missing_doc_fields:
                errors.append(f"Document missing fields {sorted(missing_doc_fields)}: {doc}")
                continue
            if not all(doc.get(field) for field in ("path", "document_code", "title", "version", "status", "language")):
                errors.append(f"{doc.get('path')}: document metadata fields must be non-empty")
            if not isinstance(doc["requirement_ids"], list) or not isinstance(doc["references"], list) or not isinstance(doc["requirement_count"], int):
                errors.append(f"{doc.get('path')}: invalid document field types")
            document_by_path[doc["path"]] = doc
        for req in registry["requirements"]:
            missing = REQUIRED_FIELDS - set(req)
            if missing:
                errors.append(f"Requirement missing fields {sorted(missing)}: {req}")
                continue
            key = req["current_id"] or req["temporary_key"]
            if not isinstance(req["statement"], str) or not req["statement"].strip():
                errors.append(f"{key}: statement must be a non-empty string")
            if bool(req["current_id"]) == bool(req["temporary_key"]):
                errors.append(f"{key}: exactly one of current_id/temporary_key is required")
            if req["current_id"]:
                if not EXPLICIT_ID_RE.fullmatch(req["current_id"]):
                    errors.append(f"{key}: invalid canonical requirement ID format")
                all_ids.append(req["current_id"])
            if req["temporary_key"]:
                doc_meta = document_by_path.get(req["source_document"])
                expected_prefix = f"TMP-{doc_meta['document_code']}-" if doc_meta else "TMP-"
                if not req["temporary_key"].startswith(expected_prefix) or not re.fullmatch(r".+-\d{3,}", req["temporary_key"]):
                    errors.append(f"{key}: temporary key does not match TMP-{{document-code}}-{{sequence}}")
                all_tmp.append(req["temporary_key"])
            if req["scope_status"] not in SCOPE_VALUES:
                errors.append(f"{key}: invalid scope_status {req['scope_status']}")
            if req["lifecycle_status"] not in LIFECYCLE_VALUES:
                errors.append(f"{key}: invalid lifecycle_status {req['lifecycle_status']}")
            if req["requirement_type"] not in TYPE_VALUES:
                errors.append(f"{key}: invalid requirement_type {req['requirement_type']}")
            if not isinstance(req["acceptance_present"], bool) or not isinstance(req["duplicate_or_overlap"], list) or not isinstance(req["referenced_requirements"], list):
                errors.append(f"{key}: invalid field types")
            if req["acceptance_status"] not in ACCEPTANCE_VALUES or not isinstance(req["acceptance_references"], list):
                errors.append(f"{key}: invalid acceptance metadata")
            elif req["acceptance_present"] != (req["acceptance_status"] in {"DIRECT", "LINKED"}):
                errors.append(f"{key}: acceptance_present is inconsistent with acceptance_status")
            elif bool(req["acceptance_references"]) != (req["acceptance_status"] in {"DIRECT", "LINKED"}):
                errors.append(f"{key}: acceptance_references are inconsistent with acceptance_status")
            if req["scope_basis"] not in SCOPE_BASIS_VALUES or not isinstance(req["scope_evidence"], str) or not req["scope_evidence"]:
                errors.append(f"{key}: invalid scope provenance")
            if req["scope_status"] in {"FUTURE", "DEFERRED", "OUT_OF_SCOPE"} and req["scope_basis"] != "SOURCE_EXPLICIT":
                errors.append(f"{key}: non-active scope must have SOURCE_EXPLICIT provenance")
            if req["scope_status"] == "UNCLEAR" and req["scope_basis"] != "HUMAN_REVIEW_REQUIRED":
                errors.append(f"{key}: UNCLEAR scope must require human review")
            if req["scope_basis"] == "FRAMEWORK_DECISION" and not re.fullmatch(r"SD-03|UXD-11", req["scope_evidence"]):
                errors.append(f"{key}: invalid framework decision scope evidence")
            if req["ambiguity"] is not None and not isinstance(req["ambiguity"], str):
                errors.append(f"{key}: ambiguity must be a string or null")
            source = ROOT / req["source_document"]
            if req["source_document"] not in document_paths or not source.is_file():
                errors.append(f"{key}: source file does not exist or is not registered: {req['source_document']}")
                continue
            anchor = parse_anchor(req["source_anchor"])
            lines = source.read_text(encoding="utf-8").splitlines()
            if anchor is None or anchor[0] < 1 or anchor[1] > len(lines) or anchor[0] > anchor[1]:
                errors.append(f"{key}: invalid source anchor {req['source_anchor']}")
            elif lines[anchor[0] - 1] != req["source_marker"]:
                errors.append(f"{key}: source marker not found at {req['source_anchor']}")
            elif req["source_fingerprint"] != fingerprint(source, {
                "start": anchor[0], "end": anchor[1], "kind": req["extraction_kind"], "marker": req["source_marker"]
            }):
                errors.append(f"{key}: source fingerprint does not match source anchor")
            actual_fingerprints.add(req["source_fingerprint"])
            per_doc_counts[req["source_document"]] += 1
        if expected_fingerprints != actual_fingerprints:
            errors.append(f"{name} requirement coverage mismatch: missing={sorted(expected_fingerprints-actual_fingerprints)}, extra={sorted(actual_fingerprints-expected_fingerprints)}")
        for doc in registry["documents"]:
            if doc.get("requirement_count") != per_doc_counts[doc.get("path")]:
                errors.append(f"{doc.get('path')}: document requirement aggregate mismatch")
            actual_doc_ids = [req["current_id"] for req in registry["requirements"] if req["source_document"] == doc.get("path") and req["current_id"]]
            if doc.get("requirement_ids") != actual_doc_ids:
                errors.append(f"{doc.get('path')}: requirement_ids mismatch")
    for value in duplicate_values(all_ids):
        errors.append(f"Duplicate canonical requirement ID: {value}")
    for value in duplicate_values(all_tmp):
        errors.append(f"Duplicate temporary key: {value}")
    known = set(all_ids)
    for registry in registries.values():
        for req in registry["requirements"]:
            for reference in req["referenced_requirements"]:
                if reference not in known:
                    errors.append(f"{req['current_id'] or req['temporary_key']}: dangling reference {reference}")
    for dangling in dangling_source_references(registries, known):
        errors.append(f"{dangling['source_document']}:{dangling['source_anchor']}: dangling reference {dangling['reference']}")
    if summary is not None:
        expected_summary = calculate_summary(registries)
        expected_summary["generated_on"] = summary.get("generated_on")
        if summary != expected_summary:
            errors.append("registry-summary.json aggregates/details do not match registry data")
    if qa is not None:
        expected_qa = build_qa(registries)
        expected_qa["generated_on"] = qa.get("generated_on")
        if qa != expected_qa:
            errors.append("registry-qa.json does not match independently recomputed semantic QA data")
        audited = [item.get("source_document") for item in qa.get("extraction_audit", {}).get("per_file", [])]
        physical = [rel(path) for name in ("BRD", "UXF") for path in source_files(name)]
        if audited != physical:
            errors.append("Not every source file in inventory has a QA audit record")
        selection = qa.get("deterministic_sample", {}).get("selection", {})
        for category in ("brd_existing_id", "brd_temporary_key", "uxf_existing_id", "uxf_temporary_key"):
            if len(selection.get(category, [])) != 10:
                errors.append(f"Deterministic sample category {category} must contain exactly 10 requirements")
        all_requirements = [req for registry in registries.values() for req in registry["requirements"]]
        expected_ambiguity = {requirement_key(req) for req in all_requirements if req["ambiguity"]}
        if set(selection.get("all_ambiguity", [])) != expected_ambiguity:
            errors.append("Deterministic sample does not contain every ambiguity")
        for status, category in (("FUTURE", "all_future"), ("DEFERRED", "all_deferred"), ("OUT_OF_SCOPE", "all_out_of_scope")):
            expected = {requirement_key(req) for req in all_requirements if req["scope_status"] == status}
            if set(selection.get(category, [])) != expected:
                errors.append(f"Deterministic sample does not contain every {status} requirement")
        if len(selection.get("representative_overlap_groups", [])) < 10:
            errors.append("Deterministic sample must contain at least 10 representative overlap groups")
        overlap = qa.get("overlap_normalization", {})
        pair_tuples = [(pair.get("left"), pair.get("right")) for pair in overlap.get("pairs", [])]
        if len(pair_tuples) != len(set(pair_tuples)) or any(left >= right for left, right in pair_tuples):
            errors.append("Overlap pairs are not unique canonical A-B pairs")
        group_ids = [group.get("group_id") for group in overlap.get("groups", [])]
        if len(group_ids) != len(set(group_ids)):
            errors.append("Overlap group IDs are not unique")
    if not QA_REPORT_PATH.is_file():
        errors.append(f"Missing QA report {rel(QA_REPORT_PATH)}")
    return errors


# Phase 1C is deliberately layered over the Phase 1B extractor.  The raw extractor
# remains reproducible so the reconciliation ledger can prove the disposition of
# every QA finding instead of making findings disappear by changing the scanner.

PHASE_1C_TYPE_VALUES = {
    "BUSINESS_REQUIREMENT", "BUSINESS_RULE", "BUSINESS_DECISION", "SCOPE_CONSTRAINT",
    "UX_REQUIREMENT", "ACCESSIBILITY_REQUIREMENT", "SECURITY_REQUIREMENT",
    "PRIVACY_REQUIREMENT", "PERFORMANCE_REQUIREMENT", "OPERATIONAL_REQUIREMENT",
    "DATA_REQUIREMENT", "INTEGRATION_REQUIREMENT", "DESIGN_PRINCIPLE",
}
PHASE_1C_REQUIRED_FIELDS = {
    "source_document", "source_section", "source_anchor", "source_lines",
    "source_excerpt", "source_fingerprint", "statement", "current_id",
    "temporary_key", "requirement_type", "scope_status", "source_scope_status",
    "scope_basis", "scope_evidence", "scope_conflict_resolved", "lifecycle_status",
    "priority", "acceptance_present", "acceptance_status", "acceptance_references",
    "ambiguity", "duplicate_or_overlap", "referenced_requirements", "derived_from",
    "extraction_kind",
}


def normalized_excerpt(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def excerpt_fingerprint(value: str) -> str:
    return hashlib.sha256(normalized_excerpt(value).encode("utf-8")).hexdigest()


def raw_file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def raw_bytes_sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def aggregate_file_hash(entries: list[dict]) -> str:
    records = "".join(
        f"{entry['path']}\0{entry['sha256']}\n"
        for entry in sorted(entries, key=lambda item: item["path"])
    ).encode("utf-8")
    return hashlib.sha256(records).hexdigest()


def github_slug(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\- ]", "", value, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", value).strip("-")


def source_locator(path: Path, start: int, end: int) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    stack: list[tuple[int, str]] = []
    for index, line in enumerate(lines[:start], 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        stack = [item for item in stack if item[0] < level]
        stack.append((level, match.group(2)))
    section = " > ".join(text for _, text in stack) or "(document root)"
    anchor = "#" + github_slug(stack[-1][1]) if stack else None
    excerpt = "\n".join(lines[start - 1:end]).strip()
    return {
        "source_section": section,
        "source_anchor": anchor,
        "source_lines": f"L{start}" if start == end else f"L{start}-L{end}",
        "source_excerpt": excerpt,
        "source_fingerprint": excerpt_fingerprint(excerpt),
    }


def legacy_source_scope(statement: str, scope_hint: str | None = None) -> str:
    signals = []
    if DEFERRED_RE.search(statement):
        signals.append("DEFERRED")
    if OUT_RE.search(statement):
        signals.append("OUT_OF_SCOPE")
    if FUTURE_RE.search(statement):
        signals.append("FUTURE")
    if scope_hint and scope_hint not in signals:
        signals.append(scope_hint)
    return signals[0] if len(set(signals)) == 1 else "UNCLEAR" if signals else "V2.3_ACTIVE"


def semantic_requirement_type(req: dict, lines: list[str]) -> str:
    text = req["statement"]
    lowered = text.lower()
    line_range = parse_anchor(req.get("source_lines") or req.get("source_anchor"))
    heading = nearest_heading(lines, line_range[0] if line_range else 1).lower()
    if req["scope_status"] != "V2.3_ACTIVE" or re.search(r"ngoài phạm vi|chưa triển khai|future|deferred|phiên bản sau", lowered):
        return "SCOPE_CONSTRAINT"
    if re.search(r"accessib|wcag|screen reader|keyboard|aria|contrast|focus order", lowered):
        return "ACCESSIBILITY_REQUIREMENT"
    if re.search(r"privacy|personal data|pii|consent|data retention|right to erasure", lowered):
        return "PRIVACY_REQUIREMENT"
    if re.search(r"security|permission|authentication|authorization|otp|encrypt|token|secret|password", lowered):
        return "SECURITY_REQUIREMENT"
    if re.search(r"latency|throughput|response time|performance|concurrent|scalability", lowered):
        return "PERFORMANCE_REQUIREMENT"
    if re.search(r"availability|backup|restore|archive|monitor|alert|audit|operat|replay|disaster", lowered):
        return "OPERATIONAL_REQUIREMENT"
    if re.search(r"api|integration|connector|external system|webhook|gateway", lowered):
        return "INTEGRATION_REQUIREMENT"
    if re.search(r"schema|data type|data model|business object|snapshot|event payload", lowered):
        return "DATA_REQUIREMENT"
    if req["source_document"].startswith("docs/UXF/"):
        return "UX_REQUIREMENT"
    if "business decision" in heading or (req.get("current_id", "") or "").startswith("BD-") and "decision" in req.get("source_section", "").lower():
        return "BUSINESS_DECISION"
    if re.search(r"principle|nguyên tắc|invariant", heading):
        return "DESIGN_PRINCIPLE"
    if re.search(r"business rule|quy tắc|policy", heading):
        return "BUSINESS_RULE"
    return "BUSINESS_REQUIREMENT"


def stable_entry(raw: dict) -> dict:
    req = dict(raw)
    old_anchor = req["source_anchor"]
    start, end = parse_anchor(old_anchor) or (0, 0)
    path = ROOT / req["source_document"]
    req.update(source_locator(path, start, end))
    req.pop("source_marker", None)
    req["derived_from"] = []
    req["source_scope_status"] = legacy_source_scope(req["statement"])
    req["scope_conflict_resolved"] = req["scope_basis"] == "FRAMEWORK_DECISION"
    if req["scope_conflict_resolved"]:
        if req["source_scope_status"] == "V2.3_ACTIVE" and re.search(r"future|roadmap", req["source_section"], re.IGNORECASE):
            req["source_scope_status"] = "FUTURE"
        req["scope_status"] = "V2.3_ACTIVE"
        req["ambiguity"] = None
    req["requirement_type"] = semantic_requirement_type(req, path.read_text(encoding="utf-8").splitlines())
    return req


def ledger_record(source: str, finding_type: str, disposition: str, rationale: str,
                  resulting: list[str], evidence: dict, reviewer: str = "RECONCILED") -> dict:
    return {
        "source_key_or_candidate": source,
        "finding_type": finding_type,
        "disposition": disposition,
        "rationale": rationale,
        "resulting_keys": resulting,
        "reviewer_status": reviewer,
        "source_evidence": evidence,
    }


def qa_findings(qa: dict, field: str) -> list[dict]:
    result = []
    for audit in qa["extraction_audit"]["per_file"]:
        for item in audit[field]:
            result.append({"source_document": audit["source_document"], **item})
    return result


FP_REQUIREMENTS = {
    "TMP-BRD-BO-INDEX-041", "TMP-BRD-BO-INDEX-042", "TMP-BRD-CAP-INDEX-023",
}
SPLIT_SPECS = {
    "TMP-BRD-META-MODEL-002": [
        "Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này.",
        "Mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.",
    ],
    "TMP-BRD-POLICY-INDEX-010": [
        "Nguyên tắc:\n\n- Scope thấp hơn ưu tiên kế thừa.",
        "Nguyên tắc:\n\n- Chỉ Override khi thực sự cần thiết.",
        "Nguyên tắc:\n\n- Không được Override các System Policy bắt buộc.",
    ],
    "TMP-BRD-SNAPSHOT-INDEX-011": [
        "Nguyên tắc:\n\n- Event không thay thế Snapshot.",
        "Nguyên tắc:\n\n- Snapshot không thay thế Audit.",
        "Nguyên tắc:\n\n- Audit không thay thế History.",
        "Nguyên tắc:\n\n- History không phải Business Evidence.",
    ],
    "TMP-BRD-WS-05-010": [
        "Trong phiên bản 2.0:\n\n- Payment Owner được cố định theo Commercial Agreement.",
        "Trong phiên bản 2.0:\n\n- Không hỗ trợ thay đổi theo Campaign.",
        "Trong phiên bản 2.0:\n\n- Nếu thanh toán tiền mặt thì Payment Owner là Organization sở hữu Storefront.",
    ],
    "TMP-BRD-WS-14-002": [
        "Nguyên tắc:\n\n- Scope thấp hơn có thể Override các thuộc tính được phép.",
        "Nguyên tắc:\n\n- Các thuộc tính không được Override sẽ kế thừa.",
        "Nguyên tắc:\n\n- Effective Configuration luôn được tính tại Runtime.",
    ],
    "TMP-BRD-WS-14-027": [
        "Nguyên tắc:\n\n- Scope thấp hơn có độ ưu tiên cao hơn.",
        "Nguyên tắc:\n\n- Chỉ các thuộc tính được phép mới được Override.",
        "Nguyên tắc:\n\n- Các thuộc tính khác kế thừa từ Scope phía trên.",
        "Nguyên tắc:\n\n- Effective Configuration luôn được tính tại Runtime.",
    ],
    "TMP-BRD-WS-16-009": [
        "Sau thời gian này:\n\n- Audit được Archive",
        "Sau thời gian này:\n\n- Archive chỉ đọc",
        "Sau thời gian này:\n\n- Không được chỉnh sửa",
        "Sau thời gian này:\n\n- Không được xóa trực tiếp",
    ],
    "TMP-BRD-WS-17-005": [
        "Mọi thao tác đều:\n\n- Kiểm tra Permission",
        "Mọi thao tác đều:\n\n- Ghi Audit",
        "Mọi thao tác đều:\n\n- Tuân thủ Security Policy",
    ],
}
COMPOSITE_PARENT_SPLITS = {
    "BO-P06": [
        {
            "statement": "Mọi tài liệu YSim phải sử dụng đúng Business Object được định nghĩa trong Business Object Registry.",
            "requirement_type": "DATA_REQUIREMENT",
        },
        {
            "statement": "Không được tạo Business Object mới ngoài Registry nếu chưa được Architecture Review.",
            "requirement_type": "OPERATIONAL_REQUIREMENT",
        },
    ],
    "BD-15-002": [
        {
            "statement": "API Gateway là thành phần bắt buộc.",
            "requirement_type": "INTEGRATION_REQUIREMENT",
        },
        {
            "statement": "Business Domain không được tích hợp trực tiếp với hệ thống bên ngoài.",
            "requirement_type": "INTEGRATION_REQUIREMENT",
        },
    ],
}
COMPOSITE_CHILD_SUBSTITUTIONS = {
    "BD-15-002": {
        "TMP-BRD-WS-15-027": "EP-15-001",
    },
}
COMPOUND_UNRESOLVED: set[str] = set()
OVERLAP_ALIAS_DECISIONS = {
    "OVL-EXACT-001": {
        "canonical_requirement": "BD-06-007",
        "alias_requirement": "EP-06-004",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) là requirement owner, Enterprise Design Principles là restatement.",
    },
    "OVL-EXACT-009": {
        "canonical_requirement": "BD-16-026",
        "alias_requirement": "EP-16-009",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) là canonical owner, Enterprise Design Principle giữ source-backed ID dưới dạng alias.",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-009",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-16.md",
            "wording": "Identity Platform hỗ trợ Federation.",
            "required_clarification": "The current Federation wording is insufficient for implementation and acceptance.",
            "minimum_definition": [
                "Federation actors and use cases.",
                "Trust boundaries and tenant isolation.",
                "Supported protocol/profile.",
                "Claim/attribute mapping.",
                "Account linking and conflict handling.",
                "Provisioning/deprovisioning or related lifecycle behavior.",
                "Authentication assurance, MFA, and risk interaction.",
                "Audit, revocation, and failure behavior.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not select a protocol or design a solution in Phase 1C.",
        },
    },
    "OVL-EXACT-010": {
        "canonical_requirement": "BD-16-027",
        "alias_requirement": "EP-16-008",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) là canonical security owner, Enterprise Design Principle giữ source-backed ID dưới dạng alias.",
        "canonical_requirement_type": "SECURITY_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-010",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-16.md",
            "wording": "Security Platform Publish Business Event.",
            "required_clarification": "The current Business Event wording is insufficient for implementation and acceptance.",
            "minimum_definition": [
                "Mandatory security event taxonomy.",
                "Trigger and producer ownership.",
                "Event schema, versioning, and classification.",
                "Tenant/Organization context.",
                "Sensitive-data constraints.",
                "Delivery guarantee, retry, and dead-letter handling.",
                "Ordering, deduplication, and idempotency.",
                "Consumer authorization.",
                "Audit, retention, and observability.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not design an event solution in Phase 1C.",
        },
    },
    "OVL-EXACT-011": {
        "canonical_requirement": "BD-17-011",
        "alias_requirement": "EP-17-005",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) là canonical operational owner, Enterprise Design Principle giữ source-backed ID dưới dạng alias.",
        "canonical_requirement_type": "OPERATIONAL_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-011",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-17.md",
            "wording": "Operation Retry độc lập Connector Retry.",
            "required_clarification": "The independence between Operation Retry and Connector Retry must be specified when the BRD is revised.",
            "minimum_definition": [
                "Ownership and scope of each retry layer.",
                "Independent counters and state.",
                "Timeout, backoff, jitter, and retry budget.",
                "Idempotency and duplicate prevention.",
                "Conditions that escalate connector failure to operation failure.",
                "Controls for nested retry amplification and retry storms.",
                "Exhaustion, DLQ, and manual recovery.",
                "Correlation, audit, and observability.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not design a retry policy in Phase 1C.",
        },
    },
    "OVL-EXACT-012": {
        "canonical_requirement": "BD-17-026",
        "alias_requirement": "EP-17-009",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) là canonical operational owner, Enterprise Design Principle giữ source-backed ID dưới dạng alias.",
        "canonical_requirement_type": "OPERATIONAL_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-012",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-17.md",
            "wording": "Operations Platform Publish Business Event.",
            "required_clarification": "The Operations Platform Business Event requirement must be specified when the BRD is revised.",
            "minimum_definition": [
                "Event taxonomy for operation lifecycle, retry, maintenance, runbook, and recovery.",
                "Trigger and producer ownership.",
                "Operation, correlation, and causation identifiers.",
                "Organization, scope, and actor context.",
                "Payload schema, versioning, and data classification.",
                "Delivery guarantee, ordering, and idempotency.",
                "Retry, DLQ, and replay.",
                "Consumer authorization.",
                "Audit, retention, and observability.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not design an event architecture in Phase 1C.",
        },
    },
    "OVL-EXACT-013": {
        "canonical_requirement": "CAP-P07",
        "alias_requirement": "CAP-EP-006",
        "rationale": "Exact duplicate trong cùng source; Capability Model principle là canonical owner, Enterprise Capability Principle giữ source-backed ID dưới dạng alias.",
        "canonical_requirement_type": "BUSINESS_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "semantic_clarification": [
            "CAP-P07 mô tả khả năng của Capability Model, không bắt buộc mọi capability phải event-driven.",
            "Mỗi capability có thể khai báo vai trò PUBLISHER, SUBSCRIBER, BOTH hoặc NONE.",
            "Khi khai báo event role, capability phải tham chiếu canonical Business Event definition và versioned event contract tương ứng.",
            "Không tự tạo event relationship nếu registry không khai báo.",
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-013",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-CAP-INDEX.md",
            "wording": "Capability có thể Publish hoặc Subscribe Business Event.",
            "classification_recommendation": "Consider reclassifying CAP-P07 from BUSINESS_REQUIREMENT to DESIGN_PRINCIPLE when the BRD is revised.",
            "minimum_definition": [
                "Clarify event-role metadata, canonical event reference, ownership, and versioning.",
                "Add validation for dangling or invalid event references.",
                "Add acceptance criteria.",
            ],
            "phase_constraint": "Do not reclassify CAP-P07 or design an event model in Phase 1C.",
        },
    },
    "OVL-PROB-002": {
        "canonical_requirement": "BD-06-011",
        "alias_requirement": "EP-06-005",
        "rationale": "Both statements express the same semantic invariant; 'luôn' does not create an independent requirement, and Business Decisions (Locked) is the canonical owner.",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "semantic_clarification": [
            "Mỗi Promotion có đúng một Funding Owner.",
            "Funding Owner là Organization tạo Promotion theo source hiện tại.",
            "V2.3 không hỗ trợ nhiều Funding Owner hoặc co-funded Promotion.",
            "Không suy diễn khả năng chuyển Funding Owner.",
            "Nếu tương lai hỗ trợ reassignment, phải có lifecycle, approval, effective date, financial reconciliation và audit.",
            "Promotion budget reservation/consumption phải hạch toán về Funding Owner này.",
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-PROB-002",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-06.md",
            "wording": "Promotion Funding thuộc Organization tạo Promotion.",
            "required_clarification": "The BRD must explicitly connect Promotion, Funding Owner, Organization ownership, and the associated financial lifecycle.",
            "minimum_definition": [
                "Promotion.",
                "Funding Owner.",
                "Organization ownership.",
                "Promotion budget reservation, consumption, and release.",
                "Financial attribution.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not design a financial model in Phase 1C.",
        },
    },
    "OVL-PROB-003": {
        "disposition": "CANONICAL_WITH_ALIAS_AND_FRAMEWORK_CLARIFICATION",
        "canonical_requirement": "BD-06-014",
        "alias_requirement": "EP-06-006",
        "rationale": "Both source statements represent the same invariant; BDD-11 and BDD-12 clarify that only the Final Promotion Snapshot is restricted to creation after Payment Success.",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_canonical_source_record": True,
        "preserve_alias_source_record": True,
        "effective_statement": "Final Promotion Snapshot is created only after Payment Success.",
        "governing_decisions": ["BDD-11", "BDD-12"],
        "source_semantics_status": "CLARIFIED_BY_FRAMEWORK_DECISION",
        "semantic_clarification": [
            "Source statement lịch sử được bảo toàn.",
            "Effective v2.3 meaning: Final Promotion Snapshot is created only after Payment Success.",
            "Từ 'chỉ' của EP-06-006 chỉ giới hạn Final Promotion Snapshot.",
            "Requirement này không cấm Evaluation Snapshot hoặc Reservation Snapshot trước Payment Success.",
        ],
        "promotion_snapshot_lifecycle": [
            {
                "stage": "EVALUATION",
                "creation_trigger": "Tạo khi promotion được đánh giá.",
                "captures": ["Inputs", "Eligibility", "Rule/policy version", "Calculated benefit"],
            },
            {
                "stage": "RESERVATION",
                "creation_trigger": "Tạo khi payment bắt đầu và promotion budget được reserve.",
                "captures": ["Budget reservation", "Price/promotion state", "Expiry/policy context"],
            },
            {
                "stage": "FINAL",
                "creation_trigger": "Chỉ tạo sau Payment Success.",
                "captures": ["Promotion outcome", "Consumed funding", "Final financial attribution"],
            },
        ],
        "alias_effective_semantics_inherited_from": "BD-06-014",
        "documentation_finding": {
            "finding_id": "DOC-OVL-PROB-003",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-06.md",
            "wording": "Promotion Snapshot chỉ được tạo sau Payment Success.",
            "required_clarification": "The v2.3 BRD must replace the old term with Final Promotion Snapshot and specify the complete snapshot lifecycle.",
            "minimum_definition": [
                "Change 'Promotion Snapshot' to 'Final Promotion Snapshot' in the old requirement.",
                "Specify the Evaluation, Reservation, and Final lifecycle.",
                "Link Promotion budget reserve, consume, and release behavior.",
                "Define snapshot immutability, version, input, funding, currency, and timestamp.",
                "Add transition and acceptance criteria.",
                "Remove the interpretation that no snapshot may exist before Payment Success.",
            ],
        },
    },
    "OVL-PROB-004": {
        "canonical_requirement": "SNP-P07",
        "alias_requirement": "SNP-EP-007",
        "rationale": "Both statements express the same semantic invariant and differ only in the order of Security Policy and Retention Policy; SNP-P07 — Policy Controlled is the canonical owner.",
        "canonical_requirement_type": "SECURITY_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "alias_scope_coverage_unit": False,
        "preserve_alias_source_record": True,
        "semantic_clarification": [
            "Mọi Snapshot đồng thời chịu Security Policy và Retention Policy.",
            "Security Policy quản lý authorization, classification, encryption, masking và access audit.",
            "Retention Policy quản lý retention duration, archival, legal hold và deletion/anonymization.",
            "Policy resolution xét data class, jurisdiction, Organization và platform minimum.",
            "Khi policy xung đột hoặc thiếu cấu hình bắt buộc, xử lý fail-closed và chuyển governance/approval; không tự chọn policy thắng.",
            "Snapshot immutability không loại bỏ nghĩa vụ retention/deletion.",
            "Cơ chế tombstone, crypto-erasure hoặc compliant archival phải được đặc tả ở phase tài liệu phù hợp.",
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-PROB-004",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-SNAPSHOT-INDEX.md",
            "wording": "Snapshot chịu sự điều khiển của Retention Policy và Security Policy.",
            "required_clarification": "The Snapshot/Policy specification must define the joint Security Policy and Retention Policy contract.",
            "minimum_definition": [
                "Policy precedence and conflict-resolution contract.",
                "Jurisdiction and data-class mapping.",
                "Legal hold.",
                "Immutable snapshot behavior with deletion/anonymization.",
                "Audit evidence.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not design a policy engine or storage mechanism in Phase 1C.",
        },
    },
}
OVERLAP_RETIRED_TEMPORARY_DECISIONS = {
    "OVL-EXACT-002": {
        "canonical_requirement": "BD-07-003",
        "retired_temporary_key": "TMP-BRD-WS-07-002",
        "superseded_by": "BD-07-003",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) sở hữu canonical requirement, còn normative prose là supporting source.",
    },
    "OVL-EXACT-003": {
        "canonical_requirement": "BD-08-001",
        "retired_temporary_key": "TMP-BRD-WS-08-001",
        "superseded_by": "BD-08-001",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) sở hữu canonical requirement, còn normative prose là supporting source.",
    },
    "OVL-EXACT-004": {
        "canonical_requirement": "BD-08-012",
        "retired_temporary_key": "TMP-BRD-WS-08-009",
        "superseded_by": "BD-08-012",
        "rationale": "Exact duplicate trong cùng source; Business Decision sở hữu canonical scope constraint, còn mục Partial Payment là supporting source.",
        "canonical_requirement_type": "SCOPE_CONSTRAINT",
        "canonical_scope_status": "OUT_OF_SCOPE",
        "canonical_scope_basis": "SOURCE_EXPLICIT",
        "preserve_retired_historical_state": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-004",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-08.md",
            "wording": "Version 2.0",
            "required_clarification": "Clarify 'Version 2.0' as the v2.3 baseline when the BRD is revised.",
            "phase_constraint": "Do not modify docs/BRD in Phase 1C.",
            "capability_distinction": "Partial Payment and Partial Refund are distinct capabilities.",
            "non_implication": "A decision to support Partial Refund does not activate Partial Payment.",
        },
    },
    "OVL-EXACT-005": {
        "canonical_requirement": "BD-09-002",
        "retired_temporary_key": "TMP-BRD-WS-09-002",
        "superseded_by": "BD-09-002",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) sở hữu canonical requirement, còn Inventory Ownership là supporting source.",
        "canonical_scope_status": "V2.3_ACTIVE",
        "supporting_source_section": "5. Inventory Ownership",
        "preserve_retired_historical_statement": True,
    },
    "OVL-EXACT-006": {
        "canonical_requirement": "BD-10-016",
        "retired_temporary_key": "TMP-BRD-WS-10-005",
        "superseded_by": "BD-10-016",
        "rationale": "Exact duplicate trong cùng source; Business Decision sở hữu canonical scope constraint, còn mục Payout là supporting source.",
        "canonical_requirement_type": "SCOPE_CONSTRAINT",
        "canonical_scope_status": "OUT_OF_SCOPE",
        "canonical_scope_basis": "SOURCE_EXPLICIT",
        "supporting_source_section": "20. Payout",
        "preserve_retired_historical_state": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-006",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-10.md",
            "wording": "Version 2.0",
            "required_clarification": "Correct 'Version 2.0' to the v2.3 baseline when the BRD is revised.",
            "scope_decision": "Auto Payout remains out of scope for v2.3 under SD-02.",
            "phase_constraint": "Do not modify docs/BRD in Phase 1C.",
        },
    },
    "OVL-EXACT-007": {
        "canonical_requirement": "BD-10-019",
        "retired_temporary_key": "TMP-BRD-WS-10-006",
        "superseded_by": "BD-10-019",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) sở hữu canonical data requirement, còn Financial Snapshot là supporting source.",
        "canonical_requirement_type": "DATA_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "supporting_source_section": "23. Financial Snapshot",
        "preserve_retired_historical_statement": True,
    },
    "OVL-EXACT-008": {
        "canonical_requirement": "BD-12-005",
        "retired_temporary_key": "TMP-BRD-WS-12-001",
        "superseded_by": "BD-12-005",
        "rationale": "Exact duplicate trong cùng source; Business Decisions (Locked) sở hữu canonical fallback requirement, còn Notification Channels là supporting source.",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_acceptance_status": "INFERRED_ONLY",
        "supporting_source_section": "7. Notification Channels",
        "semantic_clarification": [
            "Khi tất cả delivery channel bên ngoài được áp dụng đều thất bại hoặc không thể hoàn tất, hệ thống phải fallback về Personal Inbox.",
            "Personal Inbox là kênh nội bộ, không phụ thuộc nền tảng communication bên ngoài.",
            "Personal Inbox delivery thành công khi notification đã được persist bền vững và có thể truy xuất trong inbox của đúng recipient.",
            "Delivery success không đồng nghĩa recipient đã đọc notification.",
            "Nếu internal persistence tạm thời thất bại, hệ thống phải retry theo policy và đưa vào durable recovery/DLQ khi cần; không được đánh dấu success giả hoặc bỏ mất notification.",
        ],
        "acceptance_intent": [
            {"sequence": 1, "intent": "External channels được áp dụng đều fail hoặc không thể hoàn tất."},
            {"sequence": 2, "intent": "Personal Inbox fallback được tạo."},
            {"sequence": 3, "intent": "Notification được persist bền vững và có thể truy xuất cho đúng recipient."},
            {"sequence": 4, "intent": "Trạng thái phân biệt DELIVERED_TO_INBOX và READ."},
            {"sequence": 5, "intent": "Persistence failure không tạo false success, không làm mất notification và được retry/recover qua durable recovery hoặc DLQ khi cần."},
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-008",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-12.md",
            "wording": "cuối cùng",
            "required_clarification": "BRD v2.3 must replace 'cuối cùng' with explicit fallback semantics.",
            "delivery_distinction": "Distinguish external delivery, durable inbox persistence, and user read state.",
            "required_additions": "Add retry policy, durable recovery/DLQ behavior, and source-backed acceptance criteria when the BRD is revised.",
        },
    },
    "OVL-EXACT-015": {
        "canonical_requirement": "EP-15-002",
        "retired_temporary_key": "TMP-BRD-WS-15-002",
        "superseded_by": "EP-15-002",
        "rationale": "Exact duplicate trong cùng source; Enterprise Design Principle sở hữu canonical integration requirement, còn Integration Architecture là supporting source.",
        "canonical_requirement_type": "INTEGRATION_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "supporting_source_section": "3. Integration Architecture",
        "preserve_retired_historical_statement": True,
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-015",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-15.md",
            "wording": "Toàn bộ Integration phải đi qua Gateway, Connector và Adapter.",
            "required_clarification": "The Gateway, Connector, and Adapter constraint must be clarified when the BRD is revised.",
            "minimum_definition": [
                "Scope inbound, outbound, synchronous, asynchronous, batch, and event interactions.",
                "Clarify whether all three layers are always mandatory or depend on interaction type.",
                "Clarify whether internal domain-to-domain communication is subject to the constraint.",
                "Define approved exception and bypass policy.",
                "Define enforcement, observability, and acceptance criteria.",
            ],
            "phase_constraint": "Do not interpret or design an integration topology in Phase 1C.",
        },
    },
    "OVL-EXACT-029": {
        "canonical_requirement": "UXF-505",
        "retired_temporary_key": "TMP-UXF-05-013",
        "superseded_by": "UXF-505",
        "rationale": "Exact duplicate trong cùng source; UXF-505 owns the canonical technical-decoupling requirement and Allocation Principle remains supporting evidence.",
        "canonical_requirement_type": "UX_REQUIREMENT",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "canonical_acceptance_status": "INFERRED_ONLY",
        "supporting_source_section": "13. Allocation Principle",
        "preserve_retired_historical_statement": True,
        "semantic_clarification": [
            "Storefront không được lựa chọn supplier.",
            "Storefront không được gửi supplier-selection instruction hoặc tham gia routing.",
            "Storefront không gọi trực tiếp supplier connector/API.",
            "Procurement, allocation và supplier routing nằm sau application/domain contract tương ứng.",
            "Supplier/provider/network brand có thể được hiển thị read-only nếu catalog, product disclosure, legal hoặc market policy yêu cầu.",
            "Dữ liệu supplier được hiển thị không được dùng để điều khiển allocation/routing.",
            "Internal supplier identifiers, cost, priority, health và connector details không được lộ ra Storefront nếu không có explicit disclosure contract.",
        ],
        "acceptance_intent": [
            {"sequence": 1, "intent": "Storefront request không chứa supplier-selection instruction."},
            {"sequence": 2, "intent": "Storefront không gọi supplier connector."},
            {"sequence": 3, "intent": "Allocation là capability quyết định supplier."},
            {"sequence": 4, "intent": "Provider/brand disclosure, nếu có, chỉ là read-only presentation."},
            {"sequence": 5, "intent": "Internal supplier routing, cost, và health metadata không bị lộ."},
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-EXACT-029",
            "status": "DEFERRED_TO_UXF_CORRECTION",
            "source_document": "docs/UXF/UXF-05.md",
            "wording": "Storefronts never know suppliers.",
            "required_clarification": "Replace 'never know suppliers' with explicit technical-decoupling semantics when UXF is revised.",
            "classification_recommendation": "Consider DESIGN_PRINCIPLE instead of UX_REQUIREMENT when UXF is revised.",
            "minimum_definition": [
                "Distinguish supplier operational identity from provider/brand disclosure.",
                "Add source-backed acceptance criteria.",
            ],
            "phase_constraint": "Do not reclassify UXF-505 or design an allocation solution in Phase 1C.",
        },
    },
    "OVL-PROB-001": {
        "canonical_requirement": "BD-03-006",
        "retired_temporary_key": "TMP-BRD-WS-03-001",
        "superseded_by": "BD-03-006",
        "rationale": "Both statements express one semantic invariant; 'luôn' does not create an independent requirement, and Business Decisions (Locked) is the canonical owner.",
        "canonical_requirement_type": "BUSINESS_DECISION",
        "canonical_scope_status": "V2.3_ACTIVE",
        "canonical_scope_coverage_unit": True,
        "supporting_source_section": "9. Identity Domain",
        "preserve_retired_historical_statement": True,
        "semantic_clarification": [
            "Identity là canonical authentication identity.",
            "User là actor/membership trong Organization context.",
            "Customer là commercial/customer relationship concept.",
            "User và Customer có thể liên kết nhưng không phải cùng entity.",
            "Không dùng chung lifecycle hoặc mặc định đồng nhất record.",
            "Global Customer Identity/Profile phải tách khỏi Organization Customer Relationship theo quyết định v2.3.",
            "Một Identity có thể liên kết nhiều User records theo Organization.",
        ],
        "documentation_finding": {
            "finding_id": "DOC-OVL-PROB-001",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_document": "docs/BRD/BRD-WS-03.md",
            "wording": "User và Customer là hai Business Entity độc lập.",
            "required_clarification": "The BRD/domain specification must clarify the Identity–User–Customer relationship.",
            "minimum_definition": [
                "Cardinality between Identity, User, and Customer.",
                "Organization ownership and scope.",
                "Link/unlink behavior and lifecycle.",
                "Account provisioning.",
                "Merge and conflict rules.",
                "Authorization and data-isolation implications.",
                "Acceptance criteria.",
            ],
            "phase_constraint": "Do not create a detailed data model in Phase 1C.",
        },
    },
}
OVERLAP_RETIRED_TEMPORARIES_DECISIONS = {
    "OVL-EXACT-014": {
        "canonical_requirement": "EP-15-001",
        "retired_temporary_keys": ["TMP-BRD-WS-15-001", "TMP-BRD-WS-15-027"],
        "superseded_by": "EP-15-001",
        "rationale": "The three records form one semantic equivalence class for the atomic invariant that Business Domain must not integrate directly with external systems.",
        "equivalence_class_members": ["EP-15-001", "TMP-BRD-WS-15-001", "TMP-BRD-WS-15-027"],
        "canonical_scope_status": "V2.3_ACTIVE",
        "satisfies_composite_parents": ["BD-15-002"],
        "composite_child_substitutions": {
            "BD-15-002": {"TMP-BRD-WS-15-027": "EP-15-001"},
        },
    },
}
TRUNCATED_EXTRACTION_CORRECTIONS = {
    "OVL-EXACT-016": {
        "disposition": "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT",
        "correction_type": "CORRECTED_TRUNCATED_EXTRACTION",
        "rationale": "The extractor captured only the shared trailing fragment 'ở các phiên bản sau.', making two semantically distinct scope constraints appear identical.",
        "resulting_keys": ["TMP-BRD-WS-12-003", "TMP-BRD-WS-12-004"],
        "corrections": {
            "TMP-BRD-WS-12-003": {
                "statement": "Trong phạm vi Personal Inbox, Archive, Star và Pin chưa được triển khai trong v2.3; kiến trúc được để mở để hỗ trợ các năng lực này ở phiên bản sau.",
                "requirement_type": "SCOPE_CONSTRAINT",
                "scope_status": "FUTURE",
                "scope_basis": "SOURCE_EXPLICIT",
                "source_section": "9. Personal Inbox",
                "source_start": 232,
                "source_end": 245,
                "required_excerpt_fragments": ["Read", "Read All", "Search", "Filter", "Kiến trúc mở để hỗ trợ", "Archive", "Star", "Pin", "ở các phiên bản sau."],
            },
            "TMP-BRD-WS-12-004": {
                "statement": "Trong phạm vi Localization, hỗ trợ Left-To-Right và Right-To-Left chưa được triển khai trong v2.3; kiến trúc được để mở để hỗ trợ ở phiên bản sau.",
                "requirement_type": "SCOPE_CONSTRAINT",
                "scope_status": "FUTURE",
                "scope_basis": "SOURCE_EXPLICIT",
                "source_section": "14. Localization",
                "source_start": 331,
                "source_end": 350,
                "required_excerpt_fragments": ["Language", "Currency", "Date Format", "Time Format", "Kiến trúc mở để hỗ trợ", "Left-To-Right", "Right-To-Left", "ở các phiên bản sau."],
            },
        },
    },
}
CHANNEL_CONTEXT_CORRECTIONS = {
    "OVL-EXACT-021": {
        "disposition": "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT",
        "correction_type": "CORRECTED_TRUNCATED_CHANNEL_CONTEXT",
        "rationale": "The three records share the authentication-required predicate but apply to distinct experience channels; Phase 1C restores channel context without inferring a shared authentication solution.",
        "resulting_keys": ["TMP-UXF-01-001", "TMP-UXF-01-002", "TMP-UXF-01-003"],
        "corrections": {
            "TMP-UXF-01-001": {
                "statement": "Platform Administration Portal requires authentication.",
                "applicability_scope": {"scope_type": "EXPERIENCE_CHANNEL", "channel": "PLATFORM_ADMINISTRATION_PORTAL"},
                "requirement_type": "SECURITY_REQUIREMENT",
                "scope_status": "V2.3_ACTIVE",
                "source_section": "3. Experience Channels > 3.1 Platform Administration Portal",
                "source_start": 61,
                "source_end": 86,
                "required_excerpt_fragments": ["3.1 Platform Administration Portal", "Authentication:", "Required"],
            },
            "TMP-UXF-01-002": {
                "statement": "Organization Portal requires authentication.",
                "applicability_scope": {"scope_type": "EXPERIENCE_CHANNEL", "channel": "ORGANIZATION_PORTAL"},
                "requirement_type": "SECURITY_REQUIREMENT",
                "scope_status": "V2.3_ACTIVE",
                "source_section": "3. Experience Channels > 3.2 Organization Portal",
                "source_start": 94,
                "source_end": 114,
                "required_excerpt_fragments": ["3.2 Organization Portal", "Authentication:", "Required"],
            },
            "TMP-UXF-01-003": {
                "statement": "Agency Portal requires authentication.",
                "applicability_scope": {"scope_type": "EXPERIENCE_CHANNEL", "channel": "AGENCY_PORTAL"},
                "requirement_type": "SECURITY_REQUIREMENT",
                "scope_status": "V2.3_ACTIVE",
                "source_section": "3. Experience Channels > 3.3 Agency Portal",
                "source_start": 118,
                "source_end": 137,
                "required_excerpt_fragments": ["3.3 Agency Portal", "Authentication:", "Required"],
            },
        },
    },
}
APPLICABILITY_SCOPE_CORRECTIONS = {
    "OVL-PROB-006": {
        "disposition": "DISTINCT_BY_APPLICABILITY",
        "correction_type": "CONTEXTUALIZED_DISTINCT_APPLICABILITY",
        "rationale": "The records are independent scope constraints for different bounded contexts and acceptance surfaces; shared Video exclusion wording does not make them duplicates or an equivalence class.",
        "resulting_keys": ["TMP-BRD-WS-11-010", "TMP-BRD-WS-12-013"],
        "corrections": {
            "TMP-BRD-WS-11-010": {
                "statement": "Attachment của Customer Support Ticket không hỗ trợ Video trong v2.3.",
                "source_statement": "Không hỗ trợ Video trong Version 2.0.",
                "applicability_scope": {
                    "scope_type": "ATTACHMENT_CONTEXT",
                    "attachment_context": "CUSTOMER_SUPPORT_TICKET_ATTACHMENT",
                },
                "requirement_type": "SCOPE_CONSTRAINT",
                "scope_status": "OUT_OF_SCOPE",
                "scope_basis": "SOURCE_EXPLICIT",
                "source_section": "24. Attachment",
                "source_start": 541,
                "source_end": 550,
                "required_excerpt_fragments": [
                    "# 24. Attachment", "Ticket hỗ trợ:", "Image", "PDF", "QR", "Invoice",
                    "Không hỗ trợ Video trong Version 2.0.",
                ],
            },
            "TMP-BRD-WS-12-013": {
                "statement": "Attachment của Notification không hỗ trợ Video trong v2.3.",
                "source_statement": "Không hỗ trợ Video trong Version 2.",
                "applicability_scope": {
                    "scope_type": "ATTACHMENT_CONTEXT",
                    "attachment_context": "NOTIFICATION_ATTACHMENT",
                },
                "requirement_type": "SCOPE_CONSTRAINT",
                "scope_status": "OUT_OF_SCOPE",
                "scope_basis": "SOURCE_EXPLICIT",
                "source_section": "25. Attachment",
                "source_start": 481,
                "source_end": 490,
                "required_excerpt_fragments": [
                    "# 25. Attachment", "Notification hỗ trợ:", "Image", "PDF", "Invoice", "QR Code",
                    "Không hỗ trợ Video trong Version 2.",
                ],
            },
        },
        "documentation_finding": {
            "finding_id": "DOC-OVL-PROB-006",
            "status": "DEFERRED_TO_BRD_CORRECTION",
            "source_documents": ["docs/BRD/BRD-WS-11.md", "docs/BRD/BRD-WS-12.md"],
            "wording": ["Version 2.0", "Version 2"],
            "required_clarification": "Normalize both version labels to v2.3 when docs/BRD is revised.",
            "scope_boundary": "The Video exclusion applies only to Customer Support Ticket attachments and Notification attachments.",
            "non_implication": "Phase 1C must not generalize this decision into a platform-wide Attachment policy.",
            "future_architecture": "If a shared Attachment capability is later established, its shared relationship must be designed in an architecture phase rather than this reconciliation.",
        },
    },
}


def reconcile_registries(raw_registries: dict[str, dict], qa: dict) -> tuple[dict[str, dict], dict]:
    raw_requirements = [req for registry in raw_registries.values() for req in registry["requirements"]]
    raw_by_key = {requirement_key(req): req for req in raw_requirements}
    fp = qa_findings(qa, "false_positive_candidates")
    fn = qa_findings(qa, "false_negative_candidates")
    compounds = qa_findings(qa, "compound_statement_candidates")
    fp_keys = {item["key"] for item in fp}
    retired = set(fp_keys - FP_REQUIREMENTS)
    retired.update(decision["retired_temporary_key"] for decision in OVERLAP_RETIRED_TEMPORARY_DECISIONS.values())
    retired.update(
        key for decision in OVERLAP_RETIRED_TEMPORARIES_DECISIONS.values()
        for key in decision["retired_temporary_keys"]
    )
    retired_temporary_records = []
    records = []
    for item in fp:
        key = item["key"]
        keep = key in FP_REQUIREMENTS
        records.append(ledger_record(
            key, "FALSE_POSITIVE_CANDIDATE",
            "CONFIRMED_REQUIREMENT" if keep else "CONFIRMED_FALSE_POSITIVE",
            ("Source defines a release, identifier-stability, or versioning constraint with product semantics."
             if keep else "Source is navigation, traceability, an AI-authoring instruction, a standalone label, descriptive text, or an incomplete fragment without product semantics."),
            [key] if keep else [],
            {"source_document": item["source_document"], "source_lines": item["source_anchor"], "qa_reason": item["reason"]},
        ))

    max_sequence: defaultdict[str, int] = defaultdict(int)
    document_code = {}
    for registry in raw_registries.values():
        document_code.update({doc["path"]: doc["document_code"] for doc in registry["documents"]})
    for req in raw_requirements:
        if req["temporary_key"]:
            max_sequence[document_code[req["source_document"]]] = max(
                max_sequence[document_code[req["source_document"]]], int(req["temporary_key"].rsplit("-", 1)[1])
            )

    def allocate(source_document: str) -> str:
        code = document_code[source_document]
        max_sequence[code] += 1
        return f"TMP-{code}-{max_sequence[code]:03d}"

    active = []
    split_result_keys = {}
    composite_result_keys = {}
    derived_child_sources = {}
    corrected_extraction_provenance = {}
    channel_context_provenance = {}
    applicability_scope_provenance = {}
    for raw in raw_requirements:
        key = requirement_key(raw)
        if key in retired:
            continue
        if key in SPLIT_SPECS:
            retired.add(key)
            children = []
            for statement in SPLIT_SPECS[key]:
                child = stable_entry(raw)
                child["current_id"] = None
                child["temporary_key"] = allocate(raw["source_document"])
                child["statement"] = statement
                child["derived_from"] = [key]
                child["referenced_requirements"] = sorted(set(REQ_REF_RE.findall(statement)))
                child["scope_status"], child["ambiguity"] = scope_for(statement)
                child["source_scope_status"] = child["scope_status"]
                child["scope_basis"], child["scope_evidence"] = scope_provenance(
                    "BRD" if raw["source_document"].startswith("docs/BRD/") else "UXF",
                    {"start": parse_anchor(raw["source_anchor"])[0], "end": parse_anchor(raw["source_anchor"])[1], "statement": statement},
                    child["scope_status"], child["ambiguity"],
                )
                child["requirement_type"] = semantic_requirement_type(child, (ROOT / child["source_document"]).read_text(encoding="utf-8").splitlines())
                active.append(child)
                children.append(requirement_key(child))
            split_result_keys[key] = children
            continue
        entry = stable_entry(raw)
        if key in COMPOSITE_PARENT_SPLITS:
            children = []
            child_entries = []
            for specification in COMPOSITE_PARENT_SPLITS[key]:
                child = stable_entry(raw)
                child["current_id"] = None
                child["temporary_key"] = allocate(raw["source_document"])
                child["statement"] = specification["statement"]
                child["derived_from"] = [key]
                child["requirement_type"] = specification["requirement_type"]
                child["scope_status"] = entry["scope_status"]
                child["source_scope_status"] = entry["source_scope_status"]
                child["scope_basis"] = entry["scope_basis"]
                child["scope_evidence"] = entry["scope_evidence"]
                child["scope_conflict_resolved"] = entry["scope_conflict_resolved"]
                child["lifecycle_status"] = entry["lifecycle_status"]
                child["acceptance_present"] = False
                child["acceptance_status"] = "INFERRED_ONLY"
                child["acceptance_references"] = []
                child["ambiguity"] = entry["ambiguity"]
                child["referenced_requirements"] = sorted(set(REQ_REF_RE.findall(child["statement"])))
                child["extraction_kind"] = "COMPOSITE_PARENT_CHILD"
                child_key = requirement_key(child)
                derived_child_sources[child_key] = child
                replacement = COMPOSITE_CHILD_SUBSTITUTIONS.get(key, {}).get(child_key)
                if child_key in retired and replacement:
                    children.append(replacement)
                else:
                    child_entries.append(child)
                    children.append(child_key)
            entry["is_composite"] = True
            entry["implementation_unit"] = False
            entry["acceptance_unit"] = False
            entry["coverage_mode"] = "ALL_CHILDREN"
            entry["derived_requirements"] = children
            composite_result_keys[key] = children
        active.append(entry)
        if key in COMPOSITE_PARENT_SPLITS:
            active.extend(child_entries)

    fn_actions = {
        ("docs/BRD/BRD-WS-09.md", "L491"): ("ADD", 487, 491, "SECURITY_REQUIREMENT"),
        ("docs/BRD/BRD-WS-17.md", "L612"): ("ADD", 612, 612, "SCOPE_CONSTRAINT"),
        ("docs/BRD/BRD-WS-17.md", "L922"): ("ADD", 922, 922, "SCOPE_CONSTRAINT"),
    }
    fn_result = {}
    for item in fn:
        identity = (item["source_document"], item["source_anchor"])
        action = fn_actions.get(identity)
        if action:
            _, start, end, req_type = action
            path = ROOT / item["source_document"]
            loc = source_locator(path, start, end)
            statement = loc["source_excerpt"]
            key = allocate(item["source_document"])
            meta = frontmatter(path.read_text(encoding="utf-8").splitlines())
            scope, ambiguity = scope_for(statement)
            if identity[1] in {"L612", "L922"}:
                scope = "OUT_OF_SCOPE"
                ambiguity = None
            req = {
                "source_document": item["source_document"], **loc,
                "statement": statement, "current_id": None, "temporary_key": key,
                "requirement_type": req_type, "scope_status": scope,
                "source_scope_status": scope, "scope_basis": "SOURCE_EXPLICIT" if scope != "V2.3_ACTIVE" else "BASELINE_INHERITANCE",
                "scope_evidence": loc["source_lines"] if scope != "V2.3_ACTIVE" else "V23-DOCUMENT-BASELINE §4 (BRD ADOPTED)",
                "scope_conflict_resolved": False, "lifecycle_status": lifecycle_for(meta["status"]),
                "priority": None, "acceptance_present": False, "acceptance_status": "INFERRED_ONLY",
                "acceptance_references": [], "ambiguity": ambiguity, "duplicate_or_overlap": [],
                "referenced_requirements": sorted(set(REQ_REF_RE.findall(statement))),
                "derived_from": [f"{item['source_document']}:{item['source_anchor']}"],
                "extraction_kind": "RECONCILED_FALSE_NEGATIVE",
            }
            active.append(req)
            fn_result[identity] = key
            disposition = "CONFIRMED_REQUIREMENT"
            rationale = "Context supplies mandatory authentication behavior or an explicit current-release scope constraint."
            resulting = [key]
        else:
            disposition = "EXCLUDED"
            rationale = "Candidate is a catalog/error label, a workshop-document boundary, or is already represented by the collective future-scope requirement TMP-BRD-WS-13-007."
            resulting = []
        records.append(ledger_record(
            f"{item['source_document']}:{item['source_anchor']}", "FALSE_NEGATIVE_CANDIDATE",
            disposition, rationale, resulting,
            {"source_document": item["source_document"], "source_lines": item["source_anchor"], "text": item["text"]},
        ))

    active_by_key = {requirement_key(req): req for req in active}
    for decision in OVERLAP_ALIAS_DECISIONS.values():
        canonical_key = decision["canonical_requirement"]
        alias_key = decision["alias_requirement"]
        canonical = active_by_key[canonical_key]
        alias = active_by_key[alias_key]
        canonical["is_canonical"] = True
        canonical["aliases"] = sorted(set(canonical.get("aliases", [])) | {alias_key})
        canonical["implementation_unit"] = True
        canonical["acceptance_unit"] = True
        canonical["requirement_type"] = decision.get("canonical_requirement_type", canonical["requirement_type"])
        canonical["scope_status"] = decision.get("canonical_scope_status", canonical["scope_status"])
        if "canonical_scope_coverage_unit" in decision:
            canonical["scope_coverage_unit"] = decision["canonical_scope_coverage_unit"]
        if "semantic_clarification" in decision:
            canonical["semantic_clarification"] = decision["semantic_clarification"]
        if "effective_statement" in decision:
            canonical["effective_statement"] = decision["effective_statement"]
            canonical["governed_by_decisions"] = decision["governing_decisions"]
            canonical["source_semantics_status"] = decision["source_semantics_status"]
        if "promotion_snapshot_lifecycle" in decision:
            canonical["promotion_snapshot_lifecycle"] = decision["promotion_snapshot_lifecycle"]
        alias["record_kind"] = "ALIAS"
        alias["alias_of"] = canonical_key
        alias["implementation_unit"] = False
        alias["acceptance_unit"] = False
        if "alias_scope_coverage_unit" in decision:
            alias["scope_coverage_unit"] = decision["alias_scope_coverage_unit"]
        alias["coverage_mode"] = "CANONICAL"
        if "alias_effective_semantics_inherited_from" in decision:
            alias["effective_semantics_inherited_from"] = decision["alias_effective_semantics_inherited_from"]
    for decision in OVERLAP_RETIRED_TEMPORARY_DECISIONS.values():
        canonical_key = decision["canonical_requirement"]
        retired_key = decision["retired_temporary_key"]
        canonical = active_by_key[canonical_key]
        retired_source = stable_entry(raw_by_key[retired_key])
        supporting_source = {
            "source_key": retired_key,
            "source_document": retired_source["source_document"],
            "source_section": retired_source["source_section"],
            "source_anchor": retired_source["source_anchor"],
            "source_lines": retired_source["source_lines"],
            "source_excerpt": retired_source["source_excerpt"],
            "source_fingerprint": retired_source["source_fingerprint"],
            "statement": retired_source["statement"],
        }
        canonical["is_canonical"] = True
        canonical["implementation_unit"] = True
        canonical["acceptance_unit"] = True
        canonical["supporting_sources"] = [supporting_source]
        if "canonical_scope_coverage_unit" in decision:
            canonical["scope_coverage_unit"] = decision["canonical_scope_coverage_unit"]
        canonical["requirement_type"] = decision.get("canonical_requirement_type", canonical["requirement_type"])
        canonical["scope_status"] = decision.get("canonical_scope_status", canonical["scope_status"])
        canonical["scope_basis"] = decision.get("canonical_scope_basis", canonical["scope_basis"])
        if "semantic_clarification" in decision:
            canonical["semantic_clarification"] = decision["semantic_clarification"]
        if "acceptance_intent" in decision:
            canonical["acceptance_intent"] = decision["acceptance_intent"]
        if "canonical_acceptance_status" in decision:
            canonical["acceptance_status"] = decision["canonical_acceptance_status"]
            canonical["acceptance_present"] = decision["canonical_acceptance_status"] in {"DIRECT", "LINKED"}
            canonical["acceptance_references"] = []
        retired_record = {
            "temporary_key": retired_key,
            "disposition": "SUPERSEDED_BY",
            "superseded_by": decision["superseded_by"],
            **supporting_source,
        }
        if decision.get("preserve_retired_historical_state"):
            retired_record["historical_state"] = {
                field: retired_source[field] for field in (
                    "requirement_type", "scope_status", "source_scope_status", "scope_basis",
                    "scope_evidence", "lifecycle_status", "scope_conflict_resolved",
                )
            }
        retired_temporary_records.append(retired_record)

    for decision in OVERLAP_RETIRED_TEMPORARIES_DECISIONS.values():
        canonical_key = decision["canonical_requirement"]
        canonical = active_by_key[canonical_key]
        supporting_sources = []
        for retired_key in decision["retired_temporary_keys"]:
            raw_source = raw_by_key.get(retired_key)
            retired_source = stable_entry(raw_source) if raw_source else derived_child_sources[retired_key]
            supporting_source = {
                "source_key": retired_key,
                "source_document": retired_source["source_document"],
                "source_section": retired_source["source_section"],
                "source_anchor": retired_source["source_anchor"],
                "source_lines": retired_source["source_lines"],
                "source_excerpt": retired_source["source_excerpt"],
                "source_fingerprint": retired_source["source_fingerprint"],
                "statement": retired_source["statement"],
            }
            supporting_sources.append(supporting_source)
            retired_temporary_records.append({
                "temporary_key": retired_key,
                "disposition": "SUPERSEDED_BY",
                "superseded_by": decision["superseded_by"],
                **supporting_source,
                "historical_derivation": retired_source.get("derived_from", []),
            })
        canonical["is_canonical"] = True
        canonical["implementation_unit"] = True
        canonical["acceptance_unit"] = True
        canonical["scope_coverage_unit"] = True
        canonical["scope_status"] = decision["canonical_scope_status"]
        canonical["supporting_sources"] = supporting_sources
        canonical["satisfies_composite_parents"] = decision["satisfies_composite_parents"]

    for group_id, decision in TRUNCATED_EXTRACTION_CORRECTIONS.items():
        group_provenance = {}
        for key, correction in decision["corrections"].items():
            entry = active_by_key[key]
            before = {
                "statement": entry["statement"],
                "source_lines": entry["source_lines"],
                "source_excerpt": entry["source_excerpt"],
                "source_fingerprint": entry["source_fingerprint"],
            }
            locator = source_locator(
                ROOT / entry["source_document"], correction["source_start"], correction["source_end"]
            )
            entry.update(locator)
            entry["statement"] = correction["statement"]
            entry["requirement_type"] = correction["requirement_type"]
            entry["scope_status"] = correction["scope_status"]
            entry["source_scope_status"] = correction["scope_status"]
            entry["scope_basis"] = correction["scope_basis"]
            entry["scope_evidence"] = locator["source_lines"]
            entry["extraction_kind"] = decision["correction_type"]
            entry["reconciliation_provenance"] = {
                "group_id": group_id,
                "correction_type": decision["correction_type"],
                "before_source_lines": before["source_lines"],
                "before_source_fingerprint": before["source_fingerprint"],
            }
            group_provenance[key] = {
                "before": before,
                "after": {
                    "statement": entry["statement"],
                    "source_lines": entry["source_lines"],
                    "source_excerpt": entry["source_excerpt"],
                    "source_fingerprint": entry["source_fingerprint"],
                },
            }
        corrected_extraction_provenance[group_id] = group_provenance

    for group_id, decision in CHANNEL_CONTEXT_CORRECTIONS.items():
        group_provenance = {}
        for key, correction in decision["corrections"].items():
            entry = active_by_key[key]
            before = {
                "statement": entry["statement"],
                "source_lines": entry["source_lines"],
                "source_excerpt": entry["source_excerpt"],
                "source_fingerprint": entry["source_fingerprint"],
            }
            locator = source_locator(
                ROOT / entry["source_document"], correction["source_start"], correction["source_end"]
            )
            entry.update(locator)
            entry["statement"] = correction["statement"]
            entry["applicability_scope"] = correction["applicability_scope"]
            entry["requirement_type"] = correction["requirement_type"]
            entry["scope_status"] = correction["scope_status"]
            entry["source_scope_status"] = correction["scope_status"]
            entry["extraction_kind"] = decision["correction_type"]
            entry["reconciliation_provenance"] = {
                "group_id": group_id,
                "correction_type": decision["correction_type"],
                "before_source_lines": before["source_lines"],
                "before_source_fingerprint": before["source_fingerprint"],
            }
            group_provenance[key] = {
                "before": before,
                "after": {
                    "statement": entry["statement"],
                    "applicability_scope": entry["applicability_scope"],
                    "source_lines": entry["source_lines"],
                    "source_excerpt": entry["source_excerpt"],
                    "source_fingerprint": entry["source_fingerprint"],
                },
            }
        channel_context_provenance[group_id] = group_provenance

    for group_id, decision in APPLICABILITY_SCOPE_CORRECTIONS.items():
        group_provenance = {}
        for key, correction in decision["corrections"].items():
            entry = active_by_key[key]
            before = {
                "statement": entry["statement"],
                "source_lines": entry["source_lines"],
                "source_excerpt": entry["source_excerpt"],
                "source_fingerprint": entry["source_fingerprint"],
            }
            locator = source_locator(
                ROOT / entry["source_document"], correction["source_start"], correction["source_end"]
            )
            entry.update(locator)
            entry["statement"] = correction["statement"]
            entry["source_statement"] = correction["source_statement"]
            entry["applicability_scope"] = correction["applicability_scope"]
            entry["requirement_type"] = correction["requirement_type"]
            entry["scope_status"] = correction["scope_status"]
            entry["source_scope_status"] = correction["scope_status"]
            entry["scope_basis"] = correction["scope_basis"]
            entry["scope_evidence"] = locator["source_lines"]
            entry["implementation_unit"] = True
            entry["acceptance_unit"] = True
            entry["scope_coverage_unit"] = True
            entry["extraction_kind"] = decision["correction_type"]
            entry["reconciliation_provenance"] = {
                "group_id": group_id,
                "correction_type": decision["correction_type"],
                "before_source_lines": before["source_lines"],
                "before_source_fingerprint": before["source_fingerprint"],
            }
            group_provenance[key] = {
                "before": before,
                "after": {
                    "statement": entry["statement"],
                    "source_statement": entry["source_statement"],
                    "applicability_scope": entry["applicability_scope"],
                    "source_lines": entry["source_lines"],
                    "source_excerpt": entry["source_excerpt"],
                    "source_fingerprint": entry["source_fingerprint"],
                },
            }
        applicability_scope_provenance[group_id] = group_provenance

    for item in compounds:
        key = item["key"]
        if key in SPLIT_SPECS:
            disposition, rationale, resulting, reviewer = (
                "SPLIT", "The source contains independently implementable and independently testable normative clauses.",
                split_result_keys[key], "RECONCILED",
            )
        elif key in COMPOSITE_PARENT_SPLITS:
            disposition, rationale, resulting, reviewer = (
                "SPLIT_AS_COMPOSITE_PARENT",
                "Human decision preserves the canonical statement verbatim as a non-atomic composite parent and delegates implementation and acceptance coverage to both atomic children.",
                composite_result_keys[key], "RECONCILED",
            )
        elif key in COMPOUND_UNRESOLVED:
            disposition, rationale, resulting, reviewer = (
                "NEEDS_HUMAN_DECISION", "The canonical statement contains independent clauses; splitting requires a decision on whether the canonical ID is a parent or the primary atomic requirement.",
                [key], "HUMAN_REVIEW_REQUIRED",
            )
        elif key in retired:
            disposition, rationale, resulting, reviewer = (
                "EXCLUDED_WITH_MEMBERSHIP_FINDING", "The entry was excluded by the false-positive membership review; no atomic product requirement remains.",
                [], "RECONCILED",
            )
        else:
            disposition, rationale, resulting, reviewer = (
                "REVIEWED_NO_SPLIT", "The list is a cohesive value/component set, rationale, or one invariant whose elements do not have independent requirement semantics.",
                [key], "RECONCILED",
            )
        record = ledger_record(
            key, "COMPOUND_STATEMENT_CANDIDATE", disposition, rationale, resulting,
            {"source_document": item["source_document"], "source_lines": item["source_anchor"], "bullet_count": item["bullet_count"], "normative_signal_count": item["normative_signal_count"]}, reviewer,
        )
        if disposition == "SPLIT_AS_COMPOSITE_PARENT":
            record["composite_parent"] = key
            record["coverage_mode"] = "ALL_CHILDREN"
        records.append(record)

    # Recompute exact duplicates only after membership and split decisions.
    reconciled = {}
    for name in ("BRD", "UXF"):
        registry = dict(raw_registries[name])
        registry["schema_version"] = "2.0"
        registry["phase"] = "Documentation Governance v2.3 Phase 1C Reconciliation"
        registry["requirements"] = [req for req in active if req["source_document"].startswith(f"docs/{name}/")]
        counts = Counter(req["source_document"] for req in registry["requirements"])
        registry["documents"] = [dict(doc, requirement_count=counts[doc["path"]], requirement_ids=[req["current_id"] for req in registry["requirements"] if req["source_document"] == doc["path"] and req["current_id"]]) for doc in registry["documents"]]
        reconciled[name] = registry
    overlap = build_overlap_analysis(reconciled)
    overlap_by_key: defaultdict[str, set[str]] = defaultdict(set)
    for pair in overlap["pairs"]:
        overlap_by_key[pair["left"]].add(pair["right"])
        overlap_by_key[pair["right"]].add(pair["left"])
    for registry in reconciled.values():
        for req in registry["requirements"]:
            req["duplicate_or_overlap"] = sorted(overlap_by_key[requirement_key(req)])

    active_keys = {requirement_key(req) for registry in reconciled.values() for req in registry["requirements"]}
    for finding in qa["classification_findings"]:
        key = finding["key"]
        records.append(ledger_record(
            key, finding["finding"], "CONFIRMED_SEMANTIC_TYPE" if key in active_keys else "RESOLVED_BY_EXCLUSION",
            "Type was derived from statement meaning and source section; temporary/canonical key form was not used as the sole classifier.",
            [key] if key in active_keys else [],
            {"source_document": finding["source_document"], "source_lines": finding["source_anchor"], "evidence": finding["evidence"]},
        ))
    transitive_resolution_by_group = {}
    for decision_group, decision in OVERLAP_RETIRED_TEMPORARIES_DECISIONS.items():
        equivalence_members = set(decision["equivalence_class_members"])
        for group in qa["overlap_normalization"]["groups"]:
            if group["group_id"] == decision_group or not (equivalence_members & set(group["members"])):
                continue
            if len([key for key in group["members"] if key in active_keys]) <= 1:
                transitive_resolution_by_group[group["group_id"]] = decision_group
    for group in qa["overlap_normalization"]["groups"]:
        remaining = [key for key in group["members"] if key in active_keys]
        if group["group_id"] in OVERLAP_ALIAS_DECISIONS:
            decision = OVERLAP_ALIAS_DECISIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", decision.get("disposition", "CANONICAL_WITH_ALIAS"),
                decision["rationale"], [decision["canonical_requirement"], decision["alias_requirement"]],
                {"members_before": group["members"], "classification": group["classification"]}, "RECONCILED",
            )
            record["canonical_requirement"] = decision["canonical_requirement"]
            record["alias_requirement"] = decision["alias_requirement"]
            if "semantic_clarification" in decision:
                record["semantic_clarification"] = decision["semantic_clarification"]
            for field in ("effective_statement", "governing_decisions", "source_semantics_status", "promotion_snapshot_lifecycle"):
                if field in decision:
                    record[field] = decision[field]
            if "documentation_finding" in decision:
                record["documentation_finding"] = decision["documentation_finding"]
            records.append(record)
        elif group["group_id"] in OVERLAP_RETIRED_TEMPORARY_DECISIONS:
            decision = OVERLAP_RETIRED_TEMPORARY_DECISIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", "CANONICAL_WITH_RETIRED_TEMPORARY",
                decision["rationale"], [decision["canonical_requirement"]],
                {"members_before": group["members"], "classification": group["classification"]}, "RECONCILED",
            )
            record["canonical_requirement"] = decision["canonical_requirement"]
            record["retired_temporary_key"] = decision["retired_temporary_key"]
            record["superseded_by"] = decision["superseded_by"]
            for field in ("semantic_clarification", "acceptance_intent", "canonical_acceptance_status"):
                if field in decision:
                    record[field] = decision[field]
            if "documentation_finding" in decision:
                record["documentation_finding"] = decision["documentation_finding"]
            records.append(record)
        elif group["group_id"] in OVERLAP_RETIRED_TEMPORARIES_DECISIONS:
            decision = OVERLAP_RETIRED_TEMPORARIES_DECISIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", "CANONICAL_WITH_RETIRED_TEMPORARIES",
                decision["rationale"], [decision["canonical_requirement"]],
                {
                    "members_before": decision["equivalence_class_members"],
                    "raw_group_members": group["members"],
                    "classification": group["classification"],
                }, "RECONCILED",
            )
            record["canonical_requirement"] = decision["canonical_requirement"]
            record["retired_temporary_keys"] = decision["retired_temporary_keys"]
            record["superseded_by"] = decision["superseded_by"]
            record["equivalence_class_members"] = decision["equivalence_class_members"]
            record["satisfies_composite_parents"] = decision["satisfies_composite_parents"]
            record["composite_child_substitutions"] = decision["composite_child_substitutions"]
            records.append(record)
        elif group["group_id"] in transitive_resolution_by_group:
            decision_group = transitive_resolution_by_group[group["group_id"]]
            records.append(ledger_record(
                group["group_id"], "OVERLAP_GROUP", "RESOLVED_TRANSITIVELY_BY_EQUIVALENCE_CLASS",
                f"Resolved transitively because {decision_group} retired non-canonical members of the same semantic equivalence class.",
                remaining,
                {
                    "members_before": group["members"],
                    "classification": group["classification"],
                    "equivalence_class_decision": decision_group,
                }, "RECONCILED",
            ))
        elif group["group_id"] in TRUNCATED_EXTRACTION_CORRECTIONS:
            decision = TRUNCATED_EXTRACTION_CORRECTIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", decision["disposition"],
                decision["rationale"], decision["resulting_keys"],
                {
                    "members_before": group["members"],
                    "classification": group["classification"],
                    "shared_fragment": "ở các phiên bản sau.",
                }, "RECONCILED",
            )
            record["correction_type"] = decision["correction_type"]
            record["extraction_corrections"] = corrected_extraction_provenance[group["group_id"]]
            records.append(record)
        elif group["group_id"] in CHANNEL_CONTEXT_CORRECTIONS:
            decision = CHANNEL_CONTEXT_CORRECTIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", decision["disposition"],
                decision["rationale"], decision["resulting_keys"],
                {
                    "members_before": group["members"],
                    "classification": group["classification"],
                    "shared_predicate": "requires authentication",
                    "scope_distinction": "Statements share a predicate but have distinct EXPERIENCE_CHANNEL applicability scopes.",
                }, "RECONCILED",
            )
            record["correction_type"] = decision["correction_type"]
            record["channel_context_corrections"] = channel_context_provenance[group["group_id"]]
            record["applicability_scopes"] = {
                key: correction["applicability_scope"] for key, correction in decision["corrections"].items()
            }
            records.append(record)
        elif group["group_id"] in APPLICABILITY_SCOPE_CORRECTIONS:
            decision = APPLICABILITY_SCOPE_CORRECTIONS[group["group_id"]]
            record = ledger_record(
                group["group_id"], "OVERLAP_GROUP", decision["disposition"],
                decision["rationale"], decision["resulting_keys"],
                {
                    "members_before": group["members"],
                    "classification": group["classification"],
                    "scope_distinction": "The statements describe separate attachment bounded contexts and acceptance surfaces.",
                }, "RECONCILED",
            )
            record["correction_type"] = decision["correction_type"]
            record["applicability_context_corrections"] = applicability_scope_provenance[group["group_id"]]
            record["applicability_scopes"] = {
                key: correction["applicability_scope"] for key, correction in decision["corrections"].items()
            }
            record["documentation_finding"] = decision["documentation_finding"]
            records.append(record)
        else:
            potential = group["classification"].startswith("POTENTIAL_ACCIDENTAL") and len(remaining) > 1
            records.append(ledger_record(
                group["group_id"], "OVERLAP_GROUP",
                "NEEDS_HUMAN_DECISION" if potential else "INTENTIONAL_DUPLICATE" if len(remaining) > 1 else "RESOLVED_BY_EXCLUSION",
                "Potential accidental semantic overlap requires human ownership review." if potential else "Shared UX repetition is intentional or membership reconciliation removed the duplicate.",
                remaining, {"members_before": group["members"], "classification": group["classification"]},
                "HUMAN_REVIEW_REQUIRED" if potential else "RECONCILED",
            ))
    for req in active:
        if req["scope_conflict_resolved"]:
            records.append(ledger_record(
                requirement_key(req), "SCOPE_CONFLICT", "RESOLVED_BY_FRAMEWORK_DECISION",
                "FRAMEWORK_DECISIONS explicitly restores this legacy future/deferred item to v2.3 scope.",
                [requirement_key(req)], {"source_scope_status": req["source_scope_status"], "decision_id": req["scope_evidence"]},
            ))

    unresolved = [record for record in records if record["reviewer_status"] == "HUMAN_REVIEW_REQUIRED"]
    ledger = {
        "schema_version": "1.0", "phase": "Documentation Governance v2.3 Phase 1C Reconciliation",
        "generated_on": date.today().isoformat(),
        "baseline_requirement_count": len(raw_requirements),
        "finding_coverage": {
            "false_positive_candidates": len(fp), "false_negative_candidates": len(fn),
            "compound_candidates": len(compounds), "classification_findings": len(qa["classification_findings"]),
            "overlap_groups": len(qa["overlap_normalization"]["groups"]),
        },
        "metrics": {
            "active_requirement_count": len(active),
            "atomic_requirement_count": sum(req.get("implementation_unit", not req.get("is_composite", False)) for req in active),
            "canonical_atomic_requirement_count": sum(req.get("implementation_unit", not req.get("is_composite", False)) for req in active),
            "composite_parent_count": sum(req.get("is_composite", False) for req in active),
            "alias_count": sum(req.get("record_kind") == "ALIAS" for req in active),
            "false_positive_excluded": len(fp_keys - FP_REQUIREMENTS),
            "false_positive_confirmed_requirement": len(FP_REQUIREMENTS),
            "false_negative_added": len(fn_result),
            "false_negative_excluded": len(fn) - len(fn_result),
            "compound_split_candidates": len(SPLIT_SPECS) + len(COMPOSITE_PARENT_SPLITS),
            "atomic_replacement_splits": len(SPLIT_SPECS),
            "composite_parent_splits": len(COMPOSITE_PARENT_SPLITS),
            "split_resulting_requirements": sum(len(value) for value in split_result_keys.values()) + sum(len(value) for value in composite_result_keys.values()),
            "canonical_tombstones": 0,
            "temporary_keys_retired": len({key for key in retired if key.startswith("TMP-")}),
            "unresolved_human_decisions": len(unresolved),
        },
        "retired_temporary_keys": sorted(key for key in retired if key.startswith("TMP-")),
        "retired_temporary_records": sorted(retired_temporary_records, key=lambda item: item["temporary_key"]),
        "canonical_tombstones": [],
        "transitively_resolved_overlap_groups": sorted(transitive_resolution_by_group),
        "records": records,
        "unresolved_records": [record["source_key_or_candidate"] for record in unresolved],
        "ready_to_freeze": not unresolved,
    }
    return reconciled, ledger


def documentation_finding_summary(finding: dict) -> str:
    details = []
    for field in (
            "required_clarification", "scope_decision", "phase_constraint",
            "capability_distinction", "non_implication", "delivery_distinction",
            "required_additions", "classification_recommendation", "minimum_definition",
            "scope_boundary", "future_architecture",
    ):
        if field not in finding:
            continue
        value = finding[field]
        details.append("; ".join(value) if isinstance(value, list) else value)
    return f"`{finding['finding_id']}` ({finding['status']}): {' '.join(details)}"


def semantic_decision_markdown(ledger: dict) -> str:
    blocks = []
    for record in ledger["records"]:
        if "semantic_clarification" not in record:
            continue
        lines = [
            f"- `{record['canonical_requirement']}` (`{record['source_key_or_candidate']}`) semantic clarification:"
        ]
        lines.extend(f"  - {item}" for item in record["semantic_clarification"])
        if record.get("acceptance_intent"):
            lines.append("  - Acceptance intent:")
            lines.extend(
                f"    {item['sequence']}. {item['intent']}" for item in record["acceptance_intent"]
            )
        if record.get("canonical_acceptance_status"):
            lines.append(
                f"  - Acceptance metadata remains `{record['canonical_acceptance_status']}` until source-backed acceptance criteria are added."
            )
        blocks.append("\n".join(lines))
    return "\n".join(blocks) if blocks else "None."


def reconciliation_markdown(ledger: dict, summary: dict) -> str:
    metrics = ledger["metrics"]
    unresolved = [record for record in ledger["records"] if record["reviewer_status"] == "HUMAN_REVIEW_REQUIRED"]
    unresolved_lines = [f"- `{record['finding_type']}` `{record['source_key_or_candidate']}` — {record['rationale']}" for record in unresolved]
    composite_lines = [
        f"- `{record['composite_parent']}` remains the verbatim canonical composite parent; `ALL_CHILDREN` coverage maps to {', '.join(f'`{key}`' for key in record['resulting_keys'])}."
        for record in ledger["records"] if record["disposition"] == "SPLIT_AS_COMPOSITE_PARENT"
    ]
    alias_lines = [
        f"- `{record['alias_requirement']}` remains a source-backed ID alias of canonical `{record['canonical_requirement']}`; it is not an implementation, acceptance, or scope-coverage unit."
        for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_ALIAS"
    ]
    retired_lines = [
        f"- `{record['retired_temporary_key']}` is retired as `SUPERSEDED_BY` `{record['superseded_by']}`; its source evidence is retained as a supporting source of `{record['canonical_requirement']}`."
        for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARY"
    ]
    retired_lines.extend(
        f"- `{record['source_key_or_candidate']}`: {', '.join(f'`{key}`' for key in record['retired_temporary_keys'])} are retired as `SUPERSEDED_BY` `{record['superseded_by']}`; the full equivalence class is {', '.join(f'`{key}`' for key in record['equivalence_class_members'])}."
        for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARIES"
    )
    transitive_lines = [
        f"- `{record['source_key_or_candidate']}` — {record['rationale']}"
        for record in ledger["records"] if record["disposition"] == "RESOLVED_TRANSITIVELY_BY_EQUIVALENCE_CLASS"
    ]
    correction_lines = [
        f"- `{record['source_key_or_candidate']}` `{record['correction_type']}` keeps {', '.join(f'`{key}`' for key in record['resulting_keys'])} active and replaces shared-fragment evidence with full-context source ranges."
        for record in ledger["records"] if record["disposition"] == "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT"
    ]
    channel_lines = [
        f"- `{record['source_key_or_candidate']}` `{record['correction_type']}` keeps {', '.join(f'`{key}`' for key in record['resulting_keys'])} as distinct channel-scoped requirements with the same predicate."
        for record in ledger["records"] if record["disposition"] == "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT"
    ]
    documentation_lines = [
        f"- {documentation_finding_summary(finding)}"
        for record in ledger["records"] if "documentation_finding" in record
        for finding in [record["documentation_finding"]]
    ]
    return f"""# BRD/UXF Requirement Registry Reconciliation — Phase 1C

Phase 1C applies the semantic membership rules to the complete Phase 1B finding set. BRD/UXF source content is unchanged, canonical IDs are not newly assigned, and retired temporary keys are never reused.

## Exact reconciliation result

- Baseline active requirements: **{ledger['baseline_requirement_count']}**
- Reconciled active requirements: **{metrics['active_requirement_count']}**
- False positives excluded: **{metrics['false_positive_excluded']}**
- False-positive candidates confirmed as requirements: **{metrics['false_positive_confirmed_requirement']}**
- False negatives added: **{metrics['false_negative_added']}**
- False-negative candidates excluded: **{metrics['false_negative_excluded']}**
- Compound candidates split: **{metrics['compound_split_candidates']}** into **{metrics['split_resulting_requirements']}** atomic requirements
- Composite parents retained: **{metrics['composite_parent_count']}**
- Alias records retained: **{metrics['alias_count']}**
- Atomic implementation/acceptance requirements: **{metrics['atomic_requirement_count']}**
- Canonical IDs tombstoned/deprecated: **{metrics['canonical_tombstones']}**
- Temporary keys retired: **{metrics['temporary_keys_retired']}**
- Unresolved human decisions: **{metrics['unresolved_human_decisions']}**
- Ready to freeze: **{'yes' if ledger['ready_to_freeze'] else 'no'}**

## Acceptance semantics

- Documented acceptance (`DIRECT + LINKED`): **{summary['totals']['documented_acceptance']}**
- Acceptance gap (`INFERRED_ONLY + MISSING`): **{summary['totals']['acceptance_gap']}**
- Acceptance-unit distribution: `{json.dumps(summary['by_acceptance_status_for_acceptance_units'], ensure_ascii=False, sort_keys=True)}`

## Scope-conflict treatment

The eight SD-03/UXD-11 promotions are active with `FRAMEWORK_DECISION` provenance, retain their legacy `source_scope_status`, and have `scope_conflict_resolved=true`. The resolved legacy conflict is no longer recorded as ambiguity.

## Composite parent decisions

{chr(10).join(composite_lines) if composite_lines else 'None.'}

## Canonical and alias decisions

{chr(10).join(alias_lines) if alias_lines else 'None.'}

## Canonical and retired-temporary decisions

{chr(10).join(retired_lines) if retired_lines else 'None.'}

## Transitively resolved overlap groups

{chr(10).join(transitive_lines) if transitive_lines else 'None.'}

## Corrected truncated extractions

{chr(10).join(correction_lines) if correction_lines else 'None.'}

## Corrected channel-scoped restatements

{chr(10).join(channel_lines) if channel_lines else 'None.'}

## Deferred documentation findings

{chr(10).join(documentation_lines) if documentation_lines else 'None.'}

## Human semantic clarifications

{semantic_decision_markdown(ledger)}

## Unresolved human decisions

{chr(10).join(unresolved_lines) if unresolved_lines else 'None.'}

The complete one-record-per-finding evidence, dispositions, split mappings, retired keys, and tombstones are in `requirements/registry-reconciliation.json`.
"""


def phase1c_summary(registries: dict[str, dict], ledger: dict) -> dict:
    summary = calculate_summary(registries)
    all_requirements = [req for registry in registries.values() for req in registry["requirements"]]
    implementation_units = [req for req in all_requirements if req.get("implementation_unit", not req.get("is_composite", False))]
    acceptance_units = [req for req in all_requirements if req.get("acceptance_unit", True)]
    direct = sum(req["acceptance_status"] == "DIRECT" for req in acceptance_units)
    linked = sum(req["acceptance_status"] == "LINKED" for req in acceptance_units)
    inferred = sum(req["acceptance_status"] == "INFERRED_ONLY" for req in acceptance_units)
    missing = sum(req["acceptance_status"] == "MISSING" for req in acceptance_units)
    summary["schema_version"] = "2.0"
    summary["phase"] = "Documentation Governance v2.3 Phase 1C Reconciliation"
    for name in ("BRD", "UXF"):
        reqs = registries[name]["requirements"]
        units = [req for req in reqs if req.get("acceptance_unit", True)]
        implementation = [req for req in reqs if req.get("implementation_unit", not req.get("is_composite", False))]
        summary["sets"][name]["documented_acceptance"] = sum(req["acceptance_status"] in {"DIRECT", "LINKED"} for req in units)
        summary["sets"][name]["acceptance_gap"] = sum(req["acceptance_status"] in {"INFERRED_ONLY", "MISSING"} for req in units)
        summary["sets"][name]["missing_acceptance"] = summary["sets"][name]["acceptance_gap"]
        summary["sets"][name]["composite_parent_count"] = sum(req.get("is_composite", False) for req in reqs)
        summary["sets"][name]["alias_count"] = sum(req.get("record_kind") == "ALIAS" for req in reqs)
        summary["sets"][name]["atomic_requirement_count"] = len(implementation)
        summary["sets"][name]["canonical_atomic_requirement_count"] = len(implementation)
    summary["totals"]["documented_acceptance"] = direct + linked
    summary["totals"]["acceptance_gap"] = inferred + missing
    summary["totals"]["missing_acceptance"] = inferred + missing
    summary["totals"]["composite_parent_count"] = sum(req.get("is_composite", False) for req in all_requirements)
    summary["totals"]["alias_count"] = sum(req.get("record_kind") == "ALIAS" for req in all_requirements)
    summary["totals"]["atomic_requirement_count"] = len(implementation_units)
    summary["totals"]["canonical_atomic_requirement_count"] = len(implementation_units)
    summary["by_scope_status_registry_entries"] = summary["by_scope_status"]
    summary["by_scope_status"] = dict(sorted(Counter(req["scope_status"] for req in implementation_units).items()))
    summary["by_acceptance_status_for_acceptance_units"] = dict(sorted(Counter(req["acceptance_status"] for req in acceptance_units).items()))
    summary["compatibility_notes"] = {"missing_acceptance": "Compatibility field; equals acceptance_gap (INFERRED_ONLY + MISSING) across acceptance units, excluding non-atomic composite parents."}
    summary["reconciliation"] = ledger["metrics"]
    summary["ready_to_freeze"] = ledger["ready_to_freeze"]
    return summary


def phase1c_qa(raw_qa: dict, ledger: dict) -> dict:
    qa = dict(raw_qa)
    qa["reconciliation_status"] = {
        "phase": "1C", "ledger": rel(RECONCILIATION_PATH),
        "false_positive_candidates_reconciled": ledger["finding_coverage"]["false_positive_candidates"],
        "false_negative_candidates_reconciled": ledger["finding_coverage"]["false_negative_candidates"],
        "compound_candidates_reconciled": ledger["finding_coverage"]["compound_candidates"],
        "unresolved_human_decisions": ledger["metrics"]["unresolved_human_decisions"],
        "ready_to_freeze": ledger["ready_to_freeze"],
    }
    qa["documentation_findings"] = [
        record["documentation_finding"] for record in ledger["records"] if "documentation_finding" in record
    ]
    qa["semantic_clarifications"] = [
        {
            "source_key_or_candidate": record["source_key_or_candidate"],
            "canonical_requirement": record["canonical_requirement"],
            "semantic_clarification": record["semantic_clarification"],
            "acceptance_intent": record.get("acceptance_intent", []),
            "acceptance_status": record.get("canonical_acceptance_status"),
        }
        for record in ledger["records"] if "semantic_clarification" in record
    ]
    qa["equivalence_class_decisions"] = [
        {
            "source_key_or_candidate": record["source_key_or_candidate"],
            "canonical_requirement": record["canonical_requirement"],
            "equivalence_class_members": record["equivalence_class_members"],
            "retired_temporary_keys": record["retired_temporary_keys"],
            "satisfies_composite_parents": record["satisfies_composite_parents"],
            "composite_child_substitutions": record["composite_child_substitutions"],
        }
        for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARIES"
    ]
    qa["transitively_resolved_overlap_groups"] = ledger["transitively_resolved_overlap_groups"]
    qa["corrected_extractions"] = [
        {
            "source_key_or_candidate": record["source_key_or_candidate"],
            "disposition": record["disposition"],
            "correction_type": record["correction_type"],
            "resulting_keys": record["resulting_keys"],
            "extraction_corrections": record["extraction_corrections"],
        }
        for record in ledger["records"] if record["disposition"] == "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT"
    ]
    qa["channel_scoped_restatements"] = [
        {
            "source_key_or_candidate": record["source_key_or_candidate"],
            "disposition": record["disposition"],
            "correction_type": record["correction_type"],
            "resulting_keys": record["resulting_keys"],
            "applicability_scopes": record["applicability_scopes"],
            "channel_context_corrections": record["channel_context_corrections"],
        }
        for record in ledger["records"] if record["disposition"] == "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT"
    ]
    qa["applicability_distinctions"] = [
        {
            "source_key_or_candidate": record["source_key_or_candidate"],
            "disposition": record["disposition"],
            "correction_type": record["correction_type"],
            "resulting_keys": record["resulting_keys"],
            "applicability_scopes": record["applicability_scopes"],
            "applicability_context_corrections": record["applicability_context_corrections"],
        }
        for record in ledger["records"] if record["disposition"] == "DISTINCT_BY_APPLICABILITY"
    ]
    return qa


def phase1c_report(registries: dict[str, dict], summary: dict, ledger: dict) -> str:
    base = report_markdown(registries, summary)
    report = base.replace("# Requirement Registry Report — BRD/UXF Phase 1", "# Requirement Registry Report — BRD/UXF Phase 1C Reconciled").replace(
        "| Requirements |", "| Registry entries |"
    ).replace(
        "| Missing acceptance criteria |", "| Acceptance gap (`INFERRED_ONLY + MISSING`) |"
    ).replace(
        "`acceptance_present` is true only when the requirement source block itself contains identifiable acceptance criteria; testability of a statement alone is not treated as documented acceptance criteria.",
        "`acceptance_present` is true only for `DIRECT` or `LINKED`; testability alone remains `INFERRED_ONLY` and is counted in the acceptance gap."
    ).replace(
        "- Acceptance: `", "- Acceptance metadata across registry entries (includes composite parents): `"
    ).replace(
        "- Scope: `", "- Scope coverage across canonical atomic units (aliases/composite parents excluded): `"
    ).replace(
        "## Registry interpretation", f"## Reconciliation\n\n- Baseline: **{ledger['baseline_requirement_count']}**\n- Registry entries after reconciliation: **{summary['totals']['requirement_count']}**\n- Canonical atomic requirements: **{summary['totals']['canonical_atomic_requirement_count']}**\n- Composite parents: **{summary['totals']['composite_parent_count']}**\n- Aliases: **{summary['totals']['alias_count']}**\n- Retired temporary keys: **{ledger['metrics']['temporary_keys_retired']}**\n- Documented acceptance: **{summary['totals']['documented_acceptance']}**\n- Acceptance gap: **{summary['totals']['acceptance_gap']}**\n- Ready to freeze: **{'yes' if ledger['ready_to_freeze'] else 'no — unresolved review remains'}**\n\n## Registry interpretation"
    )
    documentation_findings = [record["documentation_finding"] for record in ledger["records"] if "documentation_finding" in record]
    if documentation_findings:
        report += "\n## Deferred documentation findings\n\n" + "\n".join(
            f"- {documentation_finding_summary(finding)}"
            for finding in documentation_findings
        ) + "\n"
    if any("semantic_clarification" in record for record in ledger["records"]):
        report += "\n## Human semantic clarifications\n\n" + semantic_decision_markdown(ledger) + "\n"
    equivalence_records = [record for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARIES"]
    if equivalence_records:
        report += "\n## Semantic equivalence classes\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` canonical `{record['canonical_requirement']}`; retired {', '.join(f'`{key}`' for key in record['retired_temporary_keys'])}; composite coverage {json.dumps(record['composite_child_substitutions'], ensure_ascii=False, sort_keys=True)}."
            for record in equivalence_records
        ) + "\n"
    transitive = ledger["transitively_resolved_overlap_groups"]
    report += f"\n## Transitively resolved overlap groups\n\n{', '.join(f'`{key}`' for key in transitive) if transitive else 'None.'}\n"
    correction_records = [record for record in ledger["records"] if record["disposition"] == "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT"]
    if correction_records:
        report += "\n## Corrected truncated extractions\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` `{record['correction_type']}`: {', '.join(f'`{key}`' for key in record['resulting_keys'])} remain active with full-context source excerpts; the shared trailing fragment is not treated as an exact semantic match."
            for record in correction_records
        ) + "\n"
    channel_records = [record for record in ledger["records"] if record["disposition"] == "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT"]
    if channel_records:
        report += "\n## Channel-scoped restatements\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` `{record['correction_type']}`: {', '.join(f'`{key}`' for key in record['resulting_keys'])} remain distinct because applicability scope is part of duplicate identity."
            for record in channel_records
        ) + "\n"
    return report


def write_artifacts() -> None:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    codes = known_document_codes()
    raw = {name: build_registry(name, codes) for name in ("BRD", "UXF")}
    raw_qa = build_qa(raw)
    registries, ledger = reconcile_registries(raw, raw_qa)
    summary = phase1c_summary(registries, ledger)
    qa = phase1c_qa(raw_qa, ledger)
    for name, path in REGISTRY_PATHS.items():
        json_write(path, registries[name])
    json_write(SUMMARY_PATH, summary)
    json_write(QA_PATH, qa)
    json_write(RECONCILIATION_PATH, ledger)
    INVENTORY_PATH.write_text(inventory_markdown(registries, summary), encoding="utf-8")
    inventory_text = INVENTORY_PATH.read_text(encoding="utf-8").replace(
        "An inventory requirement is either an explicit normative heading with a pre-existing ID, or a Markdown source block containing an explicit normative modal/prohibition in English or Vietnamese. No new canonical Requirement ID is assigned; unnumbered blocks use `TMP-{document-code}-{sequence}`.",
        "The Phase 1C inventory counts only entries that pass the semantic membership rules. Excluded candidates and superseded temporary keys remain traceable in `requirements/registry-reconciliation.json`; no canonical Requirement ID is newly assigned."
    )
    inventory_text = inventory_text.replace("BRD requirements:", "BRD registry entries:").replace("UXF requirements:", "UXF registry entries:")
    INVENTORY_PATH.write_text(inventory_text, encoding="utf-8")
    REPORT_PATH.write_text(phase1c_report(registries, summary, ledger), encoding="utf-8")
    qa_text = qa_markdown(raw_qa, calculate_summary(raw))
    qa_text = qa_text.replace("# BRD/UXF Requirement Registry Semantic QA — Phase 1B", "# BRD/UXF Requirement Registry Semantic QA — Phase 1B (Reconciled in Phase 1C)")
    composite_parents = [record["composite_parent"] for record in ledger["records"] if record["disposition"] == "SPLIT_AS_COMPOSITE_PARENT"]
    aliases = [f"`{record['alias_requirement']}` → `{record['canonical_requirement']}`" for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_ALIAS"]
    retired_mappings = [f"`{record['retired_temporary_key']}` → `{record['superseded_by']}`" for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARY"]
    retired_mappings.extend(
        f"`{key}` → `{record['superseded_by']}`"
        for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARIES"
        for key in record["retired_temporary_keys"]
    )
    qa_text += f"\n## Phase 1C status\n\nAll 140 false-positive, 10 false-negative, and 137 compound candidates have ledger dispositions. Composite parents {', '.join(f'`{key}`' for key in composite_parents)} are reconciled verbatim with two atomic children each and `ALL_CHILDREN` coverage. Canonical/alias mappings: {', '.join(aliases) if aliases else 'none'}. Retired temporary mappings: {', '.join(retired_mappings) if retired_mappings else 'none'}. **{ledger['metrics']['unresolved_human_decisions']}** human decisions remain; registry ready-to-freeze: **{'yes' if ledger['ready_to_freeze'] else 'no'}**.\n"
    documentation_findings = [record["documentation_finding"] for record in ledger["records"] if "documentation_finding" in record]
    if documentation_findings:
        qa_text += "\n## Deferred documentation findings\n\n" + "\n".join(
            f"- {documentation_finding_summary(finding)}"
            for finding in documentation_findings
        ) + "\n"
    if any("semantic_clarification" in record for record in ledger["records"]):
        qa_text += "\n## Human semantic clarifications\n\n" + semantic_decision_markdown(ledger) + "\n"
    equivalence_records = [record for record in ledger["records"] if record["disposition"] == "CANONICAL_WITH_RETIRED_TEMPORARIES"]
    if equivalence_records:
        qa_text += "\n## Semantic equivalence classes\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` canonical `{record['canonical_requirement']}`; retired {', '.join(f'`{key}`' for key in record['retired_temporary_keys'])}; satisfies {', '.join(f'`{key}`' for key in record['satisfies_composite_parents'])}."
            for record in equivalence_records
        ) + "\n"
    transitive = ledger["transitively_resolved_overlap_groups"]
    qa_text += f"\n## Transitively resolved overlap groups\n\n{', '.join(f'`{key}`' for key in transitive) if transitive else 'None.'}\n"
    correction_records = [record for record in ledger["records"] if record["disposition"] == "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT"]
    if correction_records:
        qa_text += "\n## Corrected truncated extractions\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` `{record['correction_type']}`: {', '.join(f'`{key}`' for key in record['resulting_keys'])} remain active with corrected statements and full-context evidence."
            for record in correction_records
        ) + "\n"
    channel_records = [record for record in ledger["records"] if record["disposition"] == "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT"]
    if channel_records:
        qa_text += "\n## Channel-scoped restatements\n\n" + "\n".join(
            f"- `{record['source_key_or_candidate']}` `{record['correction_type']}`: identical predicate, distinct `EXPERIENCE_CHANNEL` applicability scopes for {', '.join(f'`{key}`' for key in record['resulting_keys'])}."
            for record in channel_records
        ) + "\n"
    QA_REPORT_PATH.write_text(qa_text, encoding="utf-8")
    RECONCILIATION_REPORT_PATH.write_text(reconciliation_markdown(ledger, summary), encoding="utf-8")


def validate_source_locator(req: dict) -> list[str]:
    key = requirement_key(req)
    errors = []
    path = ROOT / req["source_document"]
    if not path.is_file():
        return [f"{key}: source file does not exist: {req['source_document']}"]
    parsed = parse_anchor(req["source_lines"])
    lines = path.read_text(encoding="utf-8").splitlines()
    if not parsed or parsed[0] < 1 or parsed[1] > len(lines):
        errors.append(f"{key}: invalid source_lines {req['source_lines']}")
    current_text = normalized_excerpt("\n".join(lines))
    excerpt = normalized_excerpt(req["source_excerpt"])
    if not excerpt or excerpt not in current_text:
        errors.append(f"{key}: STALE_SOURCE source_excerpt is no longer present")
    if req["source_fingerprint"] != excerpt_fingerprint(req["source_excerpt"]):
        errors.append(f"{key}: STALE_SOURCE fingerprint does not match normalized source_excerpt")
    if not req["source_section"]:
        errors.append(f"{key}: missing source_section")
    if req["source_anchor"] and not any("#" + github_slug(line.lstrip("#").strip()) == req["source_anchor"] for line in lines if line.startswith("#")):
        errors.append(f"{key}: source_anchor {req['source_anchor']} cannot be found")
    return errors


def validate() -> list[str]:
    errors = []
    try:
        registries = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in REGISTRY_PATHS.items()}
        summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
        qa = json.loads(QA_PATH.read_text(encoding="utf-8"))
        ledger = json.loads(RECONCILIATION_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Invalid or missing registry artifact: {exc}"]
    codes = known_document_codes()
    raw = {name: build_registry(name, codes) for name in ("BRD", "UXF")}
    raw_by_key = {
        requirement_key(req): req for registry in raw.values() for req in registry["requirements"]
    }
    raw_qa = build_qa(raw)
    expected_registries, expected_ledger = reconcile_registries(raw, raw_qa)
    expected_summary = phase1c_summary(expected_registries, expected_ledger)
    expected_qa = phase1c_qa(raw_qa, expected_ledger)
    for value, stored in ((expected_summary, summary), (expected_qa, qa), (expected_ledger, ledger)):
        value["generated_on"] = stored.get("generated_on")
    if registries != expected_registries:
        errors.append("Active registry does not match deterministic semantic reconciliation")
    if summary != expected_summary:
        errors.append("registry-summary.json does not match reconciled registry")
    if qa != expected_qa:
        errors.append("registry-qa.json does not preserve the independently recomputed Phase 1B audit and Phase 1C status")
    if ledger != expected_ledger:
        errors.append("registry-reconciliation.json does not match deterministic finding dispositions")
    all_requirements = [req for registry in registries.values() for req in registry.get("requirements", [])]
    requirements_by_key = {requirement_key(req): req for req in all_requirements}
    keys = [requirement_key(req) for req in all_requirements]
    if len(keys) != len(set(keys)):
        errors.append("Canonical IDs and temporary keys are not globally unique")
    retired = set(ledger.get("retired_temporary_keys", []))
    reused = retired & set(keys)
    if reused:
        errors.append(f"Excluded/superseded temporary keys were reused: {sorted(reused)}")
    retired_records = ledger.get("retired_temporary_records", [])
    for retired_record in retired_records:
        required = {"temporary_key", "disposition", "superseded_by", "source_document", "source_section", "source_anchor", "source_lines", "source_excerpt", "source_fingerprint", "statement"}
        missing = required - set(retired_record)
        key = retired_record.get("temporary_key", "(unknown retired key)")
        if missing:
            errors.append(f"{key}: retired temporary record lacks fields {sorted(missing)}")
            continue
        if key not in retired or key in requirements_by_key:
            errors.append(f"{key}: retired temporary key is missing from retirement set or remains active")
        if retired_record["disposition"] != "SUPERSEDED_BY" or retired_record["superseded_by"] not in requirements_by_key:
            errors.append(f"{key}: retired temporary record lacks an active superseded target")
        source_path = ROOT / retired_record["source_document"]
        source_text = source_path.read_text(encoding="utf-8") if source_path.is_file() else ""
        if normalized_excerpt(retired_record["source_excerpt"]) not in normalized_excerpt(source_text):
            errors.append(f"{key}: retired supporting source excerpt is stale")
        if retired_record["source_fingerprint"] != excerpt_fingerprint(retired_record["source_excerpt"]):
            errors.append(f"{key}: retired supporting source fingerprint is stale")
    for name, registry in registries.items():
        physical = [rel(path) for path in source_files(name)]
        registered = [doc.get("path") for doc in registry.get("documents", [])]
        if physical != registered:
            errors.append(f"{name}: source file coverage mismatch")
        counts = Counter(req["source_document"] for req in registry.get("requirements", []))
        for doc in registry.get("documents", []):
            if doc.get("requirement_count") != counts[doc.get("path")]:
                errors.append(f"{doc.get('path')}: document requirement aggregate mismatch")
    for req in all_requirements:
        key = requirement_key(req)
        missing = PHASE_1C_REQUIRED_FIELDS - set(req)
        if missing:
            errors.append(f"{key}: missing fields {sorted(missing)}")
            continue
        if bool(req["current_id"]) == bool(req["temporary_key"]):
            errors.append(f"{key}: exactly one identifier/key is required")
        if req["requirement_type"] not in PHASE_1C_TYPE_VALUES:
            errors.append(f"{key}: invalid requirement_type {req['requirement_type']}")
        if req["scope_status"] not in SCOPE_VALUES or req["source_scope_status"] not in SCOPE_VALUES:
            errors.append(f"{key}: invalid scope metadata")
        if req["scope_basis"] not in SCOPE_BASIS_VALUES or not req["scope_evidence"]:
            errors.append(f"{key}: invalid scope provenance")
        if req["scope_status"] in {"FUTURE", "DEFERRED", "OUT_OF_SCOPE"} and req["scope_basis"] != "SOURCE_EXPLICIT":
            errors.append(f"{key}: non-active scope lacks SOURCE_EXPLICIT evidence")
        if req["scope_status"] == "UNCLEAR" and req["scope_basis"] != "HUMAN_REVIEW_REQUIRED":
            errors.append(f"{key}: unclear scope must require human review")
        if req["acceptance_status"] not in ACCEPTANCE_VALUES or req["acceptance_present"] != (req["acceptance_status"] in {"DIRECT", "LINKED"}):
            errors.append(f"{key}: inconsistent acceptance metadata")
        if bool(req["acceptance_references"]) != (req["acceptance_status"] in {"DIRECT", "LINKED"}):
            errors.append(f"{key}: inconsistent acceptance_references")
        if req["scope_conflict_resolved"]:
            if req["scope_status"] != "V2.3_ACTIVE" or req["scope_basis"] != "FRAMEWORK_DECISION" or req["scope_evidence"] not in {"SD-03", "UXD-11"}:
                errors.append(f"{key}: invalid resolved scope conflict")
        if req.get("is_composite"):
            composite_fields = {"implementation_unit", "acceptance_unit", "coverage_mode", "derived_requirements"}
            if not composite_fields <= set(req):
                errors.append(f"{key}: composite parent lacks metadata {sorted(composite_fields-set(req))}")
            elif req["implementation_unit"] is not False or req["acceptance_unit"] is not False or req["coverage_mode"] != "ALL_CHILDREN":
                errors.append(f"{key}: invalid composite parent unit/coverage metadata")
            elif len(req["derived_requirements"]) != 2 or any(child not in requirements_by_key for child in req["derived_requirements"]):
                errors.append(f"{key}: composite parent must map to two active children")
            else:
                for child_key in req["derived_requirements"]:
                    child = requirements_by_key[child_key]
                    if child_key in retired or child.get("record_kind") == "ALIAS":
                        errors.append(f"{key}: ALL_CHILDREN coverage references a retired key or alias: {child_key}")
                    if child.get("acceptance_unit", True) is not True:
                        errors.append(f"{key}: composite child target is not an acceptance unit: {child_key}")
        if normalized_excerpt(req["source_excerpt"]).casefold() == "ở các phiên bản sau.":
            errors.append(f"{key}: source excerpt is a trailing fragment without subject/context")
        applicability_scope = req.get("applicability_scope")
        if applicability_scope and applicability_scope.get("scope_type") == "EXPERIENCE_CHANNEL":
            channel = applicability_scope.get("channel")
            expected_channel_text = {
                "PLATFORM_ADMINISTRATION_PORTAL": "Platform Administration Portal",
                "ORGANIZATION_PORTAL": "Organization Portal",
                "AGENCY_PORTAL": "Agency Portal",
            }.get(channel)
            if not channel or not expected_channel_text:
                errors.append(f"{key}: EXPERIENCE_CHANNEL requirement lacks a valid channel token")
            elif expected_channel_text not in req["statement"] or expected_channel_text not in req["source_section"]:
                errors.append(f"{key}: EXPERIENCE_CHANNEL statement/source section does not match channel token")
        elif applicability_scope and applicability_scope.get("scope_type") == "ATTACHMENT_CONTEXT":
            attachment_context = applicability_scope.get("attachment_context")
            expected_context = {
                "CUSTOMER_SUPPORT_TICKET_ATTACHMENT": ("Customer Support Ticket", "Ticket hỗ trợ:"),
                "NOTIFICATION_ATTACHMENT": ("Notification", "Notification hỗ trợ:"),
            }.get(attachment_context)
            if not attachment_context or not expected_context:
                errors.append(f"{key}: ATTACHMENT_CONTEXT requirement lacks a valid attachment_context token")
            elif expected_context[0] not in req["statement"] or expected_context[1] not in req["source_excerpt"]:
                errors.append(f"{key}: ATTACHMENT_CONTEXT statement/source excerpt does not match its context token")
        errors.extend(validate_source_locator(req))
    for req in all_requirements:
        child_key = requirement_key(req)
        for parent_key in req.get("satisfies_composite_parents", []):
            parent = requirements_by_key.get(parent_key)
            if not parent or not parent.get("is_composite") or child_key not in parent.get("derived_requirements", []):
                errors.append(f"{child_key}: satisfies_composite_parents is not reciprocal with {parent_key}")
    canonical = {req["current_id"] for req in all_requirements if req["current_id"]}
    alias_records = [req for req in all_requirements if req.get("record_kind") == "ALIAS"]
    for alias in alias_records:
        alias_key = requirement_key(alias)
        target_key = alias.get("alias_of")
        target = requirements_by_key.get(target_key)
        if not target:
            errors.append(f"{alias_key}: alias target does not exist: {target_key}")
            continue
        if target.get("record_kind") == "ALIAS":
            errors.append(f"{alias_key}: alias chain is forbidden through {target_key}")
        if target_key == alias_key:
            errors.append(f"{alias_key}: alias cycle/self-reference is forbidden")
        if alias.get("implementation_unit") is not False or alias.get("acceptance_unit") is not False or alias.get("coverage_mode") != "CANONICAL":
            errors.append(f"{alias_key}: alias must not be an implementation/acceptance unit and must use CANONICAL coverage")
        if not alias.get("current_id"):
            errors.append(f"{alias_key}: alias must preserve its canonical source ID")
        if target.get("is_canonical") is not True or alias_key not in target.get("aliases", []):
            errors.append(f"{alias_key}: canonical target {target_key} lacks reciprocal alias metadata")
        if target.get("implementation_unit") is not True or target.get("acceptance_unit") is not True:
            errors.append(f"{target_key}: canonical alias target must remain an implementation/acceptance unit")
    framework_text = FRAMEWORK_DECISIONS_PATH.read_text(encoding="utf-8") if FRAMEWORK_DECISIONS_PATH.is_file() else ""
    framework_decisions = set(re.findall(r"^###\s+(BDD-\d+)\b", framework_text, re.MULTILINE))
    clarified_by_canonical = {
        record.get("canonical_requirement"): record
        for record in ledger.get("records", [])
        if record.get("disposition") == "CANONICAL_WITH_ALIAS_AND_FRAMEWORK_CLARIFICATION"
        and record.get("reviewer_status") == "RECONCILED"
    }
    for requirement in all_requirements:
        effective_statement = requirement.get("effective_statement")
        if not effective_statement or effective_statement == requirement.get("statement"):
            continue
        key = requirement_key(requirement)
        record = clarified_by_canonical.get(key)
        governed_by = requirement.get("governed_by_decisions", [])
        if (
            not record
            or record.get("effective_statement") != effective_statement
            or record.get("governing_decisions") != governed_by
        ):
            errors.append(f"{key}: effective_statement differs from source without reconciliation provenance")
        if requirement.get("source_semantics_status") != "CLARIFIED_BY_FRAMEWORK_DECISION":
            errors.append(f"{key}: effective_statement differs from source without framework clarification status")
        if not governed_by or any(decision not in framework_decisions for decision in governed_by):
            errors.append(f"{key}: effective_statement cites a missing governing framework decision")
    tombstones = {item["canonical_id"] for item in ledger.get("canonical_tombstones", [])}
    raw_canonical = {req["current_id"] for registry in raw.values() for req in registry["requirements"] if req["current_id"]}
    if raw_canonical - canonical - tombstones:
        errors.append(f"Canonical IDs disappeared without tombstones: {sorted(raw_canonical-canonical-tombstones)}")
    for req in all_requirements:
        for reference in req["referenced_requirements"]:
            if reference not in canonical and reference not in tombstones:
                errors.append(f"{requirement_key(req)}: dangling requirement reference {reference}")
    coverage = ledger.get("finding_coverage", {})
    expected_coverage = {"false_positive_candidates": 140, "false_negative_candidates": 10, "compound_candidates": 137}
    for field, count in expected_coverage.items():
        if coverage.get(field) != count:
            errors.append(f"Reconciliation ledger must cover exactly {count} {field}")
    records = ledger.get("records", [])
    for finding, count in (("FALSE_POSITIVE_CANDIDATE", 140), ("FALSE_NEGATIVE_CANDIDATE", 10), ("COMPOUND_STATEMENT_CANDIDATE", 137)):
        if sum(record.get("finding_type") == finding for record in records) != count:
            errors.append(f"Ledger record coverage mismatch for {finding}")
    for record in records:
        missing_ledger_fields = {"source_key_or_candidate", "finding_type", "disposition", "rationale", "resulting_keys", "reviewer_status", "source_evidence"} - set(record)
        if missing_ledger_fields:
            errors.append(f"Ledger record missing fields {sorted(missing_ledger_fields)}: {record}")
            continue
        if record.get("disposition") == "CONFIRMED_FALSE_POSITIVE" and record["source_key_or_candidate"] in keys:
            errors.append(f"Confirmed false positive remains active: {record['source_key_or_candidate']}")
        if record.get("disposition") == "CONFIRMED_REQUIREMENT" and (not record.get("resulting_keys") or any(key not in keys for key in record["resulting_keys"])):
            errors.append(f"Confirmed requirement has no resulting registry entry: {record['source_key_or_candidate']}")
        if record.get("disposition") == "SPLIT":
            mapped = record.get("resulting_keys", [])
            if len(mapped) < 2 or any(key not in keys for key in mapped):
                errors.append(f"Split compound lacks mapping: {record['source_key_or_candidate']}")
            for mapped_key in mapped:
                child = next((req for req in all_requirements if requirement_key(req) == mapped_key), None)
                if not child or record["source_key_or_candidate"] not in child.get("derived_from", []):
                    errors.append(f"Split child {mapped_key} lacks derived_from mapping")
        if record.get("disposition") == "SPLIT_AS_COMPOSITE_PARENT":
            parent_key = record.get("composite_parent")
            parent = requirements_by_key.get(parent_key)
            mapped = record.get("resulting_keys", [])
            raw_parent = next((req for registry in raw.values() for req in registry["requirements"] if requirement_key(req) == parent_key), None)
            if record.get("reviewer_status") != "RECONCILED" or parent_key != record["source_key_or_candidate"]:
                errors.append(f"{record['source_key_or_candidate']}: composite split is not reconciled to its canonical parent")
            if not parent or not parent.get("is_composite") or parent.get("derived_requirements") != mapped:
                errors.append(f"{parent_key}: composite split parent mapping is inconsistent")
            if not raw_parent or not parent or parent["statement"] != raw_parent["statement"]:
                errors.append(f"{parent_key}: canonical composite statement was not preserved verbatim")
            if len(mapped) != 2 or any(key not in requirements_by_key for key in mapped):
                errors.append(f"{parent_key}: composite split must have exactly two active children")
            for mapped_key in mapped:
                child = requirements_by_key.get(mapped_key)
                if not child:
                    continue
                native_child = child.get("derived_from") == [parent_key]
                shared_canonical = parent_key in child.get("satisfies_composite_parents", [])
                if (not native_child and not shared_canonical) or child.get("acceptance_status") != "INFERRED_ONLY" or child.get("acceptance_present") is not False:
                    errors.append(f"{mapped_key}: invalid composite-child lineage or acceptance metadata")
                if child.get("acceptance_unit", True) is not True:
                    errors.append(f"{mapped_key}: composite child target must be an acceptance unit")
                if mapped_key in retired or child.get("record_kind") == "ALIAS":
                    errors.append(f"{parent_key}: ALL_CHILDREN coverage must not reference retired keys or aliases")
                if parent and (child.get("scope_status") != parent.get("scope_status") or child.get("lifecycle_status") != parent.get("lifecycle_status")):
                    errors.append(f"{mapped_key}: scope/lifecycle does not inherit from {parent_key}")
            specifications = COMPOSITE_PARENT_SPLITS.get(parent_key, [])
            actual_children = [requirements_by_key[key] for key in mapped if key in requirements_by_key]
            if [item["statement"] for item in actual_children] != [item["statement"] for item in specifications]:
                errors.append(f"{parent_key}: composite children add, omit, or alter decided semantics")
            substitutions = COMPOSITE_CHILD_SUBSTITUTIONS.get(parent_key, {})
            substituted_targets = set(substitutions.values())
            for specification, child in zip(specifications, actual_children):
                if requirement_key(child) not in substituted_targets and child["requirement_type"] != specification["requirement_type"]:
                    errors.append(f"{parent_key}: native composite child requirement_type is inconsistent")
        if record.get("disposition") in {"CANONICAL_WITH_ALIAS", "CANONICAL_WITH_ALIAS_AND_FRAMEWORK_CLARIFICATION"}:
            canonical_key = record.get("canonical_requirement")
            alias_key = record.get("alias_requirement")
            canonical_record = requirements_by_key.get(canonical_key)
            alias_record = requirements_by_key.get(alias_key)
            decision = OVERLAP_ALIAS_DECISIONS.get(record["source_key_or_candidate"], {})
            if record.get("reviewer_status") != "RECONCILED" or record.get("resulting_keys") != [canonical_key, alias_key]:
                errors.append(f"{record['source_key_or_candidate']}: canonical/alias ledger mapping is inconsistent")
            if not canonical_record or not alias_record or alias_record.get("alias_of") != canonical_key or alias_key not in canonical_record.get("aliases", []):
                errors.append(f"{record['source_key_or_candidate']}: canonical/alias registry mapping is missing")
            expected_scope = decision.get("canonical_scope_status")
            if expected_scope and canonical_record and canonical_record.get("scope_status") != expected_scope:
                errors.append(f"{canonical_key}: decided canonical scope_status is not preserved")
            expected_type = decision.get("canonical_requirement_type")
            if expected_type and canonical_record and canonical_record.get("requirement_type") != expected_type:
                errors.append(f"{canonical_key}: decided canonical requirement_type is not preserved")
            expected_canonical_coverage = decision.get("canonical_scope_coverage_unit")
            expected_alias_coverage = decision.get("alias_scope_coverage_unit")
            if expected_canonical_coverage is not None and (
                not canonical_record or canonical_record.get("scope_coverage_unit") is not expected_canonical_coverage
            ):
                errors.append(f"{canonical_key}: canonical scope coverage metadata is invalid")
            if expected_alias_coverage is not None and (
                not alias_record or alias_record.get("scope_coverage_unit") is not expected_alias_coverage
            ):
                errors.append(f"{alias_key}: alias scope coverage metadata is invalid")
            if decision.get("preserve_alias_source_record"):
                raw_alias = raw_by_key.get(alias_key)
                stable_alias = stable_entry(raw_alias) if raw_alias else None
                preserved_fields = {
                    "current_id", "statement", "source_document", "source_anchor", "source_section",
                    "source_lines", "source_excerpt", "source_fingerprint",
                }
                if not stable_alias or not alias_record or any(alias_record.get(field) != stable_alias.get(field) for field in preserved_fields):
                    errors.append(f"{alias_key}: source-backed alias identity or evidence was altered")
            if decision.get("preserve_canonical_source_record"):
                raw_canonical_record = raw_by_key.get(canonical_key)
                stable_canonical = stable_entry(raw_canonical_record) if raw_canonical_record else None
                preserved_fields = {
                    "current_id", "statement", "source_document", "source_anchor", "source_section",
                    "source_lines", "source_excerpt", "source_fingerprint",
                }
                if not stable_canonical or not canonical_record or any(
                    canonical_record.get(field) != stable_canonical.get(field) for field in preserved_fields
                ):
                    errors.append(f"{canonical_key}: source-backed canonical identity or evidence was altered")
            if "semantic_clarification" in decision and (
                not canonical_record or canonical_record.get("semantic_clarification") != decision["semantic_clarification"]
            ):
                errors.append(f"{canonical_key}: semantic clarification is missing or altered")
            if "semantic_clarification" in decision and record.get("semantic_clarification") != decision["semantic_clarification"]:
                errors.append(f"{record['source_key_or_candidate']}: ledger semantic clarification is missing or altered")
            if "documentation_finding" in decision and record.get("documentation_finding") != decision["documentation_finding"]:
                errors.append(f"{record['source_key_or_candidate']}: documentation finding is missing or altered")
            if "effective_statement" in decision:
                expected_effective = decision["effective_statement"]
                if not canonical_record or canonical_record.get("effective_statement") != expected_effective:
                    errors.append(f"{canonical_key}: framework-clarified effective statement is missing or altered")
                if not canonical_record or canonical_record.get("governed_by_decisions") != decision["governing_decisions"]:
                    errors.append(f"{canonical_key}: governing framework decisions are missing or altered")
                if not canonical_record or canonical_record.get("source_semantics_status") != decision["source_semantics_status"]:
                    errors.append(f"{canonical_key}: source semantics clarification status is missing or altered")
                if record.get("effective_statement") != expected_effective or record.get("governing_decisions") != decision["governing_decisions"]:
                    errors.append(f"{record['source_key_or_candidate']}: effective-semantics reconciliation provenance is missing or altered")
                if record.get("source_semantics_status") != decision["source_semantics_status"]:
                    errors.append(f"{record['source_key_or_candidate']}: source semantics status is missing or altered")
                if canonical_record and canonical_record.get("promotion_snapshot_lifecycle") != decision.get("promotion_snapshot_lifecycle"):
                    errors.append(f"{canonical_key}: Promotion snapshot lifecycle is missing or altered")
                if record.get("promotion_snapshot_lifecycle") != decision.get("promotion_snapshot_lifecycle"):
                    errors.append(f"{record['source_key_or_candidate']}: reconciled Promotion snapshot lifecycle is missing or altered")
                inherited_from = decision.get("alias_effective_semantics_inherited_from")
                if not alias_record or alias_record.get("effective_semantics_inherited_from") != inherited_from:
                    errors.append(f"{alias_key}: alias does not inherit canonical effective semantics")
                if alias_record and "effective_statement" in alias_record:
                    errors.append(f"{alias_key}: alias must not define independent effective semantics")
                non_prohibition = "Requirement này không cấm Evaluation Snapshot hoặc Reservation Snapshot trước Payment Success."
                if not canonical_record or non_prohibition not in canonical_record.get("semantic_clarification", []):
                    errors.append(f"{canonical_key}: clarification conflicts with Evaluation/Reservation snapshots before Payment Success")
        if record.get("disposition") == "CANONICAL_WITH_RETIRED_TEMPORARY":
            canonical_key = record.get("canonical_requirement")
            retired_key = record.get("retired_temporary_key")
            canonical_record = requirements_by_key.get(canonical_key)
            matching_retired = next((item for item in retired_records if item.get("temporary_key") == retired_key), None)
            if record.get("reviewer_status") != "RECONCILED" or record.get("resulting_keys") != [canonical_key]:
                errors.append(f"{record['source_key_or_candidate']}: canonical/retired ledger mapping is inconsistent")
            if retired_key in requirements_by_key or retired_key not in retired or not matching_retired or matching_retired.get("superseded_by") != canonical_key:
                errors.append(f"{record['source_key_or_candidate']}: retired temporary mapping is missing or active")
            supporting = canonical_record.get("supporting_sources", []) if canonical_record else []
            support = next((item for item in supporting if item.get("source_key") == retired_key), None)
            support_fields = {"source_document", "source_section", "source_excerpt", "source_fingerprint"}
            if not canonical_record or canonical_record.get("is_canonical") is not True or canonical_record.get("implementation_unit") is not True or canonical_record.get("acceptance_unit") is not True:
                errors.append(f"{canonical_key}: canonical owner metadata is invalid")
            if not support or not support_fields <= set(support):
                errors.append(f"{canonical_key}: supporting source for {retired_key} is missing required evidence")
            elif matching_retired and any(support[field] != matching_retired[field] for field in support_fields):
                errors.append(f"{canonical_key}: supporting source does not match retired evidence for {retired_key}")
            decision = next((item for item in OVERLAP_RETIRED_TEMPORARY_DECISIONS.values() if item["retired_temporary_key"] == retired_key), {})
            expected_type = decision.get("canonical_requirement_type")
            expected_scope = decision.get("canonical_scope_status")
            expected_basis = decision.get("canonical_scope_basis")
            expected_coverage = decision.get("canonical_scope_coverage_unit")
            if expected_type and canonical_record and canonical_record.get("requirement_type") != expected_type:
                errors.append(f"{canonical_key}: decided canonical requirement_type is not preserved")
            if expected_scope and canonical_record and canonical_record.get("scope_status") != expected_scope:
                errors.append(f"{canonical_key}: decided canonical scope_status is not preserved")
            if expected_basis and canonical_record and canonical_record.get("scope_basis") != expected_basis:
                errors.append(f"{canonical_key}: decided canonical scope_basis is not preserved")
            if expected_coverage is not None and (
                not canonical_record or canonical_record.get("scope_coverage_unit") is not expected_coverage
            ):
                errors.append(f"{canonical_key}: decided canonical scope coverage metadata is invalid")
            if decision.get("preserve_retired_historical_state"):
                raw_retired = raw_by_key.get(retired_key)
                stable_retired = stable_entry(raw_retired) if raw_retired else None
                historical_fields = (
                    "requirement_type", "scope_status", "source_scope_status", "scope_basis",
                    "scope_evidence", "lifecycle_status", "scope_conflict_resolved",
                )
                expected_history = {field: stable_retired[field] for field in historical_fields} if stable_retired else None
                if not matching_retired or matching_retired.get("historical_state") != expected_history:
                    errors.append(f"{retired_key}: retired historical state is missing or altered")
            expected_supporting_section = decision.get("supporting_source_section")
            if expected_supporting_section and (not support or support.get("source_section") != expected_supporting_section):
                errors.append(f"{canonical_key}: decided supporting source section is missing or altered")
            if decision.get("preserve_retired_historical_statement"):
                raw_retired = raw_by_key.get(retired_key)
                if not matching_retired or not raw_retired or matching_retired.get("statement") != raw_retired.get("statement"):
                    errors.append(f"{retired_key}: retired historical statement is missing or altered")
            if "semantic_clarification" in decision and (
                not canonical_record or canonical_record.get("semantic_clarification") != decision["semantic_clarification"]
            ):
                errors.append(f"{canonical_key}: semantic clarification is missing or altered")
            if "semantic_clarification" in decision and record.get("semantic_clarification") != decision["semantic_clarification"]:
                errors.append(f"{record['source_key_or_candidate']}: ledger semantic clarification is missing or altered")
            if "acceptance_intent" in decision and (
                not canonical_record or canonical_record.get("acceptance_intent") != decision["acceptance_intent"]
            ):
                errors.append(f"{canonical_key}: acceptance intent is missing or altered")
            if "acceptance_intent" in decision and record.get("acceptance_intent") != decision["acceptance_intent"]:
                errors.append(f"{record['source_key_or_candidate']}: ledger acceptance intent is missing or altered")
            expected_acceptance = decision.get("canonical_acceptance_status")
            if expected_acceptance and (
                not canonical_record
                or canonical_record.get("acceptance_status") != expected_acceptance
                or canonical_record.get("acceptance_present") is not False
                or canonical_record.get("acceptance_references") != []
            ):
                errors.append(f"{canonical_key}: decided non-source-backed acceptance status is not preserved")
            if expected_acceptance and record.get("canonical_acceptance_status") != expected_acceptance:
                errors.append(f"{record['source_key_or_candidate']}: ledger acceptance status is missing or altered")
            if "documentation_finding" in decision and record.get("documentation_finding") != decision["documentation_finding"]:
                errors.append(f"{record['source_key_or_candidate']}: documentation finding is missing or altered")
        if record.get("disposition") == "CANONICAL_WITH_RETIRED_TEMPORARIES":
            decision = OVERLAP_RETIRED_TEMPORARIES_DECISIONS.get(record["source_key_or_candidate"], {})
            canonical_key = record.get("canonical_requirement")
            retired_keys = record.get("retired_temporary_keys", [])
            canonical_record = requirements_by_key.get(canonical_key)
            if (
                record.get("reviewer_status") != "RECONCILED"
                or record.get("resulting_keys") != [canonical_key]
                or retired_keys != decision.get("retired_temporary_keys")
                or record.get("equivalence_class_members") != decision.get("equivalence_class_members")
            ):
                errors.append(f"{record['source_key_or_candidate']}: equivalence-class ledger mapping is inconsistent")
            if not canonical_record or any(
                canonical_record.get(field) is not True
                for field in ("is_canonical", "implementation_unit", "acceptance_unit", "scope_coverage_unit")
            ):
                errors.append(f"{canonical_key}: canonical equivalence-class coverage metadata is invalid")
            if canonical_record and canonical_record.get("scope_status") != decision.get("canonical_scope_status"):
                errors.append(f"{canonical_key}: canonical equivalence-class scope is invalid")
            raw_canonical_record = raw_by_key.get(canonical_key)
            stable_canonical_record = stable_entry(raw_canonical_record) if raw_canonical_record else None
            primary_source_fields = {
                "source_document", "source_anchor", "source_section", "source_lines",
                "source_excerpt", "source_fingerprint", "statement",
            }
            if not stable_canonical_record or not canonical_record or any(
                canonical_record.get(field) != stable_canonical_record.get(field) for field in primary_source_fields
            ):
                errors.append(f"{canonical_key}: canonical primary ownership/source was altered")
            supporting = canonical_record.get("supporting_sources", []) if canonical_record else []
            for retired_key in retired_keys:
                matching_retired = next((item for item in retired_records if item.get("temporary_key") == retired_key), None)
                support = next((item for item in supporting if item.get("source_key") == retired_key), None)
                support_fields = {"source_document", "source_section", "source_excerpt", "source_fingerprint"}
                if retired_key in requirements_by_key or retired_key not in retired or not matching_retired:
                    errors.append(f"{retired_key}: equivalence-class temporary key remains active or lacks retirement evidence")
                    continue
                if matching_retired.get("superseded_by") != canonical_key or matching_retired.get("disposition") != "SUPERSEDED_BY":
                    errors.append(f"{retired_key}: equivalence-class retirement target is invalid")
                if not support or not support_fields <= set(support) or any(
                    support[field] != matching_retired[field] for field in support_fields
                ):
                    errors.append(f"{canonical_key}: supporting source for {retired_key} is missing or altered")
                expected_derivation = [
                    parent_key for parent_key, substitutions in decision.get("composite_child_substitutions", {}).items()
                    if retired_key in substitutions
                ]
                if not expected_derivation:
                    raw_retired = raw_by_key.get(retired_key)
                    expected_derivation = stable_entry(raw_retired).get("derived_from", []) if raw_retired else []
                if matching_retired.get("historical_derivation") != expected_derivation:
                    errors.append(f"{retired_key}: historical derivation is missing or altered")
            expected_parents = decision.get("satisfies_composite_parents", [])
            if not canonical_record or canonical_record.get("satisfies_composite_parents") != expected_parents:
                errors.append(f"{canonical_key}: composite-parent satisfaction metadata is invalid")
            for parent_key in expected_parents:
                parent = requirements_by_key.get(parent_key)
                expected_children = [
                    COMPOSITE_CHILD_SUBSTITUTIONS.get(parent_key, {}).get(child, child)
                    for child in ("TMP-BRD-WS-15-026", "TMP-BRD-WS-15-027")
                ] if parent_key == "BD-15-002" else []
                if not parent or parent.get("derived_requirements") != expected_children or canonical_key not in parent.get("derived_requirements", []):
                    errors.append(f"{parent_key}: reciprocal composite coverage does not use {canonical_key}")
                parent_children = parent.get("derived_requirements", []) if parent else []
                if any(child in retired or requirements_by_key.get(child, {}).get("record_kind") == "ALIAS" for child in parent_children):
                    errors.append(f"{parent_key}: composite coverage contains a retired key or alias")
            active_equivalence_members = [
                requirements_by_key[key] for key in decision.get("equivalence_class_members", [])
                if key in requirements_by_key
            ]
            coverage_units = [item for item in active_equivalence_members if item.get("scope_coverage_unit", True)]
            if [requirement_key(item) for item in coverage_units] != [canonical_key]:
                errors.append(f"{record['source_key_or_candidate']}: equivalence class must have exactly one canonical coverage unit")
        if record.get("disposition") == "FALSE_EXACT_MATCH_DUE_TO_SHARED_FRAGMENT":
            decision = TRUNCATED_EXTRACTION_CORRECTIONS.get(record["source_key_or_candidate"], {})
            if (
                record.get("reviewer_status") != "RECONCILED"
                or record.get("correction_type") != decision.get("correction_type")
                or record.get("resulting_keys") != decision.get("resulting_keys")
            ):
                errors.append(f"{record['source_key_or_candidate']}: corrected-extraction ledger mapping is inconsistent")
            ledger_corrections = record.get("extraction_corrections", {})
            for key, correction in decision.get("corrections", {}).items():
                corrected = requirements_by_key.get(key)
                raw_record = raw_by_key.get(key)
                stable_raw_record = stable_entry(raw_record) if raw_record else None
                locator = source_locator(
                    ROOT / corrected["source_document"], correction["source_start"], correction["source_end"]
                ) if corrected else None
                if not corrected or key in retired or corrected.get("record_kind") == "ALIAS":
                    errors.append(f"{key}: corrected extraction must remain an active non-alias key")
                    continue
                if (
                    corrected.get("statement") != correction["statement"]
                    or corrected.get("requirement_type") != correction["requirement_type"]
                    or corrected.get("scope_status") != correction["scope_status"]
                    or corrected.get("source_scope_status") != correction["scope_status"]
                    or corrected.get("scope_basis") != correction["scope_basis"]
                    or corrected.get("source_section") != correction["source_section"]
                    or corrected.get("acceptance_status") != "INFERRED_ONLY"
                    or corrected.get("acceptance_present") is not False
                ):
                    errors.append(f"{key}: corrected statement, classification, scope, or acceptance metadata is invalid")
                if not locator or any(corrected.get(field) != locator[field] for field in (
                    "source_section", "source_anchor", "source_lines", "source_excerpt", "source_fingerprint"
                )):
                    errors.append(f"{key}: corrected full-context source locator or fingerprint is invalid")
                if any(fragment not in corrected.get("source_excerpt", "") for fragment in correction["required_excerpt_fragments"]):
                    errors.append(f"{key}: corrected source excerpt lacks required subject/context")
                expected_provenance = {
                    "group_id": record["source_key_or_candidate"],
                    "correction_type": decision["correction_type"],
                    "before_source_lines": stable_raw_record["source_lines"] if stable_raw_record else None,
                    "before_source_fingerprint": stable_raw_record["source_fingerprint"] if stable_raw_record else None,
                }
                if corrected.get("reconciliation_provenance") != expected_provenance:
                    errors.append(f"{key}: corrected extraction lacks reconciliation provenance")
                expected_ledger_correction = {
                    "before": {
                        "statement": stable_raw_record["statement"],
                        "source_lines": stable_raw_record["source_lines"],
                        "source_excerpt": stable_raw_record["source_excerpt"],
                        "source_fingerprint": stable_raw_record["source_fingerprint"],
                    },
                    "after": {
                        "statement": corrected["statement"],
                        "source_lines": corrected["source_lines"],
                        "source_excerpt": corrected["source_excerpt"],
                        "source_fingerprint": corrected["source_fingerprint"],
                    },
                } if stable_raw_record else None
                if ledger_corrections.get(key) != expected_ledger_correction:
                    errors.append(f"{key}: reconciliation does not preserve before/after extraction evidence")
            corrected_pair = tuple(sorted(decision.get("resulting_keys", [])))
            overlap_pairs = {
                tuple(sorted((pair["left"], pair["right"])))
                for pair in build_overlap_analysis(registries)["pairs"]
            }
            if corrected_pair in overlap_pairs or any(
                other in requirements_by_key[key].get("duplicate_or_overlap", [])
                for key, other in (corrected_pair, corrected_pair[::-1])
            ):
                errors.append(f"{record['source_key_or_candidate']}: corrected keys remain incorrectly classified as overlap")
        if record.get("disposition") == "INTENTIONAL_CHANNEL_SCOPED_RESTATEMENT":
            decision = CHANNEL_CONTEXT_CORRECTIONS.get(record["source_key_or_candidate"], {})
            if (
                record.get("reviewer_status") != "RECONCILED"
                or record.get("correction_type") != decision.get("correction_type")
                or record.get("resulting_keys") != decision.get("resulting_keys")
            ):
                errors.append(f"{record['source_key_or_candidate']}: channel-context reconciliation mapping is inconsistent")
            ledger_corrections = record.get("channel_context_corrections", {})
            corrected_records = []
            for key, correction in decision.get("corrections", {}).items():
                corrected = requirements_by_key.get(key)
                raw_record = raw_by_key.get(key)
                stable_raw_record = stable_entry(raw_record) if raw_record else None
                locator = source_locator(
                    ROOT / corrected["source_document"], correction["source_start"], correction["source_end"]
                ) if corrected else None
                if not corrected or key in retired or corrected.get("record_kind") == "ALIAS":
                    errors.append(f"{key}: channel-context correction must remain an active non-alias key")
                    continue
                corrected_records.append(corrected)
                if (
                    corrected.get("statement") != correction["statement"]
                    or corrected.get("applicability_scope") != correction["applicability_scope"]
                    or corrected.get("requirement_type") != correction["requirement_type"]
                    or corrected.get("scope_status") != correction["scope_status"]
                    or corrected.get("source_scope_status") != correction["scope_status"]
                    or corrected.get("source_section") != correction["source_section"]
                    or corrected.get("acceptance_status") != "INFERRED_ONLY"
                    or corrected.get("acceptance_present") is not False
                ):
                    errors.append(f"{key}: corrected channel statement, applicability, classification, scope, or acceptance metadata is invalid")
                if not locator or any(corrected.get(field) != locator[field] for field in (
                    "source_section", "source_anchor", "source_lines", "source_excerpt", "source_fingerprint"
                )):
                    errors.append(f"{key}: channel-context source locator or fingerprint is invalid")
                if any(fragment not in corrected.get("source_excerpt", "") for fragment in correction["required_excerpt_fragments"]):
                    errors.append(f"{key}: source excerpt lacks channel heading or Authentication: Required context")
                expected_provenance = {
                    "group_id": record["source_key_or_candidate"],
                    "correction_type": decision["correction_type"],
                    "before_source_lines": stable_raw_record["source_lines"] if stable_raw_record else None,
                    "before_source_fingerprint": stable_raw_record["source_fingerprint"] if stable_raw_record else None,
                }
                if corrected.get("reconciliation_provenance") != expected_provenance:
                    errors.append(f"{key}: channel-context correction lacks reconciliation provenance")
                expected_ledger_correction = {
                    "before": {
                        "statement": stable_raw_record["statement"],
                        "source_lines": stable_raw_record["source_lines"],
                        "source_excerpt": stable_raw_record["source_excerpt"],
                        "source_fingerprint": stable_raw_record["source_fingerprint"],
                    },
                    "after": {
                        "statement": corrected["statement"],
                        "applicability_scope": corrected["applicability_scope"],
                        "source_lines": corrected["source_lines"],
                        "source_excerpt": corrected["source_excerpt"],
                        "source_fingerprint": corrected["source_fingerprint"],
                    },
                } if stable_raw_record else None
                if ledger_corrections.get(key) != expected_ledger_correction:
                    errors.append(f"{key}: reconciliation lacks before/after channel-context evidence")
                if any(other in corrected.get("duplicate_or_overlap", []) for other in decision["resulting_keys"] if other != key):
                    errors.append(f"{key}: distinct experience channels remain incorrectly classified as overlap")
            if record.get("applicability_scopes") != {
                key: correction["applicability_scope"] for key, correction in decision.get("corrections", {}).items()
            }:
                errors.append(f"{record['source_key_or_candidate']}: ledger applicability scopes are missing or altered")
            synthetic = {"UXF": {"requirements": [dict(item, statement="requires authentication") for item in corrected_records]}}
            if build_overlap_analysis(synthetic)["pairs"]:
                errors.append("Exact duplicate detection failed to distinguish identical predicates by applicability_scope")
        if record.get("disposition") == "DISTINCT_BY_APPLICABILITY":
            decision = APPLICABILITY_SCOPE_CORRECTIONS.get(record["source_key_or_candidate"], {})
            if (
                record.get("reviewer_status") != "RECONCILED"
                or record.get("correction_type") != decision.get("correction_type")
                or record.get("resulting_keys") != decision.get("resulting_keys")
            ):
                errors.append(f"{record['source_key_or_candidate']}: applicability reconciliation mapping is inconsistent")
            ledger_corrections = record.get("applicability_context_corrections", {})
            corrected_records = []
            for key, correction in decision.get("corrections", {}).items():
                corrected = requirements_by_key.get(key)
                raw_record = raw_by_key.get(key)
                stable_raw_record = stable_entry(raw_record) if raw_record else None
                locator = source_locator(
                    ROOT / corrected["source_document"], correction["source_start"], correction["source_end"]
                ) if corrected else None
                if not corrected or key in retired or corrected.get("record_kind") == "ALIAS":
                    errors.append(f"{key}: applicability-distinct requirement must remain an active non-alias key")
                    continue
                corrected_records.append(corrected)
                if (
                    corrected.get("statement") != correction["statement"]
                    or corrected.get("source_statement") != correction["source_statement"]
                    or corrected.get("applicability_scope") != correction["applicability_scope"]
                    or corrected.get("requirement_type") != "SCOPE_CONSTRAINT"
                    or corrected.get("scope_status") != "OUT_OF_SCOPE"
                    or corrected.get("source_scope_status") != "OUT_OF_SCOPE"
                    or corrected.get("scope_basis") != "SOURCE_EXPLICIT"
                    or corrected.get("source_section") != correction["source_section"]
                    or corrected.get("implementation_unit") is not True
                    or corrected.get("acceptance_unit") is not True
                    or corrected.get("scope_coverage_unit") is not True
                ):
                    errors.append(f"{key}: contextualized attachment statement, applicability, scope, or unit metadata is invalid")
                if stable_raw_record and (
                    corrected.get("lifecycle_status") != stable_raw_record.get("lifecycle_status")
                    or corrected.get("acceptance_status") != stable_raw_record.get("acceptance_status")
                    or corrected.get("acceptance_present") != stable_raw_record.get("acceptance_present")
                    or corrected.get("acceptance_references") != stable_raw_record.get("acceptance_references")
                ):
                    errors.append(f"{key}: lifecycle or acceptance status changed during applicability reconciliation")
                if not locator or any(corrected.get(field) != locator[field] for field in (
                    "source_section", "source_anchor", "source_lines", "source_excerpt", "source_fingerprint"
                )):
                    errors.append(f"{key}: full Attachment source locator or fingerprint is invalid")
                if any(fragment not in corrected.get("source_excerpt", "") for fragment in correction["required_excerpt_fragments"]):
                    errors.append(f"{key}: source excerpt does not preserve the full Attachment section evidence")
                if correction["source_statement"] not in corrected.get("source_excerpt", "") or "v2.3" not in corrected.get("statement", ""):
                    errors.append(f"{key}: historical version wording or contextualized v2.3 statement is not preserved")
                expected_provenance = {
                    "group_id": record["source_key_or_candidate"],
                    "correction_type": decision["correction_type"],
                    "before_source_lines": stable_raw_record["source_lines"] if stable_raw_record else None,
                    "before_source_fingerprint": stable_raw_record["source_fingerprint"] if stable_raw_record else None,
                }
                if corrected.get("reconciliation_provenance") != expected_provenance:
                    errors.append(f"{key}: applicability correction lacks reconciliation provenance")
                expected_ledger_correction = {
                    "before": {
                        "statement": stable_raw_record["statement"],
                        "source_lines": stable_raw_record["source_lines"],
                        "source_excerpt": stable_raw_record["source_excerpt"],
                        "source_fingerprint": stable_raw_record["source_fingerprint"],
                    },
                    "after": {
                        "statement": corrected["statement"],
                        "source_statement": corrected["source_statement"],
                        "applicability_scope": corrected["applicability_scope"],
                        "source_lines": corrected["source_lines"],
                        "source_excerpt": corrected["source_excerpt"],
                        "source_fingerprint": corrected["source_fingerprint"],
                    },
                } if stable_raw_record else None
                if ledger_corrections.get(key) != expected_ledger_correction:
                    errors.append(f"{key}: reconciliation lacks before/after applicability evidence")
                if (
                    corrected.get("supporting_sources")
                    or corrected.get("derived_from")
                    or corrected.get("satisfies_composite_parents")
                ):
                    errors.append(f"{key}: applicability reconciliation must not create source transfer or shared-parent lineage")
                if any(other in corrected.get("duplicate_or_overlap", []) for other in decision["resulting_keys"] if other != key):
                    errors.append(f"{key}: distinct attachment contexts remain incorrectly classified as overlap")
            if record.get("applicability_scopes") != {
                key: correction["applicability_scope"] for key, correction in decision.get("corrections", {}).items()
            }:
                errors.append(f"{record['source_key_or_candidate']}: ledger applicability scopes are missing or altered")
            if record.get("documentation_finding") != decision.get("documentation_finding"):
                errors.append(f"{record['source_key_or_candidate']}: documentation finding is missing or altered")
            synthetic = {"BRD": {"requirements": [dict(item, statement="Attachment không hỗ trợ Video trong v2.3.") for item in corrected_records]}}
            if build_overlap_analysis(synthetic)["pairs"]:
                errors.append("Duplicate detection failed to distinguish identical predicates by attachment applicability_scope")
    unresolved = [record["source_key_or_candidate"] for record in records if record.get("reviewer_status") == "HUMAN_REVIEW_REQUIRED"]
    if unresolved != ledger.get("unresolved_records") or ledger.get("ready_to_freeze") == bool(unresolved):
        errors.append("Unresolved finding status is inconsistent or hidden")
    if {"BO-P06", "BD-15-002", "OVL-EXACT-001", "OVL-EXACT-002", "OVL-EXACT-003", "OVL-EXACT-004", "OVL-EXACT-005", "OVL-EXACT-006", "OVL-EXACT-007", "OVL-EXACT-008", "OVL-EXACT-009", "OVL-EXACT-010", "OVL-EXACT-011", "OVL-EXACT-012", "OVL-EXACT-013", "OVL-EXACT-014", "OVL-EXACT-015", "OVL-EXACT-016", "OVL-EXACT-021", "OVL-EXACT-029", "OVL-PROB-001", "OVL-PROB-002", "OVL-PROB-003", "OVL-PROB-004", "OVL-PROB-006"} & set(unresolved) or unresolved:
        errors.append("All twenty-five decided records must be reconciled with no unresolved overlap records")
    transitive_records = sorted(
        record["source_key_or_candidate"] for record in records
        if record.get("disposition") == "RESOLVED_TRANSITIVELY_BY_EQUIVALENCE_CLASS"
    )
    if ledger.get("transitively_resolved_overlap_groups") != transitive_records:
        errors.append("Transitively resolved overlap groups are inconsistent or hidden")
    raw_refs = raw_qa["raw_reference_validation"]
    if qa.get("raw_reference_validation") != raw_refs:
        errors.append("Raw requirement reference audit is not independently preserved")
    audited = [item["source_document"] for item in qa.get("extraction_audit", {}).get("per_file", [])]
    physical = [rel(path) for name in ("BRD", "UXF") for path in source_files(name)]
    if audited != physical:
        errors.append("Not every inventory source file was audited")
    overlap = build_overlap_analysis(registries)
    pairs = [(pair["left"], pair["right"]) for pair in overlap["pairs"]]
    if len(pairs) != len(set(pairs)) or any(left >= right for left, right in pairs):
        errors.append("Reconciled overlap pairs are not unique normalized A-B pairs")
    group_ids = [group["group_id"] for group in overlap["groups"]]
    if len(group_ids) != len(set(group_ids)):
        errors.append("Reconciled overlap group identifiers are not unique")
    for path in (INVENTORY_PATH, REPORT_PATH, QA_REPORT_PATH, RECONCILIATION_REPORT_PATH):
        if not path.is_file():
            errors.append(f"Missing report artifact {rel(path)}")
    if FREEZE_MANIFEST_PATH.is_file():
        errors.extend(validate_freeze_manifest(registries, summary, qa, ledger))
    return errors


def validate_freeze_manifest(registries: dict[str, dict], summary: dict, qa: dict, ledger: dict) -> list[str]:
    errors = []
    try:
        manifest = json.loads(FREEZE_MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"Invalid freeze manifest {rel(FREEZE_MANIFEST_PATH)}: {exc}"]

    required_fields = {
        "schema_version", "candidate_id", "supersedes_candidate_id", "correction", "baseline_kind", "status", "approval_status",
        "branch", "source_git_commit", "generated_on", "freeze_scope", "explicit_non_claims",
        "validator_result", "ready_to_freeze", "exact_registry_counts", "scope_distribution",
        "lifecycle_distribution", "requirement_type_distribution", "acceptance_distribution",
        "canonical_id_count", "active_temporary_key_count", "composite_parent_count",
        "alias_count", "retired_temporary_key_count", "unresolved_count", "known_gaps",
        "source_baseline", "source_hash_basis", "line_ending_semantics", "source_documents",
        "registry_artifacts", "validator_artifacts",
        "hash_algorithm", "aggregate_hash_algorithm", "source_aggregate_hash",
        "registry_aggregate_hash", "approval",
    }
    missing = required_fields - set(manifest)
    if missing:
        return [f"Freeze manifest lacks required fields {sorted(missing)}"]

    expected_freeze_scope = [
        "SOURCE_INVENTORY",
        "EXTRACTION_AND_RECONCILIATION_RESULTS",
        "CURRENT_IDENTITY_MAPPING",
        "ALIAS_COMPOSITE_RETIRED_KEY_DECISIONS",
        "CURRENT_SCOPE_CLASSIFICATION",
        "SOURCE_TRACEABILITY",
        "DEFERRED_DOCUMENTATION_FINDINGS",
    ]
    expected_non_claims = [
        "NOT_FINAL_BRD_UXF_V2.3_FREEZE",
        "NOT_FINAL_ACCEPTANCE_BASELINE",
        "NOT_ARCHITECTURE_APPROVAL",
        "NOT_IMPLEMENTATION_AUTHORIZATION",
        "NOT_DECLARATION_OF_TEMPORARY_KEYS_AS_FINAL_CANONICAL_IDS",
    ]
    if manifest.get("schema_version") != "1.1" or manifest.get("candidate_id") != "V23-REQ-REGISTRY-FC2":
        errors.append("Freeze manifest schema_version or candidate_id is invalid")
    if manifest.get("supersedes_candidate_id") != "V23-REQ-REGISTRY-FC1":
        errors.append("FC2 freeze manifest must supersede V23-REQ-REGISTRY-FC1")
    expected_correction = {
        "category": "SOURCE_HASH_BASIS_REPAIR",
        "fc1_failure": "CLEAN_CHECKOUT_SOURCE_HASH_MISMATCH",
        "root_cause": "RAW_WORKING_TREE_CRLF_VS_CANONICAL_GIT_BLOB_LF",
        "affected_source_document_count": 28,
        "semantic_payload_changed": False,
    }
    if manifest.get("correction") != expected_correction:
        errors.append("FC2 freeze manifest correction provenance is missing or altered")
    if manifest.get("baseline_kind") != "RECONCILED_REQUIREMENT_REGISTRY":
        errors.append("Freeze manifest baseline_kind is invalid")
    if manifest.get("status") != "CANDIDATE" or manifest.get("approval_status") != "PENDING_HUMAN_APPROVAL":
        errors.append("Freeze candidate must remain CANDIDATE with PENDING_HUMAN_APPROVAL")
    if manifest.get("freeze_scope") != expected_freeze_scope:
        errors.append("Freeze manifest scope is missing or overclaims the Phase 1C payload")
    if manifest.get("explicit_non_claims") != expected_non_claims:
        errors.append("Freeze manifest does not explicitly preserve all required non-claims")
    if not isinstance(manifest.get("branch"), str) or not manifest["branch"]:
        errors.append("Freeze manifest branch must be non-empty")
    if not re.fullmatch(r"[0-9a-f]{40}", str(manifest.get("source_git_commit", ""))):
        errors.append("Freeze manifest source_git_commit must be a full lowercase Git SHA")
    if manifest.get("source_git_commit") != "7f16d4c4b8ab514bd45de184f65ace221b03f4db":
        errors.append("Freeze manifest source_git_commit differs from the approved source baseline commit")
    if manifest.get("source_hash_basis") != "GIT_BLOB_CONTENT_AT_SOURCE_COMMIT":
        errors.append("Freeze manifest source_hash_basis must use canonical Git blob content")
    if manifest.get("line_ending_semantics") != "GIT_CANONICAL_TEXT":
        errors.append("Freeze manifest line_ending_semantics must be GIT_CANONICAL_TEXT")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(manifest.get("generated_on", ""))):
        errors.append("Freeze manifest generated_on must use YYYY-MM-DD")
    if manifest.get("validator_result") != {
        "command": "python3 scripts/docs/validate-requirement-registry.py",
        "status": "VALID_READY_TO_FREEZE",
    }:
        errors.append("Freeze manifest validator_result is invalid")
    if manifest.get("ready_to_freeze") is not True or ledger.get("ready_to_freeze") is not True:
        errors.append("Freeze readiness must be derived as true from a reconciled ledger")
    if ledger.get("unresolved_records") or ledger.get("metrics", {}).get("unresolved_human_decisions") != 0:
        errors.append("Freeze candidate cannot contain unresolved reconciliation records")

    all_requirements = [req for registry in registries.values() for req in registry["requirements"]]
    implementation_units = [req for req in all_requirements if req.get("implementation_unit", not req.get("is_composite", False))]
    acceptance_units = [req for req in all_requirements if req.get("acceptance_unit", True)]
    scope_coverage_units = [
        req for req in all_requirements
        if req.get("scope_coverage_unit", req.get("implementation_unit", not req.get("is_composite", False)))
    ]
    for requirement in all_requirements:
        key = requirement_key(requirement)
        unit_values = (
            requirement.get("implementation_unit", not requirement.get("is_composite", False)),
            requirement.get("acceptance_unit", True),
            requirement.get("scope_coverage_unit", requirement.get("implementation_unit", not requirement.get("is_composite", False))),
        )
        if len(set(unit_values)) != 1:
            errors.append(f"{key}: implementation, acceptance, and scope coverage unit flags are inconsistent")

    source_paths = [rel(path) for name in ("BRD", "UXF") for path in source_files(name)]
    brd_source_count = sum(path.startswith("docs/BRD/") for path in source_paths)
    uxf_source_count = sum(path.startswith("docs/UXF/") for path in source_paths)
    documentation_finding_count = sum("documentation_finding" in record for record in ledger["records"])
    expected_counts = {
        "source_document_count": len(source_paths),
        "brd_source_document_count": brd_source_count,
        "uxf_source_document_count": uxf_source_count,
        "active_registry_entry_count": len(all_requirements),
        "implementation_unit_count": len(implementation_units),
        "acceptance_unit_count": len(acceptance_units),
        "scope_coverage_unit_count": len(scope_coverage_units),
        "canonical_atomic_requirement_count": len(implementation_units),
        "canonical_id_count": sum(bool(req.get("current_id")) for req in all_requirements),
        "active_temporary_key_count": sum(bool(req.get("temporary_key")) for req in all_requirements),
        "composite_parent_count": sum(bool(req.get("is_composite")) for req in all_requirements),
        "alias_count": sum(req.get("record_kind") == "ALIAS" for req in all_requirements),
        "retired_temporary_key_count": len(ledger.get("retired_temporary_keys", [])),
        "unresolved_count": len(ledger.get("unresolved_records", [])),
        "documentation_finding_count": documentation_finding_count,
    }
    if manifest.get("exact_registry_counts") != expected_counts:
        errors.append("Freeze manifest exact_registry_counts do not match the reconciled registry")
    mirrors = {
        "canonical_id_count": expected_counts["canonical_id_count"],
        "active_temporary_key_count": expected_counts["active_temporary_key_count"],
        "composite_parent_count": expected_counts["composite_parent_count"],
        "alias_count": expected_counts["alias_count"],
        "retired_temporary_key_count": expected_counts["retired_temporary_key_count"],
        "unresolved_count": expected_counts["unresolved_count"],
    }
    if any(manifest.get(field) != value for field, value in mirrors.items()):
        errors.append("Freeze manifest top-level identity/reconciliation counts are inconsistent")

    expected_scope = {status: 0 for status in sorted(SCOPE_VALUES)}
    expected_scope.update(Counter(req["scope_status"] for req in scope_coverage_units))
    expected_lifecycle = {status: 0 for status in sorted(LIFECYCLE_VALUES)}
    expected_lifecycle.update(Counter(req["lifecycle_status"] for req in all_requirements))
    expected_types = dict(sorted(Counter(req["requirement_type"] for req in all_requirements).items()))
    expected_acceptance = {status: 0 for status in sorted(ACCEPTANCE_VALUES)}
    expected_acceptance.update(Counter(req["acceptance_status"] for req in acceptance_units))
    if manifest.get("scope_distribution") != expected_scope or sum(expected_scope.values()) != len(scope_coverage_units):
        errors.append("Freeze manifest scope distribution does not match canonical atomic scope coverage")
    if manifest.get("lifecycle_distribution") != expected_lifecycle:
        errors.append("Freeze manifest lifecycle distribution does not match active registry entries")
    if manifest.get("requirement_type_distribution") != expected_types:
        errors.append("Freeze manifest requirement-type distribution does not match active registry entries")
    if manifest.get("acceptance_distribution") != expected_acceptance or sum(expected_acceptance.values()) != len(acceptance_units):
        errors.append("Freeze manifest acceptance distribution does not match acceptance units")
    if expected_counts["canonical_id_count"] != summary["totals"]["with_id"] or expected_counts["active_temporary_key_count"] != summary["totals"]["without_id"]:
        errors.append("Summary identity counts do not match the active registries")
    if len(scope_coverage_units) != summary["totals"]["canonical_atomic_requirement_count"]:
        errors.append("Summary scope coverage total does not match canonical atomic requirement count")
    if len(acceptance_units) != summary["totals"]["documented_acceptance"] + summary["totals"]["acceptance_gap"]:
        errors.append("Summary acceptance totals do not match acceptance unit count")

    expected_source_baseline = {
        "origin": "ARCHITECTURE_BASELINE_V2.2",
        "origin_tag": "architecture-v2.2",
        "brd_v2.3_classification": "ADOPTED",
        "uxf_v2.3_classification": "DRAFT_REVIEW",
        "purpose": "CORRECTION_AND_APPROVAL_FOR_V2.3",
    }
    if manifest.get("source_baseline") != expected_source_baseline:
        errors.append("Freeze manifest source baseline does not preserve the v2.2-to-v2.3 governance status")

    canonical_source_blobs: dict[str, bytes] = {}
    source_commit = manifest.get("source_git_commit", "")
    commit_type = subprocess.run(
        ["git", "cat-file", "-t", source_commit], cwd=ROOT, text=True, capture_output=True, check=False
    )
    if commit_type.returncode != 0 or commit_type.stdout.strip() != "commit":
        errors.append("Freeze manifest source_git_commit does not exist as a Git commit object")
    else:
        for source_path in sorted(source_paths):
            object_spec = f"{source_commit}:{source_path}"
            object_type = subprocess.run(
                ["git", "cat-file", "-t", object_spec], cwd=ROOT, text=True, capture_output=True, check=False
            )
            if object_type.returncode != 0 or object_type.stdout.strip() != "blob":
                errors.append(f"Freeze source object is missing or is not a blob: {object_spec}")
                continue
            blob = subprocess.run(
                ["git", "cat-file", "blob", object_spec], cwd=ROOT, capture_output=True, check=False
            )
            if blob.returncode != 0:
                errors.append(f"Freeze source Git blob cannot be read: {object_spec}")
                continue
            canonical_source_blobs[source_path] = blob.stdout

    def validate_hashed_inventory(
        field: str,
        expected_roles: dict[str, str] | None = None,
        canonical_content: dict[str, bytes] | None = None,
    ) -> list[dict]:
        entries = manifest.get(field)
        if not isinstance(entries, list):
            errors.append(f"Freeze manifest {field} must be a list")
            return []
        paths = [entry.get("path") for entry in entries if isinstance(entry, dict)]
        if len(paths) != len(entries) or paths != sorted(paths) or len(paths) != len(set(paths)):
            errors.append(f"Freeze manifest {field} paths must be unique and lexicographically sorted")
            return entries
        for entry in entries:
            path_value = entry.get("path", "")
            if (
                not isinstance(path_value, str)
                or path_value.startswith("/")
                or "\\" in path_value
                or ".." in Path(path_value).parts
                or Path(path_value).as_posix() != path_value
            ):
                errors.append(f"Freeze manifest {field} contains a non-relative-POSIX path: {path_value}")
                continue
            path = ROOT / path_value
            if not path.is_file():
                errors.append(f"Freeze manifest hashed file is missing: {path_value}")
                continue
            if canonical_content is not None:
                content = canonical_content.get(path_value)
                actual_hash = raw_bytes_sha256(content) if content is not None else None
            else:
                actual_hash = raw_file_sha256(path)
            if entry.get("sha256") != actual_hash:
                errors.append(f"Freeze manifest SHA-256 mismatch: {path_value}")
            if expected_roles is not None and entry.get("role") != expected_roles.get(path_value):
                errors.append(f"Freeze manifest artifact role mismatch: {path_value}")
        return entries

    source_entries = validate_hashed_inventory("source_documents", canonical_content=canonical_source_blobs)
    source_entry_paths = [entry.get("path") for entry in source_entries]
    if source_entry_paths != sorted(source_paths) or brd_source_count != 24 or uxf_source_count != 7:
        errors.append("Freeze manifest source inventory must contain exactly all 24 BRD and 7 UXF documents")
    for entry in source_entries:
        expected_set = "BRD" if entry.get("path", "").startswith("docs/BRD/") else "UXF"
        if entry.get("document_set") != expected_set:
            errors.append(f"Freeze manifest source document set mismatch: {entry.get('path')}")
    registry_entries = validate_hashed_inventory("registry_artifacts", PHASE_1C_REGISTRY_ARTIFACTS)
    validator_entries = validate_hashed_inventory("validator_artifacts", PHASE_1C_VALIDATOR_ARTIFACTS)
    if [entry.get("path") for entry in registry_entries] != sorted(PHASE_1C_REGISTRY_ARTIFACTS):
        errors.append("Freeze manifest does not list the complete Phase 1C registry/report/QA/reconciliation artifact set")
    if [entry.get("path") for entry in validator_entries] != sorted(PHASE_1C_VALIDATOR_ARTIFACTS):
        errors.append("Freeze manifest does not list the registry validator artifact")
    forbidden_payloads = {
        rel(FREEZE_MANIFEST_PATH),
        rel(FREEZE_CANDIDATE_PATH),
        "docs/baselines/v2.3/REQUIREMENT_REGISTRY_FREEZE_APPROVAL.md",
        "scripts/docs/validate-requirement-registry-approval.py",
    }
    if forbidden_payloads & set(entry.get("path") for entry in registry_entries + validator_entries):
        errors.append("Freeze manifest/candidate/approval artifacts must not be included in the registry aggregate payload")
    if manifest.get("hash_algorithm") != "SHA-256" or manifest.get("aggregate_hash_algorithm") != FREEZE_AGGREGATE_ALGORITHM:
        errors.append("Freeze manifest hash algorithm declaration is invalid")
    if manifest.get("source_aggregate_hash") != aggregate_file_hash(source_entries):
        errors.append("Freeze manifest source_aggregate_hash is invalid")
    if manifest.get("registry_aggregate_hash") != aggregate_file_hash(registry_entries + validator_entries):
        errors.append("Freeze manifest registry_aggregate_hash is invalid")

    required_gap_counts = {
        "SOURCE_BASELINE_V22_REQUIRES_V23_CORRECTION_AND_APPROVAL": 31,
        "ACTIVE_TEMPORARY_KEYS_REQUIRE_STABLE_IDS": expected_counts["active_temporary_key_count"],
        "INFERRED_ONLY_ACCEPTANCE_REQUIRES_DOCUMENTATION": expected_acceptance["INFERRED_ONLY"],
        "DEFERRED_DOCUMENTATION_FINDINGS_REQUIRE_SOURCE_CORRECTION": documentation_finding_count,
    }
    gap_map = {
        gap.get("gap_id"): gap for gap in manifest.get("known_gaps", []) if isinstance(gap, dict)
    }
    if set(gap_map) != set(required_gap_counts) or any(
        gap_map[gap_id].get("observed_count") != count
        or gap_map[gap_id].get("blocks_final_brd_uxf_freeze") is not True
        for gap_id, count in required_gap_counts.items()
    ):
        errors.append("Freeze manifest known gaps are incomplete, hidden, or not marked as final-freeze blockers")

    expected_approval = {
        "status": "PENDING",
        "authorized_approver": "PENDING",
        "decision": "PENDING",
        "date": "PENDING",
        "signature": "PENDING",
    }
    if manifest.get("approval") != expected_approval:
        errors.append("Freeze manifest approval block must remain entirely pending")
    if not FREEZE_CANDIDATE_PATH.is_file():
        errors.append(f"Missing freeze candidate companion {rel(FREEZE_CANDIDATE_PATH)}")
    else:
        companion = FREEZE_CANDIDATE_PATH.read_text(encoding="utf-8")
        required_approval_lines = [
            "## Human Approval", "- Status: PENDING", "- Authorized Approver: PENDING",
            "- Decision: PENDING", "- Date: PENDING", "- Signature: PENDING",
        ]
        if any(line not in companion for line in required_approval_lines):
            errors.append("Freeze candidate Markdown approval section is missing or not pending")

    inventory_text = INVENTORY_PATH.read_text(encoding="utf-8")
    report_text = REPORT_PATH.read_text(encoding="utf-8")
    qa_text = QA_REPORT_PATH.read_text(encoding="utf-8")
    reconciliation_text = RECONCILIATION_REPORT_PATH.read_text(encoding="utf-8")
    expected_markdown_evidence = {
        "inventory": [f"- BRD files: **{brd_source_count}**", f"- UXF files: **{uxf_source_count}**"],
        "report": [
            f"- Registry entries after reconciliation: **{len(all_requirements)}**",
            f"- Canonical atomic requirements: **{len(implementation_units)}**",
            f"- Aliases: **{expected_counts['alias_count']}**",
            f"- Retired temporary keys: **{expected_counts['retired_temporary_key_count']}**",
            f"- Acceptance gap: **{summary['totals']['acceptance_gap']}**",
            "- Ready to freeze: **yes**",
        ],
        "qa": ["**0** human decisions remain; registry ready-to-freeze: **yes**."],
        "reconciliation": [
            f"- Reconciled active requirements: **{len(all_requirements)}**",
            f"- Alias records retained: **{expected_counts['alias_count']}**",
            f"- Atomic implementation/acceptance requirements: **{len(implementation_units)}**",
            f"- Temporary keys retired: **{expected_counts['retired_temporary_key_count']}**",
            "- Unresolved human decisions: **0**",
            "- Ready to freeze: **yes**",
        ],
    }
    for label, text_value, snippets in (
        ("inventory", inventory_text, expected_markdown_evidence["inventory"]),
        ("report", report_text, expected_markdown_evidence["report"]),
        ("qa", qa_text, expected_markdown_evidence["qa"]),
        ("reconciliation", reconciliation_text, expected_markdown_evidence["reconciliation"]),
    ):
        if any(snippet not in text_value for snippet in snippets):
            errors.append(f"Phase 1C {label} artifact does not expose the audited counts/readiness")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="rebuild the inventory and registry artifacts before validating")
    args = parser.parse_args()
    if args.write:
        write_artifacts()
    errors = validate()
    if errors:
        print("Requirement registry validation FAILED", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    ledger = json.loads(RECONCILIATION_PATH.read_text(encoding="utf-8"))
    status = "VALID_WITH_UNRESOLVED_REVIEW" if ledger["unresolved_records"] else "VALID_READY_TO_FREEZE"
    print(f"Requirement registry validation {status}")
    print(json.dumps(summary["totals"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
