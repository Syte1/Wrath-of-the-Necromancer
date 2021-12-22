from unittest import TestCase
from unittest.mock import patch
from game import combat_game

"""
Ok, so I don't know how to PROVE this is doing something, but if you comment out the patch of the
function and the argument it's testing, the tested helper will execute. I've tested them all like
that before changing them to None to keep the test independent
"""


class Test(TestCase):

    @patch('game.attempt_to_run', return_value=None)
    @patch('game.enemy_attack', return_value=None)
    @patch('game.choose_attack', return_value=1)
    @patch('game.enemy_run', return_value=False)
    @patch('game.reward_experience', return_value=None)
    @patch('game.attack_enemy', return_value=None)
    @patch('game.choose_fight_option', return_value="2")
    @patch('game.print_enemy_encounter', return_value=None)
    @patch('game.is_dead', return_value=False)
    @patch('game.generate_enemy',
           return_value={'Level': 1, 'Current HP': 0, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10})
    def test_combat_game_choose_to_run_successfully_and_finish_function(self, _, __, ___, ____,
                                                                        _____, ______, _______,
                                                                        ________, _________,
                                                                        __________):
        character_example = {'Name': 'Belal', 'X-Coordinate': 21, 'Y-Coordinate': 1,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Saved path': [(1, 2), (0, 1), (1, 0), (1, 1)],
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 5, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}
        self.assertIsNone(combat_game(character_example))

    @patch('game.attempt_to_run', return_value=None)
    @patch('game.enemy_attack', return_value=None)
    @patch('game.choose_attack', return_value=1)
    @patch('game.enemy_run', return_value=True)
    @patch('game.reward_experience', return_value=None)
    @patch('game.attack_enemy', return_value=None)
    @patch('game.choose_fight_option', return_value="1")
    @patch('game.print_enemy_encounter', return_value=None)
    @patch('game.is_dead', return_value=False)
    @patch('game.generate_enemy',
           return_value={'Level': 1, 'Current HP': 10, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10})
    def test_combat_game_enemy_runs_successfully_and_finish_function(self, _, __, ___, ____,
                                                                     _____, ______, _______,
                                                                     ________, _________,
                                                                     __________):
        character_example = {'Name': 'Belal', 'X-Coordinate': 2, 'Y-Coordinate': 1,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Saved path': [(1, 2), (0, 1), (1, 0), (1, 1)],
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 1, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 5, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}
        self.assertIsNone(combat_game(character_example))

    @patch('game.attempt_to_run', return_value=None)
    @patch('game.enemy_attack', return_value=None)
    @patch('game.choose_attack', return_value=1)
    @patch('game.enemy_run', return_value=False)
    @patch('game.reward_experience', return_value=None)
    @patch('game.attack_enemy', return_value=None)
    @patch('game.choose_fight_option', return_value='1')
    @patch('game.print_enemy_encounter', return_value=None)
    @patch('game.is_dead', side_effect=[False, True])
    @patch('game.generate_enemy',
           return_value={'Level': 1, 'Current HP': 0, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10})
    def test_combat_game_enemy_dead_finishes_function(self, _, __, ___, ____,
                                                      _____, ______, _______,
                                                      ________, _________,
                                                      __________):
        character_example = {'Name': 'Belal', 'X-Coordinate': 11, 'Y-Coordinate': 1,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Saved path': [(1, 2), (0, 1), (1, 0), (1, 1)],
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 3, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 5, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12,
                                                     'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}
        self.assertIsNone(combat_game(character_example))

    @patch('game.attempt_to_run', return_value=None)
    @patch('game.enemy_attack', return_value=None)
    @patch('game.choose_attack', return_value=1)
    @patch('game.enemy_run', return_value=False)
    @patch('game.reward_experience', return_value=None)
    @patch('game.attack_enemy', return_value=None)
    @patch('game.choose_fight_option', return_value="2")
    @patch('game.print_enemy_encounter', return_value=None)
    @patch('game.is_dead', return_value=True)
    @patch('game.generate_enemy',
           return_value={'Level': 1, 'Current HP': 10, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10})
    def test_combat_game_character_dead_finishes_function(self, _, __, ___, ____,
                                                          _____, ______, _______,
                                                          ________, _________,
                                                          __________):
        character_example = {'Name': 'Belal', 'X-Coordinate': 11, 'Y-Coordinate': 1,
                             'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 0,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                             'Level up XP': 6400,
                             'Saved path': [(1, 2), (0, 1), (1, 0), (1, 1)],
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 1, 'Cooldown': [2, 2]},
                                 'Ice Missile  ': {'Damage Multiplier': 5, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}
        self.assertIsNone(combat_game(character_example))
