import io
from unittest import TestCase
from unittest.mock import patch

from game import choose_fight_option


class Test(TestCase):
    @patch('builtins.input', side_effect=["", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_fight_option_pick_wrong_option_then_right_option(self, mock_output, _):
        choose_fight_option()
        expected = " is not a valid selection. Choose 1, or 2\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['1'])
    def test_choose_fight_option_pick_run(self, _):
        actual = choose_fight_option()
        self.assertEqual("1", actual)

    @patch('builtins.input', side_effect=['2'])
    def test_choose_fight_option_pick_fight(self, _):
        actual = choose_fight_option()
        self.assertEqual("2", actual)
