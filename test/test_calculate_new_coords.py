from unittest import TestCase
from game import calculate_new_coords as calc_coordinates


class Test(TestCase):
    def test_calculate_new_coordinates_up(self):
        self.assertEqual((0, -1), calc_coordinates({"X-Coordinate": 0, "Y-Coordinate": 0}, 1))

    def test_calculate_new_coordinates_down(self):
        self.assertEqual((0, 1), calc_coordinates({"X-Coordinate": 0, "Y-Coordinate": 0}, 2))

    def test_calculate_new_coordinates_left(self):
        self.assertEqual((-1, 0), calc_coordinates({"X-Coordinate": 0, "Y-Coordinate": 0}, 3))

    def test_calculate_new_coordinates_right(self):
        self.assertEqual((1, 0), calc_coordinates({"X-Coordinate": 0, "Y-Coordinate": 0}, 4))
