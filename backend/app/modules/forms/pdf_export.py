# DDC-CWICR-OE: DataDrivenConstruction · OpenConstructionERP
# Solar EPC Vietnam Edition
"""High-fidelity PDF export for Forms & Submissions matching DAT Group / Solar EPC SOP templates.

Renders completed and draft form submissions into professional engineering
documents mirroring the official Microsoft Word templates:
- Mẫu Báo cáo không tuân thủ (NCR / FMS-PMC.QHSE-NCR)
- Mẫu Phiếu Yêu Cầu Thay Đổi (CRF / FMS-PMC.CSU-CRF)
- Mẫu Kế Hoạch Nghiệm Thu & Thử Nghiệm (ITP / PPD.ITP)
- Mẫu Biên Bản Nghiệm Thu Chạy Thử & Đóng Điện (COM / COD)

Features:
- Full Unicode UTF-8 support for Vietnamese accents (Arial/Times/DejaVu).
- Formal 3-column document control header table with logo/branding.
- Structured project metadata table.
- Numbered bilingual sections with shaded banners.
- Clear 2-column key-value grid for form fields.
- Official 4-party sign-off matrix (Prepared by, QA/QC, Site Manager, Client/TVGS).
- SOP distribution and document retention notes.
"""

from __future__ import annotations

import io
import os
from typing import Any

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

# ── Font Registration ────────────────────────────────────────────────────────
_FONTS_INITIALIZED = False
FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"

def _ensure_unicode_fonts() -> None:
    global _FONTS_INITIALIZED, FONT_REGULAR, FONT_BOLD, FONT_ITALIC
    if _FONTS_INITIALIZED:
        return

    # 1. Try Windows system Arial (best for Vietnamese documents)
    win_arial = "C:/Windows/Fonts/arial.ttf"
    win_arial_bd = "C:/Windows/Fonts/arialbd.ttf"
    win_arial_it = "C:/Windows/Fonts/ariali.ttf"
    if os.path.exists(win_arial) and os.path.exists(win_arial_bd):
        try:
            pdfmetrics.registerFont(TTFont("Arial-VN", win_arial))
            pdfmetrics.registerFont(TTFont("Arial-VN-Bold", win_arial_bd))
            if os.path.exists(win_arial_it):
                pdfmetrics.registerFont(TTFont("Arial-VN-Italic", win_arial_it))
            else:
                pdfmetrics.registerFont(TTFont("Arial-VN-Italic", win_arial))
            FONT_REGULAR = "Arial-VN"
            FONT_BOLD = "Arial-VN-Bold"
            FONT_ITALIC = "Arial-VN-Italic"
            _FONTS_INITIALIZED = True
            return
        except Exception:
            pass

    # 2. Try app.core.pdf_fonts (DejaVu Sans)
    try:
        from app.core.pdf_fonts import BODY_FONT, BOLD_FONT, register_pdf_fonts
        register_pdf_fonts()
        FONT_REGULAR = BODY_FONT
        FONT_BOLD = BOLD_FONT
        FONT_ITALIC = BODY_FONT
        _FONTS_INITIALIZED = True
        return
    except Exception:
        pass

    _FONTS_INITIALIZED = True


# ── Color Palette ────────────────────────────────────────────────────────────
NAVY_PRIMARY = colors.HexColor("#0f2d59")      # Deep Solar Navy
NAVY_LIGHT = colors.HexColor("#e2e8f0")        # Slate light
ACCENT_BLUE = colors.HexColor("#0284c7")       # Solar Sky Blue
BG_SHADING = colors.HexColor("#f8fafc")        # Soft off-white
BG_HEADER = colors.HexColor("#f1f5f9")         # Slate 100
BORDER_COLOR = colors.HexColor("#94a3b8")      # Slate 400
TEXT_MAIN = colors.HexColor("#0f172a")         # Slate 900
TEXT_MUTED = colors.HexColor("#475569")        # Slate 600
SUCCESS_COLOR = colors.HexColor("#16a34a")     # Emerald 600
DANGER_COLOR = colors.HexColor("#dc2626")      # Red 600


class NumberedCanvas(canvas.Canvas):
    """Canvas that computes total pages dynamically for 'Page X / Y' footer."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._saved_page_states: list[dict[str, Any]] = []

    def showPage(self) -> None:
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self) -> None:
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages: int) -> None:
        self.saveState()
        self.setFont(FONT_REGULAR, 8)
        self.setFillColor(TEXT_MUTED)

        # Top subtle running line
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.5)
        self.line(15 * mm, 282 * mm, 195 * mm, 282 * mm)

        # Bottom footer line
        self.line(15 * mm, 12 * mm, 195 * mm, 12 * mm)

        # Running header text
        self.drawString(15 * mm, 284 * mm, "OPENCONSTRUCTION SOLAR EPC · VIETNAM STANDARD FORM")
        self.drawRightString(195 * mm, 284 * mm, "ISO 9001:2015 / ISO 19650 COMPLIANT")

        # Running footer text
        self.drawString(
            15 * mm,
            8 * mm,
            "Hệ thống Quản lý Biểu mẫu & Kiểm soát Tài liệu Dự án ĐMT - Bảo mật Nội bộ Dự án",
        )
        self.drawRightString(
            195 * mm,
            8 * mm,
            f"Trang {self._pageNumber} / {total_pages}",
        )
        self.restoreState()


def build_submission_pdf_report(submission: Any) -> tuple[bytes, str]:
    """Render a FormSubmission instance into an official SOP PDF document."""
    _ensure_unicode_fonts()

    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=15 * mm,
        rightMargin=15 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )

    styles = getSampleStyleSheet()

    # Custom paragraph styles
    style_company = ParagraphStyle(
        "CompanyHeader",
        fontName=FONT_BOLD,
        fontSize=11,
        leading=14,
        textColor=NAVY_PRIMARY,
        alignment=TA_LEFT,
    )
    style_company_sub = ParagraphStyle(
        "CompanySub",
        fontName=FONT_REGULAR,
        fontSize=8,
        leading=11,
        textColor=TEXT_MUTED,
        alignment=TA_LEFT,
    )
    style_title_en = ParagraphStyle(
        "TitleEn",
        fontName=FONT_BOLD,
        fontSize=13,
        leading=16,
        textColor=NAVY_PRIMARY,
        alignment=TA_CENTER,
    )
    style_title_vn = ParagraphStyle(
        "TitleVn",
        fontName=FONT_BOLD,
        fontSize=11,
        leading=14,
        textColor=ACCENT_BLUE,
        alignment=TA_CENTER,
    )
    style_doc_ctrl = ParagraphStyle(
        "DocCtrl",
        fontName=FONT_REGULAR,
        fontSize=8,
        leading=11,
        textColor=TEXT_MAIN,
        alignment=TA_LEFT,
    )
    style_section_header = ParagraphStyle(
        "SectionHeader",
        fontName=FONT_BOLD,
        fontSize=9.5,
        leading=13,
        textColor=colors.white,
        alignment=TA_LEFT,
    )
    style_label = ParagraphStyle(
        "FieldLabel",
        fontName=FONT_BOLD,
        fontSize=8.5,
        leading=11,
        textColor=NAVY_PRIMARY,
        alignment=TA_LEFT,
    )
    style_val = ParagraphStyle(
        "FieldValue",
        fontName=FONT_REGULAR,
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_MAIN,
        alignment=TA_LEFT,
    )
    style_meta_label = ParagraphStyle(
        "MetaLabel",
        fontName=FONT_BOLD,
        fontSize=8,
        leading=11,
        textColor=TEXT_MUTED,
    )
    style_meta_val = ParagraphStyle(
        "MetaValue",
        fontName=FONT_BOLD,
        fontSize=8.5,
        leading=11,
        textColor=TEXT_MAIN,
    )
    style_sig_title = ParagraphStyle(
        "SigTitle",
        fontName=FONT_BOLD,
        fontSize=8.5,
        leading=11,
        alignment=TA_CENTER,
        textColor=NAVY_PRIMARY,
    )
    style_sig_sub = ParagraphStyle(
        "SigSub",
        fontName=FONT_ITALIC,
        fontSize=7.5,
        leading=9.5,
        alignment=TA_CENTER,
        textColor=TEXT_MUTED,
    )
    style_notice = ParagraphStyle(
        "NoticeText",
        fontName=FONT_ITALIC,
        fontSize=7.5,
        leading=10,
        textColor=TEXT_MUTED,
        alignment=TA_LEFT,
    )

    story: list[Any] = []

    # ── 1. HEADER TABLE (Branding | Title | Doc Control) ──────────────────────
    tpl_name = getattr(submission, "template_name", "BIỂU MẪU KIỂM SOÁT DỰ ÁN")
    sub_num = getattr(submission, "submission_number", "FRM-001")
    sub_ver = getattr(submission, "template_version", 1)
    status_str = str(getattr(submission, "status", "draft")).upper()
    comp_at = getattr(submission, "completed_at", None) or "Chưa đóng"

    # Bilingual Title mapping based on template keywords
    if "NCR" in tpl_name or "không tuân thủ" in tpl_name.lower():
        title_en = "NON-CONFORMANCE REPORT (NCR)"
        title_vn = "BÁO CÁO SỰ KHÔNG PHÙ HỢP HIỆN TRƯỜNG"
        ref_prefix = "FMS-PMC.QHSE-NCR"
    elif "CRF" in tpl_name or "thay đổi" in tpl_name.lower():
        title_en = "CHANGE REQUEST FORM (CRF)"
        title_vn = "PHIẾU ĐỀ NGHỊ THAY ĐỔI THIẾT KẾ & THI CÔNG"
        ref_prefix = "FMS-PMC.CSU-CRF"
    elif "ITP" in tpl_name or "thử nghiệm" in tpl_name.lower():
        title_en = "INSPECTION & TEST PLAN (ITP)"
        title_vn = "KẾ HOẠCH & BIÊN BẢN KIỂM TRA THỬ NGHIỆM"
        ref_prefix = "FMS-PPD.ITP"
    elif "COM" in tpl_name or "đóng điện" in tpl_name.lower() or "chạy thử" in tpl_name.lower():
        title_en = "COMMISSIONING & ENERGIZATION RECORD"
        title_vn = "BIÊN BẢN NGHIỆM THU CHẠY THỬ & ĐÓNG ĐIỆN"
        ref_prefix = "FMS-COM.COD"
    else:
        title_en = "PROJECT SITE RECORD / CHECKLIST"
        title_vn = tpl_name.upper()
        ref_prefix = "FMS-SITE"

    doc_ref = f"{ref_prefix}-{sub_num.replace('FRM-', '')}" if "FRM-" in sub_num else sub_num

    header_left = [
        Paragraph("DAT GROUP / SOLAR EPC", style_company),
        Paragraph("BAN QUẢN LÝ DỰ ÁN NĂNG LƯỢNG MẶT TRỜI", style_company_sub),
        Paragraph("Hệ thống QLCL ISO 9001:2015 & ISO 19650", style_company_sub),
    ]

    header_center = [
        Paragraph(title_en, style_title_en),
        Spacer(1, 1 * mm),
        Paragraph(title_vn, style_title_vn),
    ]

    status_color = SUCCESS_COLOR if status_str == "COMPLETED" else DANGER_COLOR
    header_right = [
        Paragraph(f"<b>Mã số / Ref:</b> {doc_ref}", style_doc_ctrl),
        Paragraph(f"<b>Phiên bản / Rev:</b> {sub_ver}.0", style_doc_ctrl),
        Paragraph(f"<b>Ngày lập / Date:</b> {comp_at[:10] if comp_at else '---'}", style_doc_ctrl),
        Paragraph(
            f"<b>Trạng thái:</b> <font color='{status_color.hexval()}'>{status_str}</font>",
            style_doc_ctrl,
        ),
    ]

    header_table = Table(
        [[header_left, header_center, header_right]],
        colWidths=[55 * mm, 75 * mm, 50 * mm],
    )
    header_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 1, NAVY_PRIMARY),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("TOPPADDING", (0, 0), (-1, -1), 3 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3 * mm),
                ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2.5 * mm),
                ("BACKGROUND", (0, 0), (-1, -1), BG_HEADER),
            ]
        )
    )
    story.append(header_table)
    story.append(Spacer(1, 3 * mm))

    # ── 2. PROJECT METADATA STRIP ─────────────────────────────────────────────
    title_text = getattr(submission, "title", None) or "Dự Án Điện Mặt Trời Áp Mái (Solar Rooftop EPC)"
    loc_text = getattr(submission, "location", None) or "Hiện trường công trình Solar"
    cat_text = str(getattr(submission, "template_category", "Quality")).capitalize()
    result_str = getattr(submission, "result", None)

    res_badge = "-"
    if result_str:
        if result_str.lower() == "pass":
            res_badge = f"<font color='{SUCCESS_COLOR.hexval()}'><b>[✓] ĐẠT / PASS</b></font>"
        elif result_str.lower() == "fail":
            res_badge = f"<font color='{DANGER_COLOR.hexval()}'><b>[✕] KHÔNG ĐẠT / FAIL</b></font>"
        else:
            res_badge = result_str.upper()

    meta_data = [
        [
            Paragraph("DỰ ÁN / PROJECT NAME:", style_meta_label),
            Paragraph(title_text, style_meta_val),
            Paragraph("PHÂN LOẠI / CATEGORY:", style_meta_label),
            Paragraph(cat_text, style_meta_val),
        ],
        [
            Paragraph("VỊ TRÍ / LOCATION:", style_meta_label),
            Paragraph(loc_text, style_meta_val),
            Paragraph("KẾT QUẢ / RESULT:", style_meta_label),
            Paragraph(res_badge, style_meta_val),
        ],
    ]
    meta_table = Table(meta_data, colWidths=[36 * mm, 64 * mm, 38 * mm, 42 * mm])
    meta_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.75, BORDER_COLOR),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, NAVY_LIGHT),
                ("BACKGROUND", (0, 0), (0, -1), BG_SHADING),
                ("BACKGROUND", (2, 0), (2, -1), BG_SHADING),
                ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                ("LEFTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2 * mm),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    story.append(meta_table)
    story.append(Spacer(1, 4 * mm))

    # ── 3. BODY: RENDER FIELDS IN STRUCTURED NUMBERED SECTIONS ────────────────
    snapshot: list[dict[str, Any]] = getattr(submission, "template_snapshot", []) or []
    answers: dict[str, Any] = getattr(submission, "answers_data", {}) or {}

    # Separate fields into sections
    current_section_title = "1.0 NỘI DUNG CHI TIẾT / HIGHLIGHTED PARTICULARS"
    sections: list[tuple[str, list[dict[str, Any]]]] = []
    current_fields: list[dict[str, Any]] = []

    sec_counter = 0
    for field in snapshot:
        ftype = str(field.get("type", ""))
        flabel = str(field.get("label", ""))
        if ftype == "section":
            if current_fields:
                sections.append((current_section_title, current_fields))
                current_fields = []
            sec_counter += 1
            flabel_clean = flabel.strip()
            if flabel_clean and flabel_clean[0].isdigit():
                current_section_title = flabel_clean.upper()
            else:
                current_section_title = f"{sec_counter}.0 {flabel_clean.upper()}"
        else:
            current_fields.append(field)
    if current_fields:
        sections.append((current_section_title, current_fields))

    # If no section was defined in the template, split neatly into 2 or 3 sections
    if len(sections) == 1 and len(sections[0][1]) > 5:
        all_f = sections[0][1]
        mid = (len(all_f) + 1) // 2
        sections = [
            ("1.0 NỘI DUNG MÔ TẢ & HIỆN TRẠNG / PARTICULARS & DESCRIPTION", all_f[:mid]),
            ("2.0 BIỆN PHÁP XỬ LÝ & ĐÁNH GIÁ KỸ THUẬT / CORRECTIVE ACTION & ASSESSMENT", all_f[mid:]),
        ]

    for sec_title, fields in sections:
        # Section Header Banner
        sec_banner = Table(
            [[Paragraph(sec_title, style_section_header)]],
            colWidths=[180 * mm],
        )
        sec_banner.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, -1), NAVY_PRIMARY),
                    ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                    ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
                ]
            )
        )
        story.append(KeepTogether([sec_banner, Spacer(1, 1 * mm)]))

        # Fields Table
        field_rows: list[list[Any]] = []
        for f in fields:
            fkey = str(f.get("key", ""))
            flabel = str(f.get("label", ""))
            ftype = str(f.get("type", ""))
            val = answers.get(fkey)

            formatted_val = _render_field_value_html(ftype, val, f)
            p_label = Paragraph(flabel, style_label)
            p_val = Paragraph(formatted_val, style_val)
            field_rows.append([p_label, p_val])

        if field_rows:
            f_table = Table(field_rows, colWidths=[65 * mm, 115 * mm])
            f_table.setStyle(
                TableStyle(
                    [
                        ("BOX", (0, 0), (-1, -1), 0.75, BORDER_COLOR),
                        ("INNERGRID", (0, 0), (-1, -1), 0.5, NAVY_LIGHT),
                        ("BACKGROUND", (0, 0), (0, -1), BG_SHADING),
                        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 2.5 * mm),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ]
                )
            )
            story.append(f_table)
            story.append(Spacer(1, 3.5 * mm))

    # ── 4. OFFICIAL 4-PARTY ENGINEERING SIGN-OFF BLOCK ────────────────────────
    sig_banner = Table(
        [[Paragraph("XÁC NHẬN & PHÊ DUYỆT CÁC BÊN / CONFIRMATION & APPROVAL", style_section_header)]],
        colWidths=[180 * mm],
    )
    sig_banner.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY_PRIMARY),
                ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ]
        )
    )

    completed_by_name = getattr(submission, "completed_by", None) or "Kỹ sư Hiện trường"

    sig_data = [
        [
            Paragraph("NGƯỜI LẬP PHIẾU<br/><font size='7'>Prepared by</font>", style_sig_title),
            Paragraph("KỸ SƯ GIÁM SÁT / QA-QC<br/><font size='7'>Site Supervisor / QA-QC</font>", style_sig_title),
            Paragraph("CHỈ HUY TRƯỞNG<br/><font size='7'>Site Manager</font>", style_sig_title),
            Paragraph("TƯ VẤN GIÁM SÁT / CĐT<br/><font size='7'>Consultant / Client</font>", style_sig_title),
        ],
        [
            Paragraph("<font size='7' color='#64748b'>(Ký & ghi rõ họ tên)</font>", style_sig_sub),
            Paragraph("<font size='7' color='#64748b'>(Ký & ghi rõ họ tên)</font>", style_sig_sub),
            Paragraph("<font size='7' color='#64748b'>(Ký & ghi rõ họ tên)</font>", style_sig_sub),
            Paragraph("<font size='7' color='#64748b'>(Ký & ghi rõ họ tên)</font>", style_sig_sub),
        ],
        [
            Spacer(1, 14 * mm),
            Spacer(1, 14 * mm),
            Spacer(1, 14 * mm),
            Spacer(1, 14 * mm),
        ],
        [
            Paragraph(f"<b>{completed_by_name}</b>", style_sig_title),
            Paragraph("<b>Bộ Phận QA/QC</b>", style_sig_title),
            Paragraph("<b>Chỉ Huy Trưởng CT</b>", style_sig_title),
            Paragraph("<b>Đại Diện TVGS / CĐT</b>", style_sig_title),
        ],
        [
            Paragraph(f"Ngày: {comp_at[:10] if comp_at else '___/___/202___'}", style_sig_sub),
            Paragraph("Ngày: ___/___/202___", style_sig_sub),
            Paragraph("Ngày: ___/___/202___", style_sig_sub),
            Paragraph("Ngày: ___/___/202___", style_sig_sub),
        ],
    ]

    sig_table = Table(
        sig_data,
        colWidths=[45 * mm, 45 * mm, 45 * mm, 45 * mm],
    )
    sig_table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.75, BORDER_COLOR),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, NAVY_LIGHT),
                ("BACKGROUND", (0, 0), (-1, 0), BG_SHADING),
                ("TOPPADDING", (0, 0), (-1, -1), 1.5 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5 * mm),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )

    # ── 5. DISTRIBUTION & SOP NOTE ───────────────────────────────────────────
    notice_box = Table(
        [
            [
                Paragraph(
                    "<b>* GHI CHÚ PHÂN PHỐI & LƯU TRỮ (DISTRIBUTION NOTE):</b><br/>"
                    "1. Báo cáo này được lập thành 03 bản gốc: 01 bản lưu tại Ban Chỉ huy công trường, "
                    "01 bản gửi Đơn vị liên quan / Nhà thầu, 01 bản nộp vào Hồ sơ Chất lượng Dự án (CDE ISO 19650).<br/>"
                    "2. Các hành động khắc phục (CAPA) phải được phản hồi và gửi lại Chỉ huy trưởng trong vòng <b>03 ngày làm việc</b>.",
                    style_notice,
                )
            ]
        ],
        colWidths=[180 * mm],
    )
    notice_box.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.5, BORDER_COLOR),
                ("BACKGROUND", (0, 0), (-1, -1), BG_HEADER),
                ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
            ]
        )
    )

    story.append(KeepTogether([sig_banner, sig_table, Spacer(1, 3 * mm), notice_box]))

    # Build PDF with dynamic page numbering
    doc.build(story, canvasmaker=NumberedCanvas)
    pdf_bytes = buf.getvalue()

    safe_name = (doc_ref or "form").replace(" ", "_").replace("/", "-")
    filename = f"{safe_name}.pdf"
    return pdf_bytes, filename


def _render_field_value_html(ftype: str, val: Any, field_def: dict[str, Any]) -> str:
    """Format an answer value into styled HTML for ReportLab Paragraph."""
    if val is None or (isinstance(val, str) and val.strip() == ""):
        return "<font color='#94a3b8'><i>(Không có dữ liệu / None)</i></font>"

    if ftype == "checkbox":
        return "<b>[✓] Có / Yes</b>" if val is True else "<font color='#64748b'>[ ] Không / No</font>"

    if ftype == "pass_fail_na":
        s = str(val).strip().lower()
        if s == "pass":
            return "<font color='#16a34a'><b>[✓] ĐẠT / PASS</b></font>"
        elif s == "fail":
            return "<font color='#dc2626'><b>[✕] KHÔNG ĐẠT / FAIL</b></font>"
        elif s == "na":
            return "<font color='#64748b'><b>[-] KHÔNG ÁP DỤNG / N/A</b></font>"
        return str(val)

    if ftype == "signature":
        if isinstance(val, dict):
            name = val.get("name", "Người ký")
            dt = val.get("signed_at", "")[:19].replace("T", " ")
            return (
                f"<b>[ ĐÃ KÝ ĐIỆN TỬ ]</b> {name}<br/>"
                f"<font size='7' color='#64748b'>Thời gian ký: {dt}</font>"
            )
        return "<b>[ ĐÃ KÝ XÁC NHẬN ]</b>"

    if ftype == "photo":
        count = len(val) if isinstance(val, (list, tuple)) else 1
        return f"<b>[ ĐÍNH KÈM HÌNH ẢNH ]</b>: Đã ghi nhận {count} hình ảnh hiện trường tại công trường Solar"

    if ftype == "rating":
        max_r = field_def.get("max_rating") or 5
        try:
            stars = int(val)
            return f"<b>{stars} / {max_r}</b> điểm"
        except Exception:
            return str(val)

    if ftype == "number":
        unit = field_def.get("unit") or ""
        return f"<b>{val}</b> {unit}".strip()

    if ftype == "multi_choice" and isinstance(val, (list, tuple)):
        items = [f"• {v}" for v in val]
        return "<br/>".join(items)

    # Long text / short text: escape XML entities and preserve breaks
    text = str(val).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text.replace("\n", "<br/>")
