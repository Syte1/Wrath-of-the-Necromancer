import io
from unittest import TestCase
from unittest.mock import patch
from game import describe_current_location


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_grassy_area(self, mock_output):
        describe_current_location({(0, 0): 1, (0, 1): 2, (0, 2): 3},
                                  {'X-Coordinate': 0, 'Y-Coordinate': 0})
        expected = "[38;2;150;35;35;40mA dark grassy area. The sky is red and it's getting" \
                   " hard to see.\n"

        self.assertEqual(expected, mock_output.getvalue())
