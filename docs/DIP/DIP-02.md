---
document_code: DIP-02
document_name: AI Context Resolution & Prompt Assembly Standard
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

# AI Context Resolution & Prompt Assembly Standard

## DIP-02

---

# 1. Purpose

AI Coding Assistant chỉ có thể tạo ra Source Code đúng khi được cung cấp đầy đủ Context.

DIP-02 định nghĩa cơ chế thu thập, hợp nhất và chuẩn hóa Context trước khi bắt đầu mỗi Sprint hoặc Task.

Mọi Prompt đều phải được sinh ra từ Context đã được chuẩn hóa.

Không cho phép AI Coding Assistant triển khai khi Context chưa đầy đủ.

---

# 2. Position in Software Factory

```text
Repository

↓

Discovery

↓

Context Resolution

↓

Prompt Assembly

↓

AI Coding

↓

Validation
```

Context Resolution là bước bắt buộc trước AI Coding.

---

# 3. Objectives

Context Resolution nhằm:

- xác định đúng phạm vi Sprint;
- giảm Hallucination;
- loại bỏ Prompt thủ công;
- tăng khả năng tái lập;
- bảo đảm tuân thủ Architecture;
- tối ưu Token sử dụng.

---

# 4. Principles

Context Resolution tuân thủ:

- Context First
- Source of Truth
- Minimal but Complete
- Architecture-aware
- Capability-aware
- Explainable
- Deterministic
- Repeatable

---

# 5. Context Layers

Context được chia thành nhiều lớp.

```text
Business

↓

Architecture

↓

Engineering

↓

Capability

↓

Repository

↓

Runtime

↓

Task
```

Không được bỏ qua bất kỳ lớp nào nếu có liên quan.

---

# 6. Context Sources

AI có thể sử dụng Context từ:

- BRD
- ABP
- DMS
- DBD
- API
- ESP
- SGP
- YADF
- DIP
- Repository
- Sprint Manifest
- Seed Package

Không sử dụng nguồn ngoài nếu chưa được phê duyệt.

---

# 7. Context Resolution Pipeline

```text
Discovery

↓

Repository Scan

↓

Sprint Manifest

↓

Capability Manifest

↓

Business Context

↓

Architecture Context

↓

Engineering Context

↓

Repository Context

↓

Task Context

↓

Prompt Assembly
```

Prompt chỉ được tạo sau khi Context Resolution hoàn thành.

---

# 8. Business Context

Business Context tối thiểu gồm:

- Capability
- Business Rules
- Actors
- Use Cases
- Constraints
- Acceptance Criteria

Business Context được lấy từ BRD.

---

# 9. Architecture Context

Architecture Context gồm:

- Business Domains
- Services
- Modules
- Events
- Ownership
- Integration
- Deployment Constraints

Nguồn chính:

- ABP
- AFM
- YADF

---

# 10. Engineering Context

Engineering Context gồm:

- Coding Standards
- Naming Standards
- API Standards
- Testing Standards
- Security Standards
- Performance Standards

Nguồn:

ESP.

---

# 11. Repository Context

Repository Context gồm:

- Folder Structure
- Existing Modules
- Package Dependencies
- Build System
- Existing Tests
- Existing APIs

Repository luôn là Source of Truth cho trạng thái hiện tại của Source Code.

---

# 12. Capability Context

Capability Context bao gồm:

- Domain Model
- API
- Database
- Frontend
- Experience API
- Seed Data
- Demonstration

Capability Context được lấy từ Sprint Package.

---

# 13. Runtime Context

Runtime Context bao gồm:

- Environment
- Feature Flags
- Configuration
- Secrets Reference
- Infrastructure

Không nhúng Secret trực tiếp vào Prompt.

---

# 14. Task Context

Task Context chỉ chứa:

- Objective
- Files Allowed
- Files Protected
- Dependencies
- Expected Outputs
- Validation Commands

Task Context phải nhỏ nhất có thể.

---

# 15. Prompt Assembly

Prompt được tạo theo thứ tự:

```text
Role

↓

Objective

↓

Scope

↓

Context

↓

Business Rules

↓

Architecture Constraints

↓

Engineering Constraints

↓

Repository Constraints

↓

Implementation Tasks

↓

Validation

↓

Completion Criteria
```

Prompt không được viết thủ công cho từng Sprint.

Prompt phải được sinh từ Context.

---

# 16. Context Size Control

AI không được nạp toàn bộ tài liệu.

Chỉ nạp:

- tài liệu liên quan;
- Capability hiện tại;
- Repository hiện tại.

Ưu tiên Context có mức ảnh hưởng cao.

---

# 17. Conflict Resolution

Nếu phát hiện:

- Architecture Conflict
- Business Conflict
- Repository Conflict

AI phải:

- dừng Prompt Assembly;
- sinh ACP;
- không Coding.

---

# 18. Rules

CTX-001 — Context Resolution bắt buộc trước Coding.

CTX-002 — Prompt sinh từ Context.

CTX-003 — Không Coding nếu thiếu Context.

CTX-004 — Repository là Source of Truth cho Source Code.

CTX-005 — Architecture Document là Source of Truth cho Design.

CTX-006 — Không nhúng Secret.

CTX-007 — Chỉ nạp Context liên quan.

CTX-008 — Capability Context luôn ưu tiên.

CTX-009 — Conflict kích hoạt ACP.

CTX-010 — Prompt phải tái lập được.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| CRC-0201 | Business Context đầy đủ |
| CRC-0202 | Architecture Context đầy đủ |
| CRC-0203 | Engineering Context đầy đủ |
| CRC-0204 | Repository Context đầy đủ |
| CRC-0205 | Capability Context đầy đủ |
| CRC-0206 | Prompt được sinh tự động |
| CRC-0207 | Không có Conflict |
| CRC-0208 | Validation Commands đầy đủ |
| CRC-0209 | Context tối ưu |
| CRC-0210 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

DIP-02 liên kết với:

- DIP-00 Implementation Constitution
- DIP-01 Executable Sprint Package Standard
- AFM-00
- BRD
- ABP
- YADF
- AAP
- SGP
- ESP

DIP-02 là tài liệu chuẩn hóa Context Resolution của YSim AI Software Factory.

---

# 21. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Prompt của AI Coding Assistant phải được tạo thông qua Context Resolution theo tiêu chuẩn của DIP-02.

Không cho phép AI Coding trực tiếp từ Prompt thủ công hoặc Context không đầy đủ.