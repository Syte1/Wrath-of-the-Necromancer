import io
from unittest import TestCase
from unittest.mock import patch

from game import choose_color_saved_path


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_color_saved_path_coordinate_is_saved_path(self, mock_output):

        character_example = {'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1)]}

        board_example = {(0, 0): 1,
                         (1, 0): 2,
                         (2, 0): 3,
                         (0, 0): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        coordinates_example = (0, 0)

        level_color_example = 32

        choose_color_saved_path(board_example, coordinates_example, character_example,
                                level_color_example)

        expected = "[1;37;40m,O.[0m"

        self.assertEqual(expected, mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_color_saved_path_coordinate_is_not_saved(self, mock_output):

        character_example = {'Saved path': [(0, 1), (1, 0), (1, 1)]}

        board_example = {(0, 0): 1,
                         (3, 0): 2,
                         (2, 0): 3,
                         (4, 0): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        coordinates_example = (0, 0)

        level_color_example = 32

        choose_color_saved_path(board_example, coordinates_example, character_example,
                                level_color_example)

        expected = "[1;32;40m,.,[0m"

        self.assertEqual(expected, mock_output.getvalue())
