# HƯỚNG DẪN CÀI ĐẶT & SỬ DỤNG HỆ SINH THÁI ADD-IN SITEMASTER PRO & QLVB - MINITOOL
**Phiên bản: SiteMaster Pro Suite v3.0 (Portable & Central Project Database Edition)**

---

## I. CẤU TRÚC BỘ CÔNG CỤ TẬP TRUNG (ALL-IN-ONE & PORTABLE)
Tất cả các tệp và thư mục của bộ công cụ được gom chung vào cùng 1 thư mục [BO_CAI_DAT_SITEMASTER_PRO](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO) để bạn có thể mang đi bất cứ đâu (chép sang máy khác, cắm USB hoặc lưu trữ đám mây):

1. [SiteMaster.xlam](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/SiteMaster.xlam): **Add-in Kỹ thuật & Hồ sơ QA/QC (V3.0)**.
   * Cung cấp Tab **SITEMASTER PRO** trên thanh Ribbon.
   * Cơ chế **Bảo vệ Biểu mẫu gốc**: Khi bấm *Tạo Dự Án*, tự động sinh file mới, không bao giờ làm đổi biểu mẫu gốc.
   * Tích hợp **Quản lý CSDL Hồ sơ Dự án**: Nạp nhanh dự án, xuất/nhập file JSON.
2. [QLVB_MiniTool.xlam](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/QLVB_MiniTool.xlam): **Add-in Quản Lý Văn Bản & Tiện Ích MiniTool**.
   * Cung cấp 2 Tab sạch: **QLVB** và **MiniTool**.
3. [Template_ITP_Pro.xlsx](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/Template_ITP_Pro.xlsx): **File mẫu dự án ITP sạch** (chuẩn ban đầu, không macro).
4. [Template_QLVB.xlsx](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/Template_QLVB.xlsx): **File mẫu cơ sở dữ liệu Quản lý Văn bản** (.xlsx).
5. [SiteMaster_Projects.json](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/SiteMaster_Projects.json): **Cơ sở dữ liệu thông tin các công trình/dự án**.
6. Thư mục `MiniTool/`: Chứa các động cơ con phụ trợ (In ấn, trộn Word, PDF, đổi font, QR code).
7. [CAI_DAT_TU_DONG_1_CLICK.bat](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/CAI_DAT_TU_DONG_1_CLICK.bat): Bộ cài đặt tự động 1 chạm khi sang máy tính mới.

---

## II. CÁCH SỬ DỤNG TÍNH NĂNG MỚI (BẢO VỆ MẪU & CSDL DỰ ÁN)

### 1. Tạo dự án an toàn - Không làm đổi biểu mẫu gốc:
* Nhấp vào nút **`Tạo Dự Án`** trên Ribbon.
* Excel sẽ tự động mở ra một bản sao mới (ví dụ: `Template_ITP_Pro1.xlsx`).
* Biểu mẫu gốc trong máy tính hoàn toàn được bảo vệ, không bao giờ bị lưu đè dữ liệu.

### 2. Nạp nhanh dự án vào file (⚡ 1 giây):
* Mở một file dự án Excel bất kỳ.
* Nhấp vào menu **`Hồ Sơ Dự Án`** trên Ribbon -> Chọn **`⚡ Nạp Nhanh Dự Án Vào File...`**.
* Nhập số thứ tự của dự án bạn muốn nạp (ví dụ `1` hoặc `2`).
* Toàn bộ tên công trình, địa điểm, chủ đầu tư, tư vấn, nhà thầu, số hợp đồng, đại diện ký... sẽ được tự động điền chuẩn xác vào bảng tính.

### 3. Tự động ghi nhớ dự án mới:
* Mở hộp thoại **`Cài Đặt Dự Án`** trên Ribbon.
* Nhập thông tin công trình mới và bấm **`Lưu Dự Án`**.
* Hệ thống sẽ vừa cập nhật vào file hiện tại, vừa tự động lưu vào CSDL [SiteMaster_Projects.json](file:///c:/Users/Admin/Desktop/01.%20MAIN%20ITP%202.5/BO_CAI_DAT_SITEMASTER_PRO/SiteMaster_Projects.json) để dùng lại cho các lần sau.

### 4. Xuất / Nhập CSDL khi chuyển sang máy khác:
* **Xuất CSDL**: Bấm **`📤 Xuất CSDL Dự Án (JSON)...`** -> Chọn nơi lưu file backup.
* **Nhập CSDL**: Trên máy mới, bấm **`📥 Nhập CSDL Dự Án (JSON)...`** -> Chọn file CSDL để khôi phục toàn bộ danh sách dự án.
