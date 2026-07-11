---
document_code: ESP-04
document_name: API Engineering Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# API Engineering Standards

## ESP-04

---

# 1. Purpose

API Engineering Standards định nghĩa các tiêu chuẩn thiết kế, triển khai và quản lý API trong nền tảng YSim.

API là Contract giữa các hệ thống và giữa các Business Capability.

Mọi API phải:

- nhất quán;
- có khả năng mở rộng;
- có khả năng kiểm thử;
- có khả năng quan sát;
- có khả năng truy vết.

---

# 2. Principles

API tuân thủ các nguyên tắc:

- Contract First
- Business Capability Driven
- Versioned
- Stateless
- Secure by Default
- Backward Compatible
- Observable
- AI Friendly
- Full-stack API Design
- Experience-aware Contracts

---

# 3. API Objectives

API phải:

- phản ánh Business Capability;
- phản ánh Domain Model;
- phản ánh Business Object;
- không phụ thuộc UI implementation;
- hỗ trợ Experience Composition;
- không phụ thuộc Database;
- ổn định theo thời gian.

---

# 4. API Classification

Platform chuẩn hóa các loại API.

| Type | Purpose |
|------|----------|
| Public API | Đối tác, khách hàng |
| Internal API | Giao tiếp giữa các module |
| Administrative API | Quản trị hệ thống |
| Integration API | Kết nối hệ thống bên ngoài |
| Webhook API | Nhận sự kiện từ bên ngoài |
| Experience API | Cung cấp dữ liệu tổng hợp cho Storefront / Portal |

Mỗi API phải được phân loại rõ ràng.

---

# 5. API Architecture

```text
Client
    │
API Gateway
    │
Application Layer
    │
Domain Layer
    │
Infrastructure
```

API không truy cập Database trực tiếp.

---

# 5A. Experience API

Đối với các Capability có giao diện người dùng, ưu tiên cung cấp Experience API thay vì để Frontend gọi trực tiếp nhiều Business API.

Experience API có thể tổng hợp dữ liệu từ nhiều Domain nhằm phục vụ:

- Portal
- Storefront
- Landing Page
- Checkout
- Dashboard
- Capability Demonstration

Business API vẫn giữ nguyên tính độc lập và không phụ thuộc Experience Layer.

---

# 6. Resource Design

API sử dụng Resource-Oriented Design.

Ví dụ:

```text
/customers

/orders

/payments

/packages

/activations
```

Không sử dụng:

```text
/getCustomer

/createOrder

/updatePackage
```

---

# 7. HTTP Methods

| Method | Purpose |
|---------|----------|
| GET | Read |
| POST | Create hoặc Command |
| PUT | Replace |
| PATCH | Partial Update |
| DELETE | Remove (nếu nghiệp vụ cho phép) |

Không sử dụng GET cho các thao tác làm thay đổi trạng thái.

---

# 8. URI Standards

URI phải:

- lowercase;
- plural resource;
- kebab-case nếu nhiều từ.

Ví dụ:

```text
/api/v1/customers

/api/v1/customer-profiles

/api/v1/payment-sessions
```

Không sử dụng động từ trong URI.

---

# 9. Request Standards

Request phải:

- sử dụng DTO;
- validate đầy đủ;
- không nhận dữ liệu ngoài Contract;
- có schema rõ ràng.

Validation không đặt trong Controller nếu Framework hỗ trợ Validation Layer.

---

# 10. Response Standards

Response chuẩn:

```json
{
  "success": true,
  "data": {},
  "metadata": {},
  "traceId": "...",
  "timestamp": "..."
}
```

Response Error:

```json
{
  "success": false,
  "error": {
    "code": "...",
    "message": "...",
    "details": []
  },
  "traceId": "...",
  "timestamp": "..."
}
```

Không trả về định dạng khác nhau giữa các API nếu không có lý do chính đáng.

---

# 11. Error Handling

API sử dụng Error Model thống nhất.

Bao gồm:

- Error Code
- Error Message
- Error Details
- Trace ID

Không trả Stack Trace cho Client.

---

# 12. Versioning

API phải được Version.

Ví dụ:

```text
/api/v1/
/api/v2/
```

Không thay đổi Breaking Contract trong cùng Version.

Breaking Change yêu cầu Version mới hoặc chiến lược tương thích đã được phê duyệt.

---

# 13. Pagination

Collection API hỗ trợ:

- page
- pageSize

hoặc

- cursor

Response bao gồm Metadata phân trang.

---

# 14. Filtering & Sorting

Chuẩn hóa:

```text
?status=ACTIVE

?sort=name

?page=1&pageSize=20
```

Không tạo query parameter tùy ý giữa các Module.

---

# 15. Idempotency

Các API có nguy cơ thực hiện lặp (ví dụ thanh toán, tạo giao dịch) nên hỗ trợ Idempotency Key.

Ví dụ:

```text
Idempotency-Key:
```

Mọi yêu cầu Idempotent phải được xử lý thống nhất.

---

# 16. Authentication & Authorization

API phải:

- Authentication trước.
- Authorization sau.

Không truy cập Business Logic nếu Authentication thất bại.

Chuẩn xác thực và phân quyền được quy định chi tiết tại ESP-10.

---

# 17. Observability

Mỗi Request phải có:

- Trace ID
- Correlation ID (nếu có)
- Request Log
- Response Log (theo chính sách)

Không ghi log dữ liệu nhạy cảm.

---

# 18. API Documentation

Mỗi API phải có:

- Description
- Request Schema
- Response Schema
- Error Codes
- Authentication
- Examples

API Documentation là một Deliverable bắt buộc.

Đối với Experience API cần bổ sung:
- Sample UI Flow
- Sample Response
- Capability Demonstration Scenario

---

# 19. API Testing

Mỗi API phải có:

- Unit Test
- Integration Test
- Contract Test

Các yêu cầu hiệu năng hoặc bảo mật được bổ sung theo phạm vi Sprint và ESP-07.

---

# 20. Prohibited Practices

Không được:

- Truy cập Database từ Controller.
- Trả Exception thô.
- Hardcode Business Rules.
- Hardcode Permission.
- Thay đổi API Contract không qua Version hoặc phê duyệt.
- Trả dữ liệu dư thừa không được định nghĩa trong Contract.

---

# 21. API Rules

API-001 — API là Contract.

API-002 — API phải Versioned.

API-003 — API phải Stateless.

API-004 — API phải Validate Request.

API-005 — API phải sử dụng DTO.

API-006 — API phải có Documentation.

API-007 — API phải có Test.

API-008 — API phải hỗ trợ Traceability.

API-009 — API phải tuân thủ Security Standards.

API-010 — AI phải tuân thủ API Engineering Standards.

API-011 — Frontend không được phụ thuộc trực tiếp vào nhiều Business API khi đã có Experience API.

API-012 — Experience API phải có Contract và Test độc lập.

---

# 22. API Compliance Checklist

| Rule | Validation |
|------|------------|
| APC-0401 | Resource Design đúng chuẩn |
| APC-0402 | HTTP Method đúng |
| APC-0403 | URI đúng chuẩn |
| APC-0404 | DTO được sử dụng |
| APC-0405 | Response Model thống nhất |
| APC-0406 | Error Model thống nhất |
| APC-0407 | API được Version |
| APC-0408 | Authentication & Authorization đúng chuẩn |
| APC-0409 | API Documentation đầy đủ |
| APC-0410 | API Test đầy đủ |
| APC-0411 | Experience API đúng chuẩn |
| APC-0412 | Experience API có Demonstration Scenario |

---

# 23. Relationship to Other Documents

ESP-04 liên kết với:

- ESP-02 Source Code Engineering Standards
- ESP-03 Enterprise Naming Standards
- ESP-05 Database Standards
- ESP-07 Testing Standards
- ESP-08 Logging & Observability Standards
- ESP-10 Security Standards
- ABP-04 Domain Architecture
- ABP-05 Event Architecture
- ABP-06 Integration Architecture

API Engineering Standards là tiêu chuẩn thống nhất cho mọi API của nền tảng YSim, bao gồm Business API, Integration API và Experience API phục vụ Full-stack Capability Delivery.

---

# 24. Document Status

**Status: FROZEN**

ESP-04 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn thiết kế, triển khai và quản lý API của YSim.

Mọi API mới hoặc thay đổi API hiện có phải tuân thủ tài liệu này.

---