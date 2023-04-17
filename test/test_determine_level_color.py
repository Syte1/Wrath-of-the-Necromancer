from unittest import TestCase
from unittest.mock import patch

from game import determine_level_color


class Test(TestCase):
    @patch('game.area_level', return_value=3)
    def test_determine_level_color_lvl_3(self, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 1}

        self.assertEqual(31, determine_level_color(character))

    @patch('game.area_level', return_value=2)
    def test_determine_level_color_lvl_2(self, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 10}

        self.assertEqual(33, determine_level_color(character))

    @patch('game.area_level', return_value=1)
    def test_determine_level_color_lvl_1(self, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 20}

        self.assertEqual(32, determine_level_color(character))

    @patch('game.area_level', return_value=1)
    def test_determine_level_color_number_number_larger_than_24(self, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 200}

        self.assertEqual(32, determine_level_color(character))

    @patch('game.area_level', return_value=3)
    def test_determine_level_color_number_smaller_than_0(self, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': -20}

        self.assertEqual(31, determine_level_color(character))
