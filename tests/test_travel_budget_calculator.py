from travel_budget_calculator import (
    calculate_remaining_budget,
    convert_krw_to_usd
)


def test_calculate_remaining_budget():
    result = calculate_remaining_budget(2_000_000, 500_000)

    assert result == 1_500_000


def test_convert_krw_to_usd():
    result = convert_krw_to_usd(1_500_000, 1_400)

    assert round(result, 2) == 1071.43