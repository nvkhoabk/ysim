---
document_code: AAP-02
document_name: Sprint Contract Model
project: YSim v2.1
document_set: AI Architecture Pack
version: 2.1
status: FROZEN
language: en-US
---

# Sprint Contract Model

## AAP-02

---

# 1. Purpose

Sprint Contract Model định nghĩa mô hình Sprint Contract của nền tảng YSim.

Sprint Contract là đầu vào chính thức của AI trước khi thực hiện Sprint.

Sprint Contract quy định:

- Scope
- Capability
- Ownership
- Dependencies
- Constraints
- Deliverables
- Acceptance Criteria

Sprint Contract là bất biến trong suốt quá trình triển khai.

---

# 2. Principles

Sprint Contract tuân thủ các nguyên tắc:

- Contract First
- Scope Controlled
- Architecture Governed
- Incremental
- Evidence Driven
- Traceable
- Full-stack Capability Delivery
- Experience-oriented Planning

Sprint Contract không phải Prompt.

Sprint Contract không phải Requirement.

Sprint Contract là Implementation Contract.

---

# 3. Sprint Objectives

Một Sprint chỉ được phép triển khai:

- một hoặc nhiều Technical Capability có liên quan;
- trong phạm vi Ownership đã được phê duyệt;
- theo đúng Architecture Baseline.

Sprint không được mở rộng Scope.

---

# 4. Sprint Contract Structure

Sprint Contract bao gồm các phần sau:

```text
Sprint Metadata

↓

Business Context

↓

Technical Capability

↓

Implementation Scope

↓

Dependencies

↓

Constraints

↓

Acceptance Criteria

↓

Full-stack Deliverables

↓

Deliverables

↓

Validation

↓

Evidence
```

---

# 5. Sprint Metadata

Sprint Metadata bao gồm:

- Sprint ID
- Sprint Name
- Version
- Status
- Owner
- Priority
- Target Release

Metadata là định danh duy nhất của Sprint.

---

# 6. Business Context

Business Context xác định:

- Business Domain
- Business Capability
- Business Objects
- Business Policies
- Business Events
- Business Snapshots

AI không được tự mở rộng Business Context.

---

# 7. Technical Capability

Technical Capability mô tả chính xác chức năng kỹ thuật cần triển khai.

Ví dụ:

- Payment Session
- Inventory Allocation
- Settlement Processing
- Notification Delivery

Sprint được tổ chức theo Technical Capability, không theo Business Domain.

Đối với Capability có giao diện người dùng, Sprint phải lập kế hoạch đồng thời cho:

- Backend
- API
- Frontend
- Seed Data
- Capability Demonstration
- Verification

---

# 8. Implementation Scope

Sprint Contract xác định rõ:

Được phép:

- tạo mới;
- mở rộng;
- sửa đổi.

Không được phép:

- thay đổi ngoài phạm vi;
- sửa Domain khác;
- thay đổi Architecture Baseline.

---

# 9. Domain Ownership

Sprint chỉ được Modify các Domain đã được chỉ định.

Ví dụ:

| Domain | Access |
|---------|--------|
| Payment | Modify |
| Order | Read |
| Shared | Approved Extension |
| Customer | Read Only |

Ownership là ràng buộc bắt buộc.

---

# 10. Dependencies

Sprint Contract phải liệt kê:

- Required Modules
- Required APIs
- Required Events
- Required Snapshots
- Required Configurations
- Required Integrations

Dependency được xác minh trong Repository Discovery.

---

# 11. Constraints

Sprint Contract quy định các giới hạn.

Ví dụ:

- Không thay đổi Public API.
- Không thay đổi Event Contract.
- Không đổi Module Ownership.
- Không sửa Migration cũ.
- Không thay đổi Registry.

Constraints luôn có độ ưu tiên cao.

---

# 12. Acceptance Criteria

Acceptance Criteria được chia thành các nhóm.

## Business

- Capability hoàn thành.
- Business Rule đúng.
- Event đúng.
- Snapshot đúng.

## Technical

- Build PASS.
- Static Analysis PASS.
- Contract Validation PASS.

## Operational

- Logging.
- Monitoring.
- Metrics.
- Alert.

---

# 13. Deliverables

Sprint tối thiểu phải tạo:

- Backend Source Code
- Frontend Source Code (nếu có UI)
- Tests
- Migration
- Configuration
- Seed Data
- Capability Demonstration Surface
- Documentation
- Validation Report
- Evidence Package

Deliverables được định nghĩa trước khi triển khai.


---

# 13A. Full-stack Capability Contract

Đối với Capability có giao diện người dùng, Sprint Contract phải mô tả đầy đủ:

- Backend Modules
- Frontend Pages
- API Contracts
- UI Routes
- Design System Components
- Seed Data
- Demonstration Scenarios

Không được lập Sprint chỉ bao gồm Backend nếu Capability yêu cầu trải nghiệm người dùng.


---

# 14. Validation Requirements

Sprint phải vượt qua:

- Architecture Validation
- Dependency Validation
- Contract Validation
- Testing Validation
- Security Validation

Validation là điều kiện để hoàn thành Sprint.

---

# 15. Architecture Change

Nếu AI phát hiện Sprint Contract không thể thực hiện:

AI không được tự thay đổi.

AI phải sinh:

- Architecture Change Proposal (ACP)
- Impact Analysis
- Suggested Resolution

Sprint chỉ tiếp tục sau khi được phê duyệt.

---

# 16. Sprint Lifecycle

```text
Draft

↓

Approved

↓

Repository Discovery

↓

Planning

↓

Backend + Frontend Implementation

↓

Capability Demonstration

↓

Validation

↓

Evidence Generation

↓

Review

↓

Completed
```

Sprint chỉ được chuyển sang bước tiếp theo khi bước hiện tại hoàn thành.

---

# 17. Sprint Deliverable Manifest

Mỗi Sprint phải sinh Sprint Manifest.

Sprint Manifest bao gồm:

- Source Code
- Changed Modules
- New APIs
- New Events
- New Snapshots
- Tests
- Documentation
- Validation Results
- Evidence

Manifest là đầu ra chính thức của Sprint.

---

# 18. Sprint Rules

SC-001 — Sprint Contract là bất biến.

SC-002 — Repository Discovery là bắt buộc.

SC-003 — Không vượt Scope.

SC-004 — Không thay đổi Architecture.

SC-005 — Chỉ Modify Domain Ownership được cấp.

SC-006 — Mọi Dependency phải được xác minh.

SC-007 — Mọi Deliverable phải được sinh.

SC-008 — Validation là bắt buộc.

SC-009 — ACP thay thế việc tự sửa Contract.

SC-010 — Sprint chỉ hoàn thành khi có đầy đủ Evidence.

---

# 19. Sprint Resolution Pipeline (SRP)

```text
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Dependency Resolution
        │
        ▼
Implementation Planning
        │
        ▼
Implementation
        │
        ▼
Validation
        │
        ▼
Evidence Generation
        │
        ▼
Sprint Manifest
        │
        ▼
Human Review
```

Sprint Resolution Pipeline là mô hình chuẩn cho mọi Sprint trong YSim.

---

# 20. Sprint Evidence

Mỗi Sprint phải sinh tối thiểu:

- Sprint Manifest
- Validation Report
- Test Report
- Coverage Report
- Architecture Compliance Report
- Change Summary
- Review Report
- Demonstration Report

Evidence là điều kiện để nghiệm thu Sprint.

---

# 21. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0201 | Sprint Contract được Approved |
| ACC-0202 | Scope không bị mở rộng |
| ACC-0203 | Repository Discovery hoàn thành |
| ACC-0204 | Dependency được xác minh |
| ACC-0205 | Ownership được tuân thủ |
| ACC-0206 | Constraints không bị vi phạm |
| ACC-0207 | Deliverables đầy đủ |
| ACC-0208 | Validation PASS |
| ACC-0209 | Sprint Manifest được tạo |
| ACC-0210 | Evidence đầy đủ |

---

# 22. Relationship to Other Documents

AAP-02 liên kết với:

- YADF
- ABP-15 AI Implementation Architecture
- AAP-01 Repository Discovery Model
- Sprint Governance Pack (SGP)
- Verification & Acceptance Pack (VAP)
- Codex Implementation Pack (CIP)

Sprint Contract là hợp đồng triển khai duy nhất mà AI được phép thực hiện và là nền tảng của Full-stack Capability Delivery.

---

# 23. Document Status

**Status: FROZEN**

AAP-02 là tài liệu nền tảng quy định mô hình Sprint Contract của nền tảng YSim.

Mọi AI Coding Assistant, Sprint Planning và quy trình triển khai phải tuân thủ Sprint Contract Model trước khi bắt đầu phát triển.

---