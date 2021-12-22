from unittest import TestCase
from game import symbol_dictionary


class Test(TestCase):
    def test_symbol_dictionary_level_1(self):
        self.assertEqual("[1;32;40m,.,[0m", symbol_dictionary(32, 1))

    def test_symbol_dictionary_level_2(self):
        self.assertEqual("[1;33;40m,.,[0m", symbol_dictionary(33, 1))

    def test_symbol_dictionary_level_3(self):
        self.assertEqual("[1;31;40m,.,[0m", symbol_dictionary(31, 1))

    def test_symbol_dictionary_symbol_grass(self):
        self.assertEqual("[1;32;40m,.,[0m", symbol_dictionary(32, 1))

    def test_symbol_dictionary_symbol_flowers(self):
        self.assertEqual("[1;32;40m','[0m", symbol_dictionary(32, 2))

    def test_symbol_dictionary_symbol_bushes(self):
        self.assertEqual("[1;32;40m<o>[0m", symbol_dictionary(32, 3))

    def test_symbol_dictionary_symbol_rocks(self):
        self.assertEqual("[1;32;40m,O.[0m", symbol_dictionary(32, 4))

    def test_symbol_dictionary_symbol_vertical_wall(self):
        self.assertEqual("[1;36;40m | [0m", symbol_dictionary(32, "V"))

    def test_symbol_dictionary_symbol_horizontal_wall(self):
        self.assertEqual("[1;36;40m---[0m", symbol_dictionary(32, "H"))

    def test_symbol_dictionary_symbol_wall_corner(self):
        self.assertEqual("[1;36;40m + [0m", symbol_dictionary(32, "+"))

    def test_symbol_dictionary_symbol_boss(self):
        self.assertEqual("[1;91;47m B [0m", symbol_dictionary(32, "B"))

    def test_symbol_dictionary_symbol_treasure(self):
        self.assertEqual("[1;35;40m t [0m", symbol_dictionary(32, "t"))

    def test_symbol_dictionary_symbol_character(self):
        self.assertEqual("[1;98;40m(*)[0m", symbol_dictionary(32, "@"))