#!/usr/bin/env python3
# Advent of Code 2025 - Day 1
import argparse

MIN_LIMIT = 0
MAX_LIMIT = 99
START_NUMBER = 50


def clicker(start: int, clicks: int, negative: bool) -> tuple[int, int]:
    current = start
    zeroes_passed = 0
    clicks_left = clicks

    for _ in range(clicks):
        if negative:
            current -= 1
        else:
            current += 1

        if current < MIN_LIMIT:
            current = MAX_LIMIT
        elif current > MAX_LIMIT:
            current = MIN_LIMIT

        clicks_left -= 1
        if current == 0 and clicks_left > 0:
            zeroes_passed += 1

    return current, zeroes_passed


def parse_and_rotate(
    instruction: str, current_number: int, zeroes: int
) -> tuple[int, int, int]:
    instruction = instruction.upper()
    clicks = int(instruction[1:])

    if instruction[0] == "L":
        new_number, additional_zeroes = clicker(current_number, clicks, True)
        return (new_number, zeroes + (1 if new_number == 0 else 0), additional_zeroes)
    elif instruction[0] == "R":
        new_number, additional_zeroes = clicker(current_number, clicks, False)
        return (new_number, zeroes + (1 if new_number == 0 else 0), additional_zeroes)
    else:
        raise ValueError(f"Invalid instruction: {instruction}")


def main(instructions: list[str]) -> None:
    current_number = START_NUMBER
    zeroes = 0
    total_passed_zeroes = 0
    print(f"The dial starts by pointing at {current_number}.")

    for instruction in instructions:
        current_number, zeroes, passed_zeroes = parse_and_rotate(
            instruction, current_number, zeroes
        )
        msg = f"The dial is rotated {instruction} to point at {current_number}."
        if passed_zeroes > 0:
            msg += f" (Passed over zero {passed_zeroes} time(s))"
            total_passed_zeroes += passed_zeroes
        print(msg)
        if current_number < MIN_LIMIT:
            raise ValueError("Number went below minimum limit!")
        if current_number > MAX_LIMIT:
            raise ValueError("Number went above maximum limit!")

    print(f"Final number: {current_number}")
    print(f"Number of times landed on zero: {zeroes}")
    print(f"Total number of times passed over zero: {total_passed_zeroes}")
    print(f"Total number of times zero was encountered: {zeroes + total_passed_zeroes}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", type=str, default="input.txt", help="Input file with instructions"
    )
    args = parser.parse_args()

    with open(args.file, "r") as f:
        instructions = [line.strip() for line in f if line.strip()]
        main(instructions)
