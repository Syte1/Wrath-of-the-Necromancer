from unittest import TestCase
from game import class_info


class Test(TestCase):
    def test_class_info_pull_up_class_dictionary(self):
        class_to_check = class_info("Knight")
        expected = {'Accuracy': 85,
                    'Damage': 3,
                    'Max HP': 23,
                    'Skills': {'Slash        ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Sword Barrage': {'Cooldown': [3, 3], 'Damage Multiplier': 3}}}
        self.assertEqual(expected, class_to_check)
