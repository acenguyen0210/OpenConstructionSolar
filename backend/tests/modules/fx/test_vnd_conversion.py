from datetime import date
from decimal import Decimal

import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.fx import repository as repo
from app.modules.fx.service import FxService
from tests.modules.fx.conftest import make_policy, make_rate_set


@pytest.mark.asyncio
async def test_vnd_conversion_with_ecb_feed(session: AsyncSession) -> None:
    """VND is not in ECB feed, but should seamlessly fall back to seed rate."""
    # Create an ECB rate set with only USD and EUR
    rate_set = await make_rate_set(
        session,
        rate_date=date(2026, 11, 2),
        rates={"USD": "1.08"},
        source="ecb",
    )
    service = FxService(session)

    # 1. Convert EUR -> VND (1000 EUR * 27500 = 27,500,000 VND)
    result = await service.convert(1000, "EUR", "VND", rate_set_id=rate_set.id)
    assert result["available"] is True
    assert Decimal(str(result["converted"])) == Decimal("27500000")

    # 2. Convert VND -> EUR
    result2 = await service.convert(27500000, "VND", "EUR", rate_set_id=rate_set.id)
    assert result2["available"] is True
    assert round(Decimal(str(result2["converted"])), 2) == Decimal("1000")

    # 3. Validate project policy with VND
    policy = await make_policy(
        session,
        estimating_currency="VND",
        procurement_currency="VND",
        reporting_currency="VND",
        max_rate_age_days=3650,
    )
    report = await service.validate_project(policy.project_id, on_date=date(2026, 11, 2))
    assert report.errors == []
    assert report.status.value == "passed"
