from unittest import TestCase
from game import check_for_exit


class Test(TestCase):
    def test_check_for_exit_character_is_on_exit(self):
        character_example = {"X-Coordinate": 0, "Y-Coordinate": 0}
        board_example = {(0, 0): "E", (0, 2): "1"}
        is_on_exit = check_for_exit(character_example, board_example)
        self.assertTrue(is_on_exit)

    def test_check_for_exit_character_is_not_on_exit(self):
        character_example = {"X-Coordinate": 0, "Y-Coordinate": 1}
        board_example = {(0, 0): "E", (0, 1): "2", (0, 2): "1"}
        is_on_exit = check_for_exit(character_example, board_example)
        self.assertFalse(is_on_exit)

    def test_check_for_exit_character_is_moved_on_exit(self):
        character_example = {"X-Coordinate": 0, "Y-Coordinate": 0}
        board_example = {(0, 0): "E", (0, 2): "1"}
        check_for_exit(character_example, board_example)
        expected = {'X-Coordinate': 0, 'Y-Coordinate': 2}
        self.assertEqual(expected, character_example)

    def test_check_for_exit_character_is_not_moved_when_not_on_exit(self):
        character_example = {"X-Coordinate": 0, "Y-Coordinate": 1}
        board_example = {(0, 0): "E", (0, 1): "2", (0, 2): "1"}
        check_for_exit(character_example, board_example)
        expected = {"X-Coordinate": 0, "Y-Coordinate": 1}
        self.assertEqual(expected, character_example)
