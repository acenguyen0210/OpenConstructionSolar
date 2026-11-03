"""Build the ``PartnerPackManifest`` instance for the vietnam-solar pack.

Kept in its own module so unit tests can import the manifest without
triggering package ``__init__`` side-effects.
"""

from __future__ import annotations

from app.core.partner_pack.manifest import PartnerBranding, PartnerPackManifest

MANIFEST = PartnerPackManifest(
    slug="vietnam-solar",
    partner_name="Vietnam Solar EPC Pack",
    partner_url=None,
    pack_version="1.0.0",
    pack_type="industry",
    description=(
        "Pre-configured for solar EPC contractors and developers in Vietnam: "
        "Rooftop C&I and utility-scale PV takeoff, BESS energy storage, EVN Grid Code "
        "(Circular 39/2015/TT-BCT & Circular 30/2019/TT-BCT), TCVN 11855 / IEC 62446, "
        "QCVN 01/02/06, PCCC C07/3288, Decree 135/2024/ND-CP (Self-consumption & Zero Export), "
        "Decree 80/2024/ND-CP (DPPA) and Circular 11/2021/TT-BXD cost structures in VND."
    ),
    default_locale="vi",
    additional_locales={},
    cwicr_regions=[
        "VN_NATIONAL",
    ],
    default_currency="VND",
    default_tax_template=None,
    default_methodology="vietnam-solar",
    validation_rule_packs=[
        "vietnam_solar_regulations",
        "vietnam_solar_pv_design",
        "vietnam_solar_fire_safety",
        "vietnam_evn_grid_compliance",
        "vietnam_solar_lcoe",
    ],
    validation_rule_sets=[
        "boq_quality",
    ],
    default_modules=[],
    hidden_modules=[],
    demo_template_ids=[
        "vietnam-solar-rooftop-epc",
        "vietnam-solar-farm-epc",
    ],
    branding=PartnerBranding(
        primary_color="#00875A",
        accent_color="#F5A623",
        logo_path="logo.svg",
        favicon_path=None,
        powered_by_text=None,
    ),
    onboarding_script_path="onboarding.yaml",
    metadata={
        "country": "VN",
        "country_name_en": "Vietnam",
        "classification_standard": "masterformat",
        "measurement_system": "metric",
        "regulator_refs": [
            "Decree 135/2024/ND-CP (Rooftop solar self-consumption & zero-export)",
            "Decree 80/2024/ND-CP (Direct Power Purchase Agreement - DPPA)",
            "Decision 500/QD-TTg (National Power Development Plan VIII - PDP8)",
            "Circular 39/2015/TT-BCT & Circular 30/2019/TT-BCT (EVN Distribution Grid Code)",
            "Circular 25/2016/TT-BCT (EVN Transmission Grid Code)",
            "TCVN 11855-1:2017 / IEC 62446-1:2016 (PV system testing and documentation)",
            "TCVN 6781:2017 / IEC 61215:2016 (Terrestrial PV module qualification)",
            "TCVN 10884:2015 / IEC 61730:2011 (PV module safety qualification)",
            "QCVN 01:2020/BCT (National technical regulation on electrical safety)",
            "QCVN 02:2022/BXD (Natural conditions and climate data for construction)",
            "QCVN 06:2022/BXD & Document 3288/C07-P4 (Fire safety for rooftop PV)",
            "Circular 11/2021/TT-BXD & Circular 14/2023/TT-BXD (Construction cost estimation)",
            "Circular 12/2021/TT-BXD (National construction cost norms - Dinh Muc)",
        ],
        "vat_standard_rate": 8,
        "support_email": "info@datadrivenconstruction.io",
    },
)

