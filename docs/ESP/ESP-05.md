---
document_code: ESP-05
document_name: Data Persistence Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Data Persistence Standards

## ESP-05

---

# 1. Purpose

Data Persistence Standards định nghĩa các tiêu chuẩn thiết kế, triển khai và quản lý tầng lưu trữ dữ liệu của nền tảng YSim.

Persistence bao gồm:

- Relational Database
- Cache
- Object Storage
- Search Index
- Queue Persistence
- Snapshot Storage

Tiêu chuẩn này đảm bảo dữ liệu được lưu trữ nhất quán, an toàn và có khả năng mở rộng.

---

# 2. Principles

Persistence tuân thủ các nguyên tắc:

- Domain Driven
- Single Source of Truth
- Explicit Persistence
- Transaction Safe
- Consistent
- Auditable
- Scalable
- Technology Agnostic
- Full-stack Data Model
- Experience-aware Persistence

---

# 3. Persistence Objectives

Persistence phải:

- phản ánh Domain Model;
- phản ánh Business Object;
- hỗ trợ Transaction;
- hỗ trợ Traceability;
- hỗ trợ Audit;
- hỗ trợ Backup & Recovery.
- hỗ trợ Experience Composition và Capability Demonstration.

Persistence không quyết định Business Logic.

---

# 4. Persistence Architecture

```text
Application
        │
Repository
        │
Persistence Layer
        │
Storage Engine
```

Business Logic không được truy cập Storage trực tiếp.

---

# 5. Persistence Classification

Platform chuẩn hóa các loại Persistence.

| Type | Purpose |
|-------|----------|
| Relational Database | Transactional Data |
| Cache | High-speed Access |
| Object Storage | Binary Files |
| Search Index | Full-text Search |
| Queue Storage | Message Persistence |
| Snapshot Store | Historical State |
| Experience Cache | Storefront / Portal Experience Cache |

Mỗi loại Persistence có trách nhiệm riêng.

---

# 5A. Experience Persistence

Đối với các Capability có giao diện người dùng, Persistence có thể cung cấp thêm các mô hình dữ liệu tối ưu cho Experience.

Bao gồm:

- Experience Cache
- Read Model
- View Model
- Aggregated Projection

Các mô hình này không được thay thế Domain Model và không phải là Source of Truth.


---

# 6. Relational Database Standards

Relational Database dùng cho:

- Business Transaction
- Master Data
- Reference Data
- Configuration Data

Database phải phản ánh Domain Model.

Không thiết kế theo UI.

---

# 7. Entity Standards

Entity phải:

- đại diện Business Object;
- có Identity ổn định;
- có Lifecycle rõ ràng.

Không tạo Entity chỉ để phục vụ một màn hình giao diện.

---

# 8. Primary Key Standards

Primary Key:

- sử dụng UUID hoặc định danh theo chuẩn dự án;
- không sử dụng Business Value làm Primary Key.

Ví dụ:

```text
id
```

---

# 9. Foreign Key Standards

Foreign Key:

```text
customer_id

order_id

package_id
```

Quan hệ phải phản ánh Domain.

Không tạo quan hệ vòng (Circular Relationship).

---

# 10. Repository Pattern

Persistence chỉ được truy cập thông qua Repository.

```text
Application

↓

Repository

↓

Database
```

Controller không truy cập Database.

Integration Adapter không ghi trực tiếp vào Domain Database.

---

# 11. Transaction Standards

Transaction:

- ngắn;
- rõ ràng;
- có phạm vi xác định;
- rollback được.

Không thực hiện gọi dịch vụ bên ngoài trong Transaction nếu có thể tránh.

---

# 12. Soft Delete

Business Object mặc định ưu tiên:

- Soft Delete

Bao gồm:

```text
deleted_at

deleted_by
```

Hard Delete chỉ áp dụng khi được Business và Architecture phê duyệt.

---

# 13. Audit Fields

Mọi Entity nghiệp vụ nên có:

```text
created_at

created_by

updated_at

updated_by

version
```

Nếu áp dụng Soft Delete thì bổ sung:

```text
deleted_at

deleted_by
```

---

# 14. Cache Standards

Cache chỉ lưu:

- Read Model
- Session
- Temporary Data
- Derived Data

Cache không là nguồn dữ liệu chính.

Experience Cache chỉ lưu dữ liệu tổng hợp phục vụ Portal, Storefront và Capability Demonstration.

Cache phải có chính sách TTL và Invalidaton rõ ràng.

---

# 15. Object Storage Standards

Object Storage dùng cho:

- QR Images
- Attachments
- Reports
- Export Files
- Documents

Database chỉ lưu Metadata và Reference.

Không lưu Binary lớn trực tiếp trong Database trừ khi có lý do đặc biệt.

---

# 16. Search Index Standards

Search Index:

- đồng bộ từ Business Data;
- có khả năng Rebuild;
- không là Source of Truth.

---

# 17. Snapshot Persistence

Snapshot:

- bất biến sau khi tạo;
- có Timestamp;
- có Version;
- có Traceability.

Snapshot phục vụ Audit và Historical View.

---

# 18. Data Integrity

Persistence phải đảm bảo:

- Referential Integrity
- Uniqueness
- Consistency
- Optimistic Locking (khi phù hợp)
- Idempotency (đối với các nghiệp vụ yêu cầu)

---

# 19. Prohibited Practices

Không được:

- Business Logic trong SQL.
- Controller truy cập Database.
- Hardcode SQL trong Controller.
- Circular Foreign Key.
- Duplicate Master Data.
- Lưu Secret ở dạng rõ (plaintext).

---

# 20. Persistence Rules

DP-001 — Persistence phản ánh Domain.

DP-002 — Repository là điểm truy cập chuẩn.

DP-003 — Transaction phải rõ phạm vi.

DP-004 — Cache không là Source of Truth.

DP-005 — Object Storage lưu Binary.

DP-006 — Snapshot bất biến.

DP-007 — Entity phải có Audit Fields.

DP-008 — Persistence phải hỗ trợ Traceability.

DP-009 — AI phải tuân thủ Persistence Standards.

DP-010 — Không truy cập Database trực tiếp từ Presentation Layer.

DP-011 — Experience Persistence không được chứa Business Logic.

DP-012 — Read Model phải được đồng bộ từ Domain Model.

---

# 21. Persistence Compliance Checklist

| Rule | Validation |
|------|------------|
| DPC-0501 | Repository Pattern được áp dụng |
| DPC-0502 | Entity phản ánh Domain |
| DPC-0503 | Primary Key đúng chuẩn |
| DPC-0504 | Transaction đúng phạm vi |
| DPC-0505 | Audit Fields đầy đủ |
| DPC-0506 | Cache sử dụng đúng mục đích |
| DPC-0507 | Object Storage tách khỏi Database |
| DPC-0508 | Snapshot bất biến |
| DPC-0509 | Data Integrity được đảm bảo |
| DPC-0510 | Persistence tuân thủ ESP |
| DPC-0511 | Experience Persistence đúng chuẩn |
| DPC-0512 | Read Model đồng bộ Domain |

---

# 22. Relationship to Other Documents

ESP-05 liên kết với:

- ESP-02 Source Code Engineering Standards
- ESP-03 Enterprise Naming Standards
- ESP-04 API Engineering Standards
- ESP-06 Migration Standards
- ABP-04 Domain Architecture
- ABP-07 Data Architecture
- DBD (Database Design Documents)

Data Persistence Standards là tiêu chuẩn thống nhất cho toàn bộ tầng lưu trữ dữ liệu của nền tảng YSim, bao gồm Domain Persistence và Experience Persistence phục vụ Full-stack Capability Delivery.

---

# 23. Document Status

**Status: FROZEN**

ESP-05 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn thiết kế và triển khai tầng lưu trữ dữ liệu của YSim.

Mọi cơ chế lưu trữ dữ liệu phải tuân thủ tài liệu này.

---