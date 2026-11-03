# NGUYÊN TẮC PHÁT TRIỂN & CHUẨN MỰC DỰ ÁN OPENCONSTRUCTIONSOLAR
*(Tài liệu định hướng kiến trúc, tiêu chuẩn kỹ thuật và quy trình kiểm thử chất lượng)*

Tài liệu này tổng hợp toàn bộ các nguyên tắc cốt lõi của nền tảng **OpenConstructionERP**, kết hợp cùng các tiêu chuẩn pháp lý & kỹ thuật chuyên sâu của phiên bản **Vietnam Solar EPC Edition**. Bất kỳ kỹ sư hay trợ lý AI nào khi xây dựng, chỉnh sửa hoặc biên dịch mã nguồn trong dự án này đều **bắt buộc tuân thủ nghiêm ngặt**.

---

## 1. TÔN CHỈ & KIẾN TRÚC HỆ THỐNG CỐT LÕI

1. **Nhẹ, Tối giản và Độc lập (Lightweight & Self-contained)**:
   - Cơ sở dữ liệu bắt buộc duy nhất là **PostgreSQL** (hỗ trợ Embedded PG không cần Docker cho môi trường cục bộ).
   - Không cài cắm các dependency nặng nề hoặc không cần thiết.
2. **Kiến trúc Hướng Module (Module-First Architecture)**:
   - Mọi tính năng backend phải là một module độc lập đặt trong `backend/app/modules/<module_name>/`.
   - **Bẫy chí mạng**: Thư mục module nếu thiếu file `manifest.py` sẽ hoàn toàn **vô hình (invisible)** đối với loader mà không sinh ra bất kỳ cảnh báo lỗi nào. Mọi module bắt buộc phải có `manifest.py` và `__init__.py`.
3. **Mô hình Dữ liệu Chuẩn & Chuyển đổi định dạng (Conversion-First)**:
   - Mọi dữ liệu CAD/BIM nhập vào đều được chuyển đổi về định dạng chuẩn nội bộ (canonical format) của nền tảng để các module đọc/ghi.
   - Tuyệt đối **không nhúng trực tiếp các thư viện hình học CAD/IFC nặng nề** vào trong backend hay frontend; việc xử lý hình học được thông qua chuyển đổi hoặc công cụ chuyên trách.
4. **Cơ chế AI Có Người Giám Sát (Human-in-the-Loop AI)**:
   - Các công cụ AI sửa đổi dữ liệu (bắt đầu bằng tiền tố `propose_*`) **không được tự ý ghi đè dữ liệu** vào database.
   - Luôn tạo ra một thẻ đề xuất (Proposal Card) kèm điểm tin cậy (`confidence` từ 0 đến 1) để người dùng xem xét, chấp thuận hoặc từ chối.
5. **Thẩm định & Kiểm tra tính hợp lệ là quy trình lõi (Validation-First)**:
   - Mọi module phải khai báo các quy tắc kiểm tra nghiệp vụ của mình trong `validators.py` và đăng ký vào `rule_registry`. Không có danh sách kiểm tra tập trung dùng chung.

---

## 2. QUY CHUẨN PHÁT TRIỂN BACKEND (PYTHON / FASTAPI)

### 2.1. Thứ tự viết mã nguồn module
Khi phát triển một module mới, bắt buộc triển khai theo đúng thứ tự phân lớp phụ thuộc:
```
backend/app/modules/<module_name>/
├── manifest.py      # [Bắt buộc] Khai báo metadata, version, dependencies
├── __init__.py      # [Bắt buộc] Khởi tạo package
├── models.py        # Định nghĩa bảng cơ sở dữ liệu SQLAlchemy
├── schemas.py       # Pydantic schemas (Request / Response validation)
├── repository.py    # Thao tác truy vấn dữ liệu (Data Access Layer)
├── service.py       # Logic nghiệp vụ (Business logic & Event publishing)
├── router.py        # Các API endpoints FastAPI (kebab-case)
├── permissions.py   # Phân quyền RBAC cho module
├── events.py        # Đăng ký nhận sự kiện từ các module khác
└── validators.py    # Bộ quy tắc kiểm tra hợp lệ nghiệp vụ
```
*Lưu ý*: Kiểm thử (Tests) phải đặt tại `backend/tests/`, không đặt bên trong thư mục module.

### 2.2. Quy ước API & Định tuyến
- URL endpoint sử dụng **kebab-case**: Thư mục `site_supervision` sẽ được ánh xạ thành `/api/v1/site-supervision`. (Định dạng gạch dưới `site_supervision` chỉ là bí danh tương thích cũ).
- Schema validation phải chặt chẽ (sử dụng `Literal`, regex pattern rõ ràng, không dùng kiểu chuỗi tự do để tránh lỗ hổng 422/500).

### 2.3. Định dạng Code & Linter
- **Line length**: Cố định **120 ký tự** (cấu hình tại `backend/pyproject.toml`).
- **Formatter & Linter**: Dùng `ruff format --check` và `ruff check`. Phải chạy lệnh từ bên trong thư mục `backend/` để nạp đúng file cấu hình.
- Type hints bắt buộc cho toàn bộ tham số và giá trị trả về của hàm public.

---

## 3. QUY CHUẨN PHÁT TRIỂN FRONTEND (REACT / TYPESCRIPT / VITE)

### 3.1. Phân biệt rõ hai hệ thống giao diện
1. **Core Screens (`frontend/src/features/<name>/`)**:
   - Dành cho các tính năng cốt lõi của nền tảng.
   - Phải import thủ công và khai báo route tường minh trong `frontend/src/app/App.tsx`.
2. **Opt-in Plugin Modules (`frontend/src/modules/<name>/`)**:
   - Dành cho các phân hệ mở rộng tùy chọn.
   - Khai báo qua `manifest.ts` và đăng ký 1 dòng duy nhất trong `frontend/src/modules/_registry.ts`. Giao diện tự động lazy-load, nạp menu và ghép i18n tự động.

### 3.2. Tiêu chuẩn Kiểm định Bản dựng (Build Gate)
- **`npm run build` là cổng kiểm soát duy nhất**:
  - `npm run typecheck` (`tsc --noEmit`) chỉ kiểm tra cú pháp nhanh và thường xuyên bỏ sót lỗi liên kết bundle thực tế.
  - Một thay đổi Frontend chỉ được coi là hoàn tất khi lệnh `npm run build` (`tsc -b` + `vite build`) chạy thành công và tạo ra bundle sạch trong thư mục `dist/`.

### 3.3. Thiết kế & Token màu sắc
- Sử dụng đúng bảng mã màu và component có sẵn: `text-content-primary`, `text-content-secondary`, `text-content-tertiary`, `bg-surface-elevated`, `border-border-light`, `oe-blue`.
- Tuyệt đối không pha màu hex cứng ngắt quãng làm mất tính nhất quán giữa chế độ Light và Dark mode.

---

## 4. QUY CHUẨN ĐA NGÔN NGỮ (I18N) - BẢO VỆ TRẢI NGHIỆM NGƯỜI DÙNG

1. **Tuyệt đối không hardcode chuỗi hiển thị**:
   - Mọi chuỗi văn bản người dùng nhìn thấy (nhãn nút, tiêu đề, thông báo lỗi, toast, placeholder) đều phải thông qua hàm `t('namespace.key')`.
2. **Cơ chế chống lỗi im lặng (Silent Fallback)**:
   - Nếu bạn thêm một key mới vào `en.ts` mà không thêm vào `vi.ts`, hệ thống không hề báo lỗi, TypeScript không báo lỗi, build vẫn xanh, nhưng toàn bộ người dùng tiếng Việt sẽ bị nhìn thấy chữ tiếng Anh rơi về fallback.
   - **Quy tắc bắt buộc**: Bất kỳ key nào thêm mới phải được cập nhật đồng thời ở cả **`vi.ts`** và **`en.ts`**.
3. **Giữ nguyên biến nội suy**: Khi dịch các chuỗi có tham số như `{{name}}`, `{{count}}`, `{{amount}}`, tuyệt đối không làm mất hoặc đổi tên biến bên trong dấu ngoặc nhọn kép.

---

## 5. HỆ THỐNG TIÊU CHUẨN EPC SOLAR VIỆT NAM (BẮT BUỘC)

Khi xây dựng các tính năng, biểu mẫu, logic tính toán hay tư vấn kỹ thuật trong phân hệ Solar EPC, bắt buộc đối chiếu theo hệ quy chuẩn sau:

1. **An toàn cháy & PCCC**:
   - Tuân thủ **QCVN 06** (Quy chuẩn an toàn cháy cho nhà và công trình) phiên bản hiện hành và Hướng dẫn số 3288/C07-PCCC.
   - Kiểm soát nghiêm ngặt: Lối thoát hiểm mái, hành lang kỹ thuật chữa cháy (khoảng lùi mép mái, lối đi bảo trì rộng tối thiểu 1.0 - 1.2m), vật liệu chống cháy lan, giải pháp ngắt mạch nhanh (**Rapid Shutdown**) cấp chuỗi/tấm pin.
2. **Tải trọng & Kết cấu công trình**:
   - Đối chiếu **QCVN 02** (Số liệu điều kiện tự nhiên) và **TCVN 2737** (Tải trọng và tác động) để tính áp lực gió bão cục bộ, tải tĩnh (Dead Load: module, rail, inverter) và tải động (Live Load bảo trì).
   - Yêu cầu báo cáo thẩm tra độ võng xà gồ, độ bền liên kết bulong/chân rail và dư tải kết cấu mái hiện hữu trước khi thi công.
3. **Tiêu chuẩn Thiết bị & Điện**:
   - Module PV: **IEC 61215**, **IEC 61730**.
   - Biến tần (Inverter): **IEC 62109** (An toàn biến tần), **IEC 61727** / **IEC 62116** (Anti-Islanding - chống phát ngược vào lưới mất điện).
   - Cáp DC chuyên dụng đạt chuẩn **EN 50618** / **IEC 62930**; độ sụt áp DC/AC thiết kế dưới **1 - 2%**; thiết bị chống sét lan truyền SPD Type 1/Type 2 theo **IEC 62305**; nối đất & đẳng thế theo **TCVN 9358** / **TCVN 9385**.
4. **Pháp lý Đấu nối & Đo đếm EVN**:
   - Tuân thủ Thông tư 39/2015/TT-BCT và Thông tư 30/2019/TT-BCT.
   - Hệ thống không bán điện bắt buộc có thiết bị chống phát ngược (**Zero Export controller**).
   - Tuân thủ **Nghị định 135/2024/NĐ-CP** (tự sản tự tiêu, bán dư tối đa 20%, miễn trừ GPĐL dưới 1.000 kW) và **Nghị định 80/2024/NĐ-CP** (DPPA).
5. **Zero-Hallucination**:
   - Tuyệt đối không tự bịa đặt số hiệu văn bản pháp luật hay mức phạt. Trích dẫn rõ: *Số hiệu, Cơ quan ban hành, Ngày có hiệu lực, Điều/Khoản cụ thể* và trạng thái *[Đang có hiệu lực] / [Đã hết hiệu lực] / [Dự thảo]*.

---

## 6. QUY TRÌNH KIỂM SOÁT HYGIENE & COMMIT (CHECKLIST)

Trước khi coi một công việc là hoàn thành và đưa vào commit:
- [ ] Backend: Chạy `ruff format --check` và `ruff check` từ thư mục `backend/`.
- [ ] Backend: Chạy unit test liên quan (`pytest`).
- [ ] Frontend: Chạy `npm run build` từ thư mục `frontend/` (đảm bảo 0 lỗi typecheck và bundle thành công).
- [ ] Đa ngôn ngữ: Đã bổ sung bản dịch tiếng Việt (`vi.ts`) và tiếng Anh (`en.ts`).
- [ ] Đồng bộ phiên bản: Nếu có nâng version, phải đồng bộ đủ trên 9 file (pyproject.toml, package.json, package-lock.json x2, tauri.conf.json, Cargo.toml, Cargo.lock, index.html, CHANGELOG.md).
- [ ] An toàn bảo mật: Không để lộ API key, token, mật khẩu hoặc dữ liệu nhạy cảm trong commit.
- [ ] Thông điệp commit: Tuân thủ chuẩn [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`).

