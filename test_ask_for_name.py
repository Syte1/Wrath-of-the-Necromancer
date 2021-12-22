from unittest import TestCase
from unittest.mock import patch
from game import ask_for_name


class Test(TestCase):
    @patch('builtins.input', side_effect=['test'])
    def test_ask_for_name(self, _):
        character = {}
        ask_for_name(character)
        expected = {'Name': 'test'}
        self.assertEqual(expected, character)
