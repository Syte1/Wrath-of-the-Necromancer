from unittest import TestCase
from unittest.mock import patch

from game import move_character as move


class Test(TestCase):
    @patch('game.calculate_new_coords', return_value=(0, -1))
    def test_move_character_up(self, _):
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        move(character, 1)
        self.assertEqual({'X-Coordinate': 0, 'Y-Coordinate': -1}, character)

    @patch('game.calculate_new_coords', return_value=(0, 1))
    def test_move_character_down(self, _):
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        move(character, 2)
        self.assertEqual({'X-Coordinate': 0, 'Y-Coordinate': 1}, character)

    @patch('game.calculate_new_coords', return_value=(-1, 0))
    def test_move_character_left(self, _):
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        move(character, 3)
        self.assertEqual({'X-Coordinate': -1, 'Y-Coordinate': 0}, character)

    @patch('game.calculate_new_coords', return_value=(1, 0))
    def test_move_character_right(self, _):
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        move(character, 4)
        self.assertEqual({'X-Coordinate': 1, 'Y-Coordinate': 0}, character)
