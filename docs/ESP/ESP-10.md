---
document_code: ESP-10
document_name: Secure Engineering Standards
project: YSim v2.1
document_set: Engineering Standards Pack
version: 2.1
status: FROZEN
language: en-US
---

# Secure Engineering Standards

## ESP-10

---

# 1. Purpose

Secure Engineering Standards định nghĩa các tiêu chuẩn bảo mật áp dụng xuyên suốt vòng đời phát triển phần mềm của nền tảng YSim.

Security không phải là một bước kiểm tra cuối cùng.

Security là một thuộc tính của mọi Engineering Artifact.

Tiêu chuẩn này áp dụng cho:

- Source Code
- API
- Database
- Configuration
- Infrastructure
- AI Workspace
- CI/CD
- Runtime Environment
- Frontend
- Design System
- Experience Layer

---

# 2. Principles

Secure Engineering tuân thủ:

- Security by Design
- Secure by Default
- Least Privilege
- Zero Trust
- Defense in Depth
- Fail Secure
- Privacy by Design
- Continuous Verification
- Full-stack Security
- Experience Security

---

# 3. Objectives

Security nhằm:

- bảo vệ dữ liệu;
- bảo vệ người dùng;
- bảo vệ hệ thống;
- bảo vệ Repository;
- bảo vệ AI Artifact;
- giảm thiểu rủi ro bảo mật.

---

# 4. Security Domains

Platform chuẩn hóa các Domain bảo mật.

| Domain | Scope |
|---------|-------|
| Identity Security | Authentication |
| Access Security | Authorization |
| API Security | API Protection |
| Data Security | Data Protection |
| Infrastructure Security | Runtime Environment |
| Configuration Security | Secret & Configuration |
| AI Security | AI Workspace & Artifacts |
| Supply Chain Security | Dependency & Build Pipeline |
| Frontend Security | Browser, UI Assets |
| Experience Security | Storefront & Experience APIs |

---

# 4A. Experience Security

Đối với Capability có giao diện người dùng, Security Standards còn áp dụng cho:

- Frontend Assets
- Experience API
- Storefront Runtime
- Design System Assets
- Capability Demonstration Environment

Các thành phần Experience phải tuân thủ cùng mức bảo vệ như Backend.

---

# 5. Authentication Standards

Authentication phải:

- xác thực trước mọi nghiệp vụ được bảo vệ;
- hỗ trợ MFA khi yêu cầu;
- sử dụng chuẩn xác thực thống nhất;
- có thời hạn phiên làm việc rõ ràng.

Không tự triển khai cơ chế xác thực khi đã có nền tảng chuẩn.

---

# 6. Authorization Standards

Authorization phải:

- dựa trên Permission hoặc Policy;
- thực hiện ở tầng Application;
- tuân thủ nguyên tắc Least Privilege.

Không kiểm tra quyền chỉ ở giao diện người dùng.

---

# 7. API Security

API phải:

- sử dụng HTTPS;
- xác thực đầy đủ;
- kiểm tra quyền truy cập;
- giới hạn tốc độ (Rate Limiting) khi phù hợp;
- ghi nhận Audit đối với các thao tác nhạy cảm.

---

# 8. Data Security

Dữ liệu phải được phân loại:

| Classification | Example |
|----------------|---------|
| Public | Tài liệu công khai |
| Internal | Cấu hình nội bộ |
| Confidential | Thông tin khách hàng |
| Restricted | Secret, khóa mã hóa |

Mỗi mức phân loại phải có chính sách bảo vệ tương ứng.

---

# 9. Sensitive Data Handling

Không được:

- ghi Password vào Log;
- ghi Secret vào Log;
- trả Secret qua API;
- lưu Token ở dạng không an toàn;
- hiển thị dữ liệu nhạy cảm khi không cần thiết.

Áp dụng Masking hoặc Redaction khi hiển thị dữ liệu nhạy cảm.

---

# 10. Secret Management

Secrets bao gồm:

- API Keys
- JWT Secret
- OAuth Secret
- Database Password
- Encryption Keys
- Certificate Private Keys

Secrets phải:

- lưu ngoài Source Code;
- được quản lý tập trung;
- có chính sách xoay vòng (Rotation) khi phù hợp;
- có Audit.

---

# 11. Encryption

Áp dụng mã hóa:

- dữ liệu truyền tải (TLS);
- dữ liệu lưu trữ khi yêu cầu;
- Secret;
- Backup.

Thuật toán và cơ chế mã hóa phải tuân theo tiêu chuẩn của tổ chức và yêu cầu pháp lý áp dụng.

---

# 12. Dependency Security

Dependency phải:

- có nguồn gốc rõ ràng;
- được kiểm tra lỗ hổng định kỳ;
- được cập nhật có kiểm soát;
- không sử dụng thư viện không còn được bảo trì nếu có lựa chọn phù hợp.

---

# 13. Secure Coding

Source Code:

- Validate Input;
- Encode Output khi cần;
- xử lý Error an toàn;
- tránh Injection;
- tránh Hardcode Secret;
- tránh sử dụng thư viện không an toàn.

Chi tiết Coding Standards tham chiếu ESP-02.

---

# 14. AI Security

AI Agent:

- không sinh Secret giả vào Repository;
- không tạo Credential mặc định;
- không tự mở rộng quyền truy cập;
- không ghi dữ liệu nhạy cảm vào Evidence.

AI Artifact phải tuân thủ Security Standards.

---

# 15. CI/CD Security

Pipeline phải:

- kiểm tra Secret;
- kiểm tra Dependency;
- chạy Security Scan theo chính sách;
- bảo vệ Artifact;
- kiểm soát quyền phát hành.

Không lưu Secret trực tiếp trong Pipeline Definition.

---

# 16. Security Logging

Các sự kiện sau phải được Audit:

- Authentication
- Authorization
- Permission Changes
- Configuration Changes
- Administrative Actions
- Security Exceptions

Audit Log phải bất biến.

---

# 17. Security Testing

Mỗi Sprint cần xem xét:

- Dependency Scan;
- Secret Scan;
- Static Security Analysis (khi áp dụng);
- API Security Validation;
- Frontend Security Validation;
- Experience Security Validation.

Các hoạt động kiểm thử chuyên sâu (Penetration Test, Red Team...) thuộc phạm vi VAP hoặc ROP khi cần.

---

# 18. Incident Readiness

Platform phải hỗ trợ:

- Security Alert
- Incident Investigation
- Evidence Collection
- Recovery Verification

Security Event phải truy vết được.

---

# 19. Prohibited Practices

Không được:

- Hardcode Password.
- Hardcode API Key.
- Commit Secret.
- Ghi Secret vào Log.
- Tắt Authentication.
- Bỏ qua Authorization.
- Bỏ qua Security Review đối với thay đổi có rủi ro cao.

---

# 20. Security Rules

SEC-001 — Security by Design.

SEC-002 — Least Privilege.

SEC-003 — Secret không nằm trong Repository.

SEC-004 — API phải được Authentication.

SEC-005 — Authorization là bắt buộc.

SEC-006 — Dữ liệu nhạy cảm phải được bảo vệ.

SEC-007 — Dependency phải được kiểm soát.

SEC-008 — AI phải tuân thủ Security Standards.

SEC-009 — Security Event phải Audit.

SEC-010 — Security là yêu cầu bắt buộc của mọi Sprint.

SEC-011 — Capability có UI phải trải qua Frontend Security Review.

SEC-012 — Experience API phải tuân thủ Security Standards như Business API.

---

# 21. Security Compliance Checklist

| Rule | Validation |
|------|------------|
| SCC-1001 | Authentication đúng chuẩn |
| SCC-1002 | Authorization đúng chuẩn |
| SCC-1003 | HTTPS được sử dụng |
| SCC-1004 | Secret được quản lý an toàn |
| SCC-1005 | Dependency được kiểm tra |
| SCC-1006 | Không Hardcode Secret |
| SCC-1007 | Security Audit hoạt động |
| SCC-1008 | AI Artifact không chứa dữ liệu nhạy cảm |
| SCC-1009 | Security Scan đạt yêu cầu |
| SCC-1010 | Tuân thủ ESP |
| SCC-1011 | Frontend Security đạt yêu cầu |
| SCC-1012 | Experience Security đạt yêu cầu |

---

# 22. Relationship to Other Documents

ESP-10 liên kết với:

- ESP-02 Source Code Engineering Standards
- ESP-04 API Engineering Standards
- ESP-08 Observability & Diagnostics Standards
- ESP-09 Configuration & Feature Management Standards
- ABP-11 Security Architecture
- SGP-08 Sprint Governance Gates
- ROP (Release & Operations Pack)

Secure Engineering Standards là nền tảng bảo mật xuyên suốt cho toàn bộ nền tảng YSim, bao gồm Backend, Frontend, Design System và Experience Layer.

---

# 23. Document Status

**Status: FROZEN**

ESP-10 là tài liệu chuẩn hóa các tiêu chuẩn Secure Engineering của YSim.

Mọi Sprint, AI Agent, Developer và Pipeline CI/CD phải tuân thủ tài liệu này trước khi triển khai hoặc phát hành bất kỳ thay đổi nào.

---