import io
from unittest import TestCase
from unittest.mock import patch

from game import attack_enemy


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_attack_enemy_damage_enemy(self, _):
        character_example = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [3, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}

        enemy_example = {'Current HP': 10}

        attack_enemy(1, enemy_example, character_example)

        expected = {'Current HP': 6}  # enemy took 4 damage

        self.assertEqual(expected, enemy_example)

    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_enemy_damage_enemy_print(self, mock_output, _):
        character_example = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 0,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [3, 3]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}

        enemy_example = {'Current HP': 10}

        attack_enemy(1, enemy_example, character_example)

        expected = ("You use Firebolt     \n"
                    "It was an accurate hit!\n"
                    "You dealt 4 damage\n")

        self.assertEqual(expected, mock_output.getvalue())
