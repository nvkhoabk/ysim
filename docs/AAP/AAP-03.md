---
document_code: AAP-03
document_name: AI Planning Model
project: YSim v2.1
document_set: AI Architecture Pack
version: 2.1
status: FROZEN
language: en-US
---

# AI Planning Model

## AAP-03

---

# 1. Purpose

AI Planning Model định nghĩa mô hình lập kế hoạch triển khai Sprint của AI.

Planning là bước trung gian giữa:

- Repository Discovery
- Code Generation

AI không được sinh mã nguồn trước khi hoàn thành Planning.

---

# 2. Principles

Planning tuân thủ các nguyên tắc:

- Contract First
- Dependency First
- Architecture Safe
- Incremental
- Deterministic
- Evidence Driven
- Full-stack Planning
- Experience-oriented Planning

Planning không được thay đổi Sprint Contract.

Planning chỉ xác định phương án triển khai.

---

# 3. Planning Objectives

Planning nhằm:

- xác định thứ tự triển khai;
- xác định Dependency;
- xác định phạm vi thay đổi;
- giảm rủi ro;
- tối đa khả năng tái sử dụng;
- đảm bảo tuân thủ Architecture.

---

# 4. Planning Inputs

Planning sử dụng:

- Sprint Contract
- Repository Discovery Report
- Dependency Graph
- Module Inventory
- Architecture Baseline
- Engineering Standards

Không sử dụng Prompt tự do làm nguồn quyết định.

---

# 5. Planning Outputs

Planning tạo:

- Sprint Execution Plan
- Task Graph
- Dependency Graph
- Risk Assessment
- Validation Plan
- Demonstration Plan
- Evidence Plan

Đây là đầu vào của Code Generation.

---

# 6. Planning Dimensions

AI phải lập kế hoạch trên các khía cạnh sau.

| Dimension | Description |
|------------|-------------|
| Business | Capability, Scope |
| Architecture | Module, Layer |
| Dependency | Module, Event, API |
| Data | Migration, Snapshot |
| Integration | Connector, Gateway |
| Security | Permission |
| Testing | Test Strategy |
| Operations | Logging, Monitoring |
| Frontend | Pages, Components, Routes |
| Experience | Design System, Demonstration Surface |

---

# 7. Task Decomposition

Sprint được chia thành các Task nhỏ.

Ví dụ:

```text
Capability

↓

Migration

↓

Domain

↓

Application

├── API

├── Backend Services

├── Frontend Pages

├── UI Components

├── Seed Data

├── Demonstration

├── Tests

└── Documentation
```

Task phải có Dependency rõ ràng.

---

# 7A. Full-stack Task Planning

Planning phải tạo Work Package đồng bộ cho từng Capability.

Mỗi Capability có giao diện người dùng phải được phân rã tối thiểu thành:

- Backend
- API
- Frontend
- Design System Integration
- Seed Data
- Capability Demonstration
- Testing
- Documentation

Không được lập kế hoạch chỉ cho Backend nếu Capability yêu cầu Experience.

---

# 8. Task Graph

Planning xây dựng Task Graph.

```text
Migration
      │
      ▼
Domain
      │
      ▼
Application
      │
      ├── API
      ├── Event
      └── Tests
```

Task Graph là Directed Acyclic Graph (DAG).

Không cho phép Circular Task Dependency.

---

# 9. Dependency Resolution

Planning phải phân loại Dependency.

| Type | Strategy |
|------|----------|
| Existing | Reuse |
| Missing | Implement |
| External | Mock hoặc Wait |
| Architecture | ACP |

Planning không được bỏ qua Dependency.

---

# 10. Risk Assessment

Planning đánh giá:

- Architecture Risk
- Technical Risk
- Dependency Risk
- Integration Risk
- Testing Risk

Risk được ghi trong Sprint Plan.

---

# 11. Parallel Planning

AI được phép thực hiện song song khi:

- không vi phạm Dependency;
- không thay đổi cùng một Module;
- không vi phạm Ownership.

Planning phải chỉ rõ các Task có thể chạy song song.

---

# 12. Validation Planning

Planning xác định:

- Unit Test
- Contract Test
- Integration Test
- Scenario Test
- Security Validation

Validation được lập kế hoạch trước khi Code Generation.

---

# 13. Evidence Planning

Planning xác định Evidence cần tạo.

Ví dụ:

- Migration
- Tests
- Validation
- Documentation
- Reports

Evidence không được sinh sau khi kết thúc Sprint.

---

# 14. Architecture Constraints

Planning phải kiểm tra:

- Module Boundary
- Dependency Rules
- Transaction Boundary
- Event Rules
- Snapshot Rules
- Security Rules

Nếu vi phạm:

↓

Architecture Change Proposal.

---

# 15. Planning Rules

PM-001 — Planning là bắt buộc.

PM-002 — Planning sau Discovery.

PM-003 — Planning trước Code Generation.

PM-004 — Task Graph phải là DAG.

PM-005 — Dependency phải được giải quyết.

PM-006 — Validation được lập kế hoạch trước.

PM-007 — Evidence được lập kế hoạch trước.

PM-008 — Không thay đổi Sprint Contract.

PM-009 — Không thay đổi Architecture.

PM-010 — ACP thay thế việc tự sửa Architecture.

---

# 16. AI Planning Resolution Pipeline (APRP)

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
Task Decomposition
        │
        ▼
Task Graph
        │
        ▼
Risk Assessment
        │
        ▼
Capability Demonstration Planning
        │
        ▼
Validation Planning
        │
        ▼
Evidence Planning
        │
        ▼
Sprint Execution Plan
```

Planning Resolution Pipeline là đầu vào trực tiếp cho AI Code Generation.

---

# 17. Planning Evidence

Planning phải sinh:

- Sprint Execution Plan
- Task Graph
- Dependency Matrix
- Risk Report
- Validation Plan
- Demonstration Plan
- Evidence Plan

Planning hoàn thành trước khi Code Generation bắt đầu.

---

# 18. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0301 | Planning hoàn thành |
| ACC-0302 | Task Graph hợp lệ |
| ACC-0303 | Không có Circular Dependency |
| ACC-0304 | Dependency được phân loại |
| ACC-0305 | Validation Plan đầy đủ |
| ACC-0306 | Evidence Plan đầy đủ |
| ACC-0307 | Architecture Constraints được kiểm tra |
| ACC-0308 | Risk Assessment hoàn thành |
| ACC-0309 | Sprint Execution Plan được tạo |
| ACC-0310 | Không thay đổi Sprint Contract |

---

# 19. Relationship to Other Documents

AAP-03 liên kết với:

- AAP-01 Repository Discovery Model
- AAP-02 Sprint Contract Model
- ABP-03 Dependency Rules
- ABP-15 AI Implementation Architecture
- Sprint Governance Pack (SGP)

Planning là cầu nối giữa Discovery và Full-stack Code Generation, bảo đảm Backend, Frontend và Capability Demonstration được lập kế hoạch đồng thời.

---

# 20. Document Status

**Status: FROZEN**

AAP-03 là tài liệu nền tảng quy định mô hình lập kế hoạch triển khai của AI.

Mọi AI Coding Assistant phải hoàn thành Planning trước khi sinh mã nguồn.

---