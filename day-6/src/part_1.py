import argparse
import re
from functools import reduce
from typing import Any


def add(a: int, b: int) -> int:
    return a + b


def mult(a: int, b: int) -> int:
    return a * b


def parse_input(input_file_path: str) -> tuple[list[list[int]], list[str]]:
    full_input: list[str] = []
    with open(input_file_path, "r") as f:
        full_input = [line.strip() for line in f.readlines()]

    operands_unparsed = full_input[:-1]
    operands = []
    for operand in operands_unparsed:
        operands_list = list(map(int, re.split(r"\s+", operand)))
        operands.append(operands_list)
    operators_unparsed = full_input[-1]
    operators = re.split(r"\s+", operators_unparsed)
    return operands, operators


def transpose(operands: list[list[int]], operators: list[str]) -> list[Any]:
    operations = []
    for i in range(len(operands[0])):
        operations.append([operand[i] for operand in operands] + [operators[i]])
    return operations


def calculate_result(operation: list[Any]) -> int:
    operator = operation[-1]
    if operator == "+":
        return reduce(add, operation[:-1])
    elif operator == "*":
        return reduce(mult, operation[:-1])
    else:
        raise ValueError(f"Unknown operator '{operator}'")


def main(input_file_path: str) -> None:
    operands, operators = parse_input(input_file_path)
    print(operands, operators)
    operations = transpose(operands, operators)
    print(operations)

    grand_total = 0
    for operation in operations:
        result = calculate_result(operation)
        print(f"{operation} -> {result}")
        grand_total += result

    print(f"Grand total = {grand_total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
