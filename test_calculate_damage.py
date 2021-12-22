from unittest import TestCase
from unittest.mock import patch

from game import calculate_damage


class Test(TestCase):
    @patch('random.choices', return_value=[True])
    def test_calculate_damage_accurate_hit_higher_than_normal_damage(self, _):
        chosen_attack_example = 1
        character_example = {'Damage': 21.0,
                             'Accuracy': 65,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]}}}
        actual = calculate_damage(chosen_attack_example, character_example)
        raw_damage_example = character_example["Damage"] * 2  # Firebolt has 2 damage multiplier
        damage_is_increased = actual[0] > raw_damage_example
        self.assertTrue(damage_is_increased)  # check if damage increased from raw

    @patch('random.choices', return_value=[False])
    def test_calculate_damage_inaccurate_hit_lower_than_normal_damage(self, _):
        chosen_attack_example = 1
        character_example = {'Damage': 21.0,
                             'Accuracy': 65,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [2, 2]}}}
        actual = calculate_damage(chosen_attack_example, character_example)
        raw_damage_example = character_example["Damage"] * 2  # Firebolt has 2 damage multiplier
        damage_is_increased = actual[0] > raw_damage_example
        self.assertFalse(damage_is_increased)  # check if damage increased from raw
