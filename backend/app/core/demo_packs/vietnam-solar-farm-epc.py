# DDC-CWICR-OE: DataDrivenConstruction · OpenConstructionERP
# Copyright (c) 2026 Artem Boiko / DataDrivenConstruction
from __future__ import annotations

from app.core.demo_projects import DemoTemplate

# ---------------------------------------------------------------------------
# Vietnam Solar EPC Industry Pack - Utility-scale Solar Farm + BESS
# Ground-mounted Utility Solar PV + Battery Energy Storage (BESS), Turnkey EPC.
#
# Program:  50 MWp DC Ground-mount Solar PV Plant
#           (~38 MWac point of interconnection, DC/AC ratio ~1.32)
#           + 10 MWh / 5 MW Lithium Iron Phosphate (LFP) BESS
#           + 110 kV Step-up Substation & 110 kV Transmission Bay.
#           Operating under the Direct Power Purchase Agreement (DPPA)
#           mechanism per Decree 80/2024/ND-CP.
#
# Location: Thuan Nam District, Ninh Thuan Province, Vietnam.
# Currency / Price Level: VND, Vietnam 2026.
# Standards: TCVN 11855-1:2017 / IEC 62446-1:2016,
#            Circular 25/2016/TT-BCT & Circular 30/2019/TT-BCT (EVN Grid Codes),
#            QCVN 01:2020/BCT (Electrical safety), QCVN 02:2022/BXD (Wind load),
#            IEC 62619 / NFPA 855 (BESS battery energy storage safety),
#            Circular 11/2021/TT-BXD (Cost breakdown & statutory markup structure).
# ---------------------------------------------------------------------------

TEMPLATE = DemoTemplate(
    demo_id="vietnam-solar-farm-epc",
    project_name="Nhà Máy ĐMT Thuận Nam - 50 MWp + BESS 10 MWh (Cơ Chế DPPA)",
    project_description=(
        "Dự án Tổng thầu EPC Nhà máy điện mặt trời mặt đất công suất 50 MWp DC (~38 MWac) "
        "kết hợp hệ thống pin lưu trữ năng lượng BESS 10 MWh / 5 MW tại huyện Thuận Nam, tỉnh Ninh Thuận. "
        "Dự án áp dụng cơ chế mua bán điện trực tiếp (DPPA) theo Nghị định 80/2024/NĐ-CP, kết nối xuất công suất "
        "lên lưới điện truyền tải 110kV của EVN. Sử dụng tấm pin Mono Bifacial công suất 620 Wp gắn trên hệ khung giá "
        "đỡ thép mạ kẽm nhúng nóng cọc ép tĩnh, hệ thống biến tần chuỗi 330 kW, trạm biến áp nâng áp 22/110 kV 63 MVA, "
        "và hệ thống lưu trữ container LFP tích hợp quản lý năng lượng EMS. "
        "Tổng giá trị dự toán EPC đạt xấp xỉ 695 tỷ VNĐ."
    ),
    region="VN",
    classification_standard="masterformat",
    currency="VND",
    locale="vi",
    address={
        "street": "Khu vực đồng muối Quán Thẻ, Xã Phước Minh",
        "city": "Thuận Nam",
        "postcode": "59000",
        "country": "Vietnam",
        "lat": 11.4125,
        "lng": 108.9247,
    },
    validation_rule_sets=["masterformat", "boq_quality"],
    boq_name="Dự toán Tổng thầu EPC - Nhà Máy Điện Mặt Trời 50 MWp + BESS",
    boq_description=(
        "Bảng dự toán chi tiết các hạng mục xây dựng, mua sắm thiết bị và thí nghiệm đóng điện "
        "nhà máy ĐMT 50 MWp + BESS 10 MWh và Trạm biến áp 110kV tại Ninh Thuận."
    ),
    boq_metadata={
        "standard": "MasterFormat / TCVN / DDC Vietnam Solar",
        "phase": "Dự toán thi công EPC chi tiết (FID Stage)",
        "base_date": "2026-Q1",
        "price_level": "Vietnam 2026",
    },
    sections=[
        # -- 01 Quản lý dự án & Chi phí chung EPC -----------------------------
        (
            "01",
            "01 - Quản lý Dự án & Các Yêu Cầu Chung của Hợp Đồng EPC",
            {"masterformat": "01"},
            [
                ("01.001", "Ban quản lý dự án tổng thầu EPC, kỹ sư giám sát trưởng và chuyên viên HSE", "month", 12, 185000000.0, {"masterformat": "01 31 00"}),
                ("01.002", "Khảo sát địa hình, khảo sát địa chất công trình và đo điện trở suất đất bãi cọc", "lsum", 1, 450000000.0, {"masterformat": "01 31 00"}),
                ("01.003", "Thiết kế kỹ thuật thi công, thẩm tra thiết kế và mô phỏng năng lượng SolarGIS/PVSyst", "lsum", 1, 980000000.0, {"masterformat": "01 33 00"}),
                ("01.004", "Báo cáo đánh giá tác động môi trường ĐTM & hồ sơ thẩm duyệt PCCC Công an tỉnh Ninh Thuận", "lsum", 1, 520000000.0, {"masterformat": "01 45 00"}),
                ("01.005", "Thỏa thuận đấu nối 110kV và thỏa thuận rơ le bảo vệ với EVN CPC & Trung tâm Điều độ A0", "lsum", 1, 650000000.0, {"masterformat": "01 45 00"}),
                ("01.006", "Văn phòng ban chỉ huy, khu nhà nghỉ công nhân, kho vật tư và hàng rào tạm công trường", "month", 12, 65000000.0, {"masterformat": "01 52 00"}),
                ("01.007", "Điện, nước tạm thi công và trạm phát điện diesel dự phòng 250 kVA", "month", 12, 48000000.0, {"masterformat": "01 51 00"}),
                ("01.008", "Hồ sơ hoàn công, quy trình COD và đào tạo chuyển giao vận hành nhà máy", "lsum", 1, 380000000.0, {"masterformat": "01 78 00"}),
            ],
        ),
        # -- 31 San nền & Công tác đất -----------------------------------------
        (
            "31",
            "31 - Chuẩn Bị Mặt Bằng, San Lấp & Thoát Nước Trọng Yếu (60 ha)",
            {"masterformat": "31"},
            [
                ("31.001", "Phát quang bụi rậm, bóc dọn lớp đất hữu cơ bề mặt diện tích 60 ha", "ha", 60, 28000000.0, {"masterformat": "31 11 00"}),
                ("31.002", "Đào đắp, san gạt tạo mặt bằng độ dốc thoát nước khu vực lắp đặt pin", "m3", 145000, 48000.0, {"masterformat": "31 22 00"}),
                ("31.003", "Hệ thống mương hở thoát nước mưa bằng bê tông đúc sẵn B600-B1000", "m", 8500, 680000.0, {"masterformat": "31 25 00"}),
                ("31.004", "Mương cáp ngầm nội bộ, đào rãnh cáp, rải cát đệm và tấm đan bảo vệ", "m", 28000, 145000.0, {"masterformat": "31 23 33"}),
                ("31.005", "Đường giao thông nội bộ kết cấu cấp phối đá dăm lu lèn dày 20cm, rộng 5m", "m2", 35000, 165000.0, {"masterformat": "31 23 23"}),
                ("31.006", "Hàng rào bảo vệ chu vi khu đất bằng lưới thép B40 mạ kẽm cao 2.4m kèm dây kẽm gai", "m", 4800, 420000.0, {"masterformat": "31 23 23"}),
            ],
        ),
        # -- 34 Cọc móng & Khung giá đỡ thép mạ kẽm ---------------------------
        (
            "34",
            "34 - Cọc Móng Ép Tĩnh & Hệ Khung Giá Đỡ Thép Mạ Kẽm Nhúng Nóng",
            {"masterformat": "34"},
            [
                ("34.001", "Cọc thép dập hình C/U mạ kẽm nhúng nóng dày lớp mạ ≥ 80 μm chống ăn mòn đất mặn", "pcs", 24500, 480000.0, {"masterformat": "34 71 00"}),
                ("34.002", "Nhân công và máy ép cọc tĩnh định vị tọa độ GPS chính xác", "pcs", 24500, 120000.0, {"masterformat": "34 71 00"}),
                ("34.003", "Thí nghiệm kéo nhổ (Pull-out test) và nén tĩnh kiểm tra sức chịu tải cọc", "pcs", 120, 2500000.0, {"masterformat": "34 71 00"}),
                ("34.004", "Khung giàn giá đỡ xà gồ thép mạ kẽm nhúng nóng cố định góc nghiêng 12° đón nắng", "t", 1450, 36000000.0, {"masterformat": "34 71 00"}),
                ("34.005", "Phụ kiện liên kết, bu-lông đai ốc Inox 304 và kẹp pin chuyên dụng", "t", 65, 68000000.0, {"masterformat": "34 71 00"}),
                ("34.006", "Lắp dựng, căn chỉnh cơ khí hệ khung giá đỡ pin", "t", 1450, 5500000.0, {"masterformat": "34 71 00"}),
            ],
        ),
        # -- 48A Tấm pin năng lượng mặt trời 620 Wp ---------------------------
        (
            "48A",
            "48 - Tấm Pin Quang Điện Mono Bifacial 620 Wp (TCVN 6781)",
            {"masterformat": "48"},
            [
                ("48A.001", "Tấm pin Mono N-Type TOPCon hai mặt kính 620 Wp Tier 1 (JA / Jinko / Canadian)", "pcs", 80645, 1950000.0, {"masterformat": "48 14 00"}),
                ("48A.002", "Vận chuyển nội địa, bốc dỡ và phân phối tấm pin đến từng block mảng pin", "pcs", 80645, 25000.0, {"masterformat": "48 14 00"}),
                ("48A.003", "Thi công lắp đặt tấm pin lên xà gồ, siết lực cân lực theo tiêu chuẩn nhà sản xuất", "pcs", 80645, 55000.0, {"masterformat": "48 14 00"}),
                ("48A.004", "Tấm pin dự phòng chiến lược (1.0% tổng số lượng)", "pcs", 806, 1950000.0, {"masterformat": "48 14 00"}),
                ("48A.005", "Kiểm định chất lượng tấm pin độc lập tại phòng lab quốc tế và công trường", "lsum", 1, 280000000.0, {"masterformat": "48 14 00"}),
            ],
        ),
        # -- 48B Biến tần String Inverter 330 kW ------------------------------
        (
            "48B",
            "48 - Biến Tần Chuỗi Công Suất Lớn String Inverter 330 kW",
            {"masterformat": "48"},
            [
                ("48B.001", "Biến tần chuỗi 3 pha String Inverter 330 kW điện áp DC 1500V (Sungrow/Huawei)", "pcs", 115, 245000000.0, {"masterformat": "48 15 00"}),
                ("48B.002", "Giá đỡ biến tần ngoài trời bằng thép mạ kẽm kèm mái che tản nhiệt", "pcs", 115, 9500000.0, {"masterformat": "48 15 00"}),
                ("48B.003", "Thi công lắp đặt cơ điện, đấu nối cáp AC/DC vào biến tần 330 kW", "pcs", 115, 12000000.0, {"masterformat": "48 15 00"}),
                ("48B.004", "Kiểm tra cấu hình, hiệu chỉnh đáp ứng tần số P(f) và điện áp Q(U) theo Grid Code EVN", "pcs", 115, 6500000.0, {"masterformat": "48 15 00"}),
            ],
        ),
        # -- 48C Hệ thống cáp DC & Gom chuỗi ----------------------------------
        (
            "48C",
            "48 - Hệ Thống Cáp Điện DC 1500V & Đầu Nối Chuyên Dụng Solar",
            {"masterformat": "48"},
            [
                ("48C.001", "Cáp Solar DC 1x4.0 mm² ruột đồng tráng thiếc cách điện XLPO 1500V", "m", 320000, 14500.0, {"masterformat": "48 14 00"}),
                ("48C.002", "Cáp Solar DC 1x6.0 mm² chống chịu bức xạ UV khắc nghiệt", "m", 185000, 19800.0, {"masterformat": "48 14 00"}),
                ("48C.003", "Đầu nối chuyên dụng MC4-Evo2 1500V IP68 chính hãng", "pcs", 12500, 45000.0, {"masterformat": "48 14 00"}),
                ("48C.004", "Ống bảo vệ cáp luồn dưới lòng đất HDPE gân xoắn chịu lực D65/50", "m", 35000, 24000.0, {"masterformat": "48 14 00"}),
                ("48C.005", "Thi công rải cáp, đấu nối và đánh số dây nhãn mác chống phai màu", "m", 505000, 6500.0, {"masterformat": "48 14 00"}),
            ],
        ),
        # -- 48D Mạng trung thế gom điện 22 kV & Trạm Skid --------------------
        (
            "48D",
            "48 - Lưới Điện Thu Gom Trung Thế 22 kV & Trạm Biến Áp Hợp Bộ Skid",
            {"masterformat": "48"},
            [
                ("48D.001", "Trạm biến áp hợp bộ Skid 3150 kVA 0.8/22 kV tích hợp RMU trung thế (12 trạm)", "pcs", 12, 1650000000.0, {"masterformat": "48 13 00"}),
                ("48D.002", "Cáp ngầm trung thế 24 kV Cu/XLPE/PVC/DSTA/PVC 3x240 mm² liên kết vòng", "m", 16500, 890000.0, {"masterformat": "48 13 00"}),
                ("48D.003", "Móng bê tông cốt thép đặt trạm Skid và bể chứa dầu sự cố thu gom tràn", "pcs", 12, 45000000.0, {"masterformat": "48 13 00"}),
                ("48D.004", "Đầu cáp ngầm trung thế 24kV co nguội 3 pha ngoài trời và trong tủ", "pcs", 72, 8500000.0, {"masterformat": "48 13 00"}),
                ("48D.005", "Thử nghiệm cao thế VLF cáp ngầm 22kV và đo phóng điện cục bộ PD", "lsum", 1, 220000000.0, {"masterformat": "48 13 00"}),
            ],
        ),
        # -- 48E Hệ thống lưu trữ năng lượng BESS 10 MWh -----------------------
        (
            "48E",
            "48 - Hệ Thống Pin Lưu Trữ Năng Lượng BESS 10 MWh (LFP Lithium)",
            {"masterformat": "48"},
            [
                ("48E.001", "Container pin lưu trữ BESS 5 MWh làm mát bằng chất lỏng Liquid-cooling (2 cụm)", "pcs", 2, 28500000000.0, {"masterformat": "48 17 00"}),
                ("48E.002", "Hệ thống biến đổi điện áp PCS 2.5 MW hai chiều Bi-directional", "pcs", 2, 6800000000.0, {"masterformat": "48 17 00"}),
                ("48E.003", "Máy biến áp nâng áp BESS 5 MVA 0.69/22 kV", "pcs", 1, 2200000000.0, {"masterformat": "48 17 00"}),
                ("48E.004", "Hệ thống quản lý pin BMS & Hệ thống điều khiển năng lượng EMS tích hợp", "lsum", 1, 3500000000.0, {"masterformat": "48 17 00"}),
                ("48E.005", "Hệ thống chữa cháy khí aerosol tự động & cảnh báo khí nổ theo NFPA 855", "lsum", 1, 1650000000.0, {"masterformat": "48 17 00"}),
                ("48E.006", "Bệ móng bê tông cốt thép đặt container BESS và tường ngăn cháy bảo vệ", "m3", 180, 3600000.0, {"masterformat": "48 17 00"}),
            ],
        ),
        # -- 33 Trạm biến áp 110 kV & Đấu nối xuất tuyến -----------------------
        (
            "33",
            "33 - Trạm Biến Áp Nâng Áp 22/110 kV & Đường Dây Đấu Nối 110 kV",
            {"masterformat": "33"},
            [
                ("33.001", "Máy biến áp lực chính 63 MVA 22/110 kV kèm bộ đổi nấc dưới tải OLTC", "pcs", 1, 26500000000.0, {"masterformat": "33 71 00"}),
                ("33.002", "Ngăn lộ xuất tuyến 110 kV ngoài trời (Máy cắt 110kV, dao cách ly, biến dòng TI, biến điện áp TU, chống sét van CSG)", "pcs", 1, 14500000000.0, {"masterformat": "33 72 00"}),
                ("33.003", "Hệ thống tủ đóng cắt 22 kV trong nhà (Ngăn lộ lộ vào, lộ đo lường, lộ xuất tuyến)", "pcs", 14, 380000000.0, {"masterformat": "33 72 00"}),
                ("33.004", "Hệ thống tủ bảo vệ rơ le kỹ thuật số (Bảo vệ so lệch F87T, quá dòng F50/51, khoảng cách F21)", "lsum", 1, 4800000000.0, {"masterformat": "33 72 00"}),
                ("33.005", "Nhà điều hành trạm biến áp 110 kV và phòng phân phối 22 kV (kết cấu BTCT)", "m2", 280, 12500000.0, {"masterformat": "33 72 00"}),
                ("33.006", "Cột thép đơn thân / dàn gantry trạm 110kV mạ kẽm nhúng nóng", "t", 65, 42000000.0, {"masterformat": "33 71 00"}),
                ("33.007", "Đường dây trên không 110 kV mạch kép dây dẫn ACSR 240 mm² đấu nối vào lưới (3.2 km)", "m", 3200, 3200000.0, {"masterformat": "33 71 19"}),
                ("33.008", "Hệ thống đo đếm điện năng thương mại ranh giới cấp chính xác 0.2S (Chính và phụ)", "lsum", 1, 1850000000.0, {"masterformat": "33 79 00"}),
            ],
        ),
        # -- 25 SCADA & Điều độ Điều khiển Nhà máy PPC ------------------------
        (
            "25",
            "25 - Hệ Thống SCADA, Bộ Điều Khiển Nhà Máy PPC & Viễn Thông EVN",
            {"masterformat": "25"},
            [
                ("25.001", "Hệ thống SCADA điều khiển giám sát tập trung tại phòng điều hành nhà máy", "lsum", 1, 2800000000.0, {"masterformat": "25 35 00"}),
                ("25.002", "Bộ điều khiển công suất nhà máy Power Plant Controller (PPC) đáp ứng điều tần và AGC", "lsum", 1, 2400000000.0, {"masterformat": "25 35 00"}),
                ("25.003", "Trạm đo bức xạ thời tiết chuẩn quốc tế (2 trạm đầy đủ cảm biến bức xạ trực xạ, xiên, nhiệt độ)", "pcs", 2, 280000000.0, {"masterformat": "25 14 00"}),
                ("25.004", "Hệ thống kênh truyền viễn thông cáp quang OPGW kết nối về Trung tâm Điều độ A0 & A2", "lsum", 1, 1650000000.0, {"masterformat": "25 13 00"}),
                ("25.005", "Hệ thống an ninh giám sát camera nhiệt và cảnh báo xâm nhập hàng rào chu vi", "lsum", 1, 1250000000.0, {"masterformat": "25 36 00"}),
            ],
        ),
        # -- 48F Thí nghiệm, COD & Nghiệm thu truyền tải -----------------------
        (
            "48F",
            "48 - Thí Nghiệm Đóng Điện, Thử Nghiệm Grid Code & Nghiệm Thu COD",
            {"masterformat": "48"},
            [
                ("48F.001", "Thí nghiệm đo kiểm chuỗi PV và cáp DC theo TCVN 11855 / IEC 62446", "lsum", 1, 450000000.0, {"masterformat": "48 19 00"}),
                ("48F.002", "Thí nghiệm thông số đường dây và trạm biến áp 110kV phối hợp với Trung tâm Thí nghiệm điện", "lsum", 1, 1200000000.0, {"masterformat": "48 19 00"}),
                ("48F.003", "Thử nghiệm đặc tính kỹ thuật tuân thủ Grid Code EVN (FRT, điều khiển Q-V, P-f)", "lsum", 1, 1850000000.0, {"masterformat": "48 19 00"}),
                ("48F.004", "Kiểm tra nghiệm thu công tác PCCC trạm 110kV và container BESS với Cục Cảnh sát PCCC", "lsum", 1, 650000000.0, {"masterformat": "48 19 00"}),
                ("48F.005", "Đóng điện điểm đấu nối, chạy thử nghiệm thu 72 giờ và công nhận vận hành thương mại COD", "lsum", 1, 2100000000.0, {"masterformat": "48 19 00"}),
            ],
        ),
    ],
    markups=[
        ("Chi phí chung (Overhead theo TT 11/2021/TT-BXD)", 6.5, "overhead", "direct_cost"),
        ("Chi phí nhà tạm để ở và điều hành thi công", 1.2, "overhead", "direct_cost"),
        ("Chi phí không xác định từ thiết kế", 2.0, "contingency", "direct_cost"),
        ("Thu nhập chịu thuế tính trước (Profit)", 6.0, "profit", "cumulative"),
        ("Thuế giá trị gia tăng (VAT 8% theo NĐ 72/2024)", 8.0, "tax", "cumulative"),
    ],
    total_months=12,
    tender_name="Gói thầu Cung cấp Tấm pin & Biến tần Inverter 50 MWp",
    tender_companies=[
        ("Tập đoàn Năng lượng Xanh Trung Nam", "tenders@trungnam-energy.example.vn", 0.98),
        ("Công ty Cổ phần Năng lượng Tái tạo Bim", "epc@bim-energy.example.vn", 1.02),
        ("Liên danh EPC Solar Việt - Hàn", "bids@vietkor-solar.example.vn", 1.01),
    ],
    project_metadata={
        "client": "Công ty Cổ phần Năng lượng Mặt trời Thuận Nam Ninh Thuận",
        "epc_contractor": "Liên danh Tổng thầu EPC Solar & Substation 110kV",
        "owner_engineer": "Tư vấn Điện lực Quốc gia (PECC)",
        "dc_capacity_mwp": 50,
        "ac_capacity_mwac": 38,
        "dc_ac_ratio": 1.32,
        "bess_energy_mwh": 10,
        "bess_power_mw": 5,
        "site_area_ha": 60,
        "module_count": 80645,
        "module_type": "Mono N-Type TOPCon 620 Wp Bifacial",
        "inverter_type": "String Inverter 330 kW 1500V",
        "grid_connection_voltage_kv": 110,
        "substation_capacity_mva": 63,
        "regulatory_scheme": "Nghị định 80/2024/NĐ-CP (Cơ chế mua bán điện trực tiếp DPPA)",
        "expected_annual_yield_gwh": 82.5,
        "co2_avoided_ton_per_year": 70800,
        "standards": [
            "TCVN 11855-1:2017 / IEC 62446-1:2016",
            "Circular 25/2016/TT-BCT & TT 30/2019/TT-BCT (EVN Grid Code)",
            "QCVN 01:2020/BCT (Electrical safety)",
            "QCVN 02:2022/BXD (Wind loads - Ninh Thuan Zone)",
            "IEC 62619 / NFPA 855 (BESS battery energy storage safety)",
            "Circular 11/2021/TT-BXD (Statutory estimate breakdown)",
        ],
    },
    tender_packages=[
        (
            "Cung cấp thiết bị chính (Tấm pin PV 620 Wp & Inverter 330 kW)",
            "Cung cấp 80.645 tấm pin TOPCon 620 Wp và 115 bộ biến tần chuỗi 330 kW",
            "awarded",
            [
                ("Tập đoàn Năng lượng Xanh Trung Nam", "tenders@trungnam-energy.example.vn", 0.98),
                ("Công ty TNHH Cung ứng Năng lượng Toàn Cầu", "sales@global-pv.example.vn", 1.03),
                ("Công ty Cổ phần Năng lượng Tái tạo Bim", "epc@bim-energy.example.vn", 1.01),
            ],
        ),
        (
            "Trạm biến áp 110 kV, Máy biến áp 63 MVA & Đường dây 110 kV",
            "Trạm nâng áp 22/110 kV 63 MVA, ngăn xuất tuyến 110kV và 3.2 km ĐZ 110kV",
            "evaluating",
            [
                ("Công ty Cổ phần Xây lắp Điện 1 (PCC1)", "thau@pcc1.example.vn", 0.99),
                ("Tổng công ty Xây dựng Điện Việt Nam (VNECO)", "epc@vneco.example.vn", 1.03),
                ("Công ty Cổ phần Kỹ thuật Điện Miền Nam", "bids@dienmiennam.example.vn", 1.01),
            ],
        ),
        (
            "Hệ thống lưu trữ pin BESS 10 MWh / 5 MW",
            "Container pin LFP 10 MWh, bộ đổi điện PCS 5 MW, hệ thống chữa cháy NFPA 855",
            "evaluating",
            [
                ("Công ty Công nghệ Lưu trữ Năng lượng Thông minh", "ess@smartbess.example.vn", 0.97),
                ("Tập đoàn Năng lượng Tái tạo & Lưu trữ Toàn Cầu", "bids@global-storage.example.vn", 1.04),
                ("Liên danh EPC Solar Việt - Hàn", "bids@vietkor-solar.example.vn", 1.02),
            ],
        ),
    ],
)

