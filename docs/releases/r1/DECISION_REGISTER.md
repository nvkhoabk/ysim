# Release 1 Decision Register

| ID         | Quyết định                                                            | Trạng thái |
| ---------- | --------------------------------------------------------------------- | ---------- |
| R1-DEC-001 | Release 1 là pilot production                                         | APPROVED   |
| R1-DEC-002 | Thị trường đầu tiên là Việt Nam và Lào                                | APPROVED   |
| R1-DEC-003 | Ngôn ngữ bắt buộc gồm Việt, Lào và Anh                                | APPROVED   |
| R1-DEC-004 | Tiền tệ gồm VND, LAK và USD                                           | APPROVED   |
| R1-DEC-005 | YSim Platform sở hữu Order, Payment và Fulfillment                    | APPROVED   |
| R1-DEC-006 | WooCommerce chỉ là content/channel system trong giai đoạn chuyển tiếp | APPROVED   |
| R1-DEC-007 | YSim Storefront tiếp tục là repository riêng                          | APPROVED   |
| R1-DEC-008 | Gigago là supplier runtime đầu tiên                                   | APPROVED   |
| R1-DEC-009 | Domain model phải hỗ trợ nhiều supplier                               | APPROVED   |
| R1-DEC-010 | Payment providers gồm GPay, OnePay và uMoney                          | APPROVED   |
| R1-DEC-011 | GPay và OnePay thuộc R1.0; uMoney có thể kích hoạt trong R1.1         | APPROVED   |
| R1-DEC-012 | Guest checkout không yêu cầu đăng nhập                                | APPROVED   |
| R1-DEC-013 | Email và Customer Portal là delivery channel bắt buộc                 | APPROVED   |
| R1-DEC-014 | Release 1 bao gồm Agency Portal                                       | APPROVED   |
| R1-DEC-015 | Agency sử dụng referral commission                                    | APPROVED   |
| R1-DEC-016 | Agency chưa có wallet hoặc credit limit                               | APPROVED   |
| R1-DEC-017 | Reference QR có thể dùng nhiều lần và có thể hết hạn                  | APPROVED   |
| R1-DEC-018 | Reference QR sử dụng Agency Offer Version bất biến                    | APPROVED   |
| R1-DEC-019 | Agency không tự đặt giá tùy ý trong Release 1                         | APPROVED   |
| R1-DEC-020 | Mỗi currency có Price Book độc lập                                    | APPROVED   |
| R1-DEC-021 | Commission đủ điều kiện sau fulfillment thành công                    | APPROVED   |
| R1-DEC-022 | Refund đảo ngược commission tương ứng                                 | APPROVED   |
| R1-DEC-023 | Thanh toán commission thực hiện ngoài hệ thống                        | APPROVED   |
| R1-DEC-024 | Manual eSIM replacement không cần approval                            | APPROVED   |
| R1-DEC-025 | Manual eSIM replacement vẫn được ghi audit tự động                    | APPROVED   |
| R1-DEC-026 | Support được xem đầy đủ QR trong Release 1                            | APPROVED   |
| R1-DEC-027 | Release 1 chỉ lưu thông tin xuất hóa đơn                              | APPROVED   |
| R1-DEC-028 | Sandbox và production dùng database và credential riêng               | APPROVED   |
| R1-DEC-029 | Hệ thống tiếp tục triển khai trên Debian server hiện có               | APPROVED   |
| R1-DEC-030 | Order và Audit Event được lưu tối thiểu sáu tháng                     | APPROVED   |
| R1-DEC-031 | Quy mô dự kiến là 300 order/ngày và peak 20 order/phút                | APPROVED   |
| R1-DEC-032 | Mục tiêu 12 tháng là khoảng 20 agency và sáu supplier                 | APPROVED   |
| R1-DEC-033 | Release 1 sử dụng modular monolith                                    | APPROVED   |
| R1-DEC-034 | Order, Payment, Fulfillment và Commission có state riêng              | APPROVED   |
| R1-DEC-035 | Provider callback phải idempotent và có reconciliation                | APPROVED   |

## Thay đổi quyết định

Mọi thay đổi đối với quyết định `APPROVED` phải:

1. Tạo decision record mới.
2. Tham chiếu decision cũ.
3. Ghi lý do thay đổi.
4. Ghi ảnh hưởng đến scope, database, API và migration.
5. Không sửa lịch sử quyết định cũ để làm mất dấu vết.
