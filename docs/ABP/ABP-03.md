---
document_code: ABP-03
document_name: Dependency Rules
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Dependency Rules

## ABP-03

---

# 1. Purpose

Dependency Rules định nghĩa các quy tắc phụ thuộc giữa các Module trong nền tảng YSim.

Mục tiêu:

- loại bỏ Circular Dependency;
- chuẩn hóa Module Communication;
- đảm bảo Domain Boundary;
- đảm bảo Repository Discoverability;
- đảm bảo AI Implementation nhất quán.

Dependency Rules là một phần của Architecture Constitution.

---

# 2. Principles

Dependency phải tuân thủ:

- One Direction
- Contract First
- Domain Ownership
- Explicit Dependency
- No Hidden Dependency

Không được phụ thuộc ngầm.

---

# 3. Dependency Types

Platform định nghĩa bốn loại Dependency.

| Type | Description |
|-------|-------------|
| Compile Dependency | Import Source Code |
| Runtime Dependency | Runtime Invocation |
| Event Dependency | Publish / Subscribe |
| Shared Contract Dependency | DTO / Interface / Contract |

Mỗi Dependency phải được xác định rõ loại.

---

# 4. Layer Dependency

Dependency giữa các Layer.

```text
Presentation
        │
        ▼
Application
        │
        ▼
Domain
        │
        ▼
Infrastructure
        │
        ▼
Platform
```

Không được phụ thuộc ngược.

---

# 5. Module Dependency

Module chỉ được phụ thuộc:

- Shared Kernel
- Public Contract
- Platform Service

Không được Import:

- Internal Entity
- Internal Repository
- Internal Service
- Internal Database

---

# 6. Domain Ownership

Domain sở hữu:

- Business Object
- Event
- Policy
- Snapshot
- API

Module khác không được sửa.

---

# 7. Communication Rules

Module chỉ giao tiếp qua:

- REST API
- Internal API
- Event
- Queue
- Shared Contract

Không được truy cập trực tiếp Database của Module khác.

---

# 8. Shared Kernel Rules

Shared Kernel chỉ chứa:

- Base Types
- Common Interface
- Common Exception
- Utility
- Result Object

Không chứa:

- Business Rule
- Business Service
- Domain Entity

---

# 9. Integration Rules

Integration luôn thông qua:

```text
Business Module

↓

Gateway

↓

Connector

↓

External System
```

Business Module không gọi Supplier trực tiếp.

---

# 10. Event Dependency

Business Event là Dependency yếu (Loose Coupling).

Publisher không biết Subscriber.

Subscriber đăng ký Event.

Không được gọi ngược Publisher.

---

# 11. API Dependency

API chỉ được gọi:

- Public API
- Versioned API

Không gọi Internal Endpoint.

---

# 12. Database Dependency

Database Ownership thuộc Module.

Module khác:

- không SELECT trực tiếp;
- không UPDATE trực tiếp;
- không JOIN trực tiếp.

Trao đổi dữ liệu thông qua Contract.

---

# 13. Configuration Dependency

Configuration được đọc qua Configuration Service.

Không đọc trực tiếp Database.

Không Hard-code.

---

# 14. Security Dependency

Security Module được phép được tất cả Module sử dụng.

Security không phụ thuộc Business Domain.

---

# 15. Logging Dependency

Logging thông qua Logging Framework.

Không gọi Logger của Module khác.

---

# 16. Notification Dependency

Business Module Publish Event.

Notification Subscribe Event.

Business Module không gửi Notification trực tiếp.

---

# 17. Analytics Dependency

Analytics đọc:

- Snapshot
- Event
- Reporting View

Không đọc Runtime Database để tạo báo cáo.

---

# 18. Dependency Matrix

| From | Allowed |
|------|---------|
| Commercial | Shared, Configuration, Security, Integration |
| Order | Commercial, Shared, Configuration |
| Payment | Order (Contract), Commercial (Contract), Shared |
| Inventory | Order (Contract), Shared |
| Fulfillment | Inventory, Payment (Contract), Shared |
| Notification | Event Bus, Shared |
| Analytics | Snapshot, Event, Reporting View |
| Configuration | Shared |
| Security | Shared |
| Operations | Shared |

Mọi Dependency khác phải được Architecture Review.

---

# 19. Forbidden Dependencies

Không được:

- Circular Dependency
- Cross Database Query
- Shared Entity
- Shared Repository
- Business Logic trong Shared
- Module gọi Internal Service của Module khác

---

# 20. AI Dependency Rules

AI không được:

- tạo Dependency mới;
- Import Internal Module;
- Bypass Contract;
- tạo Circular Dependency.

Nếu cần:

↓

Architecture Change Proposal.

---

# 21. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0301 | Không có Circular Dependency |
| ACC-0302 | Không Import Internal Module |
| ACC-0303 | Không Cross Database Query |
| ACC-0304 | Chỉ dùng Public Contract |
| ACC-0305 | Event tuân thủ Event Registry |
| ACC-0306 | Shared Kernel không chứa Business Logic |
| ACC-0307 | Module Ownership không bị vi phạm |
| ACC-0308 | Integration thông qua Gateway |
| ACC-0309 | Configuration không Hard-code |
| ACC-0310 | Dependency Matrix được tuân thủ |

Checklist này được sử dụng bởi:

- Architecture Review
- AI Review
- CI/CD Validation
- Code Review

---

# 22. Document Status

**Status: FROZEN**

ABP-03 quy định toàn bộ Dependency Rules của nền tảng YSim.

Mọi Module, Sprint và AI Implementation phải tuân thủ các quy tắc trong tài liệu này.

---