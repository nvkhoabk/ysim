---
document_code: ABP-02
document_name: Module Architecture
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Module Architecture

## ABP-02

---

# 1. Purpose

Module Architecture định nghĩa cấu trúc chuẩn của một Module trong nền tảng YSim.

Mục tiêu:

- Chuẩn hóa Module Structure.
- Chuẩn hóa Layering.
- Chuẩn hóa Dependency.
- Chuẩn hóa Ownership.
- Chuẩn hóa Runtime Boundary.
- Chuẩn hóa AI Implementation.

Module là đơn vị triển khai nhỏ nhất của Platform.

---

# 2. Module Principles

Mọi Module phải tuân thủ các nguyên tắc sau:

- Single Responsibility
- High Cohesion
- Low Coupling
- Contract First
- Domain Ownership
- Event Driven
- Testable
- Observable

---

# 3. Module Definition

Module là một đơn vị triển khai độc lập, chịu trách nhiệm hiện thực một hoặc nhiều **Business Capability** có liên quan trong cùng một **Business Domain**.

Một Module:

- Có Ownership riêng.
- Có API riêng (nếu cần).
- Có Event riêng.
- Có Test riêng.
- Có Documentation riêng.
- Có Lifecycle riêng.

---

# 4. Module Layering

Mỗi Module sử dụng cấu trúc phân lớp chuẩn.

```text
Module

├── Application
├── Domain
├── Infrastructure
└── Interface
```

Không được bổ sung Layer mới nếu chưa được Architecture Review.

---

# 5. Application Layer

Application Layer chịu trách nhiệm:

- Use Cases
- Command
- Query
- Orchestration
- Transaction Boundary
- Permission Check

Application Layer không chứa Business Persistence.

---

# 6. Domain Layer

Domain Layer là trung tâm của Module.

Bao gồm:

- Aggregate
- Entity
- Value Object
- Domain Service
- Domain Event
- Domain Policy
- Domain Validation

Domain Layer không phụ thuộc Infrastructure.

---

# 7. Infrastructure Layer

Infrastructure Layer hiện thực các thành phần kỹ thuật.

Ví dụ:

- Repository
- ORM
- External Connector
- Queue Adapter
- Cache
- Storage
- Mail
- Payment Gateway Adapter

Infrastructure không chứa Business Decision.

---

# 8. Interface Layer

Interface Layer cung cấp điểm truy cập vào Module.

Ví dụ:

- REST Controller
- GraphQL Resolver
- Message Consumer
- Scheduler Entry
- CLI
- Admin Endpoint

Interface chỉ chuyển tiếp yêu cầu vào Application Layer.

---

# 9. Module Folder Structure

Ví dụ:

```text
payment/

application/
domain/
infrastructure/
interface/
tests/
docs/
```

Không đặt Business Logic ngoài Module.

---

# 10. Module Ownership

Mỗi Module có Ownership rõ ràng.

Ownership bao gồm:

- Business Owner
- Architecture Owner
- Sprint Ownership
- Source Code Ownership

Không có Module "không chủ".

---

# 11. Module Contract

Mỗi Module công bố Contract.

Contract có thể gồm:

- Public API
- Published Events
- Consumed Events
- Configuration
- Permissions
- Error Codes

Module khác chỉ được sử dụng Contract công khai.

---

# 12. Module Communication

Các Module giao tiếp thông qua:

- API
- Event
- Shared Contract

Không truy cập trực tiếp Internal Implementation của Module khác.

---

# 13. Module Dependency Rules

Module chỉ được phụ thuộc:

- Shared Kernel
- Public Contract của Module khác
- Platform Services

Không phụ thuộc trực tiếp vào:

- Database của Module khác
- Internal Repository
- Internal Service
- Internal Entity

---

# 14. Module Lifecycle

Mỗi Module có Lifecycle.

```text
Design

↓

Implementation

↓

Testing

↓

Release

↓

Maintenance

↓

Deprecation

↓

Retirement
```

---

# 15. Module Observability

Mọi Module phải hỗ trợ:

- Logging
- Metrics
- Health Check
- Trace ID
- Audit (nếu áp dụng)

Observability là yêu cầu bắt buộc.

---

# 16. Module Testability

Mỗi Module phải có:

- Unit Test
- Contract Test
- Integration Test (nếu cần)

Business Scenario Test được thực hiện ở mức Sprint.

---

# 17. Module Versioning

Module hỗ trợ Version.

Breaking Change phải:

- Version.
- Migration.
- Approval.

Không thay đổi Public Contract trực tiếp.

---

# 18. AI Implementation Rules

AI chỉ được triển khai trong phạm vi Module.

AI không được:

- tạo Module mới;
- thay đổi Module Boundary;
- thay đổi Ownership.

Nếu cần thay đổi:

→ Architecture Change Proposal.

---

# 19. Module Principles

MA-001 — One Module, One Responsibility.

MA-002 — Business Logic belongs to Domain Layer.

MA-003 — Application orchestrates.

MA-004 — Infrastructure implements technology.

MA-005 — Interface exposes contracts.

MA-006 — Module owns its data.

MA-007 — Module communicates by contract.

MA-008 — Module publishes events.

MA-009 — Module is independently testable.

MA-010 — Module is independently deployable (when architecture allows).

---

# 20. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0201 | Module có Ownership rõ ràng |
| ACC-0202 | Business Logic chỉ nằm trong Domain Layer |
| ACC-0203 | Application Layer không truy cập trực tiếp Infrastructure của Module khác |
| ACC-0204 | Infrastructure không chứa Business Rule |
| ACC-0205 | Interface không chứa Business Logic |
| ACC-0206 | Module chỉ sử dụng Public Contract |
| ACC-0207 | Module có Logging, Metrics và Health Check |
| ACC-0208 | Module có Test tối thiểu theo chuẩn YADF |
| ACC-0209 | Module công bố đầy đủ API/Event Contract |
| ACC-0210 | Module tuân thủ Domain Ownership |

Checklist này được sử dụng trong:

- Architecture Review.
- Code Review.
- AI Review.
- CI/CD Validation.

---

# 21. Document Status

**Status: FROZEN**

ABP-02 là tài liệu nền tảng quy định kiến trúc chuẩn của mọi Module trong nền tảng YSim.

Mọi Module mới phải tuân thủ tài liệu này trước khi được đưa vào triển khai hoặc phát hành.

---