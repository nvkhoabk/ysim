# YSim Global eSIM Commerce & Distribution Platform

## Release 1 Definition

| Thuộc tính          | Giá trị                   |
| ------------------- | ------------------------- |
| Release             | R1                        |
| Loại phát hành      | Pilot Production          |
| Trạng thái tài liệu | Proposed Baseline         |
| Ngày baseline       | 2026-07-29                |
| Nền tảng mã nguồn   | `rebuild/v2.3-foundation` |
| Product owner       | YSim                      |
| Thị trường đầu tiên | Việt Nam và Lào           |

---

## 1. Mục tiêu Release 1

Release 1 triển khai một nền tảng thương mại và phân phối eSIM có khả năng phục vụ đồng thời:

1. Khách hàng B2C mua trực tiếp qua YSim Storefront.
2. Khách hàng được giới thiệu từ đại lý qua Reference QR hoặc Reference Link.
3. Đại lý theo dõi đơn hàng, doanh thu và hoa hồng.
4. Nhân viên YSim theo dõi, xử lý và phục hồi các giao dịch lỗi.
5. Hệ thống tự động xử lý từ thanh toán đến cấp và giao eSIM.

Release 1 là pilot production dành cho khách hàng thật và các đại lý thật, không chỉ là môi trường chứng minh kỹ thuật.

---

## 2. Phạm vi thị trường

### 2.1. Thị trường

* Việt Nam.
* Lào.

### 2.2. Ngôn ngữ bắt buộc

* Tiếng Việt: `vi`.
* Tiếng Lào: `lo`.
* Tiếng Anh: `en`.

Mọi nội dung giao dịch quan trọng phải có khả năng bản địa hóa, bao gồm:

* Product name và product description.
* Checkout.
* Payment instruction.
* Trạng thái order.
* Email giao eSIM.
* Customer Portal.
* Agency Portal.
* Thông báo lỗi hướng tới người dùng.

### 2.3. Tiền tệ

* VND.
* LAK.
* USD.

Mỗi thị trường và currency sử dụng Price Book độc lập. Không sử dụng tỷ giá thời gian thực để quyết định trực tiếp giá checkout.

Tỷ giá nội bộ có thể được sử dụng cho:

* Báo cáo.
* Quy đổi giá vốn.
* Phân tích margin.
* Báo cáo hợp nhất đa tiền tệ.

---

## 3. Kênh bán hàng

### 3.1. YSim Storefront

YSim Storefront tiếp tục được duy trì ở repository riêng.

Storefront chịu trách nhiệm:

* Nội dung marketing.
* SEO.
* Hình ảnh sản phẩm.
* Trang danh mục.
* Trang chi tiết sản phẩm.
* Trải nghiệm lựa chọn sản phẩm.
* Điều hướng khách vào checkout.

Storefront không phải nguồn sự thật của:

* Order.
* Payment.
* Procurement.
* Fulfillment.
* eSIM asset.
* Commission.

### 3.2. Agency Reference Channel

Đại lý có thể tạo Reference QR hoặc Reference Link gắn với:

* Agency.
* Organization.
* Product Offer.
* Market.
* Currency.
* Locale.
* Payment provider.
* Giá bán.
* Commission rule.
* Campaign metadata.
* Thời gian hiệu lực.

Khách mở Reference QR sẽ được đưa trực tiếp đến checkout phù hợp mà không cần tìm kiếm lại sản phẩm.

### 3.3. Agency Portal

Release 1 bao gồm Agency Portal với phạm vi tối thiểu:

* Đăng nhập.
* Dashboard.
* Danh sách đơn hàng được attribution cho đại lý.
* Doanh thu.
* Hoa hồng.
* Commission statement.
* Product Offer được phép bán.
* Tạo Reference QR.
* Quản lý Reference QR.
* Vô hiệu hóa Reference QR.
* Tải QR dạng ảnh.
* Xuất báo cáo CSV.

Release 1 chưa bao gồm:

* Agency wallet.
* Credit limit.
* Nạp tiền.
* Wholesale prepaid balance.
* Sub-agency.
* Agency tự cấu hình commission rule.
* Agency tự thực hiện refund.

---

## 4. Quyền sở hữu dữ liệu

YSim GeCDP Platform là canonical system và nguồn sự thật cho:

* Organization.
* Agency.
* Agency membership.
* Product Offer.
* Supplier Plan Mapping.
* Price Book.
* Agency Offer.
* Reference QR.
* Customer.
* Checkout Session.
* Sales Order.
* Order Item.
* Payment.
* Procurement.
* Allocation.
* Fulfillment.
* eSIM Asset.
* Delivery.
* Commission.
* Refund.
* Reconciliation.
* Audit Event.

WooCommerce được sử dụng như một hệ thống nội dung hoặc commerce channel trong giai đoạn chuyển tiếp.

WooCommerce có thể tiếp tục quản lý:

* Nội dung marketing.
* SEO metadata.
* Ảnh.
* Slug.
* Bài viết.
* Nội dung hướng dẫn.

Không triển khai đồng bộ hai chiều cho trạng thái Order, Payment và Fulfillment.

---

## 5. Product và supplier

### 5.1. Product được hỗ trợ

Release 1 hỗ trợ các nhóm sản phẩm Gigago đang bán thực tế:

* Single-country eSIM.
* Regional eSIM.
* Global eSIM.
* Total-data package.
* Daily-data package.
* Unlimited hoặc FUP package nếu supplier cung cấp.
* Data-only eSIM.

Release 1 chưa bắt buộc:

* Voice.
* SMS.
* Phone number.
* Top-up.
* Subscription hoặc recurring package.

### 5.2. Supplier

Supplier runtime đầu tiên:

* Gigago.

Domain model và Supplier Gateway phải hỗ trợ nhiều supplier.

Mục tiêu trong 12 tháng:

* Khoảng sáu supplier.

Release 1 không yêu cầu:

* Supplier routing tự động nâng cao.
* Tối ưu giá động giữa supplier.
* Tự động fallback sang supplier thứ hai.

Tuy nhiên Order và Product không được phụ thuộc trực tiếp vào cấu trúc dữ liệu riêng của Gigago.

---

## 6. Pricing

### 6.1. Price Book

Giá bán được quản lý bằng Price Book theo:

* Organization.
* Market.
* Currency.
* Product Offer.
* Effective period.

Các currency VND, LAK và USD có giá độc lập.

### 6.2. Agency Offer

Release 1 sử dụng mô hình referral commission.

YSim xác định:

* Giá bán.
* Product Offer mà agency được phép giới thiệu.
* Commission rule.
* Thời gian hiệu lực.

Agency không được tự nhập giá tùy ý trong Release 1.

### 6.3. Reference QR price

Reference QR gắn với một phiên bản Agency Offer bất biến.

Agency Offer Version lưu snapshot của:

* Product Offer.
* Currency.
* Giá bán.
* Payment provider.
* Commission rule.
* Effective period.

Reference QR:

* Có thể sử dụng nhiều lần.
* Có thể đặt ngày hết hạn.
* Có thể bị vô hiệu hóa.
* Không được thay đổi nội dung snapshot sau khi đã phát hành.

---

## 7. Payment

### 7.1. Payment providers

Release train hỗ trợ:

* GPay cho thị trường Việt Nam.
* OnePay cho thanh toán thẻ quốc tế.
* uMoney cho thị trường Lào.

### 7.2. Kế hoạch kích hoạt

#### R1.0 Core Pilot

* GPay.
* OnePay.
* VND.
* USD.
* Việt Nam.
* Agency channel.
* B2C Storefront.

#### R1.1 Laos Activation

* uMoney.
* LAK.
* Tiếng Lào.
* Kích hoạt thương mại tại Lào.

Kiến trúc locale, market và LAK phải có từ R1.0. Việc kích hoạt uMoney production có thể phụ thuộc vào tài liệu, credential và hợp đồng từ đối tác.

### 7.3. Nghiệp vụ payment

Release 1 hỗ trợ:

* Payment Intent.
* Payment Attempt.
* Payment expiration.
* Retry payment.
* Provider callback.
* Provider webhook.
* Signature verification.
* Idempotent webhook processing.
* Payment reconciliation.
* Full refund.
* Payment audit timeline.

Partial refund không bắt buộc trong Release 1.

Payment thành công chỉ được xác nhận từ server-side verification hoặc reconciliation đáng tin cậy.

Không xác nhận payment chỉ dựa trên redirect của trình duyệt.

---

## 8. Order

Sales Order được tạo trước payment với trạng thái ban đầu:

```text
PENDING_PAYMENT
```

Order, Payment, Procurement, Fulfillment và Delivery có state machine độc lập.

Overall Order Status là trạng thái suy ra từ các domain state machine, không phải một trạng thái được sửa tùy ý.

Order phải lưu immutable snapshot của:

* Product.
* Product Offer.
* Giá bán.
* Currency.
* Customer.
* Market.
* Locale.
* Agency attribution.
* Commission rule.
* Supplier mapping.
* Storefront context.
* Payment provider.

---

## 9. Fulfillment

Luồng chuẩn:

```text
Payment succeeded
→ Procurement requested
→ Supplier order created
→ Supplier order monitored
→ eSIM received
→ eSIM asset secured
→ Fulfillment succeeded
→ Delivery requested
→ Customer notified
```

Khi supplier chưa trả eSIM:

```text
Retry
→ Polling theo supplier request ID
→ Recovery job
→ Operations Queue
→ Manual resolution hoặc refund theo policy
```

Không tự động refund chỉ vì webhook đến chậm hoặc supplier đang ở trạng thái processing.

### 9.1. Manual fulfillment

Nhân viên được phép:

* Gắn eSIM khác vào order.
* Nhập ICCID.
* Nhập QR hoặc activation code.
* Thay thế eSIM.
* Gửi lại eSIM.
* Đánh dấu fulfillment hoàn thành.

Release 1 không yêu cầu approval trước thao tác.

Tất cả thao tác vẫn phải được hệ thống ghi audit log tự động.

---

## 10. Customer checkout và delivery

### 10.1. Guest checkout

Khách không bắt buộc đăng nhập.

Thông tin tối thiểu:

* Email bắt buộc.
* Tên người nhận.
* Market.
* Currency.
* Locale.
* Thông tin xuất hóa đơn nếu khách yêu cầu.

Sau payment thành công, hệ thống có thể tạo customer identity hoặc portal access bằng magic link.

Khách không bị yêu cầu tạo mật khẩu tại checkout.

### 10.2. Delivery channels

Bắt buộc trong Release 1:

* Email.
* Customer Portal.

Chưa bắt buộc:

* SMS.
* Zalo OA.
* WhatsApp.
* Telegram.

### 10.3. Customer Portal

Phạm vi tối thiểu:

* Danh sách đơn hàng.
* Chi tiết đơn hàng.
* Trạng thái payment.
* Trạng thái fulfillment.
* Hiển thị QR eSIM.
* Sao chép activation code.
* Hướng dẫn cài đặt.
* Gửi lại email.
* Tạo yêu cầu hỗ trợ.
* Truy cập bằng magic link có thời hạn.

---

## 11. Organization và agency

Runtime Release 1 có:

* Organization YSim.
* Tối thiểu hai organization agency sau khi pilot ổn định.
* Mục tiêu khoảng 20 agency.

Các dữ liệu business phải có ownership hoặc organization scope phù hợp.

Agency chỉ được truy cập dữ liệu thuộc phạm vi attribution của mình.

Thông tin khách hàng trên Agency Portal được che một phần, trừ trường hợp nghiệp vụ được YSim cho phép rõ ràng.

---

## 12. Commission

Commission lifecycle:

```text
Order attributed
→ ATTRIBUTED

Payment succeeded
→ ACCRUED

Fulfillment succeeded
→ ELIGIBLE

Refund completed
→ REVERSED

YSim thanh toán ngoài hệ thống
→ PAID
```

Release 1 hỗ trợ:

* Commission cố định.
* Commission theo tỷ lệ phần trăm.
* Commission rule theo Agency Offer.
* Commission snapshot theo Order.
* Commission ledger.
* Manual mark as paid.
* Commission statement.
* Reversal khi refund.

Việc chuyển tiền thực tế cho agency được thực hiện ngoài hệ thống trong Release 1.

---

## 13. Operations và support

### 13.1. Vai trò tối thiểu

* Platform Admin.
* Operations.
* Support.
* Finance Read-only.

### 13.2. Operations Queue

Phải hỗ trợ ít nhất:

* Payment chưa xác minh.
* Payment reconciliation mismatch.
* Supplier processing quá SLA.
* Fulfillment failed.
* Webhook processing failed.
* Email delivery failed.
* Refund pending.
* Manual review.

### 13.3. Quyền xem eSIM

Support được phép xem đầy đủ QR và activation code trong Release 1.

Hệ thống vẫn tự động ghi:

* Người truy cập.
* Thời điểm.
* Order.
* eSIM asset.
* Hành động xem, tải hoặc gửi lại.
* Session hoặc IP nếu có.
* Giá trị cũ và mới đối với thao tác thay thế.

Không yêu cầu approval hai cấp trong Release 1.

---

## 14. Invoice information

Release 1 chỉ lưu thông tin yêu cầu xuất hóa đơn.

Không bắt buộc:

* Tích hợp nhà cung cấp hóa đơn điện tử.
* Phát hành hóa đơn tự động.
* Đồng bộ phần mềm kế toán.

---

## 15. Hạ tầng

Release 1 tiếp tục triển khai trên Debian server hiện có.

Sandbox và production phải tách biệt:

* Database.
* Credential.
* Payment merchant configuration.
* Supplier credential.
* Webhook URL.
* Encryption key.
* Cache namespace.
* Queue namespace.
* Log.
* eSIM asset storage hoặc supplier environment tương ứng.

Các environment:

```text
Local Development
Sandbox / Staging
Production
```

Không sử dụng production credential trong local hoặc sandbox.

---

## 16. Quy mô thiết kế

Thiết kế Release 1 phải hỗ trợ:

* Khoảng 300 order/ngày.
* Peak khoảng 20 order/phút.
* Khoảng 20 agency.
* Khoảng sáu supplier trong 12 tháng.
* Lưu Order và Audit Event tối thiểu sáu tháng.

Load acceptance tối thiểu:

* 20 order/phút trong khoảng kiểm thử liên tục.
* Không mất order.
* Không tạo fulfillment trùng.
* Không tạo commission trùng.
* Không xử lý payment webhook trùng thành giao dịch mới.

---

## 17. Chỉ số thành công

### 17.1. Business outcomes

* Khách thanh toán và nhận eSIM hoàn toàn tự động.
* Đại lý theo dõi được doanh thu và hoa hồng.
* Đại lý tạo được Reference QR.
* Khách từ Reference QR đi thẳng tới checkout.
* Order giữ đúng attribution và commission.

### 17.2. Operational metrics

Hệ thống phải đo được:

* Payment success rate.
* Fulfillment success rate.
* Thời gian từ payment success đến nhận eSIM.
* Tỷ lệ giao email thành công.
* Tỷ lệ order cần xử lý thủ công.
* Supplier processing time.
* Webhook failure rate.
* Commission amount theo agency.
* Revenue theo market, currency và channel.

### 17.3. Release acceptance

Release 1 chỉ được chấp nhận khi:

* Happy path hoàn toàn tự động.
* Duplicate webhook không tạo duplicate payment hoặc fulfillment.
* Supplier processing được phục hồi bằng polling hoặc operations workflow.
* Agency attribution không bị mất qua checkout và payment redirect.
* Reference QR không thể bị sửa giá bằng query parameter.
* eSIM được giao qua email và Customer Portal.
* Operations có thể tìm và xử lý order lỗi.
* Audit log được tạo cho thao tác xem hoặc thay eSIM.
* Sandbox và production được tách cấu hình.
* Runtime evidence được lưu cho các luồng chính.

---

## 18. Ngoài phạm vi Release 1

* Agency wallet.
* Credit limit.
* Postpaid agency billing.
* Sub-agency.
* Multi-level commission.
* Automated supplier optimization.
* Automated supplier fallback.
* Full promotion engine.
* Partial refund.
* Top-up.
* Voice và SMS eSIM.
* Advanced recommendation.
* Full accounting integration.
* Automated invoice issuance.
* Partner Portal cho supplier.
* Advanced white-label builder.

---

## 19. Release train

### R1.0 — Core Pilot

* Organization và Agency foundation.
* Canonical Product Catalog.
* Price Book.
* Reference QR.
* Guest Checkout.
* Sales Order.
* GPay.
* OnePay.
* Gigago.
* Secure eSIM Delivery.
* Customer Portal.
* Agency Portal.
* Commission.
* Operations Queue.
* Reconciliation.

### R1.1 — Laos Activation

* uMoney.
* LAK production activation.
* Lao localization completion.
* Laos payment reconciliation.
* Laos-specific operational validation.

---

## 20. Nguyên tắc triển khai

1. Modular monolith trước microservices.
2. Một nguồn sự thật cho mỗi business entity.
3. Provider integration phải đi qua adapter.
4. Mọi external request phải có idempotency strategy.
5. Payment và fulfillment phải có reconciliation.
6. Business snapshot không bị thay đổi hồi tố.
7. Không coi scaffold hoặc mock là completed slice.
8. Mỗi slice phải có runtime evidence.
9. Không triển khai đồng thời toàn bộ Release 1.
10. Triển khai theo vertical slice có thể chạy end-to-end.
