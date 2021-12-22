import io
from unittest import TestCase
from unittest.mock import patch

from game import print_board


class Test(TestCase):
    @patch('game.determine_level_color', return_value=31)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_board_print_correct_map(self, mock_output, _):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 1,
                     'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1)]}

        board = {(0, 0): 2, (1, 0): 1, (2, 0): 3,
                 (0, 1): 4, (1, 1): "B", (2, 1): "t",
                 (0, 2): 2, (1, 2): 2, (2, 3): 1}

        print_board(board, character)
        expected = '[1;37;40m\',\'[0m[1;37;40m,.,[0m[1;31;40m<o>[0m[1;98;40' \
                   'm(*)[0m[1;91;47m B [0m[1;35;40m t [0m[1;31;40m\',\'[0m' \
                   '[1;31;40m\',\'[0m[1;31;40m,.,[0m'

        self.assertEqual(expected, mock_output.getvalue())
