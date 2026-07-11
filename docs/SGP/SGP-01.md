---
document_code: SGP-01
document_name: Sprint Lifecycle
project: YSim v2.0
document_set: Sprint Governance Pack
version: 1.0
status: FROZEN
language: en-US
---

# Sprint Lifecycle

## SGP-01

---

# 1. Purpose

Sprint Lifecycle định nghĩa vòng đời chuẩn của một Sprint trong nền tảng YSim.

Lifecycle được sử dụng để:

- quản lý trạng thái Sprint;
- kiểm soát Quality Gates;
- kiểm soát Governance Checkpoints;
- xác định Decision Authority;
- đảm bảo Traceability.

Mọi Sprint phải tuân theo Lifecycle này.

---

# 2. Lifecycle Principles

Sprint Lifecycle tuân thủ các nguyên tắc:

- Stage-Based
- Governance Controlled
- Evidence Driven
- Architecture First
- Human Approved
- Traceable
- Non-Skippable

Không được bỏ qua bất kỳ Stage nào.

---

# 3. Sprint Lifecycle

```text
Draft
    │
    ▼
Planned
    │
    ▼
Approved
    │
    ▼
Executing
    │
    ▼
Verifying
    │
    ▼
Reviewing
    │
    ▼
Accepted
    │
    ▼
Release Ready
    │
    ▼
Closed
```

Sprint chỉ được chuyển sang Stage tiếp theo khi Stage hiện tại hoàn thành.

---

# 4. Lifecycle Stages

| Stage | Description |
|---------|-------------|
| Draft | Sprint được tạo |
| Planned | Sprint Contract và Planning hoàn thành |
| Approved | Được phê duyệt triển khai |
| Executing | AI và Development triển khai |
| Verifying | Validation và Verification |
| Reviewing | Human Review |
| Accepted | Sprint được nghiệm thu |
| Release Ready | Đủ điều kiện đưa vào Release |
| Closed | Sprint hoàn thành |

---

# 5. Stage Entry Criteria

Mỗi Stage đều có điều kiện bắt đầu.

Ví dụ:

| Stage | Entry Criteria |
|---------|---------------|
| Planned | Sprint Contract tồn tại |
| Approved | Planning hoàn thành |
| Executing | Approval hoàn thành |
| Verifying | Code Freeze |
| Reviewing | Verification PASS |
| Accepted | Review PASS |
| Release Ready | Acceptance PASS |
| Closed | Release hoặc Handover hoàn thành |

---

# 6. Stage Exit Criteria

Một Stage chỉ được kết thúc khi:

- Deliverables hoàn thành.
- Evidence đầy đủ.
- Quality Gate đạt.
- Governance Checkpoint được thông qua.

Không được chuyển Stage chỉ vì Build PASS.

---

# 7. Governance Checkpoints (GCP)

Sprint Lifecycle sử dụng các Governance Checkpoint.

| GCP | Description |
|------|-------------|
| GCP-1 | Sprint Planning Approved |
| GCP-2 | Sprint Execution Started |
| GCP-3 | Verification Completed |
| GCP-4 | Human Review Approved |
| GCP-5 | Sprint Accepted |
| GCP-6 | Release Ready |

Governance Checkpoint là điểm quyết định của Sprint.

---

# 8. Quality Gates

Mỗi giai đoạn có Quality Gate riêng.

| Gate | Validation |
|-------|------------|
| QG-1 | Repository Discovery PASS |
| QG-2 | Planning PASS |
| QG-3 | Build PASS |
| QG-4 | Verification PASS |
| QG-5 | Review PASS |
| QG-6 | Acceptance PASS |

Quality Gate đánh giá chất lượng.

Governance Checkpoint đánh giá quyết định quản trị.

---

# 9. Stage Ownership

Mỗi Stage có Owner.

| Stage | Owner |
|---------|-------|
| Draft | Sprint Owner |
| Planned | Architecture Owner |
| Approved | Architecture Owner |
| Executing | AI Agent / Development Team |
| Verifying | AI Agent + QA |
| Reviewing | Reviewer |
| Accepted | Business Owner |
| Release Ready | Release Manager |
| Closed | Sprint Owner |

Không có Stage nào không có Owner.

---

# 10. Lifecycle Deliverables

Mỗi Stage sinh Deliverables.

Ví dụ:

| Stage | Deliverables |
|---------|-------------|
| Planned | Sprint Contract |
| Executing | Source Code |
| Verifying | Verification Report |
| Reviewing | Review Summary |
| Accepted | Acceptance Record |
| Release Ready | Release Manifest |
| Closed | Sprint Archive |

---

# 11. Lifecycle Events

Sprint Lifecycle phát sinh Business Events.

Ví dụ:

- SprintPlanned
- SprintApproved
- SprintExecutionStarted
- SprintVerificationCompleted
- SprintReviewed
- SprintAccepted
- SprintReleased
- SprintClosed

Các Event tuân thủ ABP-05 Event Architecture.

---

# 12. Lifecycle Metrics

Platform theo dõi:

- Planning Time
- Execution Time
- Verification Time
- Review Time
- Acceptance Time
- Total Sprint Duration

Metrics phục vụ cải tiến liên tục.

---

# 13. Lifecycle Rules

SL-001 — Sprint phải bắt đầu từ Draft.

SL-002 — Không được bỏ qua Stage.

SL-003 — Stage phải có Entry Criteria.

SL-004 — Stage phải có Exit Criteria.

SL-005 — Stage phải có Owner.

SL-006 — Stage phải có Deliverables.

SL-007 — Stage phải có Evidence.

SL-008 — Stage phải vượt Quality Gate.

SL-009 — Stage phải vượt Governance Checkpoint.

SL-010 — Sprint chỉ Closed sau khi hoàn tất Acceptance hoặc Handover.

---

# 14. Sprint Lifecycle Resolution Pipeline (SLRP)

```text
Draft
    │
    ▼
Planning
    │
    ▼
Approval
    │
    ▼
Execution
    │
    ▼
Verification
    │
    ▼
Human Review
    │
    ▼
Acceptance
    │
    ▼
Release Readiness
    │
    ▼
Closure
```

SLRP là vòng đời chuẩn của mọi Sprint.

---

# 15. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0101 | Sprint bắt đầu từ Draft |
| ACC-0102 | Không bỏ qua Stage |
| ACC-0103 | Entry Criteria đầy đủ |
| ACC-0104 | Exit Criteria đầy đủ |
| ACC-0105 | Governance Checkpoint được thông qua |
| ACC-0106 | Quality Gate đạt yêu cầu |
| ACC-0107 | Deliverables đầy đủ |
| ACC-0108 | Evidence đầy đủ |
| ACC-0109 | Lifecycle Event được phát sinh |
| ACC-0110 | Sprint được Closed đúng quy trình |

---

# 16. Relationship to Other Documents

SGP-01 liên kết với:

- SGP-00 Sprint Governance Overview
- AAP-02 Sprint Contract Model
- AAP-04 AI Verification Model
- AAP-05 AI Evidence Model
- VAP (Verification & Acceptance Pack)
- ROP (Release & Operations Pack)

Sprint Lifecycle là trục chính điều phối toàn bộ vòng đời của Sprint.

---

# 17. Document Status

**Status: FROZEN**

SGP-01 là tài liệu nền tảng quy định vòng đời Sprint của YSim.

Mọi Sprint phải tuân thủ Sprint Lifecycle trước khi được phép chuyển sang Release.

---