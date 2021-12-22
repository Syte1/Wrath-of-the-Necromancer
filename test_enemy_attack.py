import io
from unittest import TestCase
from unittest.mock import patch

from game import enemy_attack


class Test(TestCase):
    @patch('game.calculate_enemy_damage', return_value=(4, True))
    def test_enemy_attack_player_takes_damage(self, _):
        character_example = {'Current HP': 63}

        enemy_example = {'Accuracy': 50,
                         'Damage': 4,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        expected = {'Current HP': 59}  # take 4 damage

        enemy_attack(enemy_example, character_example)

        self.assertEqual(expected, character_example)

    @patch('game.calculate_enemy_damage', return_value=(4, True))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_enemy_attack_player_takes_damage_print(self, mock_output, _):
        character_example = {'Current HP': 63}

        enemy_example = {'Accuracy': 50,
                         'Damage': 4,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        expected = ("Dirty Raccoon bites at your leg\n"
                    "It was an accurate hit!\n"
                    "You take 4 damage\n")

        enemy_attack(enemy_example, character_example)

        self.assertEqual(expected, mock_output.getvalue())
