import io
from unittest import TestCase
from unittest.mock import patch

from game import attempt_to_run


class Test(TestCase):
    @patch('random.randint', return_value=8)
    @patch('random.choices', return_value=[True])
    def test_attempt_to_run_unsuccessfully(self, _, __):
        character_example = {'Current HP': 63,
                             'Max HP': 63}

        enemy_example = {'Accuracy': 50,
                         'Damage': 3,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        attempt_to_run(enemy_example, character_example)

        expected = {'Current HP': 61, 'Max HP': 63}

        self.assertEqual(expected, character_example)

    @patch('random.choices', return_value=[False])
    def test_attempt_to_run_successfully(self, _):

        character_example = {'Current HP': 60,
                             'Max HP': 60}

        enemy_example = {'Accuracy': 50,
                         'Damage': 3,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        attempt_to_run(enemy_example, character_example)

        expected = {'Current HP': 60, 'Max HP': 60}

        self.assertEqual(expected, character_example)

    @patch('random.randint', return_value=8)
    @patch('random.choices', return_value=[True])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_to_run_unsuccessfully_print(self, mock_output, _, __):
        character_example = {'Current HP': 60,
                             'Max HP': 60}

        enemy_example = {'Accuracy': 50,
                         'Damage': 3,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        attempt_to_run(enemy_example, character_example)

        expected = ("You attempt to run\n"
                    "Dirty Raccoon bites at your leg\n"
                    "It was an accurate hit!\n"
                    "You take 2 damage\n"
                    "Current Health: 58 / 60\n")

        self.assertEqual(expected, mock_output.getvalue())

    @patch('random.choices', return_value=[False])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attempt_to_run_successfully_print(self, mock_output, _):
        character_example = {'Current HP': 62,
                             'Max HP': 62}

        enemy_example = {'Accuracy': 50,
                         'Damage': 3,
                         'Name': 'Dirty Raccoon',
                         'Move': 'bites at your leg'}

        attempt_to_run(enemy_example, character_example)

        expected = ("You attempt to run\n"
                    "You manage you run away safely\n")
        self.assertEqual(expected, mock_output.getvalue())
