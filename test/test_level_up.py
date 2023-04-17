import io
from unittest import TestCase
from unittest.mock import patch

from game import level_up


class Test(TestCase):
    @patch('game.class_info',
           return_value={'Skills': {'Lightning Blast': {'Cooldown': [10, 10],
                                                        'Damage Multiplier': 12}}})
    def test_level_up_lvl_1_to_2(self, _):
        character_example = {'Class': 'Wizard', 'Level': 1, 'Current HP': 62,
                             'Max HP': 62, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 90,
                             'Level up XP': 100,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}

        level_up(character_example)

        expected = {'Accuracy': 65,
                    'Class': 'Battle Mage',
                    'Current HP': 186,
                    'Damage': 27.0,
                    'Experience': -10,
                    'Level': 2,
                    'Level up XP': 900,
                    'Max HP': 186,
                    'Skills': {'Firebolt     ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Ice Missile  ': {'Cooldown': [4, 4], 'Damage Multiplier': 4},
                               'Lightning Blast': {'Cooldown': [10, 10], 'Damage Multiplier': 12}}}
        self.assertEqual(expected, character_example)

    @patch('game.class_info',
           return_value={'Skills': {'(Ultimate): Orbital Bombardment': {'Cooldown': [20, 20],
                                                                        'Damage Multiplier': 25}}})
    def test_level_up_lvl_2_to_3(self, _):
        character_example = {'Name': 'Belal', 'Class': 'Battle Mage', 'Level': 2, 'Current HP': 62,
                             'Max HP': 62, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 120,
                             'Level up XP': 100,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Cooldown': [10, 10],
                                                     'Damage Multiplier': 12}}}

        level_up(character_example)

        expected = {'Accuracy': 65,
                    'Class': 'Legendary Arcane Master',
                    'Current HP': 186,
                    'Damage': 27.0,
                    'Experience': 20,
                    'Level': 3,
                    'Level up XP': 900,
                    'Max HP': 186,
                    'Name': 'Belal',
                    'Skills': {'(Ultimate): Orbital Bombardment': {'Cooldown': [20, 20],
                                                                   'Damage Multiplier': 25},
                               'Firebolt     ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Ice Missile  ': {'Cooldown': [4, 4], 'Damage Multiplier': 4},
                               'Lightning Blast': {'Cooldown': [10, 10], 'Damage Multiplier': 12}}}
        self.assertEqual(expected, character_example)

    @patch('game.class_info', return_value={})
    def test_level_up_lvl_4_to_5_does_not_change_class(self, _):
        character_example = {'Accuracy': 65,
                             'Class': 'Legendary Arcane Master',
                             'Current HP': 186,
                             'Damage': 42.0,
                             'Experience': 1000,
                             'Level': 4,
                             'Level up XP': 800,
                             'Max HP': 186,
                             'Name': 'Belal',
                             'Skills': {'(Ultimate): Orbital'
                                        ' Bombardment': {'Cooldown': [19, 20],
                                                         'Damage Multiplier': 25},
                                        'Firebolt     ': {'Cooldown': [1, 1],
                                                          'Damage Multiplier': 2},
                                        'Ice Missile  ': {'Cooldown': [4, 4],
                                                          'Damage Multiplier': 4},
                                        'Lightning Blast': {'Cooldown': [10, 10],
                                                            'Damage Multiplier': 12}}}
        level_up(character_example)

        expected = {'Accuracy': 65,
                    'Class': 'Legendary Arcane Master',
                    'Current HP': 558,
                    'Damage': 48.0,
                    'Experience': 200,
                    'Level': 5,
                    'Level up XP': 7200,
                    'Max HP': 558,
                    'Name': 'Belal',
                    'Skills': {'(Ultimate): Orbital Bombardment': {'Cooldown': [19, 20],
                                                                   'Damage Multiplier': 25},
                               'Firebolt     ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Ice Missile  ': {'Cooldown': [4, 4], 'Damage Multiplier': 4},
                               'Lightning Blast': {'Cooldown': [10, 10], 'Damage Multiplier': 12}}}
        self.assertEqual(expected, character_example)

    @patch('game.class_info',
           return_value={'Skills': {'Lightning Blast': {'Cooldown': [10, 10],
                                                        'Damage Multiplier': 12}}})
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_print_level_up_message(self, mock_output, _):
        character_example = {'Class': 'Wizard', 'Level': 1, 'Current HP': 62,
                             'Max HP': 62, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 90,
                             'Level up XP': 120,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}

        level_up(character_example)

        expected = ("Leveled up to Battle Mage!\n"
                    "\n"
                    "Learned Lightning Blast\n")
        self.assertEqual(expected, mock_output.getvalue())
