import argparse

from z3 import Int, IntVector, Optimize


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


def get_min_presses(machine: Machine) -> int:
    # TODO: Write this process myself.

    # Setup the list of buttons and which joltage counters they contribute
    counters = [[] for _ in range(len(machine.joltage_requirements))]
    for b, button in enumerate(machine.button_wiring):
        for counter in button:
            counters[counter].append(b)

    # Define z3 variables
    buttons = IntVector("btn", len(machine.button_wiring))
    total_button_presses = Int("total_button_presses")

    # Setup z3's optimising solver
    solver = Optimize()

    # Add an equation for each joltage counter
    for counter in range(len(counters)):
        solver.add(
            sum(buttons[b] for b in counters[counter])
            == machine.joltage_requirements[counter]
        )

    # Add constraints such that button presses are non-negative
    for b in range(len(buttons)):
        solver.add(buttons[b] >= 0)

    # Define the target and that we want to minimise it
    solver.add(sum(buttons) == total_button_presses)
    solver.minimize(total_button_presses)

    solver.check()
    m = solver.model()

    total_button_presses = m.eval(total_button_presses).as_long()  # pyright: ignore[reportAttributeAccessIssue]

    return total_button_presses


def main(input_file_path: str) -> None:
    machines = []
    with open(input_file_path, "r") as f:
        machines = list(map(parse_machine, f.readlines()))

    # We can solve this problem using integer linear programming
    # In this instance, we defer to Z3
    total_min_presses = sum([get_min_presses(machine) for machine in machines])

    print(f"Total minimum presses = {total_min_presses}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
