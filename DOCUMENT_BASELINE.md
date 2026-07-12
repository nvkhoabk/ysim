# Sprint-01 Document Baseline

## Mandatory foundation documents

The Sprint context must include or directly reference:

- AFM-00
- YADF-00
- DIP-00
- DIP-01
- DIP-02
- DIP-04
- DIP-05
- DIP-06
- DIP-09
- ESPK-S00
- ABP-00
- ABP-01
- ABP-02
- ABP-03
- ABP-18
- UXF-00
- UXF-02
- UXF-05
- CAP-00
- PCS-00
- POL-00
- ESP-00
- ESP-01
- ESP-02

## Task-specific additions

Detailed task manifests may add documents relevant to:

- repository standards;
- NestJS engineering;
- configuration;
- logging;
- Docker;
- queues;
- testing;
- frontend foundation;
- CI/CD.

## Source-of-truth precedence

When sources conflict, use the following precedence:

1. frozen architecture baseline v2.2;
2. approved Sprint-01 definition;
3. approved task manifest;
4. current repository state;
5. generated prompt and runtime artifacts.

Generated output must never override frozen architecture decisions.

## Critical invariants for context generation

- YSim is the primary brand.
- Storefront is a sales channel and experience layer.
- Storefront must not know suppliers.
- Allocation is the only future capability allowed to select suppliers.
- Runtime performs Resolve → Compose → Delegate.
- Localization is broader than string translation.
- UX and business configuration require inheritance and fallback.
