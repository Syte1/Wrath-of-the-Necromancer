from unittest import TestCase
from game import save_path


class Test(TestCase):
    def test_save_path_save_current_coordinate_to_character_save_path(self):
        character = {'Name': 'Belal', 'X-Coordinate': 17, 'Y-Coordinate': 9,
                     'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                     'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                     'Level up XP': 6400,
                     'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1)]}
        save_path(character)
        expected = {'Name': 'Belal', 'X-Coordinate': 17, 'Y-Coordinate': 9,
                    'Class': 'Legendary Arcane Master', 'Level': 3, 'Current HP': 63,
                    'Max HP': 63, 'Damage': 21.0, 'Accuracy': 65, 'Experience': 159,
                    'Level up XP': 6400,
                    'Saved path': [(0, 0), (0, 1), (1, 0), (1, 1), (17, 9)]}
        self.assertEqual(expected, character)
