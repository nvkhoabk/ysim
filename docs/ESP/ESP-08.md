---
document_code: ESP-08
document_name: Observability & Diagnostics Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Observability & Diagnostics Standards

## ESP-08

---

# 1. Purpose

Observability & Diagnostics Standards định nghĩa các tiêu chuẩn thu thập, ghi nhận và phân tích thông tin vận hành của nền tảng YSim.

Observability bao gồm:

- Logging
- Metrics
- Distributed Tracing
- Health Check
- Diagnostics
- Audit Logging
- Alerting

Mục tiêu là giúp hệ thống dễ vận hành, dễ giám sát và dễ phân tích sự cố.

---

# 2. Principles

Observability tuân thủ:

- Observable by Default
- Structured Logging
- Trace Everything
- Metrics First
- Security Aware
- Privacy Aware
- Low Overhead
- Automation Friendly
- Full-stack Observability
- Experience-aware Diagnostics

---

# 3. Objectives

Observability nhằm:

- hỗ trợ Debug;
- hỗ trợ Production Monitoring;
- hỗ trợ Incident Investigation;
- hỗ trợ Performance Analysis;
- hỗ trợ Audit;
- hỗ trợ AI Diagnostics;
- hỗ trợ Experience Diagnostics;
- hỗ trợ Capability Demonstration Monitoring.

---

# 4. Observability Architecture

```text
Application

↓

Logs

↓

Metrics

↓

Traces

↓

Alerting

↓

Dashboard

↓

Experience Dashboard

↓

Incident Response
```

Observability là một khả năng xuyên suốt toàn hệ thống.

---

# 5. Logging Standards

Mọi Service phải ghi Log theo cấu trúc thống nhất.

Log tối thiểu gồm:

- Timestamp
- Level
- Service
- Module
- Trace ID
- Correlation ID (nếu có)
- Message

Log phải ở định dạng có cấu trúc (ví dụ JSON) để thuận tiện cho việc thu thập và tìm kiếm.

---

# 6. Log Levels

Chuẩn hóa:

| Level | Purpose |
|--------|----------|
| TRACE | Chi tiết nhất, phục vụ phân tích sâu |
| DEBUG | Debug trong môi trường phù hợp |
| INFO | Hoạt động bình thường |
| WARN | Cảnh báo |
| ERROR | Lỗi cần xử lý |
| FATAL | Lỗi nghiêm trọng dẫn đến không thể tiếp tục |

Không ghi mọi thông tin ở mức INFO.

---

# 7. Structured Logging

Ví dụ:

```json
{
  "timestamp": "...",
  "level": "INFO",
  "service": "payment",
  "module": "payment-processing",
  "traceId": "...",
  "message": "Payment completed"
}
```

Không ghi Log dạng chuỗi tự do nếu có thể ghi dữ liệu có cấu trúc.

---

# 8. Correlation & Trace

Mỗi Request nên có:

- Trace ID
- Correlation ID (nếu đi qua nhiều hệ thống)
- Request ID (nếu cần)

Các ID này phải được truyền xuyên suốt giữa các Service.

---

# 8A. Experience Observability

Đối với Capability có giao diện người dùng, cần quan sát thêm:

- Frontend Errors
- Page Load Time
- User Journey
- Experience API Latency
- Storefront Availability
- Capability Demonstration Health

Các Metrics này bổ sung cho Backend Metrics và không thay thế chúng.

---

# 9. Metrics Standards

Mỗi Service cần công bố các nhóm Metrics phù hợp.

Ví dụ:

- Request Count
- Request Duration
- Error Count
- Queue Length
- Active Jobs
- Database Latency
- Cache Hit Rate

Metrics phải hỗ trợ Dashboard và Alerting.

---

# 10. Distributed Tracing

Distributed Tracing áp dụng cho:

- Internal API
- Integration API
- Event Processing
- Background Jobs

Mỗi Trace phải hỗ trợ xác định đường đi của Request qua nhiều Service.

---

# 11. Health Check

Mỗi Service phải cung cấp Health Endpoint.

Tối thiểu:

```text
/health
```

Có thể mở rộng:

```text
/health/live

/health/ready
```

Health Check không được tiết lộ thông tin nhạy cảm.

---

# 12. Audit Logging

Audit Log ghi nhận:

- Authentication
- Authorization
- Administrative Actions
- Configuration Changes
- Security Events
- Business Operations theo yêu cầu nghiệp vụ

Audit Log phải bất biến và có chính sách lưu giữ rõ ràng.

---

# 13. Sensitive Data

Không ghi Log:

- Password
- Secret
- Token
- OTP
- CVV
- Khóa mã hóa
- Dữ liệu cá nhân nhạy cảm nếu không có cơ sở và biện pháp bảo vệ phù hợp

Nếu cần ghi nhận, phải áp dụng Masking hoặc Redaction.

---

# 14. Diagnostics

Diagnostics bao gồm:

- Exception Details
- Stack Trace (chỉ trong môi trường phù hợp)
- Performance Statistics
- Dependency Status
- Resource Utilization

Diagnostics phải hỗ trợ Root Cause Analysis.

---

# 15. Alerting

Alert phải dựa trên:

- Error Rate
- Latency
- Resource Usage
- Queue Backlog
- Health Status
- Availability

Không tạo Alert cho mọi Log ERROR.

---

# 16. Observability Dashboard

Dashboard tối thiểu hiển thị:

- Frontend Status
- Experience Status

- Service Status
- Error Rate
- Response Time
- Throughput
- Queue Status
- Active Alerts
- Health Status

Dashboard phải hỗ trợ Drill-down theo Service hoặc Capability.

---

# 17. Incident Support

Observability phải hỗ trợ:

- Incident Detection
- Incident Investigation
- Root Cause Analysis
- Recovery Verification

Logs, Metrics và Traces phải có khả năng liên kết với nhau.

---

# 18. Prohibited Practices

Không được:

- Ghi Password hoặc Secret vào Log.
- Ghi Token đầy đủ.
- Ghi dữ liệu cá nhân nhạy cảm khi không cần thiết.
- Ghi Log không có ngữ cảnh.
- Bỏ Trace ID đối với Request đi qua nhiều Service.
- Tắt Logging hoặc Metrics mà không có phê duyệt.

---

# 19. Observability Rules

OB-001 — Mọi Service phải hỗ trợ Logging.

OB-002 — Mọi Service phải công bố Health Check.

OB-003 — Metrics phải được thu thập.

OB-004 — API phải hỗ trợ Traceability.

OB-005 — Audit Log phải được bảo vệ.

OB-006 — Không ghi dữ liệu nhạy cảm vào Log.

OB-007 — Dashboard phải phản ánh dữ liệu thực tế.

OB-008 — Alert phải có tiêu chí rõ ràng.

OB-009 — AI phải tuân thủ Observability Standards.

OB-010 — Observability là yêu cầu bắt buộc của mọi Sprint.

OB-011 — Capability có UI phải công bố Experience Metrics.

OB-012 — Capability Demonstration phải được theo dõi bằng Observability.

---

# 20. Observability Compliance Checklist

| Rule | Validation |
|------|------------|
| OCC-0801 | Structured Logging |
| OCC-0802 | Log Level đúng chuẩn |
| OCC-0803 | Metrics được công bố |
| OCC-0804 | Trace ID hoạt động |
| OCC-0805 | Health Check tồn tại |
| OCC-0806 | Audit Logging đúng chuẩn |
| OCC-0807 | Không ghi dữ liệu nhạy cảm |
| OCC-0808 | Dashboard hoạt động |
| OCC-0809 | Alerting được cấu hình |
| OCC-0810 | Tuân thủ ESP |
| OCC-0811 | Experience Metrics đầy đủ |
| OCC-0812 | Frontend Observability đúng chuẩn |

---

# 21. Relationship to Other Documents

ESP-08 liên kết với:

- ESP-04 API Engineering Standards
- ESP-07 Engineering Testing Standards
- ESP-09 Configuration Standards
- ESP-10 Security Standards
- ABP-10 Observability Architecture
- ROP (Release & Operations Pack)

Observability & Diagnostics Standards là tiêu chuẩn thống nhất cho khả năng quan sát và chẩn đoán của toàn bộ nền tảng YSim, bao gồm Backend, Frontend, Experience và Capability Demonstration.

---

# 22. Document Status

**Status: FROZEN**

ESP-08 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn Logging, Metrics, Tracing và Diagnostics của YSim.

Mọi Service và mọi Sprint phải triển khai đầy đủ các yêu cầu về Observability trước khi được coi là sẵn sàng cho môi trường Production.

---