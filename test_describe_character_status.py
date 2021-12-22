import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_character_status as status


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_character_status_with_positive_HP(self, mock_output):
        status({"Current HP": 3, "Max HP": 3})
        self.assertEqual("\nCurrent HP: 3 / 3\n", mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_character_status_with_negative_HP(self, mock_output):
        status({"Current HP": -2, "Max HP": 3})
        self.assertEqual("\nCurrent HP: -2 / 3\n", mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_character_status_with_0_HP(self, mock_output):
        status({"Current HP": 0, "Max HP": 3})
        self.assertEqual("\nCurrent HP: 0 / 3\n", mock_output.getvalue())
