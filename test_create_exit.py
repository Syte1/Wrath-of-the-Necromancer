from unittest import TestCase
from game import create_exit


class Test(TestCase):
    def test_create_exit_change_map_spots_to_exits(self):
        board_example = {(17, 5): "1", (18, 5): "2", (19, 5): "3"}
        create_exit(board_example)
        expected = board_example = {(17, 5): "E", (18, 5): "E", (19, 5): "3"}
        self.assertEqual(expected, board_example)
