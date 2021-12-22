from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes as check_foes


class Test(TestCase):
    @patch('random.choices', return_value=[True])
    def test_check_for_foes_found(self, _):
        self.assertTrue(check_foes())

    @patch('random.choices', return_value=[False])
    def test_check_for_foes_not_found(self, _):
        self.assertFalse(check_foes())
