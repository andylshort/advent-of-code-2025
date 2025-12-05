import argparse


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


def main(input_file_path: str) -> None:
    fresh_id_ranges, available_ids = parse_input(input_file_path)

    freshness_results = {}

    for available_id in available_ids:
        freshness_results[available_id] = is_id_fresh(fresh_id_ranges, available_id)
        print(f"{available_id}: {freshness_results[available_id]}")

    print(
        f"Total fresh IDs: {sum(1 for is_fresh in freshness_results.values() if is_fresh)}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
