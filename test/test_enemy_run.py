import io
from unittest import TestCase
from unittest.mock import patch
from game import enemy_run


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choices', return_value=[True])
    def test_enemy_run_regular_enemy_flees_print(self, _, mock_output):
        enemy_example = {"Name": "Mouse"}
        enemy_run(enemy_example)

        self.assertEqual("Mouse runs away!\n", mock_output.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('random.choices', return_value=[False])
    def test_enemy_run_regular_enemy_fails_flee_print(self, _, mock_output):
        enemy_example = {"Name": "Mouse"}
        enemy_run(enemy_example)

        self.assertEqual("", mock_output.getvalue())

    @patch('random.choices', return_value=[True])
    def test_enemy_run_regular_enemy_flee_success_boolean(self, _):
        enemy_example = {"Name": "Mouse"}
        self.assertTrue(enemy_run(enemy_example))

    @patch('random.choices', return_value=[False])
    def test_enemy_run_regular_enemy_flee_fails_boolean(self, _):
        enemy_example = {"Name": "Mouse"}
        enemy_run(enemy_example)

        self.assertFalse(enemy_run(enemy_example))

    def test_enemy_run_boss_does_not_flee(self):
        enemy_example = {"Name": "Necromancer"}
        enemy_run(enemy_example)

        self.assertFalse(enemy_run(enemy_example))
