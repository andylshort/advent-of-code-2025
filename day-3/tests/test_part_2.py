import pytest

from src.part_2 import get_highest_joltage_2


class TestPart2:
    @pytest.mark.parametrize(
        "battery_bank, expected",
        [
            ("987654321111111", 987654321111),
            ("811111111111119", 811111111119),
            ("234234234234278", 434234234278),
            ("818181911112111", 888911112111),
        ],
    )
    def test_get_highest_joltage_2(self, battery_bank, expected):
        assert get_highest_joltage_2(battery_bank) == expected
