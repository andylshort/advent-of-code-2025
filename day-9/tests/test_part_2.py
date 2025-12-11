import pytest
from shapely import Point, Polygon

from src.part_2 import parse_coords, point_in_polygon


class TestPointInPolygon:
    @pytest.mark.parametrize(
        "point, polygon, expected",
        [
            (
                Point(3, 3),
                Polygon([Point(1, 1), Point(1, 5), Point(5, 5), Point(5, 1)]),
                True,
            ),  # Inside square
            (
                Point(1, 1),
                Polygon([Point(1, 1), Point(1, 5), Point(5, 5), Point(5, 1)]),
                True,
            ),  # On vertex
            (
                Point(1, 3),
                Polygon([Point(1, 1), Point(1, 5), Point(5, 5), Point(5, 1)]),
                True,
            ),  # On edge
            (
                Point(0, 0),
                Polygon([Point(1, 1), Point(1, 5), Point(5, 5), Point(5, 1)]),
                False,
            ),  # Outside square
            (
                Point(3, 6),
                Polygon([Point(1, 1), Point(1, 5), Point(5, 5), Point(5, 1)]),
                False,
            ),  # Outside square
            (
                Point(2, 2),
                Polygon([Point(0, 0), Point(0, 4), Point(4, 4), Point(4, 0)]),
                True,
            ),  # Inside larger square
            (
                Point(4, 4),
                Polygon([Point(0, 0), Point(0, 4), Point(4, 4), Point(4, 0)]),
                True,
            ),  # On vertex of larger square
            (
                Point(5, 5),
                Polygon([Point(0, 0), Point(0, 4), Point(4, 4), Point(4, 0)]),
                False,
            ),  # Outside larger square
        ],
    )
    def test_point_in_polygon(self, point, polygon, expected):
        assert point_in_polygon(point, polygon) == expected

    def test_corners_in_input_polygon(self):
        polygon_corners = []
        with open("test-input.txt") as f:
            polygon_corners = list(map(parse_coords, f.readlines()))
        polygon = Polygon(polygon_corners)

        for corner in polygon_corners:
            assert point_in_polygon(corner, polygon) is True
