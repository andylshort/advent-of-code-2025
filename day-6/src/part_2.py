import argparse
import re
from functools import reduce
from typing import Any


def add(a: int, b: int) -> int:
    return a + b


def mult(a: int, b: int) -> int:
    return a * b


def parse_input_and_get_operations(input_file_path: str) -> list[Any]:
    full_input: list[str] = []
    with open(input_file_path, "r") as f:
        full_input = [line for line in f.readlines()]

    # Handler operators as before
    operators_unparsed = full_input[-1]
    operators = re.split(r"\s+", operators_unparsed)

    operations = []

    # Need to read in numbers properly
    operands_unparsed = full_input[:-1]

    new_operation = []
    new_operator = ""
    for i in range(len(operands_unparsed[0])):
        print(f"Looking at idx '{i}'...")

        chars_in_col = [op[i] for op in operands_unparsed]
        print(f"Chars: {chars_in_col}")
        as_str = "".join(chars_in_col).strip()
        if as_str == "":
            operations.append(new_operation + [new_operator])
            new_operation = []
            new_operator = ""
            continue

        new_operand = int(as_str)
        if new_operator == "":
            new_operator = full_input[-1][i]

        chars_in_col = [op[i] for op in operands_unparsed]
        print(f"Chars: {chars_in_col}")
        new_operand = int("".join(chars_in_col).strip())
        print(f"\tFormed num -> {new_operand}")
        new_operation.append(new_operand)

    operations.append(new_operation + [new_operator])
    return operations


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
    operations = parse_input_and_get_operations(input_file_path)
    print(operations)

    grand_total = 0
    for operation in operations:
        # HACK - my last one is [''] and cba to fix
        if len(operation) < 3:
            continue
        result = calculate_result(operation)
        grand_total += result

    print(f"Grand total = {grand_total}")


# print(operands, operators)
# operations = transpose(operands, operators)
# print(operations)

# grand_total = 0
# for operation in operations:
#     result = calculate_result(operation)
#     print(f"{operation} -> {result}")
#     grand_total += result

# print(f"Grand total = {grand_total}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
