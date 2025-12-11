import argparse
from itertools import combinations

from shapely import Point, Polygon, box


def parse_coords(line: str) -> Point:
    x_str, y_str = line.strip().split(",")
    return Point(int(x_str), int(y_str))


def area(c1: Point, c2: Point) -> int:
    width = abs(c2.x - c1.x) + 1
    height = abs(c2.y - c1.y) + 1
    return int(width * height)


def four_corners(c1: Point, c2: Point) -> Polygon:
    return box(min(c1.x, c2.x), min(c1.y, c2.y), max(c1.x, c2.x), max(c1.y, c2.y))


def point_in_polygon(point: Point, polygon: Polygon) -> bool:
    # TODO: Make own algorithm
    # I used shapely because it does the job I wanted, and I didn't
    # want to be blocked on this one task. (:
    return polygon.contains(point)


def all_corners_in_polygon(corners: Polygon, polygon: Polygon) -> bool:
    return polygon.contains(corners)


def main(input_file_path: str) -> None:
    polygon_corners = []
    with open(input_file_path, "r") as f:
        polygon_corners = list(map(parse_coords, f.readlines()))
    polygon = Polygon(polygon_corners)

    corner_pairs = list(combinations(polygon_corners, 2))
    rectangles = [
        [c1, c2, four_corners(c1, c2), area(c1, c2)] for (c1, c2) in corner_pairs
    ]
    rectangles.sort(key=lambda x: x[3], reverse=True)

    for rect in rectangles:
        if not all_corners_in_polygon(rect[2], polygon):
            # print("\tNot in")
            continue
        else:
            print(f"\n=> Found largest area: {area(rect[0], rect[1])}")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", dest="input_file_path", type=str, help="Path to input file"
    )
    args = parser.parse_args()

    main(args.input_file_path)
