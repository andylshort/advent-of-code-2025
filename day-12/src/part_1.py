import argparse
import re


def parse_presents(
    lines: list[str],
) -> tuple[dict[int, list[str]], list[tuple[tuple[int, int], dict[int, int]]]]:
    # Parse the present shapes
    shapes: dict[int, list[str]] = {}

    region_regex = r"^(\d+x\d+):([\s\d+]+)$"

    line_index = 0
    while not re.match(region_regex, lines[line_index]):
        # Parse the present shapes
        line = lines[line_index].strip()
        # print(f"Current line '{line}'...")

        index = int(line[: line.index(":")])

        shapes[index] = []
        line_index += 1

        while (line := lines[line_index].strip()) != "":
            shapes[index].append(line)
            line_index += 1

        # Skip past blank line
        line_index += 1

    # We've parsed all the shapes, now do the regions
    regions: list[tuple[tuple[int, int], dict[int, int]]] = []
    while line_index < len(lines):
        line = lines[line_index].strip()
        # print(f"Parsing line '{line}'...")
        match = re.match(region_regex, line)

        dimensions = list(map(int, match.group(1).strip().split("x")))
        # print(dimensions)
        dim_tuple = (dimensions[0], dimensions[1])

        amounts = {
            i: int(elem) for i, elem in enumerate(match.group(2).strip().split(" "))
        }
        # print(amounts)

        regions.append((dim_tuple, amounts))

        line_index += 1

    return shapes, regions


def fit_shapes(shapes, region) -> None:
    # We can rotate _and_ flip a shape, that's 8 configurations per shape
    rotation = 0  # 0, 1, 2, 3
    pos = (0, 0)  # (x, y)

    grid = ["." * region[0][0]] * region[0][1]

    print("\n".join(grid))


def can_fit_shapes_theoretically(shapes, region) -> bool:
    region_area = region[0][0] * region[0][1]

    def get_shape_area(shape) -> int:
        a = 0
        for line in shape:
            a += line.count("#")
        return a

    shape_total_area = 0
    for shape, amount in region[1].items():
        shape_total_area += get_shape_area(shapes[shape]) * amount

    return region_area >= shape_total_area


def main(input_file_path: str) -> None:
    present_shapes = {}
    present_regions = {}
    with open(input_file_path, "r") as f:
        present_shapes, present_regions = parse_presents(f.readlines())

    print("---")
    for k, v in present_shapes.items():
        print(f"{k} =>")
        v_str = "\n".join([l for l in v])
        v_str = v_str.replace("#", chr(65 + k))
        print(v_str)
    # print(present_shapes)
    print(present_regions)

    count_fits = 0
    for region in present_regions:
        # fit_shapes(present_shapes, region)
        if can_fit_shapes_theoretically(present_shapes, region):
            count_fits += 1
            print("\tCan fit")
        else:
            print("\tCan't fit...")
        print("---")

    print(f"Fits = {count_fits}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
