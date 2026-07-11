---
document_code: ESP-07
document_name: Engineering Testing Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Engineering Testing Standards

## ESP-07

---

# 1. Purpose

Engineering Testing Standards định nghĩa các tiêu chuẩn kiểm thử kỹ thuật của nền tảng YSim.

Tài liệu này chuẩn hóa:

- Test Architecture
- Test Types
- Test Organization
- Test Automation
- Test Quality
- Test Evidence

ESP-07 áp dụng cho toàn bộ hoạt động kiểm thử trong quá trình Engineering.

Các hoạt động Verification và Acceptance ở cấp Sprint được quy định trong VAP.

---

# 2. Principles

Engineering Testing tuân thủ:

- Test First Mindset
- Automation First
- Repeatable
- Deterministic
- Independent
- Traceable
- Contract Driven
- Full-stack Testing
- Experience-driven Verification

---

# 3. Testing Objectives

Testing nhằm:

- xác minh Source Code;
- xác minh API;
- xác minh Integration;
- xác minh Business Rules ở cấp kỹ thuật;
- ngăn Regression;
- tạo Evidence cho Sprint.

Testing không thay thế Business Acceptance.

---

# 4. Testing Pyramid

Platform chuẩn hóa Testing Pyramid.

```text
            E2E
       Integration
            Unit
```

Ưu tiên:

- nhiều Unit Test;
- vừa đủ Integration Test;
- tối thiểu End-to-End Test theo phạm vi Sprint.

---

# 5. Test Classification

Platform chuẩn hóa:

| Test Type | Purpose |
|------------|----------|
| Unit Test | Kiểm tra đơn vị mã nguồn |
| Integration Test | Kiểm tra tương tác giữa các module |
| Contract Test | Kiểm tra API/Event Contract |
| End-to-End Test | Kiểm tra luồng nghiệp vụ chính |
| Performance Test | Kiểm tra hiệu năng (khi Sprint yêu cầu) |
| Security Test | Kiểm tra yêu cầu bảo mật (khi Sprint yêu cầu) |
| Frontend Test | Kiểm tra UI, Components, Routes |
| Experience Test | Kiểm tra User Journey và Capability Demonstration |

---

# 5A. Full-stack Testing Model

Đối với Capability có giao diện người dùng, bộ kiểm thử tối thiểu gồm:

- Backend Unit Test
- API Contract Test
- Frontend Component Test
- Frontend Integration Test
- End-to-End User Journey
- Capability Demonstration Verification

Không hoàn thành Sprint nếu chỉ kiểm thử Backend.

---

# 6. Unit Testing Standards

Unit Test:

- độc lập;
- không phụ thuộc Database thực;
- không phụ thuộc Network;
- chạy nhanh;
- dễ đọc.

Một Unit Test chỉ kiểm tra một hành vi chính.

---

# 7. Integration Testing Standards

Integration Test xác minh:

- Repository
- Database
- External Adapter (qua môi trường kiểm thử hoặc mock phù hợp)
- Message Queue
- Cache
- Object Storage (nếu thuộc phạm vi Sprint)

Integration Test phải cô lập được môi trường kiểm thử.

---

# 8. Contract Testing

Contract Test kiểm tra:

- API Contract
- Event Contract
- Request Schema
- Response Schema
- Version Compatibility

Contract Test là bắt buộc đối với API mới hoặc thay đổi Contract.

---

# 9. End-to-End Testing

E2E Test:

- tập trung vào Business Flow chính;
- không bao phủ toàn bộ hệ thống;
- ưu tiên các Capability quan trọng.

Ví dụ:

```text
Create Order

↓

Payment

↓

Package Assignment

↓

Notification
```

---

# 10. Test Organization

Repository:

```text
tests/

unit/

integration/

contract/

e2e/

fixtures/
```

Cho phép đặt Unit Test cùng module (co-located) nếu thống nhất trong toàn dự án và tuân thủ cấu trúc của framework.

---

# 11. Test Data

Test Data:

- độc lập;
- tái sử dụng;
- không dùng dữ liệu Production;
- có thể tạo và xóa tự động.

---

# 12. Test Automation

Test phải:

- chạy tự động;
- tích hợp CI;
- tạo Report;
- tạo Artifact.

Không yêu cầu chạy thủ công trong Pipeline thông thường.

---

# 13. Test Quality

Mỗi Test phải:

- rõ ràng;
- ổn định;
- có thể lặp lại;
- không phụ thuộc thứ tự chạy;
- không sinh dữ liệu tồn đọng.

---

# 14. Test Evidence

Mỗi lần chạy Test tạo:

- Test Report
- Execution Time
- Result
- Failed Cases
- Logs (khi cần)
- Coverage Summary (nếu có)

Evidence được lưu cùng Sprint.

Đối với Frontend cần bổ sung Screenshot, Video hoặc UI Evidence khi phù hợp.

---

# 15. Test Coverage

Coverage là chỉ số quan sát.

Coverage được theo dõi theo:

- Frontend
- Design System
- Experience


- Module
- Sprint
- Capability

Không đặt mục tiêu phần trăm cứng cho toàn hệ thống.

Mỗi Sprint có thể xác định ngưỡng phù hợp trong Sprint Contract hoặc VAP.

---

# 16. Regression Testing

Regression:

- chạy tự động;
- tập trung các Capability bị ảnh hưởng;
- thực hiện trước Release.

Regression Suite được duy trì và mở rộng theo thời gian.

---

# 17. Prohibited Practices

Không được:

- bỏ qua Test bắt buộc trong Sprint Contract;
- sử dụng dữ liệu Production;
- tạo Test phụ thuộc lẫn nhau;
- tạo Test ngẫu nhiên không thể tái lập;
- đánh dấu PASS khi chưa thực thi.

---

# 18. Testing Rules

TS-001 — Mọi Sprint phải có Test.

TS-002 — API mới phải có Contract Test.

TS-003 — Unit Test phải độc lập.

TS-004 — Integration Test phải cô lập môi trường.

TS-005 — Test phải chạy trong CI.

TS-006 — Test tạo Evidence.

TS-007 — Regression được cập nhật khi có thay đổi.

TS-008 — Test Data không dùng Production.

TS-009 — AI phải sinh Test theo Standards.

TS-010 — Testing Standards áp dụng cho mọi Sprint.

TS-011 — Capability có UI phải có Frontend Test.

TS-012 — Capability Demonstration phải được xác minh bằng E2E hoặc Experience Test.

---

# 19. Testing Compliance Checklist

| Rule | Validation |
|------|------------|
| TCC-0701 | Unit Test đầy đủ |
| TCC-0702 | Integration Test phù hợp |
| TCC-0703 | Contract Test đúng chuẩn |
| TCC-0704 | E2E Flow được xác định |
| TCC-0705 | Test Automation hoạt động |
| TCC-0706 | Test Evidence được tạo |
| TCC-0707 | Regression Suite được cập nhật |
| TCC-0708 | Test Data độc lập |
| TCC-0709 | Test chạy trong CI |
| TCC-0710 | Tuân thủ ESP |
| TCC-0711 | Frontend Test đầy đủ |
| TCC-0712 | Capability Demonstration được xác minh |

---

# 20. Relationship to Other Documents

ESP-07 liên kết với:

- ESP-02 Source Code Engineering Standards
- ESP-04 API Engineering Standards
- ESP-06 Migration Standards
- AAP-04 AI Verification Model
- SGP-05 Sprint Review & Acceptance
- VAP (Verification & Acceptance Pack)

Engineering Testing Standards là nền tảng kỹ thuật cho toàn bộ hoạt động Verification của nền tảng YSim, bao gồm Backend, Frontend, Design System và Experience Verification.

---

# 21. Document Status

**Status: FROZEN**

ESP-07 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn kiểm thử kỹ thuật của YSim.

Mọi Sprint phải triển khai và tự động hóa kiểm thử theo Engineering Testing Standards trước khi chuyển sang Verification và Acceptance.

---