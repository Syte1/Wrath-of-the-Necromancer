import io
from unittest import TestCase
from unittest.mock import patch

from game import reward_experience


class Test(TestCase):
    @patch('game.level_up', return_value=None)
    def test_reward_experience_grant_experience(self, _):
        character_example = {'Name': 'Belal', 'Class': 'Wizard', 'Level': 1, 'Current HP': 63,
                             'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 0,
                             'Level up XP': 6400,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}

        enemy_example = {'Level': 1, 'Current HP': 10, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10}

        reward_experience(enemy_example, character_example)

        expected = {'Accuracy': 65,
                    'Class': 'Wizard',
                    'Current HP': 63,
                    'Damage': 21.0,
                    'Experience': 25,  # experience went up
                    'Level': 1,
                    'Level up XP': 6400,
                    'Max HP': 63,
                    'Name': 'Belal',
                    'Skills': {'Firebolt     ': {'Cooldown': [1, 1], 'Damage Multiplier': 2},
                               'Ice Missile  ': {'Cooldown': [4, 4], 'Damage Multiplier': 4}}}
        self.assertEqual(expected, character_example)

    @patch('game.level_up', return_value=None)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_reward_experience_grant_experience_print(self, mock_output, _):
        character_example = {'Name': 'Belal', 'Class': 'Wizard', 'Level': 1, 'Current HP': 60,
                             'Max HP': 60, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 0,
                             'Level up XP': 6400,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}

        enemy_example = {'Level': 1, 'Current HP': 10, 'Accuracy': 50, 'Damage': 3,
                         'Experience reward': 25, 'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg', 'Max HP': 10}

        reward_experience(enemy_example, character_example)

        expected = ("\n"
                    "You have slain the Dirty Raccoon\n"
                    "Obtained 25 experience\n"
                    "\n")
        self.assertEqual(expected, mock_output.getvalue())
