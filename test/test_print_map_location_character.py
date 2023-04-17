import io
from unittest import TestCase
from unittest.mock import patch

from game import print_map_location_character as print_mlc


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_location_character_check_correct_description(self, mock_output):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 1,
                     'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                     'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                     'Level up XP': 6400,
                     'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1)]}

        board = {(0, 0): 1, (1, 0): 2, (2, 0): 3,
                 (0, 1): 4, (1, 1): "B", (2, 1): "t",
                 (0, 2): 2, (1, 2): 2, (2, 3): 1}

        print_mlc(board, character)
        expected = (
            "[1;37;40m,.,[0m[1;37;40m','[0m[1;31;40m<o>[0m[1;98;40m(*)"
            "[0m[1;91;47m B [0m[1;35;40m t [0m[1;31;40m','[0m[1;31;"
            "40m','[0m[1;31;40m,.,[0m[38;2;150;35;35;40mA dark rocky area. The "
            "sky is red, and it's very hard to see.\n"
            "\n"
            "Current HP: 63 / 63\n")
        self.assertEqual(expected, mock_output.getvalue())
