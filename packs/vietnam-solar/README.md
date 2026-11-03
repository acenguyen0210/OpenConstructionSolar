# Gói Giải Pháp Điện Mặt Trời Việt Nam (Vietnam Solar EPC Pack)

Gói cấu hình chuyên biệt hóa nền tảng **OpenConstructionERP** cho thị trường **Điện mặt trời (Solar PV) và Lưu trữ năng lượng (BESS) tại Việt Nam**, phục vụ các Tổng thầu EPC, Chủ đầu tư (IPP), Doanh nghiệp FDI/C&I và Nhà thầu thi công cơ điện.

## Tính năng và Cấu hình tích hợp

- **Tiền tệ & Ngôn ngữ mặc định**: Đơn vị tiền tệ Việt Nam Đồng (**VND - ₫**, làm tròn 0 chữ số thập phân), giao diện người dùng tiếng Việt (**vi**).
- **Bộ 5 tài liệu tiêu chuẩn kỹ thuật (Validation Rule Packs)**:
  1. `vietnam_solar_regulations`: Pháp lý ĐMT mái nhà tự sản tự tiêu (Nghị định 135/2024/NĐ-CP), Cơ chế DPPA mua bán điện trực tiếp (Nghị định 80/2024/NĐ-CP), Quy hoạch Điện VIII (PDP8), Thông tư 11/2021/TT-BXD và định mức Thông tư 12/2021/TT-BXD.
  2. `vietnam_solar_pv_design`: Tiêu chuẩn thiết kế hệ thống quang điện nhiệt đới hóa: góc nghiêng tối ưu 10°-15° tự rửa trôi mùa mưa, tỷ số DC/AC 1.25 - 1.35, suy hao nhiệt độ ở 65°C, tính toán tải trọng gió bão Vùng I-IV theo QCVN 02:2022/BXD, kiểm định module TCVN 6781 (IEC 61215) & TCVN 10884 (IEC 61730).
  3. `vietnam_solar_fire_safety`: Quy chuẩn an toàn PCCC ĐMT áp mái nhà xưởng theo Văn bản 3288/C07-P4 của Cục Cảnh sát PCCC & CNCH và QCVN 06:2022/BXD (hành lang tiếp cận chữa cháy ≥ 1.5m, giới hạn khối mảng pin ≤ 40m, nút ngắt khẩn cấp Rapid Shutdown, hệ thống chữa cháy trạm biến áp).
  4. `vietnam_evn_grid_compliance`: Quy chuẩn kỹ thuật đấu nối lưới điện phân phối/truyền tải EVN theo Thông tư 39/2015/TT-BCT và Thông tư 30/2019/TT-BCT (tần số 49.5 - 50.5 Hz, độ lệch điện áp ±5%, sóng hài THD < 5%, hệ số cos phi ≥ 0.9, rơ le bảo vệ 27/59/81/50/51/79, hệ thống chống phát ngược Zero Export Controller).
  5. `vietnam_solar_lcoe`: Mô hình tài chính phân tích LCOE, NPV, IRR, thời gian hoàn vốn (PBP) và so sánh biểu giá điện sản xuất/kinh doanh 3 biểu giá của EVN (Quyết định 2699/QĐ-BCT).
- **Cơ sở dữ liệu chi phí**: Tích hợp định mức quốc gia `VN_NATIONAL` (Thông tư 12/2021/TT-BXD) và danh mục vật tư thiết bị Solar chuyên biệt tại thị trường Việt Nam (tấm pin TopCon 585Wp, biến tần chuỗi Sungrow/Huawei, cáp Solar DC, trạm biến áp Thibidi, tủ RMU Schneider, chống sét Erico, hệ khung nhôm kẹp seamlock).
- **2 Dự án mẫu điển hình (Flagship Demo Projects)**:
  1. `vietnam-solar-rooftop-epc`: Dự án Điện mặt trời mái nhà xưởng KCN VSIP II Bình Dương - 3.5 MWp (C&I Rooftop Solar - Tự sản tự tiêu / Zero-Export theo NĐ 135/2024).
  2. `vietnam-solar-farm-epc`: Nhà máy điện mặt trời mặt đất Thuận Nam, Ninh Thuận - 50 MWp + BESS 10 MWh (Cơ chế mua bán điện trực tiếp DPPA theo NĐ 80/2024).
- **Trình hướng dẫn thiết lập 6 bước (Onboarding Wizard)** bằng tiếng Việt.
- **Phương pháp luận dự toán**: `vietnam-solar` tuân thủ công thức phân bổ chi phí xây dựng Thông tư 11/2021/TT-BXD (Chi phí trực tiếp T, Chi phí gián tiếp GT, Thu nhập chịu thuế tính trước TL 6%, Thuế GTGT VAT 8%).

---

## Tiêu chuẩn & Quy chuẩn áp dụng tại Việt Nam

- **TCVN 11855-1:2017 / IEC 62446-1:2016**: Hệ thống quang điện (PV) kết nối lưới điện - Yêu cầu đối với hồ sơ, nghiệm thu và kiểm tra.
- **TCVN 6781:2017 / IEC 61215:2016**: Mô đun quang điện mặt đất kiểu silicon tinh thể - Đánh giá chất lượng thiết kế và phê duyệt kiểu.
- **TCVN 10884:2015 / IEC 61730:2011**: Đánh giá độ an toàn của mô đun quang điện.
- **QCVN 01:2020/BCT**: Quy chuẩn kỹ thuật quốc gia về an toàn điện.
- **QCVN 02:2022/BXD**: Quy chuẩn kỹ thuật quốc gia về số liệu điều kiện tự nhiên dùng trong xây dựng.
- **QCVN 06:2022/BXD & Văn bản 3288/C07-P4**: Quy chuẩn kỹ thuật quốc gia về an toàn cháy cho nhà và công trình & Hướng dẫn PCCC cho hệ thống điện mặt trời mái nhà.
- **Thông tư 39/2015/TT-BCT & Thông tư 30/2019/TT-BCT**: Quy định hệ thống điện phân phối và tiêu chuẩn đấu nối kỹ thuật của Tập đoàn Điện lực Việt Nam (EVN).
- **Nghị định 135/2024/NĐ-CP**: Quy định cơ chế khuyến khích phát triển điện mặt trời mái nhà tự sản xuất, tự tiêu thụ.
- **Nghị định 80/2024/NĐ-CP**: Cơ chế mua bán điện trực tiếp giữa đơn vị phát điện năng lượng tái tạo và khách hàng sử dụng điện lớn (DPPA).

---

## Hướng dẫn cài đặt và kích hoạt

### Cách 1: Khởi động với biến môi trường
Khởi động hệ thống OpenConstructionERP kích hoạt sẵn Gói Điện Mặt Trời Việt Nam:

```bash
# Trên Windows PowerShell
$env:OE_PACK = "vietnam-solar"
python -m app.main

# Trên Linux / macOS
OE_PACK=vietnam-solar openconstructionerp serve
```

Hoặc chạy file kịch bản nhanh:
```powershell
.\start-solar-vn.ps1
```

### Cách 2: Kích hoạt từ giao diện Web
1. Đăng nhập vào OpenConstructionERP.
2. Vào mục **Modules (Mô-đun)** → **Partner Packs (Gói đối tác)**.
3. Nhấn **Rescan (Quét lại)**, tìm gói **"Vietnam Solar EPC Pack (Điện Mặt Trời Việt Nam)"**.
4. Nhấn **Activate pack (Kích hoạt gói)** hoặc **Full Install (Cài đặt trọn gói)**.

