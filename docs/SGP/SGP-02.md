---
document_code: SGP-02
document_name: Sprint Roles & Responsibilities
project: YSim v2.1
document_set: Sprint Governance Pack
version: 2.1
status: FROZEN
language: en-US
---

# Sprint Roles & Responsibilities

## SGP-02

---

# 1. Purpose

Sprint Roles & Responsibilities định nghĩa các vai trò, trách nhiệm và quyền quyết định trong toàn bộ vòng đời Sprint.

Tài liệu này chuẩn hóa:

- Governance Roles
- AI Roles
- Human Roles
- Decision Authority
- Responsibility Matrix
- Escalation Model

Mọi Sprint phải xác định rõ vai trò trước khi bắt đầu.

---

# 2. Principles

Sprint Governance tuân thủ các nguyên tắc:

- Clear Ownership
- Single Decision Authority
- Separation of Responsibility
- Human Governed
- AI Assisted
- Architecture First
- Traceable Decision
- Full-stack Responsibility
- Experience Ownership

Không có hoạt động nào không có Owner.

Không có quyết định nào không có Decision Authority.

---

# 3. Governance Roles

Platform chuẩn hóa các vai trò sau.

| Role | Responsibility |
|--------|----------------|
| Business Owner | Giá trị nghiệp vụ |
| Architecture Owner | Kiến trúc |
| Sprint Owner | Điều phối Sprint |
| AI Coding Agent | Triển khai |
| AI Review Agent | Tự đánh giá |
| Developer | Hỗ trợ AI |
| QA Engineer | Kiểm thử |
| Reviewer | Review kỹ thuật |
| Release Manager | Release |
| Operations | Vận hành |
| Frontend Lead | Frontend & Design System |
| Experience Owner | Storefront Experience & Demonstration |

---

# 4. Role Responsibilities

## Business Owner

Chịu trách nhiệm:

- Business Scope
- Business Acceptance
- Priority
- Business Decision

Không quyết định Architecture.

---

## Architecture Owner

Chịu trách nhiệm:

- Architecture Baseline
- Architecture Review
- ACP Approval
- Module Boundary
- Dependency Rules

Architecture Owner là người duy nhất được phê duyệt thay đổi kiến trúc.

---

## Sprint Owner

Chịu trách nhiệm:

- Sprint Planning
- Progress
- Risk
- Coordination
- Completion

Sprint Owner không thay đổi Business Requirement.

---

## AI Coding Agent

Chịu trách nhiệm:

- Repository Discovery
- Planning
- Code Generation
- Validation
- Frontend Generation
- Seed Data Generation
- Capability Demonstration Generation
- Evidence Generation

AI không có quyền phê duyệt.

---

## AI Review Agent

Chịu trách nhiệm:

- Verification
- Frontend Verification
- Architecture Checking
- Compliance Checking
- Evidence Review

AI Review chỉ đưa ra khuyến nghị.

---

## Developer

Chịu trách nhiệm:

- Hỗ trợ AI
- Xử lý tình huống đặc biệt
- Refactoring được phê duyệt
- Technical Support

---

## QA Engineer

Chịu trách nhiệm:

- Test Strategy
- Test Review
- Regression
- Acceptance Verification

---

## Reviewer

Chịu trách nhiệm:

- Code Review
- Architecture Review
- Security Review
- Quality Review

---

## Release Manager

Chịu trách nhiệm:

- Release Approval
- Deployment Coordination
- Rollback Decision
- Production Readiness

---

## Operations

Chịu trách nhiệm:

- Production Monitoring
- Incident Response
- Runbook
- Operational Feedback

---

# 4A. Full-stack Capability Ownership

Đối với Capability có giao diện người dùng, trách nhiệm được phân bổ như sau:

- Architecture Owner: Architecture & Design Principles
- Sprint Owner: Delivery Coordination
- AI Coding Agent: Backend, Frontend, Seed Data và Demonstration
- Frontend Lead: UI/UX, Design System Compliance
- QA Engineer: End-to-end Verification
- Business Owner: Experience Acceptance

Không được tách Backend và Frontend thành hai Sprint độc lập đối với cùng một Capability.

---

# 5. Decision Authority Matrix

| Decision | Authority |
|------------|-----------|
| Business Scope | Business Owner |
| Sprint Approval | Sprint Owner |
| Architecture Change | Architecture Owner |
| ACP Approval | Architecture Owner |
| Human Acceptance | Business Owner |
| Production Release | Release Manager |
| Production Rollback | Release Manager |
| Operational Incident | Operations |

Decision Authority không được chia sẻ.

---

# 6. Responsibility Matrix (RACI)

| Activity | BO | AO | SO | AI | DEV | QA | RM | OPS |
|-----------|----|----|----|----|-----|----|----|-----|
| Sprint Planning | A | C | R | C | C | I | I | I |
| Repository Discovery | I | C | C | R | C | I | I | I |
| Planning | I | C | C | R | C | I | I | I |
| Implementation | I | C | I | R | C | I | I | I |
| Verification | I | C | I | R | C | C | I | I |
| Capability Demonstration | A | C | R | R | C | R | I | I |
| Acceptance | A | C | I | I | I | R | I | I |
| Release | I | I | I | I | I | C | A | R |

**Legend**

- **R** = Responsible
- **A** = Accountable
- **C** = Consulted
- **I** = Informed

---

# 7. Escalation Model

Nếu phát sinh:

- Architecture Conflict
- Business Conflict
- Security Conflict
- Scope Conflict

thì Escalation được thực hiện theo:

```text
AI Agent

↓

Sprint Owner

↓

Architecture Owner

↓

Business Owner

↓

Steering Committee (if required)
```

AI không tự giải quyết xung đột kiến trúc.

---

# 8. AI Governance

AI được phép:

- đọc Repository;
- lập kế hoạch;
- sinh mã nguồn;
- sinh Test;
- sinh Documentation;
- sinh Evidence.
- sinh Frontend Demonstration.

AI không được:

- thay đổi Architecture Baseline;
- thay đổi Registry;
- mở rộng Sprint Scope;
- tự phê duyệt Sprint.

---

# 9. Human Governance

Con người chịu trách nhiệm cuối cùng về:

- Business Decision
- Architecture Decision
- Release Decision
- Production Decision

AI chỉ đóng vai trò hỗ trợ.

---

# 10. Collaboration Principles

AI và con người làm việc theo nguyên tắc:

- Shared Context
- Contract Driven
- Evidence Driven
- Explainable Decision
- Shared Full-stack Ownership
- Transparent Review

Mọi quyết định phải có khả năng truy vết.

---

# 11. Roles & Responsibilities Rules

RR-001 — Mọi Sprint phải có Sprint Owner.

RR-002 — Chỉ có một Decision Authority cho mỗi loại quyết định.

RR-003 — AI không có quyền Approval.

RR-004 — Architecture Owner quyết định Architecture.

RR-005 — Business Owner quyết định Business.

RR-006 — Release Manager quyết định Production Release.

RR-007 — QA xác nhận chất lượng kiểm thử.

RR-008 — Operations chịu trách nhiệm Production.

RR-009 — Escalation phải theo đúng quy trình.

RR-010 — Mọi quyết định phải truy vết được.

RR-011 — Capability Demonstration phải có Owner.

RR-012 — Frontend và Backend cùng chịu một Sprint Owner.

---

# 12. Roles Resolution Pipeline (RRP)

```text
Sprint Activity
        │
        ▼
Identify Responsibility
        │
        ▼
Identify Decision Authority
        │
        ▼
Execute Activity
        │
        ▼
Capability Demonstration
        │
        ▼
Review
        │
        ▼
Approval
        │
        ▼
Record Decision
```

Roles Resolution Pipeline xác định rõ ai thực hiện và ai quyết định tại từng bước của Sprint.

---

# 13. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0201 | Sprint Owner được chỉ định |
| ACC-0202 | Business Owner được chỉ định |
| ACC-0203 | Architecture Owner được chỉ định |
| ACC-0204 | Decision Authority rõ ràng |
| ACC-0205 | RACI Matrix đầy đủ |
| ACC-0206 | Escalation Model được định nghĩa |
| ACC-0207 | AI không có quyền Approval |
| ACC-0208 | Human Review tồn tại |
| ACC-0209 | Mọi quyết định có Traceability |
| ACC-0210 | Governance tuân thủ SGP |
| ACC-0211 | Frontend Owner được xác định |
| ACC-0212 | Capability Demonstration Owner được xác định |

---

# 14. Relationship to Other Documents

SGP-02 liên kết với:

- SGP-00 Sprint Governance Overview
- SGP-01 Sprint Lifecycle
- AAP-02 Sprint Contract Model
- AAP-04 AI Verification Model
- AAP-06 Architecture Change Proposal Model
- ROP (Release & Operations Pack)

Roles & Responsibilities là nền tảng của toàn bộ cơ chế Governance trong Sprint-Driven AI Development, bảo đảm mọi Capability đều có đầy đủ Owner cho Backend, Frontend và Experience.

---

# 15. Document Status

**Status: FROZEN**

SGP-02 là tài liệu nền tảng quy định vai trò, trách nhiệm và quyền quyết định trong toàn bộ Sprint Lifecycle.

Mọi Sprint phải xác định đầy đủ Roles, Responsibilities và Decision Authority trước khi bắt đầu triển khai.

---