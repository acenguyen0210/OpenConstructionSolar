# OpenConstructionSolar - Vietnam Solar EPC Edition

> **Giải pháp ERP và Quản lý Thi công Dự án Năng Lượng Mặt Trời (Solar PV / EPC) tại Việt Nam**  
> *Dự án được kế thừa và phát triển từ nền tảng mã nguồn mở [OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP) của DataDrivenConstruction theo giấy phép AGPL-3.0.*

---

## 📌 Giới Thiệu Dự Án

**OpenConstructionSolar (Vietnam Solar EPC Edition)** là phiên bản ERP mã nguồn mở chuyên sâu được nội địa hóa và tối ưu hóa toàn diện cho các nhà thầu EPC, chủ đầu tư, tư vấn giám sát và ban quản lý dự án Năng lượng Mặt trời tại thị trường Việt Nam.

Dự án phục vụ đầy đủ các quy mô dự án:
- ☀️ **Điện mặt trời Áp mái Công nghiệp & Thương mại (C&I Rooftop Solar):** Phục vụ các nhà máy, khu công nghiệp (như VSIP, Amata, Sóng Thần, Tân Bình...) theo cơ chế tự sản tự tiêu hoặc bán điện dư.
- ☀️ **Nhà máy Điện mặt trời Nối lưới (Utility-Scale Solar Farm):** Phục vụ các dự án quy mô lớn mặt đất hoặc nổi trên lòng hồ kèm hệ thống lưu trữ năng lượng (BESS) theo cơ chế Mua bán điện trực tiếp (DPPA) theo **Nghị định 80/2024/NĐ-CP**.

---

## ⚡ Các Tính Năng Tối Ưu Hóa Nổi Bật

### 1. Cấu Trúc Quản Lý Hồ Sơ Dự Án 12 Nhóm Chuẩn SOP
Hệ thống tài liệu và cây thư mục được tái cấu trúc 100% theo tiêu chuẩn Quy trình Kiểm soát Tài liệu Dự án Solar của **DAT Group** (`01.LEG` đến `12.PAY`) gồm **12 nhóm cấp 1 và 58 thư mục con cấp 2**:

1. **`01. Project Legal (LEG)`**: Hợp đồng EPC, phụ lục, bảo hiểm CAR/EAR/TPL, hợp đồng thầu phụ, hồ sơ chậm trễ/bất khả kháng, giấy phép PCCC, ĐTM/Giấy phép môi trường, Giấy phép xây dựng, Thỏa thuận đấu nối EVN & Hợp đồng PPA.
2. **`02. Design (DES)`**: Hồ sơ năng lực tư vấn thiết kế, thiết kế ý tưởng Concept, bản vẽ thiết kế thi công DWG, thuyết minh kỹ thuật DED, báo cáo mô phỏng PVsyst/PVR, bản vẽ hoàn công As-built.
3. **`03. Project Plan Documents (PPD)`**: Sơ đồ tổ chức BCH công trường, mặt bằng tổng thể & bố trí thiết bị, các mốc tiến độ chính (Milestones), biên bản Kick-off Meeting, tiến độ chi tiết (Gantt), kế hoạch huy động nhân sự & máy móc, bảng phân tích rủi ro RAM, bóc tách khối lượng BOM/BOC, biện pháp thi công BPTC (MAS/MOS), kế hoạch kiểm tra thí nghiệm ITP.
4. **`04. Project Management Controls (PMC)`**: Biên bản bàn giao mặt bằng HOM, phiếu yêu cầu thay đổi thiết kế CRF, bảng hỏi đáp kỹ thuật Q&A, biên bản họp điều hành tuần/tháng, nhật ký thi công & báo cáo tiến độ, kho ảnh tiến độ hiện trường PPH.
5. **`05. Environmental & Social / HSE (ENS)`**: Danh sách & hồ sơ nhân sự thi công, hồ sơ huấn luyện an toàn lao động, biên bản xử lý vi phạm an toàn, báo cáo điều tra sự cố.
6. **`06. Quality Documents (QUD)`**: Hồ sơ chất lượng vật tư thiết bị (CO, CQ, Factory Test Report, Mill Test Certificate), Biên bản nghiệm thu công việc xây dựng & lắp đặt.
7. **`07. Operation & Maintenance (OMD)`**: Hồ sơ thông tin chung hệ thống, quy trình vận hành chuẩn SOP, kế hoạch bảo trì phòng ngừa SMP/PMM, hướng dẫn xử lý sự cố, quy trình ứng phó khẩn cấp, tài liệu kỹ thuật nhà sản xuất tấm pin/inverter/máy biến áp, danh mục vật tư dự phòng khuyến nghị, hồ sơ đào tạo chuyển giao công nghệ.
8. **`08. Commissioning (COM)`**: Kế hoạch & quy trình tiền chạy thử (Pre-commissioning), biên bản đo kiểm chuỗi string/cách điện/tiếp địa, hồ sơ đóng điện và công nhận ngày vận hành thương mại COD với EVN.
9. **`09. Handover & Close-out (HCO)`**: Biên bản bàn giao công trình PAC (Nghiệm thu tạm thời) / FAC (Nghiệm thu cuối cùng), hồ sơ hoàn công tổng thể, danh mục tồn đọng Punchlist & biên bản xác nhận đóng punchlist.
10. **`10. Form & Templates (FRM)`**: Thư viện biểu mẫu chuẩn dự án Solar (NCR, CRF, RFI, ITP, Checklist nghiệm thu...).
11. **`11. Project Working & Temporary (PWT)`**: Bản vẽ nháp, tài liệu tính toán tạm thời, văn bản trao đổi nội bộ đang xử lý.
12. **`12. Payment Documents (PAY)`**: Hồ sơ tạm ứng/thanh toán với Chủ đầu tư (IPC), hồ sơ thanh toán với Thầu phụ & Nhà cung cấp vật tư.

---

### 2. Thư Viện Định Mức & Đơn Giá Vật Tư Solar Việt Nam
Bộ mã định mức và đơn giá **DDC CWICR VN SOLAR** được tích hợp sẵn bằng Tiền Việt Nam (VND) theo mặt bằng giá thị trường cung ứng vật tư Solar tại Việt Nam:
* **Tấm quang điện (PV Modules):** Canadian Solar, JA Solar, Jinko Solar, Longi Solar 550Wp - 670Wp công nghệ N-type TOPCon, Bifacial hai mặt kính.
* **Biến tần hòa lưới (Inverters):** Sungrow, Huawei, SMA, Growatt (String Inverter 100kW - 330kW và Central Inverter trạm hợp bộ).
* **Trạm biến áp & Hệ thống điện trung thế:** Máy biến áp dầu/khô 22kV - 110kV, Máy cắt Recloser Entec/Tavrida, Tủ đóng cắt RMU Schneider/ABB.
* **Cáp chuyên dụng Solar:** Cáp DC 1500V (Leader, KBE, Helukabel), Cáp AC ngầm đồng Cu/XLPE/PVC/DSTA Cadivi/Thipha/LS Vina.
* **Hệ thống kết cấu & Khung giàn:** Khung nhôm AL6005-T5 anodized, Thép C mạ kẽm nhúng nóng Z275/Z350, Kẹp kẹp giữa/kẹp biên Mid/End clamp, Bulong inox SUS304/SUS316.
* **Hệ thống lưu trữ năng lượng (BESS):** Khối pin lưu trữ LFP kèm PCS và hệ thống điều hòa nhiệt độ HVAC/PCCC chuyên dụng cho cơ chế DPPA.

---

### 3. Hai Dự Án Mẫu Khởi Tạo Sẵn
Hệ thống được nạp sẵn 2 dự án thực tế để thử nghiệm ngay lập tức:
1. **Dự án ĐMT Áp Mái KCN VSIP II - 3.5 MWp (C&I Rooftop Solar):**
   - Lắp đặt trên mái tôn nhà xưởng công nghiệp tại KCN VSIP II, Bình Dương.
   - Hợp đồng EPC trọn gói, hệ thống giám sát SCADA nội bộ, đầy đủ hồ sơ pháp lý PCCC, Giấy phép xây dựng và Thỏa thuận đấu nối EVN SPC.
2. **Nhà Máy ĐMT Mặt Đất Thuận Nam - 50 MWp + BESS 10 MWh (Cơ Chế DPPA):**
   - Nhà máy điện mặt trời mặt đất quy mô lớn tại Thuận Nam, Ninh Thuận.
   - Tích hợp trạm biến áp 110kV và hệ thống lưu trữ điện BESS 10 MWh phục vụ cơ chế mua bán điện trực tiếp (DPPA) với khách hàng lớn theo Nghị định 80/2024/NĐ-CP.

---

### 4. Hệ Thống Biểu Mẫu Kỹ Thuật Chuẩn EPC & Xuất PDF
- Biểu mẫu **NCR (Non-Conformance Report)** - Báo cáo sự không phù hợp công trường theo chuẩn quốc tế và Việt Nam.
- Biểu mẫu **CRF (Change Request Form)** - Phiếu yêu cầu thay đổi thiết kế / vật tư.
- Biểu mẫu **Punchlist** - Danh mục khiếm khuyết tồn đọng tiền nghiệm thu COD.
- Xuất file PDF sắc nét, chuẩn font chữ tiếng Việt, hỗ trợ chèn logo doanh nghiệp, chữ ký số và bảng phân tích chi phí trực quan.

---

## 🚀 Hướng Dẫn Khởi Chạy Nhanh (Windows)

Hệ thống đã được đóng gói sẵn cụm cơ sở dữ liệu PostgreSQL nhúng (không cần cài đặt phần mềm bên ngoài).

### Cách 1: Khởi động 1-Click bằng file `.bat` (Khuyên dùng)
1. Tải hoặc clone repository về máy tính.
2. Nhấp đúp chuột vào tệp:
   ```cmd
   start-solar-vn.bat
   ```
3. Hệ thống sẽ tự động khởi động cơ sở dữ liệu, thiết lập môi trường `vietnam-solar` và tự động mở trình duyệt tại:
   👉 **`http://127.0.0.1:8080`**

### Cách 2: Khởi động bằng PowerShell
Mở PowerShell tại thư mục dự án và chạy:
```powershell
.\start-solar-vn.ps1
```

### Cách 3: Khởi động bằng dòng lệnh CLI
```powershell
$env:OE_PACK = "vietnam-solar"
$env:OE_LOCALE = "vi"
$env:OE_DEFAULT_CURRENCY = "VND"
.venv\Scripts\openconstructionerp.exe serve --host 127.0.0.1 --port 8080 --open
```

---

## 🔑 Tài Khoản Đăng Nhập

| Loại tài khoản | Email đăng nhập | Mật khẩu | Quyền hạn |
| :--- | :--- | :--- | :--- |
| **Quản trị viên (Admin)** | `admin@solar.vn` | `admin123` | Toàn quyền kiểm soát, cấu hình dự án, phân quyền |
| **Tài khoản Demo** | `demo@openconstructionerp.com` | `admin123` | Xem dữ liệu, duyệt biểu mẫu, quản lý hồ sơ |

---


## 📂 Cấu Trúc Thư Mục Dự Án

```
OpenConstructionSolar/
├── backend/                             # Backend FastAPI & SQLAlchemy Async
│   ├── app/
│   │   ├── core/
│   │   │   ├── demo_packs/              # Bộ dữ liệu mẫu Solar Rooftop & Solar Farm
│   │   │   └── demo_projects.py         # Seed 2 dự án VSIP II & Thuận Nam
│   │   └── modules/
│   │       ├── forms/                   # Module Biểu mẫu kỹ thuật (NCR, CRF, PDF Export)
│   │       └── projects/                # Quản lý tệp, Cây thư mục 12 nhóm SOP & Approvals
├── frontend/                            # Giao diện React 18, TypeScript, Tailwind CSS
│   └── src/
│       ├── app/layout/                  # Header, Sidebar (đã nội địa hóa tiếng Việt)
│       └── features/
│           ├── file-manager/            # Giao diện Cây thư mục 12 nhóm, Drill-down, Upload
│           └── forms/                   # Giao diện biểu mẫu, ký duyệt, xem trước PDF
├── packs/vietnam-solar/                 # Gói cấu hình chuyên dụng Vietnam Solar EPC
├── data/catalog/regions/                # Thư viện giá & định mức vật tư DDC_CWICR_VN_SOLAR
├── Template/                            # Tài liệu SOP & Biểu mẫu gốc của dự án
├── start-solar-vn.bat                   # Kịch bản khởi động 1-Click trên Windows
├── start-solar-vn.ps1                   # Kịch bản khởi động PowerShell
├── push-to-github.bat                   # Kịch bản đẩy dữ liệu lên GitHub
├── push-to-github.ps1                   # Kịch bản đẩy dữ liệu lên GitHub (PowerShell)
└── README.md                            # Tài liệu hướng dẫn sử dụng
```

---

## 🛠️ Công Nghệ Sử Dụng (Tech Stack)

- **Backend:** Python 3.12, FastAPI, SQLAlchemy 2.0 (Async), Pydantic v2, PostgreSQL (Embedded / External), Alembic.
- **Frontend:** React 18, TypeScript, Vite, Tailwind CSS, TanStack Query v5, Lucide Icons, AG Grid Community, Cesium / MapLibre GL.
- **Tài liệu & Kỹ thuật:** PDF Generation (ReportLab / jsPDF), ExcelJS, OCR Search Indexing.

---

## ⚖️ Giấy Phép & Ghi Nhận Bản Quyền (License & Acknowledgments)

- Dự án được xây dựng và phát triển dựa trên nền tảng mã nguồn mở **[OpenConstructionERP](https://github.com/datadrivenconstruction/OpenConstructionERP)** của tác giả **Artem Boiko / DataDrivenConstruction**.
- Toàn bộ mã nguồn được phân phối công khai theo giấy phép **GNU Affero General Public License v3.0 (AGPL-3.0)**.
- Dự án hoàn toàn phi lợi nhuận phục vụ mục đích nghiên cứu, học tập và triển khai cho cộng đồng kỹ sư xây dựng, năng lượng tái tạo tại Việt Nam.

---
*OpenConstructionSolar — Trao quyền chuyển đổi số cho ngành Năng lượng Tái tạo Việt Nam.*
