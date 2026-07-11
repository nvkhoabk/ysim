---
document_code: ESP-06
document_name: Migration Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Migration Standards

## ESP-06

---

# 1. Purpose

Migration Standards định nghĩa các tiêu chuẩn thiết kế, triển khai và quản lý Database Migration trong nền tảng YSim.

Migration là một Engineering Artifact.

Mọi thay đổi đối với cấu trúc dữ liệu phải được quản lý thông qua Migration.

Không được thay đổi Schema trực tiếp trên môi trường.

---

# 2. Principles

Migration tuân thủ các nguyên tắc:

- Migration First
- Immutable
- Incremental
- Repeatable
- Versioned
- Auditable
- Rollback Aware
- Full-stack Migration
- Experience-safe Evolution

---

# 3. Objectives

Migration phải:

- phản ánh thay đổi Domain Model;
- có khả năng chạy nhiều môi trường;
- hỗ trợ CI/CD;
- hỗ trợ Audit;
- hỗ trợ Rollback (khi khả thi).

---

# 4. Migration Scope

Migration bao gồm:

- Schema Changes
- Table Creation
- Column Changes
- Constraint Changes
- Index Changes
- View Changes
- Function Changes
- Seed Data (nếu được định nghĩa)
- Experience Read Models
- Experience Cache Structures

Migration không được chứa Business Logic.

---

# 5. Migration Lifecycle

```text
Planned
    │
    ▼
Generated
    │
    ▼
Reviewed
    │
    ▼
Approved
    │
    ▼
Executed
    │
    ▼
Verified
    │
    ▼
Archived
```

Migration phải được quản lý như một Artifact.

---

# 6. Migration Naming

Tên Migration phải:

- duy nhất;
- có thứ tự;
- mô tả mục đích.

Ví dụ:

```text
20260715_create_customer_table

20260718_add_package_status

20260722_create_payment_index
```

Không sử dụng:

```text
migration1

update

fix
```

---

# 7. Migration Organization

Repository:

```text
database/

migrations/
seed/
fixtures/
```

Không lưu Migration ngoài thư mục chuẩn.

---

# 8. Schema Changes

Schema chỉ được thay đổi bằng Migration.

Không:

- ALTER trực tiếp trên Production;
- sửa Migration đã phát hành;
- bỏ qua Version.

---

# 8A. Experience Migration

Đối với Capability có giao diện người dùng, Migration có thể bao gồm:

- Read Model Schema
- View Model
- Experience Cache Structure
- Materialized View (nếu sử dụng)

Các thành phần này phải được tách biệt với Domain Schema và không được trở thành Source of Truth.

---

# 9. Seed Data

Seed Data chỉ dùng cho:

- Master Data
- Reference Data
- Demo Data (môi trường phù hợp)
- Capability Demonstration Data

Không sử dụng Seed để xử lý Business Transaction.

---

# 10. Backward Compatibility

Migration phải ưu tiên:

- Additive Changes
- Backward Compatibility
- Zero-Downtime (khi khả thi)

Ví dụ:

- thêm cột mới trước;
- triển khai mã nguồn tương thích;
- chỉ loại bỏ cột sau khi không còn sử dụng.

---

# 11. Data Transformation

Nếu cần chuyển đổi dữ liệu:

- phải có Migration riêng hoặc bước chuyển đổi được mô tả rõ;
- phải kiểm tra tính toàn vẹn dữ liệu;
- phải có khả năng chạy lặp an toàn nếu được thiết kế như vậy.

---

# 12. Rollback Strategy

Mỗi Migration phải xác định:

- Rollback Supported
- Rollback Limited
- Rollback Not Supported

Nếu không hỗ trợ Rollback phải nêu rõ lý do và phương án khôi phục.

---

# 13. Migration Review

Migration phải được Review về:

- Domain Impact
- Data Integrity
- Performance
- Compatibility
- Rollback Strategy

---

# 14. Migration Testing

Mỗi Migration phải được kiểm tra:

- chạy trên cơ sở dữ liệu mới;
- nâng cấp từ phiên bản trước;
- tính toàn vẹn dữ liệu;
- khả năng chạy trong Pipeline CI.

---

# 15. Production Execution

Migration Production phải:

- theo Release Plan;
- có Backup phù hợp;
- có Monitoring;
- có Verification sau khi chạy.

Không chạy Migration Production ngoài quy trình Release.

---

# 16. Prohibited Practices

Không được:

- sửa Migration đã Release;
- chạy SQL thủ công trên Production (trừ trường hợp khẩn cấp theo quy trình được phê duyệt);
- gộp nhiều thay đổi không liên quan vào một Migration;
- bỏ qua bước Review;
- phụ thuộc vào dữ liệu cục bộ của Developer.

---

# 17. Migration Rules

MG-001 — Mọi thay đổi Schema phải dùng Migration.

MG-002 — Migration là bất biến sau Release.

MG-003 — Migration phải có Version.

MG-004 — Migration phải được Review.

MG-005 — Migration phải được Test.

MG-006 — Migration phải được lưu trong Repository.

MG-007 — Migration phải hỗ trợ Audit.

MG-008 — Seed Data tách biệt Migration.

MG-009 — AI phải sinh Migration theo Standards.

MG-010 — Không thay đổi trực tiếp Database Production.

MG-011 — Experience Schema phải được Migration quản lý.

MG-012 — Demonstration Seed Data phải tách biệt Production Seed Data.

---

# 18. Migration Compliance Checklist

| Rule | Validation |
|------|------------|
| MCC-0601 | Migration có Version |
| MCC-0602 | Tên đúng chuẩn |
| MCC-0603 | Không sửa Migration đã Release |
| MCC-0604 | Review hoàn thành |
| MCC-0605 | Test hoàn thành |
| MCC-0606 | Rollback Strategy được xác định |
| MCC-0607 | Seed Data tách biệt |
| MCC-0608 | Migration lưu đúng Repository |
| MCC-0609 | Verification sau khi chạy |
| MCC-0610 | Tuân thủ ESP |
| MCC-0611 | Experience Migration đúng chuẩn |
| MCC-0612 | Demonstration Seed Data tách biệt |

---

# 19. Relationship to Other Documents

ESP-06 liên kết với:

- ESP-05 Data Persistence Standards
- ESP-07 Testing Standards
- ESP-15 Release Standards
- ABP-07 Data Architecture
- DBD (Database Design Documents)
- ROP (Release & Operations Pack)

Migration Standards là tiêu chuẩn thống nhất cho mọi thay đổi cấu trúc dữ liệu của nền tảng YSim, bao gồm Domain Migration, Experience Migration và Seed Data phục vụ Full-stack Capability Delivery.

---

# 20. Document Status

**Status: FROZEN**

ESP-06 là tài liệu chuẩn hóa quy trình thiết kế, kiểm thử và triển khai Database Migration của YSim.

Mọi thay đổi đối với Persistence Layer phải được thực hiện thông qua Migration theo tài liệu này.

---