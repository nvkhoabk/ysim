---
document_code: ABP-05
document_name: Event Architecture
project: YSim v2.0
document_set: Architecture Baseline Pack
version: 1.0
status: FROZEN
language: en-US
---

# Event Architecture

## ABP-05

---

# 1. Purpose

Event Architecture định nghĩa kiến trúc xử lý Business Event của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Event Lifecycle
- Event Ownership
- Event Publication
- Event Subscription
- Event Delivery
- Event Reliability
- Event Versioning
- Event Traceability

Event Architecture là nền tảng của Event-Driven Architecture (EDA).

---

# 2. Event Principles

YSim áp dụng các nguyên tắc:

- Business Event First
- Immutable Event
- Contract First
- Publisher Independence
- Subscriber Independence
- Loose Coupling
- Eventual Consistency
- Traceability

Business Event không phụ thuộc công nghệ Message Broker.

---

# 3. Event Definition

Business Event là một sự kiện nghiệp vụ đã xảy ra.

Ví dụ:

- Order Created
- Payment Succeeded
- Inventory Allocated
- Fulfillment Completed
- Settlement Completed

Event mô tả **Fact**, không mô tả **Command**.

---

# 4. Event Ownership

Mỗi Business Event chỉ có một Publisher.

Publisher là Domain Owner của Event.

Subscriber không được tạo hoặc sửa Event của Domain khác.

---

# 5. Event Lifecycle

```text
Defined

↓

Published

↓

Delivered

↓

Consumed

↓

Archived
```

Mỗi Event phải đi qua đầy đủ Lifecycle.

---

# 6. Event Publication

Business Event chỉ được Publish khi:

- Business Transaction đã Commit.
- Business State hợp lệ.
- Event Contract hợp lệ.

Không Publish Event trước khi Commit.

---

# 7. Event Subscription

Subscriber đăng ký nhận Event thông qua Event Contract.

Publisher không biết Subscriber.

Subscriber có thể:

- xử lý ngay;
- xử lý bất đồng bộ;
- bỏ qua nếu không liên quan.

---

# 8. Event Contract

Mỗi Event phải có Contract.

Bao gồm:

- Event ID
- Event Name
- Event Version
- Publisher
- Payload Schema
- Metadata
- Timestamp
- Trace ID
- Correlation ID

Không thay đổi Event Contract sau khi phát hành nếu chưa Version.

---

# 9. Event Payload

Event Payload chỉ chứa dữ liệu cần thiết.

Không đưa toàn bộ Aggregate hoặc Business Object vào Payload.

Payload phải:

- nhỏ;
- rõ ràng;
- ổn định;
- độc lập với Database Schema.

---

# 10. Event Versioning

Business Event hỗ trợ Version.

Breaking Change:

- tạo Version mới;
- hỗ trợ Migration nếu cần.

Không thay đổi Event đang sử dụng.

---

# 11. Event Delivery

Platform không ràng buộc cơ chế truyền Event.

Có thể sử dụng:

- Queue
- Message Broker
- Internal Bus
- Streaming Platform

Tất cả đều phải tuân thủ cùng một Event Contract.

---

# 12. Event Reliability

Platform phải hỗ trợ:

- Retry
- Dead Letter Queue (DLQ)
- Replay
- Duplicate Detection
- Idempotency

Event không được mất trong quá trình xử lý.

---

# 13. Event Ordering

Không yêu cầu Global Ordering.

Ordering chỉ áp dụng khi Business Requirement yêu cầu.

Ordering Strategy phải cấu hình được.

---

# 14. Event Replay

Platform phải hỗ trợ Replay.

Replay được sử dụng cho:

- Recovery
- Synchronization
- Analytics
- Rebuild Projection

Replay không được tạo Business Effect lần thứ hai.

---

# 15. Event Traceability

Mỗi Event phải có khả năng truy vết.

Metadata tối thiểu:

- Event ID
- Trace ID
- Correlation ID
- Transaction ID
- Organization ID
- Timestamp
- Publisher

---

# 16. Event Security

Event phải tuân thủ Security Policy.

Có thể áp dụng:

- Authorization
- Encryption
- Data Masking
- Data Classification

Event không được chứa dữ liệu nhạy cảm nếu không cần thiết.

---

# 17. Event Observability

Mọi Event phải hỗ trợ:

- Logging
- Metrics
- Monitoring
- Delivery Status
- Processing Status
- Failure Tracking

Event phải quan sát được trong toàn bộ Lifecycle.

---

# 18. Event Rules

EA-001 — Business Event là Immutable.

EA-002 — Một Event chỉ có một Publisher.

EA-003 — Event chỉ Publish sau Commit.

EA-004 — Publisher không biết Subscriber.

EA-005 — Subscriber chỉ phụ thuộc Event Contract.

EA-006 — Event hỗ trợ Versioning.

EA-007 — Event hỗ trợ Replay.

EA-008 — Event phải Idempotent.

EA-009 — Event phải Traceable.

EA-010 — Event Contract là bất biến trong cùng Version.

---

# 19. Architecture Compliance Checklist (ACC)

| Rule | Validation |
|------|------------|
| ACC-0501 | Event đã đăng ký trong Event Registry |
| ACC-0502 | Publisher đúng Domain Ownership |
| ACC-0503 | Event Publish sau Commit |
| ACC-0504 | Event có Version |
| ACC-0505 | Event có Trace ID |
| ACC-0506 | Event hỗ trợ Retry và DLQ |
| ACC-0507 | Event Payload không phụ thuộc Database Schema |
| ACC-0508 | Event hỗ trợ Replay |
| ACC-0509 | Event được Monitoring |
| ACC-0510 | Event tuân thủ Security Policy |

Checklist này được sử dụng trong:

- Architecture Review
- AI Review
- CI/CD Validation
- Code Review

---

# 20. Document Status

**Status: FROZEN**

ABP-05 là tài liệu nền tảng quy định kiến trúc Event của nền tảng YSim.

Mọi Module, Sprint và AI Implementation phải tuân thủ các nguyên tắc trong tài liệu này.

---