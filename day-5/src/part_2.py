import argparse
from multiprocessing import get_all_start_methods
from re import L


def parse_input(input_file_path: str) -> tuple[list[tuple[int, int]], list[int]]:
    input_lines = []
    with open(input_file_path, "r") as f:
        input_lines = [line.strip() for line in f.readlines()]

    fresh_id_ranges: list[tuple[int, int]] = []
    available_ids: list[int] = []

    while len(input_lines) > 0:
        line = input_lines.pop(0)
        if line == "":
            break
        else:
            num_strs = line.split("-")
            fresh_id_ranges.append((int(num_strs[0]), int(num_strs[1])))
    while len(input_lines) > 0:
        line = input_lines.pop(0)
        available_ids.append(int(line))

    return fresh_id_ranges, available_ids


def is_id_fresh(fresh_id_ranges: list[tuple[int, int]], available_id: int) -> bool:
    for range in fresh_id_ranges:
        if range[0] <= available_id <= range[1]:
            return True
    return False


def get_all_fresh_ids(fresh_id_ranges: list[tuple[int, int]]) -> set[int]:
    # The native way of doing it
    fresh_ids = set()
    for start, end in fresh_id_ranges:
        fresh_ids.update(range(start, end + 1))
    return fresh_ids


def p(n: tuple[int, int]) -> str:
    return f"({n[0]:,}, {n[1]:,})"


def get_size_fresh_ids(fresh_id_ranges: list[tuple[int, int]]) -> int:
    sorted_ranges = sorted(fresh_id_ranges, key=lambda x: x[0])

    # print(sorted_ranges)
    print("\n".join(map(p, sorted_ranges)))
    print()

    non_overlapping_ranges = []
    current_range = sorted_ranges[0]

    for next_range in sorted_ranges[1:]:
        print(f"Comparing {p(next_range)} to {p(current_range)}...")
        if next_range[0] > current_range[1]:
            print("\tNo overlap, saving...")
            non_overlapping_ranges.append(current_range)
            current_range = next_range
        elif next_range[0] == current_range[1]:
            current_range = (current_range[0], next_range[1])
            print(f"\tExtended current range to {p(current_range)}")
        else:
            print("\tPartial overlap...")
            if next_range[1] > current_range[1]:
                print(f"\t\tNeed to merge {p(next_range)} and {p(current_range)}...")
                current_range = (current_range[0], next_range[1])
                print(f"\t\tMerged {p(current_range)}")
            else:
                print(
                    f"\t{p(current_range)} wholly contains {p(next_range)}. Skipping..."
                )
    non_overlapping_ranges.append(current_range)

    # print(sorted_ranges)
    print("\n".join(map(p, non_overlapping_ranges)))

    # Get and sum range sizes
    total_size = 0
    for range in non_overlapping_ranges:
        total_size += range[1] - range[0] + 1

    return total_size


def main(input_file_path: str) -> None:
    fresh_id_ranges, _ = parse_input(input_file_path)
    assert len(fresh_id_ranges) == 174

    total_size = get_size_fresh_ids(fresh_id_ranges)

    print(f"Total fresh IDs: {total_size}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
