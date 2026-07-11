# Sprint-00 Step 11 — YSF Knowledge Builder Migration

Generated at: 2026-07-12T02:15:01+07:00

## Command

```text
ysf build-knowledge
```

## Result

```json
{
  "command": "build-knowledge",
  "status": "PASS",
  "message": "Knowledge catalogs generated successfully.",
  "data": {
    "documentCount": 102,
    "capabilityCount": 7,
    "integrationCount": 0,
    "relationshipCount": 41,
    "outputs": [
      "knowledge/normalized/documents.json",
      "knowledge/catalog/documents.json",
      "knowledge/catalog/document-sets.json",
      "knowledge/catalog/capabilities.json",
      "knowledge/catalog/integrations.json",
      "knowledge/catalog/relationships.json",
      "knowledge/catalog/knowledge-graph.json",
      "knowledge/catalog/summary.json"
    ]
  }
}
```

## Knowledge Summary

```json
{
  "status": "PASS",
  "documentCount": 102,
  "documentSetCount": 11,
  "capabilityCount": 7,
  "integrationCount": 0,
  "relationshipCount": 41,
  "nullGovernedDocumentCodes": 0
}
```

## Tests

```text
.........                                                                [100%]
9 passed in 0.06s
```

## Compatibility

The legacy Bash entry point remains available:

```text
bash scripts/build-knowledge.sh
```
