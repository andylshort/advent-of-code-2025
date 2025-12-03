import pytest

from part_2 import clicker, parse_and_rotate


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

        assert zeroes == 6
