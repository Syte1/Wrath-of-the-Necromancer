from unittest import TestCase
from game import is_on_cooldown


class Test(TestCase):
    def test_is_on_cooldown_ability_is_ready(self):
        character_example = {'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Ice Missile  ': {'Damage Multiplier': 4, 'Cooldown': [4, 4]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [5, 10]}}}

        self.assertTrue(is_on_cooldown(character_example, 'Lightning Blast'))

    def test_is_on_cooldown_ability_is_not_ready(self):
        character_example = {'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [1, 1]},
                                 'Lightning Blast': {'Damage Multiplier': 12, 'Cooldown': [10, 10]},
                                 '(Ultimate): Orbital Bombardment': {'Damage Multiplier': 25,
                                                                     'Cooldown': [20, 20]}}}

        self.assertFalse(is_on_cooldown(character_example, 'Lightning Blast'))
