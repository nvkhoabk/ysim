---
document_code: ESP-12
document_name: Source Control & Change Management Standards
project: YSim v2.0
document_set: Engineering Standards Pack
version: 1.0
status: FROZEN
language: en-US
---

# Source Control & Change Management Standards

## ESP-12

---

# 1. Purpose

Source Control & Change Management Standards định nghĩa tiêu chuẩn quản lý mã nguồn và thay đổi kỹ thuật trong nền tảng YSim.

Source Control không chỉ quản lý Version.

Nó quản lý toàn bộ lịch sử tiến hóa của hệ thống.

Tiêu chuẩn này áp dụng cho:

- Source Code
- Configuration
- Infrastructure as Code
- Documentation as Code
- AI Artifacts
- Migration Scripts

---

# 2. Principles

Source Control tuân thủ:

- Version Controlled
- Traceable
- Atomic
- Reviewable
- Reproducible
- Auditable
- Sprint Driven

---

# 3. Objectives

Source Control nhằm:

- lưu vết mọi thay đổi;
- hỗ trợ Collaboration;
- hỗ trợ Rollback;
- hỗ trợ Audit;
- hỗ trợ Sprint Traceability.

---

# 4. Source Control Scope

Quản lý:

- Source Code
- Documentation
- Configuration
- Infrastructure
- Migration
- Test Assets
- AI Artifacts

Không quản lý dữ liệu vận hành hoặc dữ liệu nghiệp vụ.

---

# 5. Branching Strategy

Mặc định áp dụng mô hình Trunk-Based Development với nhánh chính ổn định.

Các nhánh ngắn hạn có thể được sử dụng cho:

- Sprint
- Hotfix
- Release Preparation (khi cần)

Chiến lược Branch cụ thể do tổ chức ban hành nhưng phải nhất quán trên toàn bộ Repository.

---

# 6. Branch Naming

Ví dụ:

```text
main

release/1.2.0

hotfix/payment-timeout

feature/sprint-017-payment-ledger
```

Quy tắc:

- lowercase
- kebab-case
- phản ánh mục đích

---

# 7. Commit Standards

Một Commit phải:

- có mục đích duy nhất;
- đủ nhỏ để Review;
- không trộn nhiều Capability;
- có khả năng Rollback khi cần.

---

# 8. Commit Message

Khuyến nghị sử dụng Conventional Commits.

Ví dụ:

```text
feat(payment): implement settlement ledger

fix(order): prevent duplicate activation

refactor(pricing): simplify rule evaluation

test(customer): add contract tests

docs(esp): update migration standards
```

---

# 9. Pull Request Standards

Mỗi Pull Request phải:

- liên kết Sprint;
- mô tả thay đổi;
- nêu phạm vi ảnh hưởng;
- liệt kê Migration (nếu có);
- liệt kê API thay đổi (nếu có);
- đính kèm Evidence hoặc liên kết tới Sprint Dossier khi phù hợp.

---

# 10. Change Classification

Platform chuẩn hóa:

| Type | Description |
|------|-------------|
| Feature | Tính năng mới |
| Enhancement | Cải tiến |
| Bug Fix | Sửa lỗi |
| Refactor | Tái cấu trúc |
| Documentation | Tài liệu |
| Infrastructure | Hạ tầng |
| Security | Bảo mật |
| Dependency | Cập nhật phụ thuộc |

---

# 11. Review Requirements

Không Merge khi chưa:

- Review hoàn thành;
- CI PASS;
- Test PASS theo Sprint Contract;
- Migration được Review (nếu có);
- Security Review (nếu thuộc phạm vi yêu cầu).

---

# 12. Merge Strategy

Ưu tiên Merge giữ lịch sử rõ ràng.

Không Rewrite lịch sử trên nhánh chính sau khi đã chia sẻ rộng rãi.

Lịch sử thay đổi phải phục vụ Audit.

---

# 13. Tags & Releases

Release phải được Tag.

Ví dụ:

```text
v1.0.0

v1.1.0

v2.0.0
```

Tag phải liên kết với Release Notes.

---

# 14. Change Traceability

Mọi thay đổi phải truy vết được tới:

- Sprint
- Work Item
- Capability
- Business Object (nếu có)
- ADR hoặc ACP (nếu có)
- Governance Decision (nếu có)

---

# 15. Protected Branches

Các nhánh chính phải được bảo vệ.

Ví dụ:

- yêu cầu Review;
- yêu cầu CI PASS;
- hạn chế Force Push;
- hạn chế Merge trực tiếp.

---

# 16. AI Source Control

AI Agent:

- không tự tạo Branch ngoài quy tắc;
- không Rewrite lịch sử;
- không Force Push;
- không tự Merge nếu chưa qua Governance.

AI phải tuân thủ Sprint Contract.

---

# 17. Prohibited Practices

Không được:

- Commit Secret.
- Commit Binary không cần thiết.
- Commit Code chưa Build được.
- Commit nhiều Capability trong cùng một thay đổi nếu không có lý do rõ ràng.
- Bỏ qua quy trình Review.

---

# 18. Source Control Rules

SCM-001 — Mọi thay đổi phải được Version Control.

SCM-002 — Commit phải nguyên tử (Atomic).

SCM-003 — Pull Request phải được Review.

SCM-004 — Branch Naming đúng chuẩn.

SCM-005 — Merge phải truy vết được.

SCM-006 — Release phải được Tag.

SCM-007 — Main Branch phải được bảo vệ.

SCM-008 — AI phải tuân thủ Source Control Standards.

SCM-009 — Change phải liên kết Sprint.

SCM-010 — Source Control phục vụ Audit.

---

# 19. Source Control Compliance Checklist

| Rule | Validation |
|------|------------|
| SCC-1201 | Branch Naming đúng chuẩn |
| SCC-1202 | Commit Message đúng chuẩn |
| SCC-1203 | Commit nguyên tử |
| SCC-1204 | PR có Review |
| SCC-1205 | CI PASS |
| SCC-1206 | Release được Tag |
| SCC-1207 | Traceability đầy đủ |
| SCC-1208 | Protected Branch được cấu hình |
| SCC-1209 | Không Commit Secret |
| SCC-1210 | Tuân thủ ESP |

---

# 20. Relationship to Other Documents

ESP-12 liên kết với:

- ESP-02 Source Code Engineering Standards
- ESP-06 Migration Standards
- ESP-07 Engineering Testing Standards
- ESP-11 Engineering Documentation Standards
- SGP-03 Sprint Planning & Approval
- SGP-05 Sprint Review & Acceptance
- SGP-09 Sprint Completion & Handover

Source Control & Change Management Standards là tiêu chuẩn thống nhất cho mọi thay đổi kỹ thuật của nền tảng YSim.

---

# 21. Document Status

**Status: FROZEN**

ESP-12 là tài liệu chuẩn hóa toàn bộ quy trình quản lý mã nguồn và thay đổi kỹ thuật của YSim.

Mọi thay đổi đối với Source Repository phải tuân thủ Source Control & Change Management Standards.

---