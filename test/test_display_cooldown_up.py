from unittest import TestCase
from unittest.mock import patch

from game import display_cooldown_up


class Test(TestCase):
    @patch('game.is_on_cooldown', return_value=False)
    def test_display_cooldown_up_when_ability_available(self, _):
        character_example = {'Skills': {
            'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
            'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]},
            'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [10, 10]},
            '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                'Cooldown': [20, 20]}}}
        self.assertEqual("✅", display_cooldown_up(character_example, 'Lightning Blast'))

    @patch('game.is_on_cooldown', return_value=True)
    def test_display_cooldown_up_when_ability_not_available(self, _):
        character_example = {'Skills': {
            'Lightning Blast': {'Damage Multiplier': 12,
                                'Cooldown': [5, 10]},
            '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                'Cooldown': [20, 20]}}}
        self.assertEqual("❌", display_cooldown_up(character_example, 'Lightning Blast'))
