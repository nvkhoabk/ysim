---
document_code: ESP-13
document_name: Engineering Review Standards
project: YSim v2.0
document_set: Engineering Standards Pack
version: 1.0
status: FROZEN
language: en-US
---

# Engineering Review Standards

## ESP-13

---

# 1. Purpose

Engineering Review Standards định nghĩa các tiêu chuẩn xem xét (Review) đối với mọi Engineering Artifact trong nền tảng YSim.

Review không chỉ áp dụng cho Source Code.

Review là cơ chế đảm bảo chất lượng trước khi Artifact được chấp nhận.

---

# 2. Principles

Engineering Review tuân thủ:

- Review Early
- Review Continuously
- Evidence Based
- Traceable
- Independent
- Constructive
- Risk Based
- AI Assisted

---

# 3. Objectives

Review nhằm:

- phát hiện lỗi;
- xác nhận thiết kế;
- kiểm tra Standards;
- kiểm tra Sprint Contract;
- giảm Technical Debt;
- tạo Evidence cho Acceptance.

---

# 4. Review Scope

Review áp dụng cho:

- Source Code
- API Contract
- Event Contract
- Migration
- Database Schema
- Configuration
- Documentation
- Test Assets
- Infrastructure as Code
- AI Artifacts

---

# 5. Review Classification

Platform chuẩn hóa:

| Review Type | Purpose |
|-------------|----------|
| Architecture Review | Kiến trúc |
| Design Review | Thiết kế |
| Source Code Review | Mã nguồn |
| API Review | API |
| Database Review | Schema & Migration |
| Security Review | Bảo mật |
| Test Review | Kiểm thử |
| Documentation Review | Tài liệu |
| Release Review | Trước Release |

Một Sprint có thể yêu cầu một hoặc nhiều loại Review.

---

# 6. Review Workflow

```text
Artifact

↓

Self Review

↓

AI Review

↓

Peer Review

↓

Approval

↓

Merge / Acceptance
```

Không bỏ qua các bước Review bắt buộc được quy định trong Sprint Contract.

---

# 7. Self Review

Tác giả phải tự kiểm tra:

- Build
- Test
- Standards
- Documentation
- Traceability

trước khi gửi Review.

---

# 8. AI Review

AI có thể hỗ trợ:

- Standards Compliance
- Naming Validation
- Contract Validation
- Dead Code Detection
- Duplicate Logic Detection
- Documentation Consistency
- Traceability Check

AI Review không thay thế Review của con người đối với các thay đổi cần phán đoán nghiệp vụ hoặc kiến trúc.

---

# 9. Peer Review

Peer Review kiểm tra:

- Correctness
- Maintainability
- Readability
- Security
- Performance
- Sprint Scope
- Engineering Standards

Review tập trung vào Artifact, không đánh giá cá nhân.

---

# 10. Architecture Review

Architecture Review bắt buộc khi:

- thay đổi Layer;
- thay đổi Dependency;
- thay đổi Domain Ownership;
- thay đổi Public Contract;
- có ACP hoặc ADR liên quan.

---

# 11. Review Checklist

Review tối thiểu xác nhận:

- đúng Sprint;
- đúng Capability;
- đúng Standards;
- Build PASS;
- Test PASS;
- Migration Review (nếu có);
- Documentation cập nhật.

---

# 12. Review Evidence

Review tạo:

- Review Result
- Findings
- Comments
- Approval Status
- Review Timestamp

Evidence được liên kết với Sprint Dossier.

---

# 13. Review Findings

Finding được phân loại:

| Severity | Meaning |
|-----------|----------|
| Critical | Phải sửa trước khi tiếp tục |
| Major | Cần sửa trước Merge |
| Minor | Nên sửa |
| Suggestion | Khuyến nghị cải tiến |

Mọi Finding phải được xử lý hoặc được chấp nhận có lý do.

---

# 14. Approval Rules

Artifact chỉ được coi là Approved khi:

- Review hoàn thành;
- Findings ở mức Critical và Major đã được xử lý hoặc được phê duyệt ngoại lệ;
- Standards Compliance đạt yêu cầu;
- Evidence đầy đủ.

---

# 15. Review Metrics

Theo dõi:

- Review Coverage
- Review Time
- Findings by Severity
- Rework Rate
- Review Completion Rate

Các chỉ số phục vụ cải tiến quy trình, không dùng để đánh giá cá nhân.

---

# 16. Prohibited Practices

Không được:

- Merge khi chưa Review theo yêu cầu.
- Tự phê duyệt thay đổi nếu chính sách yêu cầu người phê duyệt độc lập.
- Bỏ qua Finding mức Critical.
- Đánh dấu Approved khi chưa xem xét Artifact.
- Review chỉ dựa trên AI đối với các thay đổi cần phê duyệt của con người.

---

# 17. Review Rules

REV-001 — Mọi Sprint phải có Review.

REV-002 — Review tạo Evidence.

REV-003 — Review phải Traceable.

REV-004 — Architecture Change phải Architecture Review.

REV-005 — Review tuân thủ Sprint Contract.

REV-006 — AI Review hỗ trợ, không thay thế Human Review.

REV-007 — Review phải ghi nhận Findings.

REV-008 — Approval phải có căn cứ.

REV-009 — Review phải phục vụ Audit.

REV-010 — Engineering Review là Quality Gate bắt buộc.

---

# 18. Review Compliance Checklist

| Rule | Validation |
|------|------------|
| RCC-1301 | Self Review hoàn thành |
| RCC-1302 | AI Review hoàn thành (nếu áp dụng) |
| RCC-1303 | Peer Review hoàn thành |
| RCC-1304 | Architecture Review (khi yêu cầu) |
| RCC-1305 | Findings được xử lý |
| RCC-1306 | Approval hợp lệ |
| RCC-1307 | Review Evidence đầy đủ |
| RCC-1308 | Sprint Contract được tuân thủ |
| RCC-1309 | Traceability đầy đủ |
| RCC-1310 | Tuân thủ ESP |

---

# 19. Relationship to Other Documents

ESP-13 liên kết với:

- AAP-04 AI Verification Model
- SGP-05 Sprint Review & Acceptance
- SGP-08 Sprint Governance Gates
- ESP-02 Source Code Engineering Standards
- ESP-07 Engineering Testing Standards
- ESP-11 Engineering Documentation Standards
- VAP (Verification & Acceptance Pack)

Engineering Review Standards là tiêu chuẩn thống nhất cho mọi hoạt động Review của nền tảng YSim.

---

# 20. Document Status

**Status: FROZEN**

ESP-13 là tài liệu chuẩn hóa quy trình và tiêu chuẩn Review đối với mọi Engineering Artifact của YSim.

Mọi Artifact thuộc phạm vi Sprint phải hoàn thành Review theo tài liệu này trước khi được chấp nhận hoặc phát hành.

---