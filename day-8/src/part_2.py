import argparse
from itertools import combinations
from math import dist, prod


def parse_coord(line: str) -> tuple[int, int, int]:
    parts = line.strip().split(",")
    return int(parts[0]), int(parts[1]), int(parts[2])


def print_circuits(circuits: list[set[int]]) -> None:
    print(",".join([str(c) for c in circuits if len(c) > 0]))


def get_last_connecting_junction(
    junction_boxes: list[tuple[int, int, int]],
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    seen_pairs: set[tuple[tuple[int, int, int], tuple[int, int, int]]] = set()

    new_circuits: list[set[tuple[int, int, int]]] = list()

    matchings = 0

    ordered_pairs = sorted(combinations(junction_boxes, 2), key=lambda p: dist(*p))
    # print(ordered_pairs)

    most_recent_pair = None
    while len(new_circuits) == 0 or len(new_circuits[0]) != len(junction_boxes):
        closest_pair = ordered_pairs.pop(0)
        most_recent_pair = closest_pair

        skip = False

        set_idx_0, set_idx_1 = -1, -1
        in_set_0, in_set_1 = False, False
        for i, s in enumerate(new_circuits):
            if closest_pair[0] in s:
                in_set_0 = True
                set_idx_0 = i
            if closest_pair[1] in s:
                in_set_1 = True
                set_idx_1 = i
            if closest_pair[0] in s and closest_pair[1] in s:
                skip = True

        if skip:
            seen_pairs.add(closest_pair)
            matchings += 1
            continue

        if not in_set_0 and not in_set_1:
            new_circuits.append(set([closest_pair[0], closest_pair[1]]))
        elif in_set_0 and not in_set_1:
            new_circuits[set_idx_0].add(closest_pair[1])
        elif not in_set_0 and in_set_1:
            new_circuits[set_idx_1].add(closest_pair[0])
        else:
            new_circuits[set_idx_0] = new_circuits[set_idx_0].union(
                new_circuits[set_idx_1]
            )
            new_circuits[set_idx_1].clear()

        empty_indices = []
        for i in range(len(new_circuits)):
            if len(new_circuits[i]) == 0:
                empty_indices.append(i)
        for idx in reversed(empty_indices):
            new_circuits.pop(idx)

        seen_pairs.add(closest_pair)
        matchings += 1

    return most_recent_pair  # type: ignore


def main(input_file_path: str) -> None:
    lines = []
    with open(input_file_path, "r") as f:
        lines = f.readlines()

    junction_boxes = list(map(parse_coord, lines))

    last_pair = get_last_connecting_junction(junction_boxes)
    print(
        f"Pair -> {last_pair} => {last_pair[0][0] * last_pair[1][0]}"  # type:ignore
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
