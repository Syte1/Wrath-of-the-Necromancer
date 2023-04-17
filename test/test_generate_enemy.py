from unittest import TestCase
from unittest.mock import patch

from game import generate_enemy


class Test(TestCase):
    @patch('game.area_level', return_value=3)
    @patch('random.randint', return_value=5)
    def test_generate_enemy_lvl_3(self, _, __):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 1}
        actual = generate_enemy(character_example)
        expected = {'Accuracy': 70,
                    'Appeared': False,
                    'Current HP': 5,
                    'Damage': 5,
                    'Experience reward': 5,
                    'Level': 3,
                    'Max HP': 5,
                    'Move': 'slashes at you with its ethereal scythe',
                    'Name': 'Corrupt Wraith'}
        self.assertEqual(expected, actual)

    @patch('game.area_level', return_value=2)
    @patch('random.randint', return_value=5)
    def test_generate_enemy_lvl_2(self, _, __):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 10}
        actual = generate_enemy(character_example)
        expected = {'Accuracy': 65,
                    'Appeared': False,
                    'Current HP': 5,
                    'Damage': 5,
                    'Experience reward': 5,
                    'Level': 2,
                    'Max HP': 5,
                    'Move': 'bulldozes into you with its immense weight',
                    'Name': 'Hungry Hippo'}
        self.assertEqual(expected, actual)

    @patch('game.area_level', return_value=1)
    @patch('random.randint', return_value=5)
    def test_generate_enemy_lvl_1(self, _, __):
        character_example = {'X-Coordinate': 0, 'Y-Coordinate': 20}
        actual = generate_enemy(character_example)
        expected = {'Accuracy': 50,
                    'Appeared': False,
                    'Current HP': 5,
                    'Damage': 5,
                    'Experience reward': 5,
                    'Level': 1,
                    'Max HP': 5,
                    'Move': 'swoops into your face and pecks you',
                    'Name': 'Hungry Seagull'}
        self.assertEqual(expected, actual)
