#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

CAPABILITIES = {
    "platform-foundation": ("platform foundation", "shared kernel", "repository architecture", "module architecture"),
    "identity-access": ("identity", "authentication", "authorization", "access control", "permission", "role"),
    "organization-tenant": ("organization", "tenant", "inheritance", "agency", "partner"),
    "product-catalog": ("product", "catalog", "package", "inventory", "esim stock"),
    "pricing-commercial": ("pricing", "commercial", "commission", "promotion"),
    "commerce-experience-platform": ("commerce experience", "cxp", "storefront", "store builder", "theme", "publishing"),
    "checkout-order": ("checkout", "cart", "quote", "sales order", "fulfillment"),
    "payment-finance": ("payment", "billing", "ledger", "settlement", "financial"),
    "crm-customer-care": ("crm", "customer care", "customer", "support"),
    "analytics-reporting": ("analytics", "reporting", "business intelligence", "dashboard", "kpi"),
    "operations-monitoring": ("operations", "monitoring", "health", "observability", "scheduler", "incident"),
    "ai-software-factory": ("ai factory", "software factory", "executable sprint", "prompt", "context", "seed", "governance"),
}

INTEGRATIONS = {
    "gigago": ("gigago",),
    "onepay": ("onepay",),
    "gpay": ("gpay",),
    "paypal": ("paypal",),
    "airwallex": ("airwallex",),
    "google-oauth": ("google oauth", "gmail", "google login"),
    "smtp-email": ("smtp", "email"),
    "sms-gateway": ("sms",),
}

LAYERS = {
    "AFM": "factory", "YADF": "factory", "AAP": "factory",
    "BRD": "business", "ABP": "architecture", "SGP": "governance",
    "ESP": "engineering", "DIP": "implementation", "ESPK": "execution",
    "ROP": "operations", "ROOT": "navigation",
}


def now() -> str:
    return datetime.now().astimezone().isoformat()


def stable_id(prefix: str, *parts: str) -> str:
    digest = hashlib.sha256("\x1f".join(parts).encode()).hexdigest()[:16]
    return f"{prefix}-{digest}"


def load_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise RuntimeError(f"Missing input: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("documents"), list):
        raise RuntimeError("Input must contain a documents array")
    return data


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def normalize(raw: dict[str, Any]) -> dict[str, Any]:
    path = str(raw.get("path") or "").strip()
    filename = str(raw.get("filename") or Path(path).name).strip()
    doc_set = str(raw.get("documentSet") or "UNKNOWN").strip()
    code = str(raw["documentCode"]).strip() if raw.get("documentCode") is not None else None
    title = str(raw["title"]).strip() if raw.get("title") is not None else None
    navigation = bool(raw.get("generatedNavigation", False))
    text = " ".join(x for x in (code, title, filename, doc_set) if x).lower()
    return {
        "id": code or stable_id("doc", path),
        "path": path,
        "filename": filename,
        "documentSet": doc_set,
        "layer": LAYERS.get(doc_set, "other"),
        "documentCode": code,
        "title": title,
        "version": raw.get("version"),
        "status": raw.get("status"),
        "generatedNavigation": navigation,
        "searchableText": text,
    }


def matches(text: str, rules: dict[str, tuple[str, ...]]) -> list[str]:
    return sorted(k for k, terms in rules.items() if any(term in text for term in terms))


def catalog_documents(docs: list[dict[str, Any]], rules: dict[str, tuple[str, ...]], rel_type: str):
    grouped: defaultdict[str, set[str]] = defaultdict(set)
    edges: list[dict[str, Any]] = []
    for doc in docs:
        if doc["generatedNavigation"]:
            continue
        for target in matches(doc["searchableText"], rules):
            grouped[target].add(doc["id"])
            edges.append({
                "id": stable_id("rel", doc["id"], rel_type, target),
                "from": doc["id"], "to": target, "type": rel_type,
                "source": "deterministic-title-matching",
            })
    items = [{
        "id": key,
        "name": key.replace("-", " ").title(),
        "documentIds": sorted(ids),
        "documentCount": len(ids),
        "source": "deterministic-title-matching",
        "reviewStatus": "REQUIRES_HUMAN_REVIEW",
    } for key, ids in sorted(grouped.items())]
    return items, edges


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    try:
        repo = args.repo_root.resolve()
        source = load_json(args.input.resolve())
        output = args.output.resolve()
        generated = now()
        raw_docs = source["documents"]
        docs = [normalize(d) for d in raw_docs]

        capabilities, cap_edges = catalog_documents(docs, CAPABILITIES, "references-capability")
        integrations, int_edges = catalog_documents(docs, INTEGRATIONS, "references-integration")
        edges = sorted(cap_edges + int_edges, key=lambda x: x["id"])

        sets: defaultdict[str, list[str]] = defaultdict(list)
        for doc in docs:
            sets[doc["documentSet"]].append(doc["id"])
        document_sets = [{"id": k, "layer": LAYERS.get(k, "other"), "documentCount": len(v), "documentIds": sorted(v)} for k, v in sorted(sets.items())]

        nodes = [
            {"id": d["id"], "type": "document", "label": d["title"] or d["filename"], "path": d["path"], "documentSet": d["documentSet"], "layer": d["layer"]}
            for d in docs
        ]
        nodes += [{"id": x["id"], "type": "capability", "label": x["name"]} for x in capabilities]
        nodes += [{"id": x["id"], "type": "integration", "label": x["name"]} for x in integrations]

        null_codes = sum(1 for d in docs if not d["generatedNavigation"] and not d["documentCode"])
        counts = Counter(d["documentSet"] for d in docs)
        summary = {
            "schemaVersion": "1.0", "generatedAt": generated,
            "status": "PASS" if null_codes == 0 else "FAIL",
            "sourceIndex": str(args.input.resolve().relative_to(repo)),
            "documentCount": len(docs), "documentSetCount": len(counts),
            "capabilityCount": len(capabilities), "integrationCount": len(integrations),
            "relationshipCount": len(edges), "nullGovernedDocumentCodes": null_codes,
            "documentsBySet": dict(sorted(counts.items())),
            "notes": [
                "Heuristic capability and integration matches are bootstrap knowledge only.",
                "All heuristic matches require review before becoming authoritative.",
                "docs/ remains the authoritative source of truth.",
            ],
        }

        write_json(output / "raw/documents.json", {"schemaVersion": "1.0", "generatedAt": generated, "documentCount": len(raw_docs), "documents": raw_docs})
        write_json(output / "normalized/documents.json", {"schemaVersion": "1.0", "generatedAt": generated, "documentCount": len(docs), "documents": docs})
        write_json(output / "catalog/documents.json", {"schemaVersion": "1.0", "generatedAt": generated, "documentCount": len(docs), "documents": [{k: d[k] for k in ("id","path","filename","documentSet","layer","documentCode","title","version","status","generatedNavigation")} for d in docs]})
        write_json(output / "catalog/document-sets.json", {"schemaVersion": "1.0", "generatedAt": generated, "documentSetCount": len(document_sets), "documentSets": document_sets})
        write_json(output / "catalog/capabilities.json", {"schemaVersion": "1.0", "generatedAt": generated, "capabilityCount": len(capabilities), "capabilities": capabilities})
        write_json(output / "catalog/integrations.json", {"schemaVersion": "1.0", "generatedAt": generated, "integrationCount": len(integrations), "integrations": integrations})
        write_json(output / "catalog/relationships.json", {"schemaVersion": "1.0", "generatedAt": generated, "relationshipCount": len(edges), "relationships": edges})
        write_json(output / "catalog/knowledge-graph.json", {"schemaVersion": "1.0", "generatedAt": generated, "nodeCount": len(nodes), "edgeCount": len(edges), "nodes": nodes, "edges": edges})
        write_json(output / "catalog/summary.json", summary)

        if summary["status"] != "PASS":
            raise RuntimeError(f"{null_codes} governed document(s) have null documentCode")

        print(f"Knowledge build PASS: {len(docs)} documents, {len(capabilities)} capabilities, {len(integrations)} integrations, {len(edges)} relationships.")
        return 0
    except (OSError, ValueError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 5


if __name__ == "__main__":
    sys.exit(main())
