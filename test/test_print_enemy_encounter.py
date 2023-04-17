import io
from unittest import TestCase
from unittest.mock import patch

from game import print_enemy_encounter


class Test(TestCase):
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_encounter_enemy_encountered_print_properly(self, mock_output, _):
        character_example = {'Level': 3,
                             'Current HP': 63,
                             'Max HP': 63}

        enemy_example = {'Current HP': 10,
                         'Name': 'Dirty Raccoon',
                         'Max HP': 10,
                         'Level': 1,
                         'Appeared': False}

        expected = ("Dirty Raccoon appears!\n"
                    "\n"
                    "Dirty Raccoon:\n"
                    "Enemy:  Level		Health\n"
                    "		  1			10 / 10\n"
                    "\n"
                    "You:	Level		Health\n"
                    "		  3		    63 / 63\n")

        print_enemy_encounter(enemy_example, character_example)
        self.assertEqual(expected, mock_output.getvalue())
