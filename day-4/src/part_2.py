import argparse
from itertools import count
from posix import access
from webbrowser import get


def get_cell(row: int, col: int, layout: list[str]) -> str:
    assert 0 <= row < len(layout)
    assert 0 <= col < len(layout[row])
    return layout[row][col]


def get_neighbours(row: int, col: int, layout: list[str]) -> list[tuple[int, int]]:
    neighbours = []
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(layout) and 0 <= nc < len(layout[row]):
            neighbours.append((nr, nc))
    return neighbours


def count_neighbouring_rolls(row: int, col: int, layout: list[str]) -> int:
    count = 0
    neighbours = get_neighbours(row, col, layout)
    for nr, nc in neighbours:
        if get_cell(nr, nc, layout) == "@":
            count += 1
    return count


def get_and_remove_accessible_rolls(layout: list[str]) -> tuple[int, list[str]]:
    accessible_rolls = 0

    accessible_layout = layout[:]

    for i, row in enumerate(layout):
        for j, _ in enumerate(row):
            if (
                get_cell(i, j, layout) == "@"
                and count_neighbouring_rolls(i, j, layout) < 4
            ):
                accessible_rolls += 1
                old_row = accessible_layout[i]
                if j == len(row) - 1:
                    accessible_layout[i] = old_row[0:j] + "x"
                else:
                    accessible_layout[i] = old_row[0:j] + "x" + old_row[j + 1 :]

    print("\n".join(accessible_layout))
    return accessible_rolls, accessible_layout


def main(input_file_path: str) -> None:
    layout = []

    total_removed_rolls = 0

    accessible_rolls = 0

    with open(input_file_path, "r") as f:
        layout = [line.strip() for line in f.readlines()]

    accessible_rolls, new_layout = get_and_remove_accessible_rolls(layout)
    total_removed_rolls += accessible_rolls
    while accessible_rolls > 0:
        accessible_rolls, new_layout = get_and_remove_accessible_rolls(new_layout)
        total_removed_rolls += accessible_rolls

    print(f"Total removed rolls: {total_removed_rolls}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
