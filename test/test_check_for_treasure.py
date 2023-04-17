from unittest import TestCase
from game import check_for_treasure


class Test(TestCase):
    def test_check_for_treasure_not_on_treasure_square(self):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 1}

        board_example = {(0, 0): "t",
                         (1, 0): 2,
                         (2, 0): 3,
                         (0, 1): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        self.assertFalse(check_for_treasure(board_example, character_example))

    def test_check_for_treasure_on_treasure_square(self):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        board_example = {(0, 0): "t",
                         (1, 0): 3,
                         (2, 0): 3,
                         (0, 1): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        self.assertTrue(check_for_treasure(board_example, character_example))
