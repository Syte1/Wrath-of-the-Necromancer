import io
from unittest import TestCase
from unittest.mock import patch

from game import color_text


class Test(TestCase):
    def test_color_text_change_color_of_argument(self):
        self.assertEqual("[38;2;100;100;100;40mtest", color_text("test", [100, 100, 100]))

    def test_color_text_change_color_of_argument_to_different_color(self):
        self.assertEqual("[38;2;50;100;200;40mtest", color_text("test", [50, 100, 200]))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_color_text_change_color_of_future_text(self, mock_output):
        print(color_text("colored text", [100, 100, 100]))
        print("future text")
        expected = ("[38;2;100;100;100;40mcolored text\n"
                    "future text\n")
        self.assertEqual(expected, mock_output.getvalue())
