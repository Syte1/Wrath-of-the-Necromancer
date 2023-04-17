from unittest import TestCase
from game import is_dead


class Test(TestCase):
    def test_is_dead_positive_health(self):
        character = {"Current HP": 1}
        self.assertFalse(is_dead(character))

    def test_is_dead_zero_health(self):
        character = {"Current HP": 0}
        self.assertTrue(is_dead(character))

    def test_is_dead_negative_health(self):
        character = {"Current HP": -1}
        self.assertTrue(is_dead(character))
