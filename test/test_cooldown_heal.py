from unittest import TestCase

from game import reduce_cooldown_heal


class Test(TestCase):
    def test_reduce_cooldown_heal_replenish_health_and_cooldown_lvl_3(self):
        character_example = {'Level': 3, 'Current HP': 5,
                             'Max HP': 10,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [0, 6]}}}
        reduce_cooldown_heal(character_example)
        # replenished 3 cooldown and heal because level 3
        expected = {'Current HP': 8,
                    'Level': 3,
                    'Max HP': 10,
                    'Skills': {'Firebolt     ': {'Cooldown': [1, 6], 'Damage Multiplier': 2}}}
        self.assertEqual(expected, character_example)

    def test_reduce_cooldown_heal_replenish_health_and_cooldown_lvl_1(self):
        character_example = {'Level': 1, 'Current HP': 1,
                             'Max HP': 60,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [0, 3]}}}
        reduce_cooldown_heal(character_example)
        # replenished 1 hp and cooldown because level 1
        expected = {'Current HP': 2,
                    'Level': 1,
                    'Max HP': 60,
                    'Skills': {'Firebolt     ': {'Cooldown': [1, 3], 'Damage Multiplier': 2}}}
        self.assertEqual(expected, character_example)

    def test_reduce_cooldown_heal_replenish_cooldown_over_maximum(self):
        character_example = {'Level': 3, 'Current HP': 59,
                             'Max HP': 60,
                             'Skills': {
                                 'Firebolt     ': {'Damage Multiplier': 2, 'Cooldown': [3, 3]}}}
        reduce_cooldown_heal(character_example)
        # only replenished 1 cooldown and 1 health despite being level 3
        expected = {'Current HP': 60,
                    'Level': 3,
                    'Max HP': 60,
                    'Skills': {'Firebolt     ': {'Cooldown': [3, 3], 'Damage Multiplier': 2}}}
        self.assertEqual(expected, character_example)
