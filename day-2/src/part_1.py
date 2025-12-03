import argparse


def parse_id_range(range_str: str) -> tuple[int, int]:
    start_str, end_str = range_str.split("-")
    return int(start_str), int(end_str)


def is_even_length(num: int) -> bool:
    # pow = 2
    # while True:
    #     check_pow = 10**pow
    #     prev_pow = 10 ** (pow - 1)
    #     if num < prev_pow:
    #         return False
    #     if num > prev_pow and num < check_pow:
    #         return True
    #     pow += 2
    return len(str(num)) % 2 == 0


def find_invalid_ids(start: int, end: int) -> list[int]:
    invalid_ids = []

    for num in range(start, end + 1):
        if not is_even_length(num):
            continue

        half_len = len(str(num)) // 2

        if num // (10**half_len) == num % (10**half_len):
            invalid_ids.append(num)

    return invalid_ids


def main(input_file_path: str) -> None:
    all_invalid_ids = []

    with open(input_file_path, "r") as f:
        data = f.readline().strip()
        print(f"Input data: {data}")

        ranges = data.split(",")
        for r in ranges:
            start, end = parse_id_range(r)
            print(f"Range from {start} to {end}, length: {end - start + 1}")
            invalid_ids = find_invalid_ids(start, end)
            print(f"\tInvalid IDs: {invalid_ids}")
            all_invalid_ids.extend(invalid_ids)

    print(f"All invalid IDs: {all_invalid_ids}")
    print(f"Sum of all invalid IDs: {sum(all_invalid_ids)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
