# DDC-CWICR-OE: DataDrivenConstruction · OpenConstructionERP
# Copyright (c) 2026 Artem Boiko / DataDrivenConstruction
from __future__ import annotations

from app.core.demo_projects import DemoTemplate

# ---------------------------------------------------------------------------
# Vietnam Solar EPC Industry Pack - Flagship C&I Rooftop Demo Project
# Commercial & Industrial (C&I) Rooftop Solar PV, Turnkey EPC.
#
# Program:  3.5 MWp DC Rooftop Solar PV System on Industrial Factory
#           (~2.8 MWac point of coupling, DC/AC ratio ~1.25)
#           Self-consumption model with Zero-Export Controller per Decree 135/2024/ND-CP
#           + 3000 kVA 0.4/22 kV Compact Substation + 24 kV RMU.
#
# Location: VSIP II Industrial Park, Thu Dau Mot, Binh Duong Province, Vietnam.
# Currency / Price Level: VND, Vietnam 2026.
# Standards: TCVN 11855-1:2017 / IEC 62446-1:2016 (commissioning & testing),
#            TCVN 6781 / IEC 61215 & TCVN 10884 / IEC 61730 (PV module safety),
#            QCVN 06:2022/BXD & Document 3288/C07-P4 (Fire safety & walkways),
#            Circular 39/2015/TT-BCT & TT 30/2019/TT-BCT (EVN Distribution Grid Code),
#            QCVN 01:2020/BCT (Electrical safety & earthing R < 4 Ohms),
#            Circular 11/2021/TT-BXD (Cost breakdown & statutory markup structure).
# ---------------------------------------------------------------------------

TEMPLATE = DemoTemplate(
    demo_id="vietnam-solar-rooftop-epc",
    project_name="Dự án ĐMT Áp Mái KCN VSIP II - 3.5 MWp (C&I Rooftop Solar)",
    project_description=(
        "Hợp đồng tổng thầu EPC trọn gói hệ thống Điện mặt trời áp mái nhà xưởng 3.500 kWp DC "
        "(~2.800 kWac) tại KCN VSIP II, tỉnh Bình Dương. Thiết kế theo mô hình tự sản xuất tự tiêu thụ "
        "trang bị bộ điều khiển chống phát ngược Zero-Export Controller theo Nghị định 135/2024/NĐ-CP. "
        "Sử dụng tấm pin N-type TOPCon hai mặt kính 585 Wp Tier 1, biến tần chuỗi 110 kW - 125 kW, "
        "trạm biến áp nâng áp hợp bộ 3000 kVA 0.4/22kV, tủ đóng cắt trung thế RMU 24kV, hệ khung rail nhôm "
        "anodize kẹp ngàm seamlock chống dột mái và hệ thống PCCC theo Văn bản 3288/C07-P4. "
        "Tổng giá trị dự toán EPC xấp xỉ 42,5 tỷ VNĐ (khoảng 12,1 triệu VNĐ/kWp)."
    ),
    region="VN",
    classification_standard="masterformat",
    currency="VND",
    locale="vi",
    address={
        "street": "Đường D1, Khu công nghiệp VSIP II, Phường Hòa Phú",
        "city": "Thủ Dầu Một",
        "postcode": "75000",
        "country": "Vietnam",
        "lat": 11.0528,
        "lng": 106.6661,
    },
    validation_rule_sets=["masterformat", "boq_quality"],
    boq_name="Dự toán Tổng thầu EPC - Điện Mặt Trời Áp Mái 3.5 MWp",
    boq_description=(
        "Bảng dự toán chi tiết khối lượng và chi phí xây lắp EPC hệ thống điện mặt trời mái nhà 3.5 MWp "
        "theo định mức xây dựng và giá vật tư thiết bị thị trường Việt Nam 2026."
    ),
    boq_metadata={
        "standard": "MasterFormat / TCVN / DDC Vietnam Solar",
        "phase": "Dự toán thi công EPC chi tiết (EPC Detailed Estimate)",
        "base_date": "2026-Q1",
        "price_level": "Vietnam 2026",
    },
    sections=[
        # -- 01 Khảo sát, Thiết kế & Thủ tục pháp lý --------------------------
        (
            "01",
            "01 - Khảo sát, Thiết kế Kỹ thuật & Thủ tục Pháp lý Dự án",
            {"masterformat": "01"},
            [
                ("01.001", "Khảo sát đo đạc hiện trạng mái, kiểm định chịu lực kết cấu mái nhà xưởng", "lsum", 1, 145000000.0, {"masterformat": "01 31 00"}),
                ("01.002", "Thiết kế kỹ thuật thi công, bản vẽ PVSyst mô phỏng sản lượng điện", "lsum", 1, 185000000.0, {"masterformat": "01 33 00"}),
                ("01.003", "Hồ sơ thẩm duyệt thiết kế PCCC theo QCVN 06 & Văn bản 3288/C07-P4", "lsum", 1, 120000000.0, {"masterformat": "01 45 00"}),
                ("01.004", "Hồ sơ thỏa thuận đấu nối kỹ thuật với Điện lực Bình Dương (EVN SPC)", "lsum", 1, 95000000.0, {"masterformat": "01 45 00"}),
                ("01.005", "Đăng ký phát triển ĐMT tự sản tự tiêu theo Nghị định 135/2024/NĐ-CP", "lsum", 1, 65000000.0, {"masterformat": "01 45 00"}),
                ("01.006", "Quản lý dự án, chỉ huy trưởng công trường và giám sát an toàn HSE", "month", 4, 85000000.0, {"masterformat": "01 31 00"}),
                ("01.007", "Lán trại tạm, kho bãi tập kết vật tư và văn phòng điều hành công trường", "lsum", 1, 90000000.0, {"masterformat": "01 52 00"}),
                ("01.008", "Hồ sơ hoàn công, quy trình vận hành bảo dưỡng O&M và đào tạo chuyển giao", "lsum", 1, 75000000.0, {"masterformat": "01 78 00"}),
                ("01.009", "Bảo hiểm mọi rủi ro xây dựng lắp đặt công trình (CAR/EAR Insurance)", "lsum", 1, 65000000.0, {"masterformat": "01 31 00"}),
            ],
        ),
        # -- 48A Tấm pin quang điện PV Modules ---------------------------------
        (
            "48A",
            "48 - Tấm Pin Quang Điện PV Modules (TCVN 6781 / IEC 61215)",
            {"masterformat": "48"},
            [
                ("48A.001", "Tấm pin quang điện Mono TOPCon 585 Wp hai mặt kính (Tier 1 JA/LONGi)", "pcs", 5984, 1850000.0, {"masterformat": "48 14 00"}),
                ("48A.002", "Nhân công bốc dỡ, cẩu chuyển tấm pin lên mái nhà xưởng cao 12m", "pcs", 5984, 45000.0, {"masterformat": "48 14 00"}),
                ("48A.003", "Lắp đặt, căn chỉnh và siết bu-lông lực mô-men tấm pin lên khung giá đỡ", "pcs", 5984, 95000.0, {"masterformat": "48 14 00"}),
                ("48A.004", "Tấm pin dự phòng chiến lược thay thế (kho lưu trữ 1.5%)", "pcs", 90, 1850000.0, {"masterformat": "48 14 00"}),
                ("48A.005", "Đo kiểm kiểm định flash-test và chụp ảnh quang huỳnh quang (EL) tại công trường", "lsum", 1, 68000000.0, {"masterformat": "48 14 00"}),
            ],
        ),
        # -- 48B Biến tần hòa lưới Inverters ----------------------------------
        (
            "48B",
            "48 - Biến Tần Hòa Lưới String Inverters (IEC 62109)",
            {"masterformat": "48"},
            [
                ("48B.001", "Biến tần chuỗi 3 pha String Inverter 110 kW - 125 kW (Sungrow/Huawei)", "pcs", 24, 95000000.0, {"masterformat": "48 15 00"}),
                ("48B.002", "Hệ thống giá treo biến tần, mái che bảo vệ chống mưa nắng trực tiếp", "pcs", 24, 6500000.0, {"masterformat": "48 15 00"}),
                ("48B.003", "Thi công lắp đặt cơ điện, đấu nối cáp AC/DC vào biến tần", "pcs", 24, 8500000.0, {"masterformat": "48 15 00"}),
                ("48B.004", "Cài đặt tham số hòa lưới, hiệu chỉnh công suất phản kháng và bảo vệ tần số", "pcs", 24, 4500000.0, {"masterformat": "48 15 00"}),
            ],
        ),
        # -- 34 Khung giàn giá đỡ & Cơ khí lắp mái ----------------------------
        (
            "34",
            "34 - Hệ Khung Giàn Giá Đỡ & Ray Nhôm Kẹp Tôn Seamlock",
            {"masterformat": "34"},
            [
                ("34.001", "Ray nhôm hợp kim AL6005-T5 anodized mạ bạc chịu tải gió bão Vùng II", "m", 16800, 145000.0, {"masterformat": "34 71 00"}),
                ("34.002", "Kẹp sóng tôn seamlock chân nhôm đúc áp lực cao không bắn vít thủng tôn", "pcs", 14200, 48000.0, {"masterformat": "34 71 00"}),
                ("34.003", "Kẹp giữa (Mid clamp) và Kẹp biên (End clamp) nhôm anodized kèm bu-lông Inox 304", "pcs", 13600, 22000.0, {"masterformat": "34 71 00"}),
                ("34.004", "Chân giá đỡ chữ L (L-feet) và kẹp tiếp địa đồng bộ khung nhôm", "pcs", 3800, 32000.0, {"masterformat": "34 71 00"}),
                ("34.005", "Nhân công lắp đặt, căn chỉnh phẳng hệ khung ray nhôm trên mái tôn", "m", 16800, 38000.0, {"masterformat": "34 71 00"}),
                ("34.006", "Hành lang lối đi phục vụ cứu nạn và bảo trì PCCC bề rộng 1.5m (Walkway grating)", "m", 1200, 380000.0, {"masterformat": "34 71 00"}),
                ("34.007", "Dây cáp thép giằng an toàn chống rơi cho công nhân thi công trên mái (Lifeline safety)", "m", 650, 85000.0, {"masterformat": "34 71 00"}),
            ],
        ),
        # -- 48C Hệ thống cáp DC & Phụ kiện đấu nối ---------------------------
        (
            "48C",
            "48 - Cáp Điện DC Chuyên Dụng Solar & Phụ Kiện (IEC 62930)",
            {"masterformat": "48"},
            [
                ("48C.001", "Cáp Solar DC 1x4.0 mm² ruột đồng tráng thiếc cách điện kép XLPO 1500V", "m", 38000, 14500.0, {"masterformat": "48 14 00"}),
                ("48C.002", "Cáp Solar DC 1x6.0 mm² chống tia cực tím UV và kháng ozone", "m", 22000, 19800.0, {"masterformat": "48 14 00"}),
                ("48C.003", "Đầu nối chuyên dụng MC4 IP68 chính hãng Staubli (cặp đực/cái)", "pcs", 1850, 42000.0, {"masterformat": "48 14 00"}),
                ("48C.004", "Máng cáp lưới inox / tôn mạ kẽm nhúng nóng W200xH100 có nắp đậy", "m", 2400, 265000.0, {"masterformat": "48 14 00"}),
                ("48C.005", "Ống luồn mềm bảo vệ cáp DC luồn ruột gà bọc nhựa PVC ngoài trời", "m", 4800, 28000.0, {"masterformat": "48 14 00"}),
                ("48C.006", "Thi công luồn kéo cáp DC, bấm đầu cosse MC4 và bó kẹp cáp vào ray", "m", 60000, 8500.0, {"masterformat": "48 14 00"}),
            ],
        ),
        # -- 48D Hệ thống AC, Trạm biến áp & Tủ trung thế ---------------------
        (
            "48D",
            "48 - Hệ Thống AC, Trạm Biến Áp Nâng Áp & Đóng Cắt Trung Thế",
            {"masterformat": "48"},
            [
                ("48D.001", "Tủ gom hạ thế AC Combiner Box 400V tích hợp MCCB & thiết bị chống sét SPD", "pcs", 6, 85000000.0, {"masterformat": "48 13 00"}),
                ("48D.002", "Cáp hạ thế 0.6/1kV Cu/XLPE/PVC/DSTA/PVC 3x240+1x150 mm² (Cadivi)", "m", 2200, 780000.0, {"masterformat": "48 13 00"}),
                ("48D.003", "Trạm biến áp hợp bộ (Kiosk substation) 3000 kVA 0.4/22 kV (Thibidi)", "pcs", 1, 1450000000.0, {"masterformat": "48 13 00"}),
                ("48D.004", "Tủ đóng cắt trung thế RMU 24 kV 3 ngăn Compact SF6-free (Schneider/ABB)", "pcs", 1, 420000000.0, {"masterformat": "48 13 00"}),
                ("48D.005", "Cáp ngầm trung thế 24 kV Cu/XLPE/PVC 3x95 mm² kết nối lưới 22kV", "m", 450, 480000.0, {"masterformat": "48 13 00"}),
                ("48D.006", "Hố móng bê tông cốt thép đặt trạm biến áp, mương cáp ngầm và rào chắn", "m3", 45, 3400000.0, {"masterformat": "48 13 00"}),
                ("48D.007", "Đầu cáp ngầm trung thế co nguội 24kV ngoài trời và trong nhà", "pcs", 6, 8500000.0, {"masterformat": "48 13 00"}),
            ],
        ),
        # -- 25 SCADA, Giám sát & Bộ chống phát ngược Zero-Export -------------
        (
            "25",
            "25 - SCADA, Giám Sát Năng Lượng & Hệ Thống Zero-Export (NĐ 135)",
            {"masterformat": "25"},
            [
                ("25.001", "Bộ điều khiển chống phát ngược Zero-Export Controller chính hãng", "pcs", 1, 125000000.0, {"masterformat": "25 35 00"}),
                ("25.002", "Đồng hồ đo đa năng Smart Power Meter 3 pha cấp chính xác Class 0.5S (Acrel/Chint)", "pcs", 2, 28000000.0, {"masterformat": "25 35 00"}),
                ("25.003", "Biến dòng đo lường Current Transformer (CT) tỷ số biến 5000/5A Class 0.5", "pcs", 6, 6500000.0, {"masterformat": "25 35 00"}),
                ("25.004", "Hệ thống SCADA giám sát thời gian thực, bảng điều khiển EMS trên Web/App", "lsum", 1, 145000000.0, {"masterformat": "25 35 00"}),
                ("25.005", "Trạm quan trắc thời tiết: Cảm biến bức xạ mặt trời (Pyranometer) & cảm biến nhiệt độ tấm pin", "pcs", 2, 45000000.0, {"masterformat": "25 14 00"}),
                ("25.006", "Tủ truyền thông dữ liệu công trường, Switch công nghiệp & đường truyền cáp quang", "lsum", 1, 68000000.0, {"masterformat": "25 13 00"}),
            ],
        ),
        # -- 26 Tiếp địa, Chống sét & An toàn PCCC -----------------------------
        (
            "26",
            "26 - Tiếp Địa Đẳng Thế, Chống Sét & Nút Ngắt Khẩn Cấp PCCC",
            {"masterformat": "26"},
            [
                ("26.001", "Kim thu sét phóng điện sớm tia tiên đạo bán kính bảo vệ R = 60m (Erico/Stormaster)", "pcs", 2, 42000000.0, {"masterformat": "26 41 00"}),
                ("26.002", "Cột đỡ kim thu sét mạ kẽm cao 5m kèm bộ giằng neo chịu gió bão", "pcs", 2, 9500000.0, {"masterformat": "26 41 00"}),
                ("26.003", "Cáp đồng trần tiếp địa M70 (Bare Copper 70 mm²) liên kết toàn bộ mái", "m", 3200, 165000.0, {"masterformat": "26 05 26"}),
                ("26.004", "Cọc tiếp địa mạ đồng D16 L2.4m hàn hóa nhiệt Cadweld đạt R < 4 Ohm theo QCVN 01", "pcs", 48, 480000.0, {"masterformat": "26 05 26"}),
                ("26.005", "Dây đồng bện tiếp địa liên kết đẳng thế khung nhôm và vỏ thiết bị inverter", "pcs", 240, 65000.0, {"masterformat": "26 05 26"}),
                ("26.006", "Hệ thống nút bấm ngắt khẩn cấp Rapid Shutdown ngắt điện DC tại mặt đất phục vụ PCCC", "pcs", 4, 35000000.0, {"masterformat": "26 28 00"}),
                ("26.007", "Hệ thống bình chữa cháy tự động khí sạch FM200/Aerosol cho trạm biến áp", "lsum", 1, 95000000.0, {"masterformat": "26 28 00"}),
                ("26.008", "Bộ thiết bị cắt lọc sét lan truyền nguồn AC SPD Type 1+2 (Surge Protective Device)", "pcs", 6, 18500000.0, {"masterformat": "26 43 13"}),
            ],
        ),
        # -- 48F Thử nghiệm, Nghiệm thu COD & Đóng điện -----------------------
        (
            "48F",
            "48 - Thí Nghiệm Đo Kiểm, Nghiệm Thu COD & Đóng Điện (TCVN 11855)",
            {"masterformat": "48"},
            [
                ("48F.001", "Đo kiểm điện trở cách điện R_iso và đường đặc tuyến I-V theo TCVN 11855 / IEC 62446", "lsum", 1, 85000000.0, {"masterformat": "48 19 00"}),
                ("48F.002", "Thí nghiệm hiệu chỉnh trạm biến áp, rơ le bảo vệ 24kV phối hợp với Trung tâm Thí nghiệm điện", "lsum", 1, 115000000.0, {"masterformat": "48 19 00"}),
                ("48F.003", "Thử nghiệm đóng cắt chức năng chống phát ngược Zero-Export với tải thực tế của nhà máy", "lsum", 1, 55000000.0, {"masterformat": "48 19 00"}),
                ("48F.004", "Kiểm tra nghiệm thu an toàn PCCC với Cơ quan Cảnh sát PCCC tỉnh Bình Dương", "lsum", 1, 75000000.0, {"masterformat": "48 19 00"}),
                ("48F.005", "Thử nghiệm đóng điện nghiệm thu thương mại COD và bàn giao vận hành hệ thống", "lsum", 1, 95000000.0, {"masterformat": "48 19 00"}),
            ],
        ),
    ],
    markups=[
        ("Chi phí chung (Overhead theo TT 11/2021/TT-BXD)", 6.5, "overhead", "direct_cost"),
        ("Chi phí nhà tạm để ở và điều hành thi công", 1.2, "overhead", "direct_cost"),
        ("Chi phí một số công việc không xác định từ thiết kế", 2.0, "contingency", "direct_cost"),
        ("Thu nhập chịu thuế tính trước (Profit)", 6.0, "profit", "cumulative"),
        ("Thuế giá trị gia tăng (VAT 8% theo NĐ 72/2024)", 8.0, "tax", "cumulative"),
    ],
    total_months=4,
    tender_name="Gói thầu Mua sắm Tấm pin & Biến tần Hòa lưới 3.5 MWp",
    tender_companies=[
        ("Công ty Cổ phần Năng lượng Tái tạo Sông Đà", "tenders@songda-energy.example.vn", 0.98),
        ("Tập đoàn Công nghệ Năng lượng Xanh Việt Nam", "epc-bids@vngreen-energy.example.vn", 1.02),
        ("Công ty TNHH Cơ điện & Năng lượng Mặt trời Á Châu", "duan@achau-solar.example.vn", 0.99),
    ],
    project_metadata={
        "client": "Công ty TNHH Sản xuất & Thương mại Quốc tế VSIP",
        "epc_contractor": "Liên danh Tổng thầu Solar EPC Việt Nam",
        "owner_engineer": "Tư vấn Năng lượng Tái tạo Quốc gia",
        "dc_capacity_kwp": 3500,
        "ac_capacity_kwac": 2800,
        "dc_ac_ratio": 1.25,
        "roof_type": "Mái tôn Seamlock nhà xưởng công nghiệp KCN",
        "roof_area_m2": 24000,
        "tilt_angle_deg": 11,
        "azimuth_deg": 180,
        "module_count": 5984,
        "module_type": "N-Type TOPCon 585 Wp Bifacial (JA Solar / LONGi)",
        "inverter_type": "String Inverter 110 kW - 125 kW (Sungrow / Huawei)",
        "grid_connection_voltage_kv": 22,
        "regulatory_scheme": "Nghị định 135/2024/NĐ-CP (Tự sản tự tiêu - Zero Export)",
        "expected_annual_yield_mwh": 5180,
        "co2_avoided_ton_per_year": 4450,
        "standards": [
            "TCVN 11855-1:2017 / IEC 62446-1:2016",
            "TCVN 6781:2017 / IEC 61215:2016",
            "TCVN 10884:2015 / IEC 61730:2011",
            "QCVN 06:2022/BXD & Document 3288/C07-P4",
            "Circular 39/2015/TT-BCT & TT 30/2019/TT-BCT (EVN)",
            "QCVN 01:2020/BCT (Electrical safety)",
            "Circular 11/2021/TT-BXD (Cost estimate structure)",
        ],
    },
    tender_packages=[
        (
            "Cung cấp thiết bị chính (Tấm pin PV & Biến tần Inverter)",
            "Cung cấp tấm pin 585 Wp TOPCon, biến tần chuỗi 110/125 kW, kiểm định TCVN",
            "awarded",
            [
                ("Tập đoàn Công nghệ Năng lượng Xanh Việt Nam", "epc-bids@vngreen-energy.example.vn", 0.98),
                ("Công ty TNHH Thiết bị Năng lượng Toàn Cầu", "sales@global-energy.example.vn", 1.03),
                ("Công ty Cổ phần Năng lượng Tái tạo Sông Đà", "tenders@songda-energy.example.vn", 1.01),
            ],
        ),
        (
            "Thi công cơ khí, khung ray nhôm & an toàn PCCC",
            "Hệ ray nhôm kẹp seamlock, walkway 1.5m, kim thu sét và hành lang PCCC",
            "evaluating",
            [
                ("Công ty Cơ điện & Xây lắp Công nghiệp Nam Phát", "thau@namphat-mep.example.vn", 0.97),
                ("Công ty TNHH Cơ điện & Năng lượng Mặt trời Á Châu", "duan@achau-solar.example.vn", 1.02),
                ("Công ty Cổ phần Kết cấu Thép & Năng lượng Sài Gòn", "bids@saigon-steel.example.vn", 0.99),
            ],
        ),
        (
            "Trạm biến áp 3000 kVA, Tủ RMU 24kV & Đấu nối EVN",
            "Trạm biến áp hợp bộ Kiosk, tủ RMU, cáp ngầm trung thế và nghiệm thu EVN",
            "evaluating",
            [
                ("Công ty Thiết bị Điện & Xây lắp Lưới điện Miền Nam", "grid@dienmiennam.example.vn", 0.99),
                ("Công ty Cổ phần Kỹ thuật Điện Miền Đông", "duan@miendong-electric.example.vn", 1.04),
                ("Tổng công ty Thiết bị Điện Đông Anh (Chi nhánh miền Nam)", "sales@donganh-electric.example.vn", 1.01),
            ],
        ),
    ],
)

