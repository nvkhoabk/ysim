---
document_code: SGP-07
document_name: Sprint Exception Management
project: YSim v2.0
document_set: Sprint Governance Pack
version: 1.0
status: FROZEN
language: en-US
---

# Sprint Exception Management

## SGP-07

---

# 1. Purpose

Sprint Exception Management định nghĩa mô hình quản lý các tình huống bất thường phát sinh trong quá trình thực hiện Sprint.

Exception Management đảm bảo:

- Sprint được kiểm soát khi xảy ra sự cố.
- Không làm mất Governance.
- Không tự ý mở rộng Scope.
- Có cơ chế Escalation rõ ràng.
- Có khả năng Recovery.

Exception không đồng nghĩa với Failure.

Exception là trạng thái cần được quản trị.

---

# 2. Principles

Sprint Exception Management tuân thủ:

- Govern Before Resolve
- Evidence Driven
- Human Decision
- Architecture First
- Traceable
- Recoverable

---

# 3. Exception Categories

Platform chuẩn hóa các nhóm Exception.

| Category | Description |
|----------|-------------|
| Planning Exception | Lỗi trong Planning |
| Dependency Exception | Thiếu Dependency |
| Architecture Exception | Xung đột Architecture |
| AI Execution Exception | AI không hoàn thành |
| Validation Exception | Verification FAIL |
| Review Exception | Human Review không đạt |
| Resource Exception | Thiếu Resource |
| External Exception | Phụ thuộc bên ngoài |

---

# 4. Exception Severity

Exception được phân loại:

| Severity | Description |
|-----------|-------------|
| Low | Không ảnh hưởng Sprint |
| Medium | Ảnh hưởng tiến độ |
| High | Sprint có nguy cơ thất bại |
| Critical | Sprint phải dừng |

Severity điều khiển Escalation.

---

# 5. Exception Lifecycle

```text
Detected

↓

Recorded

↓

Classified

↓

Assigned

↓

Resolved

↓

Verified

↓

Closed
```

Exception luôn có Lifecycle riêng.

---

# 6. Exception Ownership

Mỗi Exception phải có:

- Exception ID
- Owner
- Severity
- Category
- Resolution Target
- Status

Không có Exception không có Owner.

---

# 7. Escalation Model

Exception được Escalate theo:

```text
AI Agent

↓

Sprint Owner

↓

Architecture Owner

↓

Business Owner

↓

Steering Committee
```

Escalation phụ thuộc Severity.

---

# 8. Exception Resolution

Platform hỗ trợ:

- Retry
- Replan
- Rework
- ACP
- Manual Decision
- Sprint Cancellation

Resolution phải được ghi nhận.

---

# 9. Blocked Sprint

Sprint có thể chuyển sang trạng thái:

- Blocked
- Waiting Dependency
- Waiting Decision
- Waiting Review
- Waiting External System

Blocked không đồng nghĩa Failed.

---

# 10. Exception Register

Platform duy trì Exception Register.

Mỗi Exception bao gồm:

- Description
- Impact
- Root Cause
- Resolution
- Owner
- Timeline
- Evidence

---

# 11. Governance Checkpoints

Exception có thể phát sinh tại:

- Planning
- Execution
- Verification
- Review
- Acceptance

Mỗi Checkpoint đều phải ghi nhận Exception nếu có.

---

# 12. Exception Events

Platform phát sinh:

- SprintBlocked
- ExceptionRaised
- ExceptionEscalated
- ExceptionResolved
- SprintResumed

Các Event tuân thủ ABP-05.

---

# 13. Exception Rules

EM-001 — Mọi Exception phải được ghi nhận.

EM-002 — Mọi Exception phải có Owner.

EM-003 — Exception phải được phân loại.

EM-004 — Severity điều khiển Escalation.

EM-005 — Resolution phải có Evidence.

EM-006 — Sprint chỉ Resume sau Verification.

EM-007 — Exception phải truy vết được.

EM-008 — ACP được sử dụng cho thay đổi kiến trúc.

EM-009 — Exception Register là bắt buộc.

EM-010 — Exception phải được đóng trước khi Sprint Closed.

---

# 14. Sprint Exception Resolution Pipeline (SERP)

```text
Exception Detected
        │
        ▼
Classification
        │
        ▼
Severity Assessment
        │
        ▼
Owner Assignment
        │
        ▼
Resolution
        │
        ▼
Verification
        │
        ▼
Sprint Resume
```

---

# 15. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0701 | Exception được ghi nhận |
| ACC-0702 | Exception có Owner |
| ACC-0703 | Severity được xác định |
| ACC-0704 | Escalation đúng quy trình |
| ACC-0705 | Resolution có Evidence |
| ACC-0706 | Exception Register được cập nhật |
| ACC-0707 | Sprint Resume hợp lệ |
| ACC-0708 | ACP được sử dụng đúng trường hợp |
| ACC-0709 | Exception được đóng |
| ACC-0710 | Sprint không còn Exception Critical |

---

# 16. Relationship to Other Documents

SGP-07 liên kết với:

- SGP-04 Sprint Execution Governance
- SGP-05 Sprint Review & Acceptance
- SGP-06 Sprint Metrics & Reporting
- AAP-06 Architecture Change Proposal Model
- ABP-12 Error Handling Architecture

Exception Management là cơ chế xử lý các tình huống bất thường trong quá trình thực thi Sprint.

---

# 17. Document Status

**Status: FROZEN**

SGP-07 là tài liệu nền tảng quy định mô hình quản lý Exception của Sprint trong YSim.

Mọi Exception phát sinh trong Sprint phải được quản trị theo Sprint Exception Management.

---