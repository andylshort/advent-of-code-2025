#!/usr/bin/env python3
# Advent of Code 2025 - Day 1

MIN_LIMIT = 0
MAX_LIMIT = 99
START_NUMBER = 50


def clicker(start: int, clicks: int, negative: bool) -> int:
    range_size = MAX_LIMIT - MIN_LIMIT + 1
    delta = -clicks if negative else clicks
    return ((start - MIN_LIMIT + delta) % range_size) + MIN_LIMIT


def parse_and_rotate(
    instruction: str, current_number: int, zeroes: int
) -> tuple[int, int]:
    instruction = instruction.upper()
    clicks = int(instruction[1:])

    new_number = 0

    if instruction[0] == "L":
        new_number = clicker(current_number, clicks, True)

        if new_number == 0:
            zeroes += 1

        return (new_number, zeroes)
    elif instruction[0] == "R":
        new_number = clicker(current_number, clicks, False)

        if new_number == 0:
            zeroes += 1

        return (new_number, zeroes)
    else:
        raise ValueError(f"Invalid instruction: {instruction}")


def main(instructions: list[str]) -> None:
    current_number = START_NUMBER
    zeroes = 0
    print(f"The dial starts by pointing at {current_number}.")

    for instruction in instructions:
        current_number, zeroes = parse_and_rotate(instruction, current_number, zeroes)
        print(f"The dial is rotated {instruction} to point at {current_number}.")
        if current_number < MIN_LIMIT:
            raise ValueError("Number went below minimum limit!")
        if current_number > MAX_LIMIT:
            raise ValueError("Number went above maximum limit!")

    print(f"Final number: {current_number}")
    print(f"Number of times landed on zero: {zeroes}")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]
        main(instructions)
