---
document_code: DIP-06
document_name: Validation, Evidence & Acceptance Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

# Validation, Evidence & Acceptance Standard

## DIP-06

---

# 1. Purpose

Validation, Evidence & Acceptance Standard định nghĩa tiêu chuẩn xác minh, thu thập bằng chứng và nghiệm thu đối với mọi Executable Sprint Package (ESPK).

Một Sprint chỉ được xem là hoàn thành khi:

- Validation PASS;
- Evidence đầy đủ;
- Capability được Acceptance.

Build thành công không đồng nghĩa Sprint hoàn thành.

---

# 2. Position in Software Factory

```text
AI Coding

↓

Build

↓

Validation

↓

Evidence

↓

Capability Demonstration

↓

Acceptance

↓

Git Commit

↓

Release
```

Validation và Acceptance là điều kiện bắt buộc trước Release.

---

# 3. Objectives

Tiêu chuẩn này nhằm:

- xác minh chất lượng Source Code;
- chứng minh Capability hoạt động;
- tạo Evidence phục vụ Audit;
- chuẩn hóa Acceptance;
- hỗ trợ Release;
- hỗ trợ Rollback.

---

# 4. Principles

Validation & Acceptance tuân thủ:

- Validate Everything
- Evidence by Design
- Demonstration First
- Repeatable
- Explainable
- Traceable
- AI Independent
- Automation First
- Capability Oriented

---

# 5. Validation Model

Validation gồm nhiều tầng.

```text
Source

↓

Build

↓

Static Analysis

↓

Unit Test

↓

Integration Test

↓

Contract Test

↓

Frontend Test

↓

End-to-End Test

↓

Compliance

↓

Capability Demonstration
```

Không được bỏ qua tầng Validation bắt buộc.

---

# 6. Validation Categories

| Category | Purpose |
|----------|----------|
| Build Validation | Kiểm tra Build |
| Static Validation | Lint, Type Check |
| Unit Validation | Business Logic |
| Integration Validation | Service Interaction |
| Contract Validation | API Compatibility |
| Frontend Validation | UI & Components |
| E2E Validation | User Journey |
| Compliance Validation | ESP / SGP / DIP |
| Runtime Validation | Execution Runtime |
| Demonstration Validation | Demo Scenario |

---

# 7. Capability Demonstration

Capability có UI phải chứng minh được:

- Login
- CRUD
- Search
- Checkout
- Payment
- Dashboard
- Reporting

(tùy Capability)

Demonstration là một phần của Validation.

---

# 8. Evidence Model

Mỗi Task phải sinh:

- Execution Log
- Validation Result
- Build Output
- Test Output
- Git Diff

Mỗi Sprint phải sinh:

- Sprint Report
- Capability Report
- Demonstration Report
- Acceptance Report

---

# 9. Evidence Package

```text
evidence/

├── prompts/

├── logs/

├── validation/

├── screenshots/

├── videos/

├── reports/

├── git/

└── acceptance/
```

Evidence Package phải được lưu cùng Sprint.

---

# 10. Frontend Evidence

Capability có Frontend phải có:

- Screenshot
- Navigation Flow
- UI Components
- Theme Verification
- Responsive Verification

Nếu phù hợp, bổ sung Video Demonstration.

---

# 11. Acceptance Criteria

Capability được ACCEPT khi:

✓ Build PASS

✓ Validation PASS

✓ Tests PASS

✓ Demonstration PASS

✓ Evidence đầy đủ

✓ Documentation cập nhật

✓ Git Commit thành công

---

# 12. Acceptance Checklist

Acceptance tối thiểu gồm:

- Business Rules
- API
- Database
- Frontend
- Design System
- Experience API
- Security
- Performance
- Documentation

---

# 13. PASS / FAIL Rules

Capability:

PASS

khi:

- không có Validation Error;
- không có Critical Bug;
- Acceptance PASS.

FAIL

khi:

- Build FAIL;
- Test FAIL;
- Demonstration FAIL;
- Architecture Conflict;
- Business Conflict.

---

# 14. Validation Report

Runner phải sinh:

```text
validation/

summary.md

build.md

tests.md

compliance.md

acceptance.md
```

Validation Report là đầu ra bắt buộc.

---

# 15. Evidence Traceability

Mọi Evidence phải truy vết được:

```text
Sprint

↓

Task

↓

Prompt

↓

Commit

↓

Report

↓

Acceptance
```

Không được có Evidence mồ côi.

---

# 16. Acceptance Authority

Acceptance được thực hiện bởi:

- AI Runtime (tự động)
- Developer Review
- Technical Lead
- Product Owner (nếu cần)

AI chỉ được đánh dấu PASS khi đáp ứng đầy đủ Checklist.

---

# 17. Failure Handling

Nếu Validation FAIL:

Runner phải:

- dừng Sprint;
- lưu Log;
- lưu Prompt;
- lưu Exit Code;
- sinh Failure Report.

Không Commit.

---

# 18. Rules

VAL-001 — Validation sau từng Task.

VAL-002 — Evidence sau từng Task.

VAL-003 — Capability có UI phải Demonstration.

VAL-004 — Acceptance bắt buộc.

VAL-005 — Screenshot là bắt buộc với Frontend.

VAL-006 — Validation Report phải sinh tự động.

VAL-007 — Failure Report phải được lưu.

VAL-008 — Không Commit khi Acceptance FAIL.

VAL-009 — Evidence phải Version hóa.

VAL-010 — Sprint chỉ COMPLETE khi Acceptance PASS.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| VAC-0601 | Build PASS |
| VAC-0602 | Tests PASS |
| VAC-0603 | Compliance PASS |
| VAC-0604 | Demonstration PASS |
| VAC-0605 | Frontend Evidence đầy đủ |
| VAC-0606 | Acceptance PASS |
| VAC-0607 | Failure Handling đúng chuẩn |
| VAC-0608 | Evidence đầy đủ |
| VAC-0609 | Git Commit thành công |
| VAC-0610 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

DIP-06 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- DIP-02 AI Context Resolution & Prompt Assembly Standard
- DIP-03 Seed & Reference Data Standard
- DIP-04 AI Execution Runtime & Bash Runner Standard
- DIP-05 AI Prompt Orchestration & Task Assembly Standard
- ESP Engineering Standards Pack
- SGP Sprint Governance Pack
- VAP Verification & Acceptance Pack
- ROP Release & Operations Pack

DIP-06 là tiêu chuẩn chính thức cho Validation, Evidence và Acceptance của YSim AI Software Factory.

---

# 21. Acceptance Workflow

```text
Task Completed

↓

Build

↓

Validation

↓

Evidence Collection

↓

Capability Demonstration

↓

Acceptance Checklist

↓

PASS

↓

Git Commit

↓

Next Task
```

Nếu FAIL ở bất kỳ bước nào:

```text
Failure Report

↓

Stop Sprint

↓

ACP (nếu có Architecture Conflict)
```

---

# 22. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải hoàn thành đầy đủ ba giai đoạn:

- Validation
- Evidence
- Acceptance

Capability chỉ được coi là **Completed** khi vượt qua toàn bộ Validation Pipeline, tạo đủ Evidence Package và được Acceptance theo tiêu chuẩn của DIP-06.

Validation, Evidence và Acceptance là điều kiện bắt buộc trước Git Commit và Release.