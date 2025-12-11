import argparse
from itertools import combinations


def parse_coords(line: str) -> tuple[int, int]:
    x_str, y_str = line.strip().split(",")
    return int(x_str), int(y_str)


def area(c1: tuple[int, int], c2: tuple[int, int]) -> int:
    width = abs(c2[0] - c1[0]) + 1
    height = abs(c2[1] - c1[1]) + 1
    return width * height


def main(input_file_path: str) -> None:
    coords = []
    with open(input_file_path, "r") as f:
        coords = list(map(parse_coords, f.readlines()))

    # print(coords)

    corner_pairs = list(combinations(coords, 2))
    areas = [[c1, c2, area(c1, c2)] for (c1, c2) in corner_pairs]
    areas.sort(key=lambda x: x[2], reverse=True)
    # print()
    # for a in areas:
    #     print(a)
    # print()
    print(areas[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
