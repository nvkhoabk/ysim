---
document_code: AFM-01
document_name: AI Factory Framework v2.1 Update
project: YSim v2.1
document_set: AI Factory Manual
version: 2.1
status: FROZEN
language: en-US
---

# AI Factory Framework v2.1 Update

## AFM-01

---

# 1. Purpose

AFM-01 mô tả các thay đổi kiến trúc và phương pháp phát triển được bổ sung trong YSim AI Software Factory v2.1.

Đây là tài liệu cập nhật cho AFM-00.

AFM-01 không thay thế AFM-00.

AFM-01 chỉ mô tả các Capability và nguyên tắc mới được bổ sung trước khi triển khai Development & Implementation Pack (DIP).

---

# 2. Objectives

Version 2.1 được phát hành nhằm:

- hoàn thiện mô hình Sprint-Driven Development;
- bổ sung Full-stack Capability Delivery;
- bổ sung Commerce Experience Platform (CXP);
- chuẩn hóa Frontend Engineering;
- tăng khả năng kiểm thử trực tiếp sau mỗi Sprint.

Version 2.1 không thay đổi kiến trúc nền tảng của AI Factory.

---

# 3. Major Enhancements

YSim AI Software Factory v2.1 bổ sung các nhóm năng lực sau:

| Enhancement | Description |
|-------------|-------------|
| Full-stack Capability Delivery | Backend và Frontend được phát triển trong cùng một Sprint |
| Capability Demonstration Model | Mỗi Capability phải có giao diện kiểm thử trực tiếp |
| Commerce Experience Platform (CXP) | Business Domain mới phục vụ Storefront và Digital Commerce |
| Unified Inheritance Framework | Chuẩn hóa cơ chế kế thừa theo Organization |
| Frontend Engineering Standards | Chuẩn hóa kiến trúc và quy tắc phát triển Frontend |

---

# 4. Full-stack Capability Delivery

Từ phiên bản 2.1, một Sprint không còn chỉ triển khai Backend.

Mỗi Sprint phải tạo ra một Capability hoàn chỉnh gồm:

```text
Business Capability

↓

Backend Services

↓

API & Events

↓

Frontend Experience

↓

Seed Data

↓

Verification

↓

Demonstration

↓

Operational Evidence
```

Backend và Frontend được phát triển đồng thời trên cùng một Capability.

---

# 5. Capability Demonstration Model

Mỗi Capability phải có một **Capability Demonstration Surface (CDS)**.

CDS là giao diện tối thiểu cho phép:

- kiểm thử nghiệp vụ;
- xác nhận API;
- kiểm tra Permission;
- trình diễn kết quả Sprint;
- nghiệm thu từng Capability.

Capability chỉ được coi là hoàn thành khi có thể được kiểm thử trực tiếp.

---

# 6. Commerce Experience Platform (CXP)

Version 2.1 bổ sung Business Domain mới:

**Commerce Experience Platform (CXP)**

CXP cung cấp:

- Store Management
- Theme Engine
- Landing Builder
- Storefront Runtime
- Publishing Service
- Checkout Experience
- Payment Offering
- Campaign Management
- Tracking & Analytics
- SEO Management

CXP là nền tảng giúp đối tác có thể tạo và vận hành website bán hàng trực tiếp trên YSim mà không phụ thuộc vào nền tảng thương mại điện tử bên ngoài.

---

# 7. Payment Experience Model

Version 2.1 chuẩn hóa mô hình Payment Experience.

Frontend không hiển thị Gateway.

Frontend hiển thị Payment Offering.

Ví dụ:

- Credit Card
- PayPal
- Apple Pay
- Google Pay
- Alipay
- WeChat Pay
- Bank QR

Gateway và Merchant được lựa chọn bởi Payment Orchestrator theo cấu hình của Organization.

---

# 8. Unified Inheritance Framework

Version 2.1 mở rộng mô hình kế thừa theo Organization.

Các đối tượng có thể:

- Override
- Inherit

từ Parent Organization.

Áp dụng cho:

- Pricing
- Payment Profile
- Theme
- Notification
- Feature Configuration
- Store Configuration

Framework sử dụng cùng một nguyên tắc kế thừa trên toàn bộ hệ thống.

---

# 9. Frontend Architecture

Frontend trở thành một phần chính thức của AI Factory.

Monorepo tối thiểu gồm:

```text
apps/

api/

worker/

scheduler/

admin-portal/

agency-portal/

customer-portal/

storefront-runtime/

developer-portal/
```

Frontend phải tuân thủ cùng Architecture và Engineering Standards như Backend.

---

# 10. Sprint Delivery Model

Một Sprint của Version 2.1 bao gồm:

```text
Planning

↓

Backend

↓

Frontend

↓

Integration

↓

Seed Data

↓

Capability Demonstration

↓

Verification

↓

Release
```

Không được phép hoàn thành Sprint khi chưa có Demonstration.

---

# 11. Definition of Done

Version 2.1 mở rộng Definition of Done thành bốn nhóm:

- Technical Done
- Business Done
- Demonstration Done
- Operational Done

Demonstration Done là yêu cầu bắt buộc đối với mọi Capability có giao diện người dùng.

---

# 12. AI Working Model

AI Agent phải:

- triển khai Backend và Frontend đồng thời;
- sử dụng API Contract thống nhất;
- sinh Seed Data;
- tạo Demonstration Scenario;
- tạo đầy đủ Verification Evidence.

AI không được hoàn thành Sprint chỉ với Source Code Backend.

---

# 13. Relationship to Other Documents

AFM-01 cập nhật các bộ tài liệu sau:

- BRD
- YADF
- ABP
- AAP
- SGP
- ESP

Các bộ tài liệu này sẽ được cập nhật trong Version 2.1 trước khi bắt đầu Development & Implementation Pack (DIP).

---

# 14. Migration Strategy

Version 2.1 là bản cập nhật không phá vỡ (Non-breaking Update).

Tất cả tài liệu Version 2.0 vẫn có hiệu lực.

Các tài liệu Version 2.1 chỉ bổ sung các Capability còn thiếu và mở rộng phạm vi của AI Software Factory.

---

# 15. Framework Status

Sau Version 2.1, AI Factory bao gồm:

```text
AFM
AI Factory Manual

↓

BRD
Business Knowledge

↓

YADF
Architecture & Domain Foundation

↓

ABP
Architecture Blueprint

↓

AAP
AI Collaboration

↓

SGP
Sprint Governance

↓

ESP
Engineering Standards

↓

DIP
Development & Implementation

↓

VAP
Verification & Acceptance

↓

ROP
Release & Operations
```

Framework đã sẵn sàng để bước vào giai đoạn triển khai Development & Implementation Pack.

---

# 16. Document Status

**Status: FROZEN**

AFM-01 là tài liệu công bố chính thức các thay đổi của YSim AI Software Factory Version 2.1.

Mọi tài liệu được cập nhật sau AFM-01 phải tuân thủ các nguyên tắc được định nghĩa trong tài liệu này.

---