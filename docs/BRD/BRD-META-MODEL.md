---
document_code: BRD-META-MODEL
document_name: Enterprise Business Meta Model
project: YSim v2.0
document_set: BRD
version: 1.0
status: FROZEN
language: vi-VN
---

# Enterprise Business Meta Model

## BRD-META-MODEL

---

# 1. Purpose

Tài liệu này mô tả mô hình nghiệp vụ tổng thể (Business Meta Model) của nền tảng YSim.

Đây là tài liệu định hướng giúp thống nhất cách hiểu về:

- Business Capability
- Business Object
- Business Policy
- Business Rule
- Business Event
- Business Snapshot

Tài liệu không mô tả nghiệp vụ chi tiết mà chỉ mô tả mối quan hệ giữa các thành phần cốt lõi của Platform.

---

# 2. Business Meta Model

YSim sử dụng mô hình kiến trúc nghiệp vụ như sau.

```text
Business Requirement
        │
        ▼
Business Capability
        │
        ▼
Business Object
        │
        ▼
Business Policy
        │
        ▼
Business Rule
        │
        ▼
Business Event
        │
        ▼
Business Snapshot
```


---

# 2A. Commerce Meta Model (Version 2.1)

Version 2.1 mở rộng Business Meta Model để chuẩn hóa cách xây dựng và vận hành Commerce Experience.

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
        │
        ▼
Publishing Target
```

Mô hình này bổ sung một lớp trừu tượng mới giữa Business Capability và Experience Delivery, giúp chuẩn hóa toàn bộ quá trình sinh Store và triển khai Commerce Experience.

---

# 2B. Commerce Meta Components

| Component | Responsibility |
|------------|----------------|
| Business Model | Mô hình kinh doanh chuẩn (Travel, Affiliate, OTA, Hotel, Enterprise...) |
| Business Blueprint | Chuẩn hóa Capability, Experience Flow và Business Rules của một Business Model |
| Store Template | Mẫu cấu hình mặc định để tạo Store |
| Store Instance | Cửa hàng cụ thể của từng Organization |
| Commerce Experience | Trải nghiệm mua hàng được cung cấp cho khách hàng |
| Publishing Target | Kênh xuất bản Commerce Experience |

Business Blueprint và Store Template không chứa dữ liệu vận hành của Organization mà đóng vai trò là tài sản có thể tái sử dụng (Reusable Business Assets).

---

# 2C. Business Factory

YSim áp dụng Business Factory Pattern để chuẩn hóa quá trình tạo Commerce Experience.

```text
Business Requirement
        │
        ▼
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
```

Business Factory giúp AI và đội phát triển tạo Store theo các Blueprint chuẩn thay vì triển khai từ đầu.


---

# 3. Component Responsibilities

| Component | Responsibility |
|------------|----------------|
| Business Capability | Hệ thống có khả năng làm gì |
| Business Object | Đối tượng nghiệp vụ được quản lý |
| Business Policy | Chính sách điều khiển hành vi |
| Business Rule | Logic xử lý chi tiết |
| Business Event | Điều đã xảy ra trong nghiệp vụ |
| Business Snapshot | Bằng chứng nghiệp vụ tại một thời điểm |

---

# 4. Runtime Flow

Luồng thực thi chuẩn của Platform.

```text
Business Request
        │
        ▼
Capability
        │
        ▼
Policy Decision
        │
        ▼
Business Rule
        │
        ▼
Business Transaction
        │
        ▼
Business Event
        │
        ▼
Business Snapshot
        │
        ├────► Notification
        ├────► Analytics
        ├────► Reporting
        └────► Settlement
```

---

# 5. Enterprise Registries

YSim quản lý các thành phần cốt lõi thông qua năm Registry.

| Registry | Purpose |
|----------|---------|
| BRD-BO-INDEX | Business Object Registry |
| BRD-CAP-INDEX | Business Capability Registry |
| BRD-EVENT-INDEX | Enterprise Business Event Registry |
| BRD-POLICY-INDEX | Enterprise Policy Registry |
| BRD-SNAPSHOT-INDEX | Enterprise Snapshot Registry |

Năm Registry này là **Source of Truth** cho toàn bộ Platform.

---

# 6. Design Principles

## Principle 1

Capability mô tả khả năng của Platform.

Không mô tả dữ liệu.

---

## Principle 2

Business Object là trung tâm của Business Domain.

---

## Principle 3

Policy quyết định cách Platform hoạt động.

Không Hard-code khi có thể cấu hình.

---

## Principle 4

Business Rule mô tả logic chi tiết.

Business Rule được Policy sử dụng.

---

## Principle 5

Business Event phản ánh điều đã xảy ra.

Không phản ánh điều sẽ xảy ra.

---

## Principle 6

Business Snapshot là Business Evidence.

Snapshot không phải History.

---

# 7. Traceability

Mọi thành phần đều có khả năng truy vết.

```text
Requirement
      │
      ▼
Capability
      │
      ▼
Business Object
      │
      ▼
Policy
      │
      ▼
Rule
      │
      ▼
Event
      │
      ▼
Snapshot
      │
      ▼
API
      │
      ▼
Test Case
```

---

# 8. Relationship to Architecture

Business Meta Model là nền tảng cho:

- Domain Model
- Database Design
- API Design
- Event-Driven Architecture
- Commerce Experience Platform (CXP)
- Business Blueprint
- Store Template
- Experience Composition
- Integration
- Security
- Reporting
- Analytics
- Operations

Mọi tài liệu kiến trúc phải tuân thủ Business Meta Model này và mọi Commerce Experience phải được xây dựng từ Business Model và Business Blueprint đã được chuẩn hóa.

---

# 9. Summary

Business Meta Model giúp toàn bộ nền tảng YSim thống nhất:

- Cách mô hình hóa nghiệp vụ.
- Cách đặt tên.
- Cách quản lý dữ liệu.
- Cách quản lý sự kiện.
- Cách quản lý chính sách.
- Cách quản lý bằng chứng nghiệp vụ.

Đây là tài liệu định hướng ở mức Enterprise và là điểm khởi đầu để đọc toàn bộ bộ tài liệu BRD.

---

# Document Status

**Status: FROZEN**

Business Meta Model là tài liệu nền tảng mô tả kiến trúc nghiệp vụ tổng thể của nền tảng YSim.

Mọi thay đổi đối với Business Capability, Business Object, Business Policy, Business Event hoặc Business Snapshot cần được xem xét dựa trên Business Meta Model này để đảm bảo tính nhất quán của toàn bộ hệ thống.

---