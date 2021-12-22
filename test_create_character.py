from unittest import TestCase
from unittest.mock import patch
from game import create_character


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_create_character_knight(self, _):
        character = {}
        create_character(character)
        expected = {'Accuracy': 85,
                    'Class': 'Knight',
                    'Current HP': 23,
                    'Damage': 3,
                    'Experience': 0,
                    'Level': 1,
                    'Level up XP': 100,
                    'Max HP': 23,
                    'Saved path': [],
                    'Skills': {'Slash        ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Sword Barrage': {'Cooldown': [3, 3], 'Damage Multiplier': 3}},
                    'X-Coordinate': 12,
                    'Y-Coordinate': 22}
        self.assertEqual(expected, character)

    @patch('builtins.input', side_effect=['2'])
    def test_create_character_wizard(self, _):
        character = {}
        create_character(character)
        expected = {'Accuracy': 65,
                    'Class': 'Wizard',
                    'Current HP': 10,
                    'Damage': 4,
                    'Experience': 0,
                    'Level': 1,
                    'Level up XP': 100,
                    'Max HP': 10,
                    'Saved path': [],
                    'Skills': {'Firebolt     ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Ice Missile  ': {'Cooldown': [4, 4], 'Damage Multiplier': 4}},
                    'X-Coordinate': 12,
                    'Y-Coordinate': 22}
        self.assertEqual(expected, character)

    @patch('builtins.input', side_effect=['3'])
    def test_create_character_archer(self, _):
        character = {}
        create_character(character)
        expected = {'Accuracy': 85,
                    'Class': 'Archer',
                    'Current HP': 15,
                    'Damage': 3,
                    'Experience': 0,
                    'Level': 1,
                    'Level up XP': 100,
                    'Max HP': 15,
                    'Saved path': [],
                    'Skills': {'Focused Arrow': {'Cooldown': [3, 3], 'Damage Multiplier': 3},
                               'Quick Shot   ': {'Cooldown': [1, 1], 'Damage Multiplier': 2}},
                    'X-Coordinate': 12,
                    'Y-Coordinate': 22}
        self.assertEqual(expected, character)

    @patch('builtins.input', side_effect=['4'])
    def test_create_character_fighter(self, _):
        character = {}
        create_character(character)
        expected = {'Accuracy': 65,
                    'Class': 'Fighter',
                    'Current HP': 30,
                    'Damage': 3,
                    'Experience': 0,
                    'Level': 1,
                    'Level up XP': 100,
                    'Max HP': 30,
                    'Saved path': [],
                    'Skills': {'Haymaker      ': {'Cooldown': [3, 3], 'Damage Multiplier': 4},
                               'Jab          ': {'Cooldown': [1, 1], 'Damage Multiplier': 2}},
                    'X-Coordinate': 12,
                    'Y-Coordinate': 22}
        self.assertEqual(expected, character)
