from unittest import TestCase
from game import check_for_boss


class Test(TestCase):
    def test_check_for_boss_not_on_boss_square(self):
        board_example = {(0, 1): 1,
                         (1, 0): 2,
                         (2, 0): 3,
                         (0, 0): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 1}
        self.assertFalse(check_for_boss(board_example, character_example))

    def test_check_for_boss_on_boss_square(self):
        board_example = {(0, 1): "B",
                         (1, 0): 2,
                         (2, 0): 3,
                         (0, 0): 4,
                         (1, 1): 1,
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 1}
        check_for_boss(board_example, character_example)
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 1}

        self.assertTrue(check_for_boss(board_example, character_example))
