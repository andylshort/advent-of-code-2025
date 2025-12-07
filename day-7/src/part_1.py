import argparse
from collections import OrderedDict


def index_multiple(input_str: str, char: str) -> set[int]:
    return set([i for i, c in enumerate(input_str) if c == char])


def get_split_indices(
    splitter_locations: set[int],
) -> OrderedDict[int, tuple[int, int]]:
    split_indices: dict[int, tuple[int, int]] = dict()
    for index in splitter_locations:
        split_indices[index] = (index - 1, index + 1)
    return OrderedDict(sorted(split_indices.items()))


def count_beam_splits(tachyon_manifold: list[str]) -> int:
    beam_indices: set[int] = set()
    beam_indices.add(tachyon_manifold[0].index("S"))
    print(tachyon_manifold[0].strip())

    number_of_splits = 0

    for line in tachyon_manifold[1:]:
        if line.count("^") == 0:
            continue
        splitter_locations = index_multiple(line, "^")
        split_indices = get_split_indices(splitter_locations)
        # print(split_indices)

        line_with_splits = list(line)

        for loc in splitter_locations:
            left_split, right_split = split_indices[loc]
            if loc in beam_indices:
                number_of_splits += 1
                beam_indices.remove(loc)

                if left_split not in beam_indices:
                    beam_indices.add(left_split)
                if right_split not in beam_indices:
                    beam_indices.add(right_split)

        for idx in beam_indices:
            line_with_splits[idx] = "|"

        new_line = "".join(line_with_splits).strip()
        print(f"{new_line} -> {number_of_splits}")

    return number_of_splits


def main(input_file_path: str) -> None:
    lines = []
    with open(input_file_path, "r") as f:
        lines = f.readlines()
    print(f"Read {len(lines)} lines from {input_file_path}")

    splits = count_beam_splits(lines)

    print(f"Number of beam splits: {splits}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
