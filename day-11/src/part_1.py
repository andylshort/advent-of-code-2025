import argparse


def parse_device_and_outputs(line: str) -> tuple[str, list[str]]:
    line = line.strip()
    device = line[0 : line.index(":")]
    outputs = line[line.index(":") + 2 :].split(" ")

    return device, outputs


def dfs(
    current_state: str,
    path: list[str],
    solutions: list[list[str]],
    devices_and_outputs: dict[str, list[str]],
):
    if current_state == "out":
        solutions.append(path.copy())
        return

    for next_state in devices_and_outputs[current_state]:
        path.append(next_state)
        dfs(next_state, path, solutions, devices_and_outputs)
        path.pop()


def main(input_file_path: str) -> None:
    devices_and_outputs = {}
    with open(input_file_path, "r") as f:
        devices_and_outputs = dict(map(parse_device_and_outputs, f.readlines()))

    print(devices_and_outputs)

    solutions = []
    dfs("you", ["you"], solutions, devices_and_outputs)
    print(solutions)

    num_solutions = len(solutions)

    print(f"There are {num_solutions} different paths from 'you' to 'out'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
