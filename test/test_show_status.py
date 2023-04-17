import io
from unittest import TestCase
from unittest.mock import patch
from game import show_status


class Test(TestCase):
    @patch('game.prompt_to_continue', return_value=None)
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_status_show_correct_status(self, mock_output, _, __):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 1,
                     'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                     'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                     'Level up XP': 6400,
                     'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1)],
                     'Skills': {'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]},
                                'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                    'Cooldown': [20, 20]}}}
        show_status(character)
        expected = ("\n"
                    "Name: Belal	Class: Legendary Arcane Master\n"
                    "HP: 63 / 63\n"
                    "Level: 3	Experience: 159 / 6400\n"
                    "Damage: 21.0\n"
                    "Accuracy: 65\n")
        self.assertEqual(expected, mock_output.getvalue())