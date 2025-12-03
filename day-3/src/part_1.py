import argparse


def get_highest_joltage(battery_bank: str) -> int:
    highest_seen = 0
    for i in range(len(battery_bank)):
        for j in range(i + 1, len(battery_bank)):
            candidate = int(battery_bank[i]) * 10 + int(battery_bank[j])
            # print(candidate)
            if candidate > highest_seen:
                highest_seen = candidate
    return highest_seen


def main(input_file_path: str) -> None:
    battery_banks = []
    highest_joltages = []
    with open(input_file_path, "r") as f:
        battery_banks = [line.strip() for line in f.readlines()]

        for i in range(1, len(battery_banks) + 1):
            highest_joltage = get_highest_joltage(battery_banks[i - 1])
            highest_joltages.append(highest_joltage)
            print(
                f"Battery bank {i}: {battery_banks[i - 1]} -> max joltage: {highest_joltage}"
            )
    print(f"Sum of highest joltages: {sum(highest_joltages)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
