from unittest import TestCase
from unittest.mock import patch

from game import remove_symbol_from_map


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_remove_symbol_from_map_on_treasure(self, _):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        board = {(0, 0): "t",
                 (0, 1): 4,
                 (0, 2): 2,
                 (1, 0): 2,
                 (1, 1): 'B',
                 (1, 2): 2,
                 (2, 1): 't',
                 (2, 3): 1,
                 (3, 0): 3}
        remove_symbol_from_map(character_example, board)
        expected = {(0, 0): 1,
                    (0, 1): 4,
                    (0, 2): 2,
                    (1, 0): 2,
                    (1, 1): 'B',
                    (1, 2): 2,
                    (2, 1): 't',
                    (2, 3): 1,
                    (3, 0): 3}
        self.assertEqual(expected, board)  # check that dictionary has changed

    @patch('random.randint', return_value=1)
    def test_remove_symbol_from_map_not_on_treasure(self, _):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 0}
        board = {(1, 0): "t",
                 (0, 0): 3,
                 (3, 0): 3,
                 (0, 1): 4,
                 (1, 1): "B",
                 (2, 1): "t",
                 (0, 2): 2,
                 (1, 2): 2,
                 (2, 3): 1}
        remove_symbol_from_map(character_example, board)
        expected = {(0, 0): 1,
                    (0, 1): 4,
                    (0, 2): 2,
                    (1, 0): 't',
                    (1, 1): 'B',
                    (1, 2): 2,
                    (2, 1): 't',
                    (2, 3): 1,
                    (3, 0): 3}
        self.assertEqual(expected, board)  # check that dictionary has not changed
