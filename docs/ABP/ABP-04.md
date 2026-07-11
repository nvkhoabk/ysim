---
document_code: ABP-04
document_name: Transaction Boundary
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Transaction Boundary

## ABP-04

---

# 1. Purpose

Transaction Boundary định nghĩa phạm vi và nguyên tắc xử lý Transaction của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Business Transaction
- Application Transaction
- Database Transaction
- Event Boundary
- Snapshot Boundary
- Compensation
- Consistency

Transaction Boundary là nền tảng của Event-Driven Architecture.

---

# 2. Transaction Principles

YSim áp dụng các nguyên tắc:

- Business First
- Small Transaction
- Explicit Boundary
- Event Driven
- Eventually Consistent
- Idempotent
- Traceable

Không sử dụng Distributed Database Transaction giữa nhiều Domain.

---

# 3. Transaction Levels

Platform định nghĩa bốn cấp Transaction.

| Level | Description |
|---------|-------------|
| Business Transaction | Quy trình nghiệp vụ hoàn chỉnh |
| Application Transaction | Một Use Case |
| Database Transaction | Một lần Commit Database |
| Infrastructure Transaction | Queue, Message, External API |

Không được nhầm lẫn giữa các cấp.

---

# 4. Business Transaction

Business Transaction bao gồm nhiều bước nghiệp vụ.

Ví dụ:

```text
Create Order

↓

Payment

↓

Inventory Allocation

↓

Fulfillment

↓

Notification

↓

Settlement
```

Business Transaction có thể kéo dài nhiều phút hoặc nhiều giờ.

Business Transaction không phải Database Transaction.

---

# 5. Application Transaction

Application Transaction xử lý một Use Case.

Ví dụ:

- Create Order
- Confirm Payment
- Allocate Inventory

Một Application Transaction chỉ thuộc một Module.

---

# 6. Database Transaction

Database Transaction chỉ áp dụng trong phạm vi Database Ownership của Module.

Không thực hiện Database Transaction xuyên Module.

Không sử dụng Distributed Transaction.

---

# 7. Transaction Boundary

Boundary kết thúc khi:

- Database Commit thành công.
- Event được Publish.
- Snapshot được tạo (nếu yêu cầu).

Sau Boundary, Module không được thay đổi trạng thái đã Commit.

---

# 8. Event Boundary

Business Event chỉ được Publish sau khi Business State đã được Commit thành công.

Không Publish Event trước khi Commit.

Mọi Event phải có:

- Event ID
- Event Version
- Trace ID
- Timestamp

---

# 9. Snapshot Boundary

Business Snapshot được tạo tại các mốc nghiệp vụ quan trọng.

Ví dụ:

- Payment Succeeded
- Fulfillment Completed
- Settlement Completed

Snapshot phản ánh trạng thái đã Commit.

---

# 10. Compensation

Nếu Business Transaction thất bại sau một bước đã Commit:

Platform không Rollback các bước trước.

Thay vào đó sử dụng Compensation.

Ví dụ:

```text
Payment Success

↓

Inventory Failed

↓

Compensation

↓

Refund
```

Compensation là một Business Process độc lập.

---

# 11. Consistency Model

YSim áp dụng:

- Strong Consistency trong phạm vi một Module.
- Eventual Consistency giữa các Module.

Điều này giúp mở rộng hệ thống mà không phụ thuộc Distributed Transaction.

---

# 12. Idempotency

Mọi Transaction quan trọng phải hỗ trợ Idempotency.

Ví dụ:

- Payment Callback
- Webhook
- Queue Consumer
- Retry Job

Một yêu cầu lặp lại không được tạo kết quả nghiệp vụ trùng lặp.

---

# 13. Retry Strategy

Retry chỉ áp dụng với:

- Infrastructure Failure
- Network Failure
- Temporary External Error

Không Retry khi lỗi Business Rule.

Retry Policy được cấu hình thông qua Policy Engine.

---

# 14. Transaction Timeout

Mỗi Transaction phải có Timeout.

Timeout được cấu hình theo từng loại Transaction.

Khi Timeout:

- ghi Audit;
- sinh Event (nếu cần);
- kích hoạt Compensation hoặc Manual Review theo Policy.

---

# 15. Transaction Traceability

Mỗi Transaction phải có:

- Transaction ID
- Correlation ID
- Trace ID
- Organization ID
- User ID (nếu có)
- Source Channel

Transaction phải có khả năng truy vết xuyên suốt toàn bộ Business Flow.

---

# 16. Transaction Ownership

Mỗi Transaction chỉ có một Owner.

Owner chịu trách nhiệm:

- Commit Business State.
- Publish Event.
- Create Snapshot.
- Trigger Compensation (nếu cần).

Không có Transaction với nhiều Owner.

---

# 17. Transaction Lifecycle

```text
Created

↓

Validated

↓

Executing

↓

Committed

↓

Completed

↓

Archived
```

Nếu thất bại:

```text
Executing

↓

Failed

↓

Compensated

↓

Closed
```

---

# 18. Transaction Rules

TB-001 — Một Module chỉ quản lý Transaction của chính mình.

TB-002 — Không sử dụng Distributed Database Transaction.

TB-003 — Event chỉ Publish sau Commit.

TB-004 — Snapshot chỉ tạo sau Commit.

TB-005 — Compensation thay thế Rollback xuyên Domain.

TB-006 — Mọi Transaction phải Idempotent.

TB-007 — Mọi Transaction phải Traceable.

TB-008 — Retry chỉ dành cho lỗi kỹ thuật.

TB-009 — Business Rule Failure không Retry tự động.

TB-010 — Transaction phải có Timeout.

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0401 | Không có Distributed Transaction |
| ACC-0402 | Event Publish sau Commit |
| ACC-0403 | Snapshot tạo sau Commit |
| ACC-0404 | Có Correlation ID |
| ACC-0405 | Có Idempotency |
| ACC-0406 | Retry đúng Policy |
| ACC-0407 | Có Compensation nếu cần |
| ACC-0408 | Transaction có Owner |
| ACC-0409 | Có Trace ID |
| ACC-0410 | Tuân thủ Consistency Model |

Checklist này được sử dụng trong:

- Architecture Review
- AI Review
- CI/CD Validation
- Code Review

---

# 20. Document Status

**Status: FROZEN**

ABP-04 là tài liệu nền tảng quy định Transaction Boundary của nền tảng YSim.

Mọi Module, Sprint và AI Implementation phải tuân thủ các nguyên tắc trong tài liệu này.

---