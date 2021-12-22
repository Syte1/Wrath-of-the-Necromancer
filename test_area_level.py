from unittest import TestCase
from game import area_level


class Test(TestCase):
    def test_area_level_character_in_level_3_area(self):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 1}
        self.assertEqual(3, area_level(character))

    def test_area_level_character_in_level_2_area(self):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 10}
        self.assertEqual(2, area_level(character))

    def test_area_level_character_in_level_1_area(self):
        character = {'Name': 'Belal', 'X-Coordinate': 0, 'Y-Coordinate': 20}
        self.assertEqual(1, area_level(character))
