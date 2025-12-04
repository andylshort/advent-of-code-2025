from src.part_1 import get_accessible_rolls


class TestAccessibleRolls:
    def test_example(self):
        layout = [
            "..@@.@@@@.",
            "@@.@.@.@@",
            "@@@@.@.@@",
            ".@@@@..@.",
            "@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            ".@@@.@@@@",
            ".@@@@@@@@.",
            ".@.@@@.@.",
        ]
        assert get_accessible_rolls(layout) == 13
