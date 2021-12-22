import io
from unittest import TestCase
from unittest.mock import patch

from game import choose_attack


class Test(TestCase):
    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_attack_use_ability_successfully(self, mock_output, _):
        character_example = {'Damage': 21.0,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}
        choose_attack(character_example)
        expected = ("\n"
                    "Available moves:\n"
                    "[1]	Firebolt     	✅	Cooldown: 1 / 1\n"
                    "[2]	Ice Missile  	✅	Cooldown: 4 / 4\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_attack_use_ability_unsuccessfully_then_successfully(self, mock_output, _):
        character_example = {'Damage': 21.0,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [0, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}
        choose_attack(character_example)
        expected = ("\n"
                    "Available moves:\n"
                    "[1]	Firebolt     	❌	Cooldown: 0 / 1\n"
                    "[2]	Ice Missile  	✅	Cooldown: 4 / 4\n"
                    "Firebolt      is on cooldown.\n"
                    "Walk around or use other abilities to refresh it\n"
                    "[1]	Firebolt     	❌	Cooldown: 0 / 1\n"
                    "[2]	Ice Missile  	✅	Cooldown: 4 / 4\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('builtins.input', side_effect=['1'])
    def test_choose_attack_check_skill_cooldown_is_0_after_use(self, _):
        # start with ability ready
        character_example = {'Damage': 21.0,
                             'Skills': {
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]}}}
        choose_attack(character_example)
        current_cooldown = character_example['Skills']['Ice Missile  ']['Cooldown'][0]
        self.assertEqual(0, current_cooldown)
