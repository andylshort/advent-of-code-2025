import argparse
from itertools import permutations


class Machine:
    def __init__(
        self,
        indicators: str,
        button_wiring: list[set[int]],
        joltage_requirements: list[int],
    ):
        # All indicators are initially off, i.e. '....'
        # self.indicators is a diagram that shows the indicator config needed to 'start' a machine
        self.indicators = indicators

        # Buttons can toggle indicators on/off.
        # Each entry in wiring schematic says which indicators a button toggles.
        # E.g. button_wiring[0] = {0, 2} means button 0 toggles indicators 0 and 2.
        # No elem exists in button_wiring such that it's > len(indicators).
        self.button_wiring = button_wiring

        self.joltage_requirements = joltage_requirements

    def __str__(self) -> str:
        return f"Machine(indicators=[{self.indicators}], button_wiring={self.button_wiring}, joltage_requirements={self.joltage_requirements})"

    def __repr__(self) -> str:
        return self.__str__()


def parse_machine(input_line: str) -> Machine:
    indicator_str = input_line[0 : input_line.index("(")].strip()
    buttons_str = input_line[input_line.index("(") : input_line.index("{")].strip()
    joltage_str = input_line[input_line.index("{") :].strip()

    return Machine(
        indicators=indicator_str[1:-1],
        button_wiring=[
            set(map(int, s[1:-1].split(","))) for s in buttons_str.split(" ")
        ],
        joltage_requirements=list(map(int, joltage_str[1:-1].split(","))),
    )


def press_button_sequence(num_indicators: int, sequence: list[set[int]]) -> str:
    indicators = ["." for _ in range(num_indicators)]

    for button_press in sequence:
        for indicator_index in button_press:
            if indicators[indicator_index] == ".":
                indicators[indicator_index] = "#"
            else:
                indicators[indicator_index] = "."

    return "".join(indicators)


def try_get_min_presses(machine: Machine) -> int | None:
    num_indicators = len(machine.indicators)

    # TODO: Support repeated button presses?
    for i in range(len(machine.button_wiring)):
        for permutation in permutations(machine.button_wiring, i):
            candidate_indicators = press_button_sequence(
                num_indicators, list(permutation)
            )
            if candidate_indicators == machine.indicators:
                return i
    return None


def main(input_file_path: str) -> None:
    machines = []
    with open(input_file_path, "r") as f:
        machines = list(map(parse_machine, f.readlines()))

    total_min_presses = 0

    for machine in machines:
        if (min_presses := try_get_min_presses(machine)) is not None:
            total_min_presses += min_presses
        else:
            print(f"Could not find solution for machine: {machine}")

    print(f"Total minimum presses = {total_min_presses}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
