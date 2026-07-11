---
document_code: ESP-02
document_name: Source Code Engineering Standards
project: YSim v2.0
document_set: Engineering Standards Pack
version: 1.0
status: FROZEN
language: en-US
---

# Source Code Engineering Standards

## ESP-02

---

# 1. Purpose

Source Code Engineering Standards định nghĩa các tiêu chuẩn xây dựng, tổ chức và bảo trì Source Code trong nền tảng YSim.

Tài liệu này áp dụng cho:

- AI Coding Agent
- Developer
- Reviewer
- QA
- Architecture Owner

Source Code phải được viết để:

- dễ đọc;
- dễ kiểm thử;
- dễ mở rộng;
- dễ bảo trì;
- thân thiện với AI.

---

# 2. Principles

Source Code tuân thủ các nguyên tắc:

- Readability First
- Simplicity
- Maintainability
- Testability
- Deterministic
- Explicit
- Low Coupling
- High Cohesion

---

# 3. Source Code Objectives

Source Code phải:

- phản ánh Business Capability;
- phản ánh Domain Model;
- phản ánh Architecture;
- không chứa Business Logic sai Layer;
- dễ Review;
- dễ Refactor.

---

# 4. Engineering Rules

Source Code phải:

- nhỏ;
- rõ ràng;
- có trách nhiệm duy nhất;
- có khả năng kiểm thử độc lập;
- hạn chế Side Effects.

---

# 5. Module Organization

Một Module chuẩn bao gồm:

```text
module/

controller/

service/

application/

domain/

repository/

dto/

mapper/

events/

tests/
```

Không bắt buộc mọi module phải có đầy đủ các thư mục trên, nhưng phải tuân thủ kiến trúc đã được định nghĩa trong ABP. Không được đặt Business Logic trực tiếp trong `controller`.

---

# 6. Source Code Structure

Thứ tự ưu tiên:

```text
Module

↓

Application

↓

Domain

↓

Infrastructure

↓

Integration
```

Không gọi ngược Layer.

---

# 7. Business Logic

Business Logic chỉ được phép nằm trong:

- Domain
- Application

Không được đặt trong:

- Controller
- DTO
- Mapper
- Integration Adapter
- Configuration

---

# 8. Class Standards

Mỗi Class:

- có một trách nhiệm;
- có tên rõ nghĩa;
- không vượt quá phạm vi trách nhiệm đã thiết kế;
- không phụ thuộc trực tiếp vào Infrastructure nếu không cần thiết.

---

# 9. Method Standards

Method nên:

- ngắn;
- rõ ràng;
- một mục đích;
- hạn chế lồng điều kiện sâu.

Method không nên:

- xử lý nhiều Use Case;
- chứa nhiều nhánh điều kiện không liên quan.

---

# 10. Dependency Injection

Toàn bộ Dependency phải:

- Inject
- Không new trực tiếp Service nếu Framework đã hỗ trợ DI
- Không Singleton thủ công

Dependency Injection phải tuân thủ ABP.

---

# 11. Error Handling

Source Code:

- không swallow exception;
- không ignore error;
- phải trả về Error Model chuẩn;
- phải log đúng chuẩn.

Chi tiết được quy định tại:

ESP-08 Logging Standards

ESP-10 Security Standards

---

# 12. Async Programming

Async phải:

- sử dụng async/await thống nhất;
- không tạo Promise không được await (trừ khi có chủ đích rõ ràng);
- xử lý timeout và cancellation khi phù hợp.

Không được block Event Loop.

---

# 13. Code Reuse

Ưu tiên:

- Shared Package
- Common Library
- Utility
- Base Component

Không copy/paste Business Logic giữa các Module.

---

# 14. Refactoring

Refactoring:

- không thay đổi Business Behavior;
- không thay đổi Public Contract nếu chưa được phê duyệt;
- phải giữ nguyên Sprint Scope.

Refactoring lớn phải được xem xét trong Planning hoặc thông qua ACP nếu ảnh hưởng kiến trúc.

---

# 15. Code Generation

AI sinh mã phải:

- tuân thủ ESP;
- tuân thủ ABP;
- tuân thủ Sprint Contract;
- không sinh mã ngoài Scope;
- không tự tạo Pattern mới.

---

# 16. Code Review Readiness

Code được coi là sẵn sàng Review khi:

- Build PASS;
- Test PASS theo yêu cầu Sprint;
- Static Analysis PASS (nếu áp dụng);
- Documentation đã cập nhật;
- Evidence đã tạo.

---

# 17. Source Code Quality

Mỗi Sprint phải đạt:

- Build Success
- Zero Critical Error
- Zero Compiler Warning (đối với mã nguồn mới hoặc phần được chỉnh sửa, trừ khi có ngoại lệ được phê duyệt)
- Không có TODO/FIXME chưa được theo dõi bằng Work Item
- Không Hardcode Secret
- Không Dead Code mới

---

# 18. Prohibited Practices

Không được:

- Hardcode Credentials
- Hardcode Business Rules
- Circular Dependency
- Duplicate Business Logic
- Commented-out Code
- Unused Public API
- Bypass Architecture

---

# 19. Source Code Rules

SC-001 — Source Code phải phản ánh Architecture.

SC-002 — Business Logic chỉ nằm đúng Layer.

SC-003 — Controller không chứa Business Logic.

SC-004 — Không tạo Circular Dependency.

SC-005 — Mọi Dependency phải được quản lý theo chuẩn của Framework.

SC-006 — AI không được sinh Pattern mới ngoài Standards.

SC-007 — Refactoring không thay đổi Business Behavior.

SC-008 — Source Code phải Reviewable.

SC-009 — Source Code phải Testable.

SC-010 — Source Code phải Maintainable.

---

# 20. Source Code Compliance Checklist

| Rule | Validation |
|------|------------|
| SCC-0201 | Layer đúng chuẩn |
| SCC-0202 | Business Logic đúng vị trí |
| SCC-0203 | Dependency Injection đúng chuẩn |
| SCC-0204 | Không Circular Dependency |
| SCC-0205 | Build PASS |
| SCC-0206 | Test PASS |
| SCC-0207 | Không Hardcode Secret |
| SCC-0208 | Không Dead Code mới |
| SCC-0209 | Source Code Reviewable |
| SCC-0210 | Tuân thủ ESP |

---

# 21. Relationship to Other Documents

ESP-02 liên kết với:

- ESP-01 Repository Architecture Standards
- ESP-03 Naming Standards
- ESP-04 API Standards
- ESP-05 Database Standards
- ESP-07 Testing Standards
- ESP-08 Logging & Observability Standards
- ABP-02 Layered Architecture
- ABP-03 Dependency Architecture

Source Code Engineering Standards là nền tảng cho mọi hoạt động phát triển mã nguồn của YSim.

---

# 22. Document Status

**Status: FROZEN**

ESP-02 là tài liệu chuẩn hóa toàn bộ tiêu chuẩn xây dựng và bảo trì Source Code của YSim.

Mọi AI Agent và Developer phải tuân thủ tài liệu này khi tạo, sửa đổi hoặc tái cấu trúc mã nguồn.

---