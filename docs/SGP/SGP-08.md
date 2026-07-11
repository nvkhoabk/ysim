---
document_code: SGP-08
document_name: Sprint Governance Gates
project: YSim v2.1
document_set: Sprint Governance Pack
version: 2.1
status: FROZEN
language: en-US
---

# Sprint Governance Gates

## SGP-08

---

# 1. Purpose

Sprint Governance Gates định nghĩa các Gate kiểm soát bắt buộc trong suốt vòng đời Sprint.

Governance Gate là cơ chế quyết định:

- Sprint có được phép đi tiếp hay không.
- Sprint có đủ điều kiện chuyển Stage hay không.
- Sprint có cần Rework hoặc Escalation hay không.

Governance Gate là công cụ thực thi Sprint Governance.

---

# 2. Principles

Governance Gates tuân thủ:

- Stage Controlled
- Contract Driven
- Evidence Based
- Human Governed
- Architecture First
- Non-Skippable
- Fully Traceable
- Full-stack Capability Gates
- Experience-aware Gates

Không được bỏ qua bất kỳ Gate nào.

---

# 3. Governance Gate Model

```text
Sprint Lifecycle

↓

Governance Gate

↓

Decision

↓

Next Stage
```

Mỗi Stage đều kết thúc bằng một Governance Gate.

---

# 4. Governance Gates

Platform chuẩn hóa các Gate sau.

| Gate | Purpose |
|-------|----------|
| GG-1 | Sprint Ready |
| GG-2 | Planning Approved |
| GG-3 | Execution Started |
| GG-4 | Mid Sprint Governance |
| GG-5 | Verification Ready |
| GG-5A | Capability Demonstration Ready |
| GG-6 | Review Ready |
| GG-7 | Acceptance Ready |
| GG-8 | Release Ready |
| GG-9 | Sprint Closed |

---

# 5. Gate Evaluation

Mỗi Governance Gate đánh giá:

- Scope
- Architecture
- Dependencies
- Deliverables
- Evidence
- Risks
- Issues
- Decisions
- Frontend Readiness
- Capability Demonstration

Gate không chỉ đánh giá Quality.

---

# 6. Gate Inputs

Governance Gate sử dụng:

- Sprint Contract
- Sprint Status
- Evidence Package
- Verification Report
- Risk Register
- Issue Register
- Decision Log
- Metrics Dashboard
- Capability Demonstration Report
- UI Evidence Package

---

# 7. Gate Decision

Gate chỉ có bốn kết quả.

| Status | Meaning |
|----------|----------|
| PASS | Chuyển Stage |
| PASS WITH CONDITIONS | Chuyển Stage sau khi đáp ứng điều kiện |
| HOLD | Tạm dừng Sprint |
| FAIL | Quay lại Stage trước |

Gate Decision phải có Decision Authority.

---

# 7A. Full-stack Governance Gates

Đối với Capability có giao diện người dùng, Governance Gates phải xác minh đồng thời:

- Backend hoàn thành.
- Frontend hoàn thành.
- API Integration hoàn thành.
- Design System Compliance.
- Seed Data sẵn sàng.
- Capability Demonstration PASS.

Gate GG-5A chỉ được PASS khi toàn bộ Capability có thể trình diễn thành công theo Sprint Contract.

---

# 8. Gate Decision Authority

| Gate | Authority |
|--------|-----------|
| GG-1 | Sprint Owner |
| GG-2 | Architecture Owner |
| GG-3 | Sprint Owner |
| GG-4 | Sprint Owner |
| GG-5 | QA + AI Review |
| GG-5A | Reviewer + Business Owner |
| GG-6 | Reviewer |
| GG-7 | Business Owner |
| GG-8 | Release Manager |
| GG-9 | Sprint Owner |

Mỗi Gate chỉ có một Decision Authority chính.

---

# 9. Gate Deliverables

Mỗi Gate phải tạo:

- Gate Record
- Decision
- Decision Reason
- Outstanding Actions
- Decision Timestamp
- Decision Authority
- Demonstration Evidence

Gate Record là Evidence bắt buộc.

---

# 10. Governance Gate Events

Platform phát sinh:

- GovernanceGateStarted
- GovernanceGatePassed
- GovernanceGateHeld
- GovernanceGateFailed
- GovernanceGateCompleted

Các Event tuân thủ Event Architecture.

---

# 11. Governance Gate Rules

GG-001 — Mọi Stage đều phải có Governance Gate.

GG-002 — Không được bỏ qua Governance Gate.

GG-003 — Gate phải có Decision Authority.

GG-004 — Gate phải có Evidence.

GG-005 — PASS phải có Traceability.

GG-006 — FAIL phải có Root Cause.

GG-007 — HOLD phải có Action Plan.

GG-008 — Gate Record là bắt buộc.

GG-009 — Governance Gate hỗ trợ Audit.

GG-010 — Sprint chỉ chuyển Stage sau PASS.

GG-011 — Capability Demonstration là Gate bắt buộc đối với Sprint có giao diện.

GG-012 — Frontend Evidence phải đầy đủ trước GG-5A.

---

# 12. Governance Gate Resolution Pipeline (GGRP)

```text
Stage Completed
        │
        ▼
Evidence Collection
        │
        ▼
Gate Evaluation
        │
        ▼
Capability Demonstration Review
        │
        ▼
Decision Authority
        │
        ▼
PASS / HOLD / FAIL
        │
        ▼
Next Stage
```

Governance Gate Resolution Pipeline là cơ chế kiểm soát chuẩn của Sprint.

---

# 13. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0801 | Governance Gate tồn tại |
| ACC-0802 | Evidence đầy đủ |
| ACC-0803 | Decision Authority hợp lệ |
| ACC-0804 | Decision có Traceability |
| ACC-0805 | Gate Record được tạo |
| ACC-0806 | Outstanding Actions được ghi nhận |
| ACC-0807 | HOLD có Action Plan |
| ACC-0808 | FAIL có Root Cause |
| ACC-0809 | PASS có đầy đủ Deliverables |
| ACC-0810 | Sprint chỉ chuyển Stage sau PASS |
| ACC-0811 | Capability Demonstration PASS |
| ACC-0812 | Frontend Evidence đầy đủ |

---

# 14. Relationship to Other Documents

SGP-08 liên kết với:

- SGP-01 Sprint Lifecycle
- SGP-03 Sprint Planning & Approval
- SGP-04 Sprint Execution Governance
- SGP-05 Sprint Review & Acceptance
- SGP-06 Sprint Metrics & Reporting
- SGP-07 Sprint Exception Management
- VAP (Verification & Acceptance Pack)

Governance Gates là cơ chế kiểm soát chính của toàn bộ Sprint Lifecycle, bảo đảm mọi Capability được kiểm soát đầy đủ trên Backend, Frontend và Experience.

---

# 15. Document Status

**Status: FROZEN**

SGP-08 là tài liệu nền tảng quy định các Governance Gate của Sprint trong YSim.

Mọi Sprint phải vượt qua đầy đủ Governance Gate trước khi chuyển sang giai đoạn tiếp theo.

---