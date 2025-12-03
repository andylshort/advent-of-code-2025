import pytest

from part_1 import clicker, parse_and_rotate


class TestDialRotation:
    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("L10", 50, 0, 40),
            ("R10", 50, 0, 60),
        ],
    )
    def test_rotate_left_within_bounds(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1

    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("R10", 50, 0, 60),
            ("R20", 70, 0, 90),
        ],
    )
    def test_rotate_right_within_bounds(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1

    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("L1", 0, 0, 99),
            ("L60", 50, 0, 90),
            ("L51", 0, 0, 49),
        ],
    )
    def test_rotate_left_wrap_around(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1

    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("R1", 99, 0, 0),
            ("R60", 50, 0, 10),
            ("R50", 99, 0, 49),
            ("R48", 52, 0, 0),
        ],
    )
    def test_rotate_right_wrap_around(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1

    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("L50", 50, 0, 0),
            ("R50", 50, 0, 0),
            ("L99", 99, 0, 0),
            ("R1", 99, 0, 0),
        ],
    )
    def test_landing_on_zero(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1

    def test_invalid_instruction(self):
        with pytest.raises(ValueError):
            parse_and_rotate("X10", 50, 0)

    @pytest.mark.parametrize(
        "instruction,current,zeroes,expected",
        [
            ("L100", 99, 0, 99),
            ("L200", 99, 0, 99),
            ("L202", 1, 0, 99),
            ("R202", 99, 0, 1),
            ("R100", 1, 0, 1),
            ("R123", 1, 0, 24),
            ("L386", 89, 0, 3),
        ],
    )
    def test_large_rotation(
        self, instruction: str, current: int, zeroes: int, expected: int
    ):
        new_number, new_zeroes = parse_and_rotate(instruction, current, zeroes)
        assert new_number == expected

        if new_number == 0:
            assert new_zeroes == zeroes + 1


class TestProgram:
    def test_example(self):
        instructions = [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]
        current_number = 50
        zeroes = 0
        expected_numbers = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
        for instruction, expected in zip(instructions, expected_numbers):
            current_number, zeroes = parse_and_rotate(
                instruction, current_number, zeroes
            )

            assert current_number == expected

        assert zeroes == 3


class TestClicker:
    def test_one_click(self):
        assert clicker(50, 1, False) == 51
        assert clicker(50, 1, True) == 49

    def test_one_full_turn_clicks(self):
        assert clicker(0, 99, False) == 99
        assert clicker(0, 100, False) == 0

    def test_one_many_clicks(self):
        assert clicker(89, 386, True) == 3
        assert clicker(73, 873, True) == 0
        assert clicker(2, 123, False) == 25
