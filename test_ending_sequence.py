import io
from unittest import TestCase
from unittest.mock import patch

from game import ending_sequence


class Test(TestCase):
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_ending_sequence_print_ascii_and_character_stats(self, mock_output, _):
        character_example = {'Name': 'Belal', 'X-Coordinate': 21, 'Y-Coordinate': 12,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)],
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 3, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}
        ending_sequence(character_example)
        expected = ("  _   __   _        __                   \n"
                    " | | / /  (_) ____ / /_ ___   ____  __ __\n"
                    " | |/ /  / / / __// __// _ "
                    "\\ "
                    "/ __/ / // /\n"
                    " |___/  /_/  "
                    "\\__"
                    "/ "
                    "\\__"
                    "/ "
                    "\\___//_/    "
                    "\\_, / \n"
                    "                                  /___/  \n"
                    "You have defeated the necromancer and avenged your comrades, Belal!\n"
                    "\n"
                    "\n"
                    "Name: Belal	Class: Legendary Arcane Master\n"
                    "HP: 63 / 63\n"
                    "Level: 3	Experience: 159 / 6400\n"
                    "Damage: 21.0\n"
                    "Accuracy: 65\n")
        self.assertEqual(expected, mock_output.getvalue())
