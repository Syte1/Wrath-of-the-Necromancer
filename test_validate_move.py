from unittest import TestCase
from unittest.mock import patch

from game import validate_move as validate


class Test(TestCase):
    @patch('game.calculate_new_coords', return_value=(0, -1))
    def test_validate_move_invalid_up_move_outside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertFalse(validate(board, {"X-Coordinate": 0, "Y-Coordinate": 0}, 1))

    @patch('game.calculate_new_coords', return_value=(1, 0))
    def test_validate_move_valid_up_move_inside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertTrue(validate(board, {"X-Coordinate": 1, "Y-Coordinate": 1}, 1))

    @patch('game.calculate_new_coords', return_value=(1, 2))
    def test_validate_move_invalid_down_move_outside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertFalse(validate(board, {"X-Coordinate": 1, "Y-Coordinate": 1}, 2))

    @patch('game.calculate_new_coords', return_value=(0, 1))
    def test_validate_move_valid_down_move_inside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertTrue(validate(board, {"X-Coordinate": 0, "Y-Coordinate": 0}, 2))

    @patch('game.calculate_new_coords', return_value=(-1, 0))
    def test_validate_move_invalid_left_move_outside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertFalse(validate(board, {"X-Coordinate": 0, "Y-Coordinate": 0}, 3))

    @patch('game.calculate_new_coords', return_value=(0, 1))
    def test_validate_move_valid_left_move_inside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertTrue(validate(board, {"X-Coordinate": 1, "Y-Coordinate": 1}, 3))

    @patch('game.calculate_new_coords', return_value=(0, -1))
    def test_validate_move_invalid_right_move_outside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertFalse(validate(board, {"X-Coordinate": 1, "Y-Coordinate": 1}, 4))

    @patch('game.calculate_new_coords', return_value=(1, 0))
    def test_validate_move_valid_right_move_inside_board(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        self.assertTrue(validate(board, {"X-Coordinate": 0, "Y-Coordinate": 0}, 4))

    @patch('game.calculate_new_coords', return_value=(1, 1))
    def test_validate_move_board_unchanged(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        character = {"X-Coordinate": 1, "Y-Coordinate": 0}
        validate(board, character, 2)
        self.assertEqual({(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0):
                         'Town', (1, 1): 'Town'}, board)

    @patch('game.calculate_new_coords', return_value=(0, 1))
    def test_validate_move_character_unchanged(self, _):
        board = {(0, 0): 'Grassy Area', (0, 1): 'Forested Area', (1, 0): 'Town', (1, 1): 'Town'}
        character = {"X-Coordinate": 0, "Y-Coordinate": 0}
        validate(board, character, 2)
        self.assertEqual({"X-Coordinate": 0, "Y-Coordinate": 0}, character)
