from unittest import TestCase
from unittest.mock import patch

from game import calculate_enemy_damage


class Test(TestCase):
    @patch('random.choices', return_value=[True])
    def test_calculate_enemy_damage_accurate_hit_true(self, _):
        enemy_example = {'Accuracy': 50, 'Damage': 30}
        new_damage = calculate_enemy_damage(enemy_example)
        self.assertTrue(new_damage[0] > enemy_example["Damage"])

    @patch('random.choices', return_value=[False])
    def test_calculate_enemy_damage_accurate_hit_false(self, _):
        enemy_example = {'Accuracy': 50, 'Damage': 30}
        new_damage = calculate_enemy_damage(enemy_example)
        self.assertFalse(new_damage[0] > enemy_example["Damage"])
