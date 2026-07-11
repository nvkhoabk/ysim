---
document_code: DIP-01
document_name: Executable Sprint Package Standard (ESPK)
project: YSim v2.1
document_set: Development & Implementation Pack
version: 2.1
status: FROZEN
language: en-US
---

# Executable Sprint Package Standard (ESPK)

## DIP-01

---

# 1. Purpose

Executable Sprint Package (ESPK) là đơn vị triển khai chuẩn của YSim AI Software Factory.

Mỗi Sprint không còn được phát hành chỉ dưới dạng tài liệu.

Thay vào đó, Sprint được phát hành dưới dạng một Package hoàn chỉnh có thể được AI Coding Assistant thực thi trực tiếp.

ESPK là cầu nối giữa DIP và Source Code.

---

# 2. Position in Software Factory

```text
DIP

↓

Executable Sprint Package

↓

Bash Runner

↓

AI Coding Agent

↓

Validation

↓

Evidence

↓

Git Commit
```

---

# 3. Objectives

ESPK nhằm:

- chuẩn hóa mọi Sprint;
- tạo khả năng thực thi tự động;
- cung cấp đầy đủ Context;
- giảm Prompt Engineering thủ công;
- đảm bảo khả năng Resume;
- đảm bảo khả năng Audit.

---

# 4. Principles

ESPK tuân thủ:

- Executable by Design
- Context First
- Seed-driven Development
- Capability Driven
- Full-stack Delivery
- Validation First
- Evidence First
- Repeatable Execution
- AI Independent

---

# 5. Package Structure

```text
Sprint Package
│
├── README.md
├── sprint.json
│
├── ai/
│
├── scripts/
│
├── validation/
│
├── evidence/
│
└── logs/
```

Mọi Sprint phải tuân thủ đúng cấu trúc này.

---

# 6. AI Directory

```text
ai/

├── sprints/

├── manifests/

├── prompts/

├── context/

└── seeds/
```

Không được thay đổi cấu trúc thư mục.

---

# 7. Sprint Manifest

Sprint Manifest định nghĩa:

- Sprint ID
- Capability
- Scope
- Dependencies
- Deliverables
- Validation
- Completion Criteria

Manifest là Entry Point của Sprint.

---

# 8. Task Manifest

Mỗi Task có một Manifest riêng.

```text
t00

↓

t01

↓

...

↓

t10
```

Manifest mô tả:

- Objective
- Inputs
- Outputs
- Dependencies
- Validation
- Evidence

---

# 9. Prompt Package

Prompt được lưu riêng.

```text
prompts/

t00.md

...

t10.md
```

Prompt không được Hardcode trong Runner.

---

# 10. Context Package

Context bao gồm:

- Business Context
- Architecture Context
- Engineering Context
- Repository Context
- Frontend Context
- Acceptance Context

AI chỉ được Coding sau khi Context được nạp đầy đủ.

---

# 11. Seed Package

Seed bao gồm:

- Reference Data
- Demo Data
- Integration Configuration
- Sample Users
- Sample Products
- Target Metrics

Seed là nguồn dữ liệu mặc định của Sprint.

---

# 12. Validation Package

Validation bao gồm:

- Build Commands
- Test Commands
- Lint Commands
- Demo Scenarios
- Acceptance Checklist

Validation phải có khả năng chạy tự động.

---

# 13. Bash Runner

Runner tối thiểu hỗ trợ:

- run
- resume
- dry-run
- single-task
- from-task

Runner phải:

- ghi log;
- lưu Exit Code;
- dừng khi FAIL;
- Commit khi PASS.

---

# 14. Evidence Package

Evidence phải sinh:

- Execution Log
- Validation Report
- Build Report
- Test Report
- Demonstration Report
- Git Diff
- Sprint Report

Evidence là đầu ra bắt buộc.

---

# 15. Capability Demonstration

Mỗi Capability có UI phải cung cấp:

- Demonstration Guide
- Demo Users
- Demo Data
- Demo Scenarios
- Expected Results

Capability chỉ được Accepted khi Demonstration PASS.

---

# 16. AI Independence

ESPK không phụ thuộc AI cụ thể.

Có thể thực thi bởi:

- Codex
- Claude Code
- Gemini CLI
- OpenHands
- Cursor Agent
- AI Coding Assistant khác

Không được Hardcode Prompt theo Model.

---

# 17. Versioning

Package có Version độc lập.

Ví dụ:

```text
ESPK

v2.1.0
```

Version không phụ thuộc Repository Version.

---

# 18. Rules

ESPK-001 — Mọi Sprint phải phát hành dưới dạng ESPK.

ESPK-002 — Package phải đầy đủ Manifest.

ESPK-003 — Prompt phải độc lập.

ESPK-004 — Seed là bắt buộc.

ESPK-005 — Runner phải Resume được.

ESPK-006 — Validation phải tự động.

ESPK-007 — Evidence là bắt buộc.

ESPK-008 — Demonstration là bắt buộc đối với Capability có UI.

ESPK-009 — Không phụ thuộc AI Model.

ESPK-010 — Package phải Version hóa.

---

# 19. Compliance Checklist

| Rule | Validation |
|------|------------|
| EPC-0101 | Package đúng cấu trúc |
| EPC-0102 | Manifest đầy đủ |
| EPC-0103 | Prompt đầy đủ |
| EPC-0104 | Context đầy đủ |
| EPC-0105 | Seed đầy đủ |
| EPC-0106 | Runner hoạt động |
| EPC-0107 | Validation PASS |
| EPC-0108 | Evidence đầy đủ |
| EPC-0109 | Demonstration PASS |
| EPC-0110 | Tuân thủ DIP |

---

# 20. Relationship to Other Documents

ESPK liên kết với:

- DIP-00 Implementation Constitution
- AAP Sprint Planning
- SGP Sprint Governance
- ESP Engineering Standards
- VAP Verification & Acceptance Pack
- ROP Release & Operations Pack

ESPK là Implementation Artifact chuẩn của YSim AI Software Factory.

---

# 21. Document Status

**Status: FROZEN**

Từ phiên bản 2.1, mọi Sprint của YSim phải được phát hành dưới dạng **Executable Sprint Package (ESPK)**.

ESPK là định dạng triển khai chuẩn, độc lập với AI Coding Agent, cung cấp đầy đủ Context, Seed, Prompt, Validation và Evidence để AI có thể thực thi Sprint theo mô hình Full-stack Capability Delivery.