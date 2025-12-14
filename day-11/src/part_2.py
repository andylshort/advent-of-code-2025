import argparse
from functools import lru_cache


def parse_device_and_outputs(line: str) -> tuple[str, list[str]]:
    line = line.strip()
    device = line[0 : line.index(":")]
    outputs = line[line.index(":") + 2 :].split(" ")

    return device, outputs


def count_paths(graph: dict[str, list[str]], start: str, target: str) -> int:
    @lru_cache(maxsize=None)
    def dfs(node: str) -> int:
        if node == target:
            return 1
        return sum(dfs(nxt) for nxt in graph.get(node, []))

    return dfs(start)


def main(input_file_path: str) -> None:
    devices_and_outputs = {}
    with open(input_file_path, "r") as f:
        devices_and_outputs = dict(map(parse_device_and_outputs, f.readlines()))

    devices_and_outputs["out"] = []

    svr_fft_dac_out = count_paths(devices_and_outputs, "svr", "fft")
    print(svr_fft_dac_out)
    svr_fft_dac_out *= count_paths(devices_and_outputs, "fft", "dac")
    print(svr_fft_dac_out)
    svr_fft_dac_out *= count_paths(devices_and_outputs, "dac", "out")
    print(svr_fft_dac_out)

    print("---")

    svr_dac_fft_out = count_paths(devices_and_outputs, "svr", "dac")
    print(svr_dac_fft_out)
    svr_dac_fft_out *= count_paths(devices_and_outputs, "dac", "fft")
    print(svr_dac_fft_out)
    svr_dac_fft_out *= count_paths(devices_and_outputs, "fft", "out")
    print(svr_dac_fft_out)

    solutions = svr_fft_dac_out + svr_dac_fft_out
    print(
        f"Number of paths from 'svr' to 'out' (through 'fft' and 'dac') => {solutions}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
