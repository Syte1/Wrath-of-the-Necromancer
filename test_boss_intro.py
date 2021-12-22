import io
from unittest import TestCase
from unittest.mock import patch
from game import boss_intro


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_boss_intro_showing_character_name_and_class(self, mock_output):
        character_example = {"Class": "Knight"}
        boss_intro(character_example)

        expected = ("The air is thick with the scent of blood.\n"
                    "As you step closer, a red mist pools ahead of you\n"
                    "The silhouette turns and you get a better glimpse of it.\n"
                    "\n"
                    "	'Hahaha,'\n"
                    "\n"
                    "	'I've been expecting you, Knight'\n"
                    "\n"
                    "An enormous red aura rushes in from every corner of the room \n"
                    "into the silhouette and the room fills with red light.\n"
                    "\n"
                    "The necromancer's giant grin startles you.\n"
                    "You get into combat stance.\n"
                    "\n")
        self.assertEqual(expected, mock_output.getvalue())
