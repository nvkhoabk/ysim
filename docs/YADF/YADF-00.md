---
document_code: YADF-00
document_name: YSim AI Development Framework
project: YSim v2.0
document_set: Engineering Governance
version: 2.0
status: FROZEN
language: en-US
---

# YSim AI Development Framework (YADF)

---

# 1. Purpose

YSim AI Development Framework (YADF) là framework chuẩn hóa toàn bộ quy trình phát triển phần mềm của nền tảng YSim với sự hỗ trợ của AI Coding Assistant.

YADF định nghĩa:

- Development Governance
- Architecture Governance
- Sprint Governance
- AI Collaboration
- Verification
- Operational Readiness

YADF là nền tảng để tất cả các dự án trong hệ sinh thái YSim được phát triển theo cùng một phương pháp.

---

# 2. Framework Philosophy

YADF áp dụng nguyên tắc:

> **Business-Driven, Blueprint-Oriented, Contract-Driven, Full-stack AI Development**

Business quyết định yêu cầu.

Architecture quyết định cấu trúc.

Sprint Contract quyết định phạm vi triển khai.

AI chịu trách nhiệm hiện thực hóa (Implementation).

AI không phải là Source of Truth.

---

# 3. Framework Layers

```text
Business Layer
        │
        ▼
Architecture Layer
        │
        ▼
Capability Layer
        │
        ▼
Implementation Layer
        │
        ▼
Verification Layer
        │
        ▼
Operation Layer
```

Mỗi Layer có trách nhiệm rõ ràng và độc lập.


---

# 3A. Commerce & Capability Meta Model

Version 2.1 bổ sung Meta Model chuẩn cho AI Software Factory.

```text
Business Model
        │
        ▼
Business Blueprint
        │
        ▼
Store Template
        │
        ▼
Store Instance
        │
        ▼
Commerce Experience
```

Mọi Capability có giao diện người dùng được triển khai theo mô hình Full-stack Capability Delivery:

```text
Capability
        │
        ├── Backend
        ├── API
        ├── Frontend
        ├── Seed Data
        ├── Demonstration
        └── Verification
```

YADF coi Capability là đơn vị Delivery nhỏ nhất của AI Factory.

---

# 4. Development Lifecycle

```text
Business Requirements
        │
        ▼
Business Registry
        │
        ▼
Architecture Baseline
        │
        ▼
Sprint Contract
        │
        ▼
Repository Discovery
        │
        ▼
Backend + Frontend Implementation
        │
        ▼
Capability Demonstration
        │
        ▼
Verification
        │
        ▼
Acceptance
        │
        ▼
Deployment
        │
        ▼
Operations
```

---

# 5. Core Principles

YADF tuân thủ các nguyên tắc sau:

1. Business là Source of Truth.
2. Registry là Architecture Source of Truth.
3. Sprint Contract là Sprint Source of Truth.
4. AI chỉ là Implementation Agent.
5. Mọi thay đổi phải truy vết được.
6. Mọi Sprint phải độc lập và kiểm thử được.
7. Không thay đổi Architecture trong Sprint nếu chưa được phê duyệt.
8. Mọi thay đổi phải có bằng chứng (Implementation Evidence).
9. Capability có giao diện phải được Demonstration trước khi nghiệm thu.
10. Backend và Frontend được phát triển trong cùng một Sprint.

---

# 6. Sprint Model

Sprint là đơn vị triển khai theo **Technical Capability**.

Mỗi Sprint:

- có Domain Ownership rõ ràng;
- có Sprint Contract riêng;
- có phạm vi nhỏ, độc lập;
- có thể build, test và nghiệm thu độc lập.

Sprint không phải là Business Domain và cũng không phải là Vertical Slice.

---

# 7. Sprint Contract

Sprint Contract là tài liệu bất biến trong quá trình triển khai.

Một Sprint chỉ được bắt đầu khi:

- Business Object đã được xác định.
- Business Capability đã được xác định.
- Business Policy đã được xác định.
- Business Event đã được xác định.
- Business Snapshot đã được xác định.
- API Contract đã được xác định.

Nếu phát hiện vấn đề, AI phải tạo **Architecture Change Proposal (ACP)** thay vì tự thay đổi Sprint Contract.

---

# 8. Repository Discovery

Repository Discovery là bước bắt buộc trước khi triển khai.

AI phải đánh giá:

- Existing Modules
- Existing APIs
- Existing Database Schema
- Existing Migrations
- Existing Events
- Existing Snapshots
- Existing Tests
- Existing Technical Debt
- Gap Analysis

Repository Discovery là cơ sở để lập kế hoạch triển khai Sprint.

---

# 9. Domain Ownership

Mỗi Sprint chỉ được phép thay đổi:

- Domain thuộc Ownership của Sprint.
- Shared Components được Sprint Contract cho phép.

Không được thay đổi Domain khác nếu chưa được phê duyệt.

---

# 10. Dependency Resolution

YADF định nghĩa ba mức xử lý Dependency:

## Level 1 — Available Dependency

Dependency đã tồn tại.

→ Triển khai.

## Level 2 — Mockable Dependency

Dependency chưa tồn tại nhưng được phép Mock.

→ AI tạo Mock/Stub/Fake theo Sprint Contract.

## Level 3 — Architecture Dependency

Dependency thuộc Architecture Contract.

Ví dụ:

- Business Object
- Capability
- Policy
- Event
- Snapshot
- Shared API
- Shared Database Contract

AI không được tự tạo.

Phải sinh:

- Dependency Report
- Architecture Change Proposal (ACP)

---

# 11. Safe Refactoring

AI được phép Refactor khi:

- không thay đổi Business Behavior;
- không thay đổi Public Contract;
- không thay đổi Business Flow;
- không thay đổi Domain Ownership.

Nếu Refactor ảnh hưởng Contract hoặc Architecture:

→ phải tạo ACP.

---

# 12. Verification Model

Definition of Done gồm ba nhóm.

## Technical

- Build
- Migration
- Static Analysis
- Unit Test
- Contract Test

## Business

- Capability
- Policy
- Event
- Snapshot
- Business Scenario

## Operational

- Logging
- Monitoring
- Metrics
- Alert
- Runbook (nếu áp dụng)

---

# 13. Change Control

AI không được thay đổi:

- BRD
- Business Registry
- Architecture Baseline
- Sprint Contract

Mọi thay đổi phải thông qua:

- Architecture Change Proposal (ACP)
- Architecture Review
- Approval

---

# 14. AI Collaboration Principles

AI phải:

- tuân thủ Sprint Contract;
- tuân thủ Registry;
- tuân thủ Engineering Standards;
- sinh báo cáo khi phát hiện bất thường;
- đề xuất thay đổi thay vì tự thay đổi.

AI không được tự định nghĩa Business hoặc Architecture.

---

# 15. Sprint Completion

Một Sprint chỉ được hoàn thành khi đồng thời đạt:

## Technical Done

- Build PASS
- Migration PASS
- Static Analysis PASS
- Test PASS

## Business Done

- Capability hoàn chỉnh
- Policy đúng
- Event đúng
- Snapshot đúng
- Acceptance Scenario PASS

## Operational Done

- Logging
- Monitoring
- Alert
- Metrics
- Feature Flag/Kill Switch (nếu yêu cầu)

Ngoài Source Code, Sprint phải tạo đầy đủ:

- Test
- Seed Data
- Documentation
- Validation Report
- Implementation Evidence

---

# 16. Framework Artifacts

YADF quản lý các nhóm tài liệu sau:

| Artifact | Purpose |
|----------|---------|
| Business Requirements | Định nghĩa yêu cầu nghiệp vụ |
| Enterprise Registries | Source of Truth cho kiến trúc nghiệp vụ |
| Architecture Baseline Pack | Chuẩn kiến trúc nền tảng |
| Domain Implementation Pack | Hướng dẫn triển khai theo Domain |
| Engineering Standards Pack | Quy chuẩn kỹ thuật |
| Sprint Governance Pack | Quản trị Sprint |
| Verification & Acceptance Pack | Kiểm thử và nghiệm thu |
| Operations Readiness Pack | Vận hành và triển khai |

---

# 17. Framework Principles

1. Business drives Architecture.
2. Architecture governs Implementation.
3. Sprint Contract governs Execution.
4. AI implements, never defines Architecture.
5. Every Sprint must be traceable.
6. Every Sprint must be verifiable.
7. Every Sprint must produce Implementation Evidence.
8. Every Release must be operationally ready.
9. Every Architecture change must be approved.
10. One Source of Truth for every architectural concern.

---

# Document Status

**Status: FROZEN**

YADF là framework chuẩn cho toàn bộ hoạt động phát triển phần mềm của nền tảng YSim.

Mọi dự án, Sprint, AI Coding Assistant và quy trình triển khai phải tuân thủ YADF nhằm đảm bảo tính nhất quán, khả năng truy vết và chất lượng của toàn bộ hệ sinh thái YSim.

---
