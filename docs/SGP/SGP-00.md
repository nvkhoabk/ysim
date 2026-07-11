---
document_code: SGP-00
document_name: Sprint Governance Overview
project: YSim v2.1
document_set: Sprint Governance Pack
version: 2.1
status: FROZEN
language: en-US
---

# Sprint Governance Overview

## SGP-00

---

# 1. Purpose

Sprint Governance Pack (SGP) định nghĩa mô hình quản trị Sprint của nền tảng YSim.

SGP chuẩn hóa:

- Sprint Lifecycle
- Sprint Roles
- Sprint Decision Authority
- Sprint Quality Gates
- Sprint Review
- Sprint Acceptance
- Sprint Reporting
- Sprint Completion

SGP không định nghĩa cách AI lập kế hoạch hoặc sinh mã nguồn. Các nội dung đó thuộc AI Architecture Pack (AAP).

---

# 2. Governance Principles

YSim áp dụng các nguyên tắc sau:

- Governance by Contract
- Architecture First
- Evidence Driven
- Human Governed
- AI Assisted
- Stage Gate Control
- Full Traceability
- Continuous Improvement
- Full-stack Capability Governance
- Experience Governance

Sprint không được quản lý bằng cảm tính.

---

# 3. Governance Scope

SGP áp dụng cho toàn bộ Sprint từ khi được tạo đến khi hoàn thành.

```text
Sprint Proposal
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
Capability Demonstration
        │
        ▼
Review
        │
        ▼
Acceptance
        │
        ▼
Release Ready
```

---

# 4. Governance Objectives

Sprint Governance nhằm:

- đảm bảo Sprint đúng Scope;
- đảm bảo tuân thủ Architecture;
- kiểm soát Quality Gates;
- đảm bảo đầy đủ Evidence;
- xác định rõ trách nhiệm và quyền quyết định;
- tạo khả năng truy vết toàn bộ Sprint;
- bảo đảm Backend, Frontend và Demonstration được hoàn thành trong cùng một Sprint.

---

# 5. Governance Layers

Sprint được quản trị trên bốn lớp.

| Layer | Responsibility |
|--------|----------------|
| Business Governance | Xác nhận giá trị nghiệp vụ |
| Architecture Governance | Kiểm soát kiến trúc |
| Engineering Governance | Kiểm soát chất lượng kỹ thuật |
| Delivery Governance | Kiểm soát tiến độ và phát hành |
| Experience Governance | Kiểm soát Frontend, Design System và Demonstration |

---

# 6. Governance Components

Sprint Governance bao gồm:

- Sprint Lifecycle
- Roles & Responsibilities
- Planning & Approval
- Execution Governance
- Review & Acceptance
- Metrics & Reporting
- Change Management
- Quality Gates
- Completion & Handover
- Capability Demonstration Governance

Các thành phần này được mô tả trong các tài liệu SGP-01 đến SGP-09.

---

# 7. Governance Model

```text
Sprint Contract
        │
        ▼
Governance
        │
        ├── Scope Control
        ├── Decision Control
        ├── Quality Control
        ├── Risk Control
        └── Evidence Control
```

Governance không thay thế việc triển khai.

Governance kiểm soát việc triển khai.

---

# 7A. Full-stack Governance

Đối với mọi Capability có giao diện người dùng, Sprint Governance phải kiểm soát đồng thời:

- Backend Delivery
- API Delivery
- Frontend Delivery
- Design System Compliance
- Seed Data
- Capability Demonstration
- Verification Evidence

Sprint chỉ được chuyển sang Review khi toàn bộ các thành phần trên đã hoàn thành.

---

# 8. Decision Authority

Mỗi Sprint phải xác định rõ:

- Business Owner
- Architecture Owner
- Sprint Owner
- AI Agent
- QA
- Reviewer
- Release Manager

Không có quyết định nào không có Owner.

---

# 9. Governance Outcomes

Một Sprint được coi là thành công khi:

- Scope hoàn thành.
- Kiến trúc được tuân thủ.
- Quality Gates đạt.
- Evidence đầy đủ.
- Được Human Review chấp thuận.
- Capability Demonstration PASS.
- Sẵn sàng đưa vào Release.

---

# 10. Governance Rules

SG-001 — Sprint phải có Sprint Contract.

SG-002 — Sprint phải có Owner.

SG-003 — Sprint phải tuân thủ Architecture Baseline.

SG-004 — Sprint phải vượt qua tất cả Quality Gates.

SG-005 — Sprint phải có đầy đủ Evidence.

SG-006 — Sprint phải được Human Review.

SG-007 — Mọi quyết định đều có Traceability.

SG-008 — Mọi thay đổi kiến trúc phải thông qua ACP.

SG-009 — Sprint chỉ được Accept sau Verification.

SG-010 — Sprint Governance áp dụng cho mọi AI Coding Assistant.

SG-011 — Capability có giao diện phải hoàn thành Backend và Frontend trong cùng Sprint.

SG-012 — Capability Demonstration là Quality Gate bắt buộc trước Review.

---

# 11. Governance Lifecycle

```text
Create Sprint
        │
        ▼
Governance Planning
        │
        ▼
Governance Execution
        │
        ▼
Governance Review
        │
        ▼
Capability Demonstration Review
        │
        ▼
Governance Acceptance
        │
        ▼
Continuous Improvement
```

Governance được áp dụng xuyên suốt vòng đời Sprint.

---

# 12. Relationship to Other Document Sets

SGP liên kết với:

- BRD
- Enterprise Registry
- YADF
- ABP
- AAP
- ESP
- DIP
- VAP
- ROP

SGP là tầng quản trị của toàn bộ Sprint-Driven AI Development Framework, bảo đảm Full-stack Capability Delivery được thực hiện thống nhất trên Backend, Frontend và Experience.

---

# 13. Document Roadmap

Sprint Governance Pack bao gồm:

- SGP-00 Sprint Governance Overview
- SGP-01 Sprint Lifecycle
- SGP-02 Roles & Responsibilities
- SGP-03 Sprint Planning & Approval
- SGP-04 Sprint Execution Governance
- SGP-05 Sprint Review & Acceptance
- SGP-06 Sprint Metrics & Reporting
- SGP-07 Sprint Change Management
- SGP-08 Sprint Quality Gates
- SGP-09 Sprint Completion & Handover

---

# 14. Document Status

**Status: FROZEN**

SGP-00 là tài liệu nền tảng quy định mô hình quản trị Sprint của YSim.

Mọi Sprint phải tuân thủ các nguyên tắc trong Sprint Governance Pack.

---