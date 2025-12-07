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


def count_beam_timelines(tachyon_manifold: list[str]) -> int:
    beam_timelines: dict[int, int] = dict()
    beam_timelines[tachyon_manifold[0].index("S")] = 1
    print(tachyon_manifold[0].strip())

    for line in tachyon_manifold[1:]:
        if line.count("^") == 0:
            continue

        splitter_locations = index_multiple(line, "^")
        split_indices = get_split_indices(splitter_locations)

        for loc in splitter_locations:
            left_split, right_split = split_indices[loc]

            if loc in beam_timelines:
                incoming = beam_timelines.pop(loc)

                if left_split not in beam_timelines:
                    beam_timelines[left_split] = 0
                beam_timelines[left_split] += incoming

                if right_split not in beam_timelines:
                    beam_timelines[right_split] = 0
                beam_timelines[right_split] += incoming

    return sum(beam_timelines.values())


def main(input_file_path: str) -> None:
    lines = []
    with open(input_file_path, "r") as f:
        lines = f.readlines()
    print(f"Read {len(lines)} lines from {input_file_path}")

    timelines = count_beam_timelines(lines)

    print(f"Number of timelines: {timelines}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
