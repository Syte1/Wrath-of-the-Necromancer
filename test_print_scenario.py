import io
from unittest import TestCase
from unittest.mock import patch
from game import print_scenario


class Test(TestCase):
    @patch('game.color_text', return_value=("[38;2;50;130;255;40mYou are the Knight named Belal.\n"
                                            "You know your way around a sword and have a stron"
                                            "g sense of justice.\n"
                                            "\n"
                                            "Your hometown was ravaged by a necromancer and y"
                                            "ou are hell-bent\n"
                                            "on avenging your fallen comrades. Your mission i"
                                            "s to track down and\n"
                                            "slay the necromancer with your sword.\n"
                                            "\n"
                                            "You find yourself in a grassy land.\n"
                                            "The necromancer's castle is north of you. The n"
                                            "ecromncer was so powerful that\n"
                                            "you had no chance of defeating him in the past"
                                            ", so you will need to\n"
                                            "fight enemies and collect treasure if you want"
                                            " to sta    nd any chance in combat.\n"
                                            "\n"
                                            "You head north to the necromancer's tower.\n"))
    @patch('game.prompt_to_continue', return_value=None)
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_knight(self, mock_output, _, __, ___):
        character = {'Name': 'Belal', 'Class': "Knight"}
        print_scenario(character)
        expected = ("[38;2;50;130;255;40mYou are the Knight named Belal.\n"
                    "You know your way around a sword and have a strong"
                    " sense of justice.\n"
                    "\n"
                    "Your hometown was ravaged by a necromancer and "
                    "you are hell-bent\n"
                    "on avenging your fallen comrades. Your mission "
                    "is to track down and\n"
                    "slay the necromancer with your sword.\n"
                    "\n"
                    "You find yourself in a grassy land.\n"
                    "The necromancer's castle is north of you. The "
                    "necromncer was so powerful that\n"
                    "you had no chance of defeating him in the past"
                    ", so you will need to\n"
                    "fight enemies and collect treasure if you want"
                    " to sta    nd any chance in combat.\n"
                    "\n"
                    "You head north to the necromancer's tower.\n"
                    "\n")

        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.color_text', return_value=("[38;2;50;130;255;40mYou are the Wizard named Belal.\n"
                                            "You have an expansive understanding of magic and ye"
                                            "arn for more of it.\n"
                                            "\n"
                                            "Your hometown was ravaged by a necromancer and y"
                                            "ou are hell-bent\n"
                                            "on avenging your fallen comrades. Your mission"
                                            " is to track down and\n"
                                            "slay the necromancer with your powerful magic.\n"
                                            "\n"
                                            "You find yourself in a grassy land.\n"
                                            "The necromancer's castle is north of you. The n"
                                            "ecromancer was so"
                                            " powerful that\n"
                                            "you had no chance of defeating him in the p"
                                            "ast, so you will need to\n"
                                            "fight enemies and collect treasure if you want to"
                                            " stand any chance"
                                            " in combat.\n"
                                            "\n"
                                            "You head north to the necromancer's tower."))
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_wizard(self, mock_output, _, __):
        character = {'Name': 'Belal', 'Class': "Wizard"}
        print_scenario(character)
        expected = ("[38;2;50;130;255;40mYou are the Wizard named Belal.\n"
                    "You have an expansive understanding of magic and yearn for more of it.\n"
                    "\n"
                    "Your hometown was ravaged by a necromancer and you are hell-bent\n"
                    "on avenging your fallen comrades. Your mission is to track down and\n"
                    "slay the necromancer with your powerful magic.\n"
                    "\n"
                    "You find yourself in a grassy land.\n"
                    "The necromancer's castle is north of you. The necromancer was so"
                    " powerful that\n"
                    "you had no chance of defeating him in the past, so you will need to\n"
                    "fight enemies and collect treasure if you want to stand any chance"
                    " in combat.\n"
                    "\n"
                    "You head north to the necromancer's tower.\n")

        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.color_text', return_value=("[38;2;50;130;255;40mYou are the Archer named Belal.\n"
                                            "You're skilled with a bow, have a keen eye and grea"
                                            "t reflexes.\n"
                                            "\n"
                                            "Your hometown was ravaged by a necromancer and you"
                                            " are hell-bent\n"
                                            "on avenging your fallen comrades. Your mission is"
                                            " to track down and\n"
                                            "slay the necromancer with your bow.\n"
                                            "\n"
                                            "You find yourself in a grassy land.\n"
                                            "The necromancer's castle is north of you. The nec"
                                            "romancer was so "
                                            "powerful that\n"
                                            "you had no chance of defeating him in the past, so"
                                            " you will need to\n"
                                            "fight enemies and collect treasure if you want to"
                                            " stand any chance "
                                            "in combat.\n"
                                            "\n"
                                            "You head north to the necromancer's tower."))
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_archer(self, mock_output, _, __):
        character = {'Name': 'Belal', 'Class': "Archer"}
        print_scenario(character)
        expected = ("[38;2;50;130;255;40mYou are the Archer named Belal.\n"
                    "You're skilled with a bow, have a keen eye and great reflexes.\n"
                    "\n"
                    "Your hometown was ravaged by a necromancer and you are hell-bent\n"
                    "on avenging your fallen comrades. Your mission is to track down and\n"
                    "slay the necromancer with your bow.\n"
                    "\n"
                    "You find yourself in a grassy land.\n"
                    "The necromancer's castle is north of you. The necromancer was so "
                    "powerful that\n"
                    "you had no chance of defeating him in the past, so you will need to\n"
                    "fight enemies and collect treasure if you want to stand any chance "
                    "in combat.\n"
                    "\n"
                    "You head north to the necromancer's tower.\n")

        self.assertEqual(expected, mock_output.getvalue())

    @patch('game.color_text', return_value=(
            "[38;2;50;130;255;40mYou are the Fighter named Belal.\n"
            "You're a tough brawler with huge muscles. You aren't afraid of anything.\n"
            "\n"
            "Your hometown was ravaged by a necromancer and you are hell-bent\n"
            "on avenging your fallen comrades. Your mission is to track down and\n"
            "slay the necromancer with your fists.\n"
            "\n"
            "You find yourself in a grassy land.\n"
            "The necromancer's castle is north of you. The necromancer was so powerful that\n"
            "you had no chance of defeating him in the past, so you will need to\n"
            "fight enemies and collect treasure if you want to stand any chance in combat.\n"
            "\n"
            "You head north to the necromancer's tower."))
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_fighter(self, mock_output, _, __):
        character = {'Name': 'Belal', 'Class': "Fighter"}
        print_scenario(character)
        expected = ("[38;2;50;130;255;40mYou are the Fighter named Belal.\n"
                    "You're a tough brawler with huge muscles. You aren't afraid of anything.\n"
                    "\n"
                    "Your hometown was ravaged by a necromancer and you are hell-bent\n"
                    "on avenging your fallen comrades. Your mission is to track down and\n"
                    "slay the necromancer with your fists.\n"
                    "\n"
                    "You find yourself in a grassy land.\n"
                    "The necromancer's castle is north of you. The necromancer was so "
                    "powerful that\n"
                    "you had no chance of defeating him in the past, so you will need to\n"
                    "fight enemies and collect treasure if you want to stand any"
                    " chance in combat.\n"
                    "\n"
                    "You head north to the necromancer's tower.\n")

        self.assertEqual(expected, mock_output.getvalue())
