import argparse
import itertools


def get_highest_joltage_2(battery_bank: str) -> int:
    remaining_digits = [int(i) for i in battery_bank]

    chosen_digits = []

    while len(remaining_digits) > 0:
        print(f"Chosen digits: {chosen_digits}")
        next_digit = remaining_digits.pop(0)
        print(f"Removed {next_digit} from remaining digits -> {remaining_digits}")

        if len(chosen_digits) == 0:
            chosen_digits.append(next_digit)
            continue

        if next_digit <= chosen_digits[-1]:
            if len(chosen_digits) < 12:
                print(f"Adding {next_digit} to chosen digits")
                chosen_digits.append(next_digit)
                continue
        else:
            while (
                len(chosen_digits) > 0
                and next_digit > chosen_digits[-1]
                and len(remaining_digits) + len(chosen_digits) + 1 > 12
            ):
                chosen_digits.pop()
            chosen_digits.append(next_digit)

    val = 0
    while len(chosen_digits) > 0:
        val = val * 10 + chosen_digits.pop(0)
    return val


def get_highest_joltage(battery_bank: str) -> int:
    # Way slow bruteforce approach
    return max(
        int("".join(combination))
        for combination in itertools.combinations(battery_bank, 12)
    )


def main(input_file_path: str) -> None:
    battery_banks = []
    highest_joltages = []
    with open(input_file_path, "r") as f:
        battery_banks = [line.strip() for line in f.readlines()]

    for i in range(1, len(battery_banks) + 1):
        highest_joltage = get_highest_joltage_2(battery_banks[i - 1])
        highest_joltages.append(highest_joltage)
    print(f"Sum of highest joltages: {sum(highest_joltages)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
