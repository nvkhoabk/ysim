---
document_code: SGP-10
document_name: Governance Assets & Records
project: YSim v2.1
document_set: Sprint Governance Pack
version: 2.1
status: FROZEN
language: en-US
---

# Governance Assets & Records

## SGP-10

---

# 1. Purpose

Governance Assets & Records định nghĩa toàn bộ Governance Artifact được sinh ra trong vòng đời Sprint.

Mục tiêu:

- chuẩn hóa Governance Assets;
- chuẩn hóa Governance Records;
- chuẩn hóa Traceability;
- chuẩn hóa Audit;
- chuẩn hóa Knowledge Preservation.

---

# 2. Principles

Governance Asset tuân thủ:

- Immutable
- Traceable
- Versioned
- Auditable
- Searchable
- Linked
- Full-stack Evidence
- Experience Traceability

---

# 3. Governance Asset Categories

Platform chuẩn hóa các nhóm Asset.

| Category | Description |
|-----------|-------------|
| Contract | Sprint Contract |
| Planning | Sprint Planning |
| Discovery | Repository Discovery |
| Governance | Decision Records |
| Risk | Risk Register |
| Issue | Issue Register |
| Exception | Exception Register |
| ACP | Architecture Change Proposal |
| Validation | Validation Records |
| Evidence | Evidence Package |
| Frontend | Frontend Assets & UI Evidence |
| Demonstration | Capability Demonstration Assets |
| Acceptance | Acceptance Package |
| Completion | Completion Report |
| Release | Release Recommendation |
| Archive | Sprint Archive |

---

# 4. Governance Record

Mỗi Governance Record gồm:

- Record ID
- Record Type
- Sprint ID
- Version
- Owner
- Status
- Created Time
- Updated Time
- Capability ID
- Experience ID

---

# 5. Governance Relationships

```text
Sprint

│

├── Contract

├── Discovery

├── Planning

├── Decisions

├── Risks

├── Issues

├── Exceptions

├── ACP

├── Validation

├── Evidence
├── Frontend Assets
├── Demonstration

├── Acceptance

├── Completion

└── Archive
```

---

# 6. Governance Registry

Platform duy trì Governance Registry.

Registry hỗ trợ:

- Search
- Version
- Traceability
- Relationship
- Audit

---

# 7. Governance Traceability

Mọi Governance Asset phải truy vết được tới:

- Sprint
- Capability
- Business Object
- Work Item
- Decision
- Evidence
- Release
- Frontend Experience
- Capability Demonstration

---

# 7A. Full-stack Governance Assets

Đối với Capability có giao diện người dùng, Sprint phải lưu trữ đầy đủ:

- Backend Source Summary
- Frontend Source Summary
- API Contract Snapshot
- Design System Snapshot
- Seed Data Package
- Capability Demonstration Report
- UI Screenshot Evidence
- End-to-end User Journey Evidence

Các Asset trên là thành phần bắt buộc của Sprint Dossier.

---

# 8. Governance Retention

Governance Assets được lưu giữ theo Governance Policy.

Bao gồm:

- Version
- Archive
- Retention
- Purge

---

# 9. Governance Rules

GA-001 — Mọi Governance Asset đều có ID.

GA-002 — Governance Asset phải Versioned.

GA-003 — Governance Asset phải Traceable.

GA-004 — Governance Asset phải Auditable.

GA-005 — Governance Asset phải Searchable.

GA-006 — Governance Asset không bị mất sau Release.

GA-007 — Governance Registry là Source of Truth.

GA-008 — Sprint Dossier tham chiếu tới mọi Governance Asset.

GA-009 — Governance Asset được bảo vệ theo Security Policy.

GA-010 — Governance Asset hỗ trợ AI Learning.

GA-011 — Capability Demonstration Asset là bắt buộc với Sprint có giao diện.

GA-012 — Frontend Evidence phải được lưu cùng Sprint Dossier.

---

# 10. Governance Asset Resolution Pipeline

```text
Sprint Activity
        │
        ▼
Asset Creation
        │
        ▼
Registration
        │
        ▼
Traceability
        │
        ▼
Experience Traceability
        │
        ▼
Versioning
        │
        ▼
Archive
        │
        ▼
Knowledge Repository
```

---

# 11. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-1001 | Governance Registry tồn tại |
| ACC-1002 | Governance Asset được Version |
| ACC-1003 | Governance Asset có Traceability |
| ACC-1004 | Governance Asset có Owner |
| ACC-1005 | Governance Asset được Audit |
| ACC-1006 | Governance Asset được Archive |
| ACC-1007 | Governance Asset hỗ trợ Search |
| ACC-1008 | Sprint Dossier đầy đủ |
| ACC-1009 | Governance Registry là Source of Truth |
| ACC-1010 | Governance Asset phục vụ AI Learning |
| ACC-1011 | Frontend Evidence được lưu trữ |
| ACC-1012 | Demonstration Assets đầy đủ |

---

# 12. Relationship to Other Documents

SGP-10 liên kết với:

- SGP-00 ~ SGP-09
- AAP-05 AI Evidence Model
- AAP-06 Architecture Change Proposal
- ABP-11 Platform Data Architecture
- ABP-15 AI Implementation Architecture
- VAP
- ROP

---

# 13. Document Status

**Status: FROZEN**

Governance Assets & Records là tài liệu chuẩn hóa toàn bộ Governance Artifact của Sprint.

Mọi Sprint phải quản lý Governance Assets theo tài liệu này, bảo đảm Backend, Frontend và Capability Demonstration đều có đầy đủ Artifact phục vụ Audit, AI Learning và Traceability.

---