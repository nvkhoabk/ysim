---
document_code: AAP-01
document_name: Repository Discovery Model
project: YSim v2.1
document_set: AI Architecture Pack
version: 2.1
status: FROZEN
language: en-US
---

# Repository Discovery Model

## AAP-01

---

# 1. Purpose

Repository Discovery Model định nghĩa mô hình khám phá Repository trước khi AI thực hiện bất kỳ Sprint nào.

Repository Discovery là bước bắt buộc.

AI không được phép sinh mã nguồn nếu chưa hoàn thành Repository Discovery.

Repository Discovery giúp AI:

- hiểu kiến trúc hiện tại;
- xác định phạm vi Sprint;
- tránh tạo mã nguồn trùng lặp;
- tránh phá vỡ Architecture Baseline.

---

# 2. Principles

Repository Discovery tuân thủ các nguyên tắc:

- Repository First
- Read Before Write
- Architecture First
- Contract First
- Incremental Discovery
- Evidence Driven
- Full-stack Discovery
- Experience-aware Discovery

Repository Discovery không thay đổi Repository.

Repository Discovery chỉ thu thập tri thức.

---

# 3. Discovery Scope

AI phải khám phá tối thiểu các nhóm sau.

| Area | Description |
|--------|-------------|
| Applications | apps/ |
| Modules | packages/ |
| Shared Libraries | packages/shared |
| Database | schema, migration |
| APIs | REST, GraphQL, Internal |
| Events | Published & Subscribed |
| Snapshots | Business Snapshots |
| Configuration | Runtime Configuration |
| Integration | Gateway, Connector, Adapter |
| Tests | Existing Test Assets |
| Documentation | BRD, ABP, DIP, ESP... |
| Frontend | Portal, Storefront, Components, Routes |
| Design System | Tokens, Themes, Components |

---

# 4. Discovery Objectives

Repository Discovery nhằm trả lời:

- Có Module nào đã tồn tại?
- Capability này đã được triển khai chưa?
- Có API tương tự không?
- Có Event tương tự không?
- Có Snapshot tương tự không?
- Có Migration liên quan không?
- Có Test hiện có không?
- Có Frontend tương ứng không?
- Có Capability Demonstration hiện có không?
- Có Technical Debt nào ảnh hưởng Sprint không?

---

# 5. Discovery Layers

Repository được khám phá theo các tầng.

```text
Documentation

↓

Architecture

↓

Modules

↓

Contracts

↓

Implementation

↓

Frontend Experience

↓

Tests

↓

Infrastructure
```

Không khám phá ngẫu nhiên.

---

# 6. Discovery Order

AI phải thực hiện Discovery theo trình tự.

```text
Sprint Contract

↓

Documentation

↓

Registry

↓

ABP

↓

Repository Structure

↓

Module Discovery

↓

Dependency Discovery

↓

Contract Discovery

↓

Implementation Discovery

↓

Frontend Discovery

↓

Capability Demonstration Discovery

↓

Test Discovery

↓

Gap Analysis
```

---

# 7. Module Discovery

AI phải xác định:

- Module Name
- Module Owner
- Domain
- Public API
- Published Event
- Consumed Event
- Dependencies
- Status

Không tạo Module nếu Module đã tồn tại.

---

# 8. Contract Discovery

AI phải khám phá:

- API Contract
- Event Contract
- Snapshot Contract
- Configuration Contract
- Permission Contract

Contract luôn được ưu tiên hơn Source Code.

---

# 9. Dependency Discovery

AI phải xây dựng Dependency Graph.

Bao gồm:

- Module Dependency
- Event Dependency
- API Dependency
- Configuration Dependency
- Integration Dependency

Circular Dependency phải được báo cáo.

---

# 10. Implementation Discovery

AI xác định:

- Existing Service
- Repository
- Worker
- Scheduler
- Queue
- Connector
- Adapter

Không sinh lại thành phần đã tồn tại.

---

# 11. Database Discovery

AI khám phá:

- Schema
- Entity
- Migration
- Seed
- Index
- Constraint

Migration cũ không được sửa.

---

# 12. Test Discovery

AI xác định:

- Unit Test
- Contract Test
- Integration Test
- Scenario Test
- Performance Test

Nếu thiếu Test phải ghi nhận.

---

# 12A. Frontend Discovery

AI phải khám phá đầy đủ Frontend trước khi lập kế hoạch triển khai.

Bao gồm:

- Portal hiện có
- Storefront hiện có
- Routes
- Pages
- Components
- Design Tokens
- Theme
- State Management
- API Client
- Capability Demonstration Surface

Repository Discovery chỉ hoàn thành khi AI hiểu đầy đủ cả Backend và Frontend của Capability.

---

# 13. Gap Analysis

Sau Discovery AI phải sinh Gap Analysis.

Bao gồm:

- Existing Capability
- Missing Capability
- Reusable Component
- Missing Dependency
- Architecture Risk
- Suggested Scope

Gap Analysis không được tự thay đổi Sprint.

---

# 14. Discovery Output

Repository Discovery sinh các Artifact.

- Discovery Report
- Module Inventory
- Dependency Graph
- Contract Inventory
- Gap Analysis
- Frontend Inventory
- Capability Demonstration Inventory
- Architecture Risk Report

Đây là đầu vào cho Sprint Planning.

---

# 15. Discovery Rules

RD-001 — Discovery là bắt buộc.

RD-002 — Documentation được đọc trước Source Code.

RD-003 — Registry được ưu tiên.

RD-004 — Contract được ưu tiên hơn Implementation.

RD-005 — Không sửa Repository trong Discovery.

RD-006 — Mọi Dependency phải được phát hiện.

RD-007 — Mọi Gap phải được báo cáo.

RD-008 — Không tạo Module nếu đã tồn tại.

RD-009 — Discovery phải sinh Evidence.

RD-010 — Discovery hoàn thành trước Code Generation.

RD-011 — Frontend Discovery là bắt buộc đối với Capability có giao diện.

RD-012 — Capability Demonstration phải được phát hiện hoặc lập kế hoạch.

---

# 16. Repository Knowledge Graph

Repository được mô hình hóa thành Knowledge Graph.

```text
Business Requirement

↓

Capability

↓

Business Object

↓

Module

↓

API

↓

Frontend Experience

↓

Event

↓

Snapshot

↓

Database

↓

Tests
```

AI sử dụng Knowledge Graph để xác định phạm vi ảnh hưởng của Sprint.

---

# 17. Discovery Resolution Pipeline (DiRP)

```text
Sprint Contract
        │
        ▼
Documentation Discovery
        │
        ▼
Registry Discovery
        │
        ▼
Architecture Discovery
        │
        ▼
Repository Discovery
        │
        ▼
Dependency Discovery
        │
        ▼
Contract Discovery
        │
        ▼
Gap Analysis
        │
        ▼
Discovery Evidence
```

Discovery Resolution Pipeline là Pipeline bắt buộc trước mọi Sprint.

---

# 18. Discovery Evidence

Repository Discovery phải sinh tối thiểu:

- Discovery Report
- Module Inventory
- Contract Inventory
- Dependency Graph
- Gap Analysis
- Risk Report

Đây là điều kiện để chuyển sang Sprint Planning.

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0101 | Repository Discovery hoàn thành |
| ACC-0102 | Documentation được đọc trước |
| ACC-0103 | Registry được sử dụng |
| ACC-0104 | Module Inventory đầy đủ |
| ACC-0105 | Dependency Graph được tạo |
| ACC-0106 | Contract Inventory đầy đủ |
| ACC-0107 | Gap Analysis hoàn thành |
| ACC-0108 | Risk Report được sinh |
| ACC-0109 | Discovery không thay đổi Repository |
| ACC-0110 | Discovery Evidence đầy đủ |

---

# 20. Relationship to Other Documents

AAP-01 liên kết với:

- YADF
- ABP-01 Repository Architecture
- ABP-02 Module Architecture
- ABP-03 Dependency Rules
- ABP-15 AI Implementation Architecture
- Sprint Governance Pack (SGP)

Repository Discovery là điểm khởi đầu của mọi Sprint và là cơ sở để AI lập kế hoạch Full-stack Capability Delivery.

---

# 21. Document Status

**Status: FROZEN**

AAP-01 là tài liệu nền tảng quy định mô hình Repository Discovery cho AI.

Mọi AI Coding Assistant phải hoàn thành Repository Discovery trước khi lập kế hoạch hoặc sinh mã nguồn.

---