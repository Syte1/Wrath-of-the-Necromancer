import io
from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice as get_choice


class Test(TestCase):
    @patch('builtins.input', side_effect=['W'])
    def test_get_user_choice_choose_up(self, _):
        self.assertEqual(1, get_choice())

    @patch('builtins.input', side_effect=['S'])
    def test_get_user_choice_choose_down(self, _):
        self.assertEqual(2, get_choice())

    @patch('builtins.input', side_effect=['A'])
    def test_get_user_choice_choose_left(self, _):
        self.assertEqual(3, get_choice())

    @patch('builtins.input', side_effect=['D'])
    def test_get_user_choice_choose_right(self, _):
        self.assertEqual(4, get_choice())

    @patch('builtins.input', side_effect=['r', 'W'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_choose_one_invalid_input_then_valid_input(self, mock_output, _):
        get_choice()
        expected = "r is not valid. You must input a W, A, S, or D\n"
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['r', '12', 'W'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_choose_two_invalid_inputs_then_one_valid_input(self, mock_output, _):
        get_choice()
        expected = "r is not valid. You must input a W, A, S, or D\n" \
                   "12 is not valid. You must input a W, A, S, or D\n"
        self.assertEqual(expected, mock_output.getvalue())
