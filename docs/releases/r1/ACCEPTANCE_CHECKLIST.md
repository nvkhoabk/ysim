# R1D-01 Acceptance Checklist

## A. Git baseline

* [ ] Nhánh được tạo từ `rebuild/v2.3-foundation`.
* [ ] Tên nhánh là `release/r1-definition-baseline`.
* [ ] Không chứa business runtime change.
* [ ] Không chứa database migration.
* [ ] Không chứa secret hoặc credential.
* [ ] Working tree sạch sau commit.

## B. Release definition

* [ ] Pilot production được xác định rõ.
* [ ] Việt Nam và Lào nằm trong market scope.
* [ ] Việt, Lào và Anh nằm trong locale scope.
* [ ] VND, LAK và USD nằm trong currency scope.
* [ ] GPay, OnePay và uMoney được phân loại rõ.
* [ ] R1.0 và R1.1 được phân biệt.
* [ ] YSim Platform được xác định là canonical owner.
* [ ] Vai trò chuyển tiếp của WooCommerce được xác định.
* [ ] Vai trò repository riêng của Storefront được xác định.

## C. Agency scope

* [ ] Organization và Agency nằm trong Release 1.
* [ ] Agency Portal nằm trong Release 1.
* [ ] Referral commission được xác nhận.
* [ ] Reference QR được xác nhận.
* [ ] Agency Offer Version được xác nhận.
* [ ] Commission lifecycle được xác nhận.
* [ ] Agency wallet nằm ngoài phạm vi.
* [ ] Sub-agency nằm ngoài phạm vi.

## D. Commerce scope

* [ ] Product Offer được xác định.
* [ ] Price Book độc lập theo currency được xác định.
* [ ] Guest Checkout được xác định.
* [ ] Sales Order trước payment được xác định.
* [ ] Payment server-side verification được xác định.
* [ ] Full refund được xác định.
* [ ] Partial refund nằm ngoài phạm vi.
* [ ] Gigago là supplier runtime đầu tiên.
* [ ] Multi-supplier domain readiness được xác định.

## E. Fulfillment và delivery

* [ ] Supplier retry được xác định.
* [ ] Supplier polling được xác định.
* [ ] Operations Queue được xác định.
* [ ] Manual eSIM replacement được xác định.
* [ ] Email delivery được xác định.
* [ ] Customer Portal delivery được xác định.
* [ ] Magic link access được xác định.
* [ ] Duplicate fulfillment prevention được xác định.

## F. Security và audit

* [ ] Support được phép xem QR.
* [ ] Không yêu cầu approval hai cấp.
* [ ] Audit tự động vẫn bắt buộc.
* [ ] Sandbox và production tách credential.
* [ ] Payment webhook có signature verification.
* [ ] Reference QR không cho phép sửa giá bằng URL.
* [ ] eSIM asset không nằm trong public storage.

## G. Operational readiness

* [ ] Peak 20 order/phút được ghi nhận.
* [ ] 300 order/ngày được ghi nhận.
* [ ] Khoảng 20 agency được ghi nhận.
* [ ] Khoảng sáu supplier được ghi nhận.
* [ ] Retention sáu tháng được ghi nhận.
* [ ] Success metrics được xác định.
* [ ] Operations roles được xác định.
* [ ] Error queues được xác định.

## H. Repository validation

* [ ] `git diff --check` thành công.
* [ ] `pnpm audit:versions` thành công.
* [ ] `pnpm audit:boundaries` thành công.
* [ ] `pnpm lint` thành công.
* [ ] `pnpm typecheck` thành công.
* [ ] `pnpm test` thành công.
* [ ] Không có file backup hoặc file tạm.
* [ ] Commit và candidate tag đã được tạo.

## Acceptance result

```text
R1D-01_RESULT=PENDING
```

Sau khi tất cả mục hoàn thành:

```text
R1D-01_RESULT=PASS
```
