# Sprint-00 Step 7 — Knowledge Factory Commissioning

Generated at: 2026-07-12T00:28:38+07:00

## Result

```json
{
  "status": "PASS",
  "documentCount": 102,
  "documentSetCount": 11,
  "capabilityCount": 7,
  "integrationCount": 0,
  "relationshipCount": 28,
  "nullGovernedDocumentCodes": 0,
  "documentsBySet": {
    "AAP": 6,
    "ABP": 18,
    "AFM": 2,
    "BRD": 24,
    "DIP": 11,
    "ESP": 15,
    "ESPK": 1,
    "ROOT": 2,
    "ROP": 10,
    "SGP": 11,
    "YADF": 2
  }
}
```

## Generated Catalogs

- `knowledge/raw/documents.json`
- `knowledge/normalized/documents.json`
- `knowledge/catalog/documents.json`
- `knowledge/catalog/document-sets.json`
- `knowledge/catalog/capabilities.json`
- `knowledge/catalog/integrations.json`
- `knowledge/catalog/relationships.json`
- `knowledge/catalog/knowledge-graph.json`
- `knowledge/catalog/summary.json`

## Limitation

Capability and integration relationships are generated from deterministic title and document-code matching. They are bootstrap knowledge and require review before being treated as authoritative semantic knowledge.

## Source of Truth

The Markdown documents under `docs/` remain authoritative.
