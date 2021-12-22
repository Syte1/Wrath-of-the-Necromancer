import io
from unittest import TestCase
from unittest.mock import patch

from game import pick_up_treasure


class Test(TestCase):

    @patch('game.identify_treasure', return_value="Shiny Medallion of Earth-breaking")
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pick_up_treasure_damage_print(self, mock_output, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = ("Artifact: Shiny Medallion of Earth-breaking\n"
                    "You gain 1.0 damage!\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.identify_treasure', return_value="Dusty Coin of Content")
    @patch('random.randint', return_value=2)
    def test_pick_up_treasure_upgrade_damage(self, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = {'Current HP': 63, 'Damage': 22.0, 'Max HP': 63}
        self.assertEqual(expected, character_example)

    @patch('game.identify_treasure', return_value="Dusty Coin of Content")
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pick_up_treasure_max_health_print(self, mock_output, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = ("Artifact: Dusty Coin of Content\n"
                    "You gain 1 max health!\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.identify_treasure', return_value="Dusty Coin of Content")
    @patch('random.randint', return_value=1)
    def test_pick_up_treasure_upgrade_max_health(self, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = {'Current HP': 63, 'Damage': 21.0, 'Max HP': 64}
        self.assertEqual(expected, character_example)

    @patch('game.identify_treasure', return_value="Excellent Bracelet of Scarlet-Guardian")
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pick_up_treasure_heal_to_max_health_print(self, mock_output, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = ("Artifact: Excellent Bracelet of Scarlet-Guardian\n"
                    "You heal back to max health!\n")
        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.identify_treasure', return_value="Excellent Bracelet of Scarlet-Guardian")
    @patch('random.randint', return_value=3)
    def test_pick_up_treasure_heal_to_max_health(self, _, __):
        character_example = {'Current HP': 2,
                             'Max HP': 63,
                             'Damage': 21.0}
        pick_up_treasure(character_example)
        expected = {'Current HP': 63, 'Damage': 21.0, 'Max HP': 63}
        self.assertEqual(expected, character_example)
