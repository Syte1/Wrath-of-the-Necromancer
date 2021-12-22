from unittest import TestCase
from game import create_wall


class Test(TestCase):
    def test_create_wall_vertical_wall(self):
        board_example = {(1, 0): 2,
                         (0, 0): 1,
                         (2, 0): 3,
                         (0, 1): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 3): 1}

        walls_example = [(0, 0),
                         (0, 1)]

        create_wall(board_example, walls_example)

        expected = {(0, 0): 'V',
                    (0, 1): 'V',  # vertical wall
                    (0, 2): 2,
                    (1, 0): 2,
                    (1, 1): 'B',
                    (1, 2): 2,
                    (2, 0): 3,
                    (2, 1): 't',
                    (2, 3): 1}

        self.assertEqual(expected, board_example)

    def test_create_wall_horizontal_wall(self):
        board_example = {(1, 0): 2,
                         (0, 0): 1,
                         (2, 0): 3,
                         (0, 1): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (3, 3): 1}

        walls_example = [(0, 0),
                         (1, 0)]

        create_wall(board_example, walls_example)

        expected = {(0, 0): 'H',
                    (0, 1): 4,
                    (0, 2): 2,
                    (1, 0): 'H',  # horizontal wall
                    (1, 1): 'B',
                    (1, 2): 2,
                    (2, 0): 3,
                    (2, 1): 't',
                    (3, 3): 1}

        self.assertEqual(expected, board_example)

    def test_create_wall_create_wall_joint(self):
        board_example = {(1, 0): 2,
                         (0, 0): 1,
                         (2, 0): 3,
                         (0, 1): 4,
                         (1, 1): "B",
                         (2, 1): "t",
                         (0, 2): 2,
                         (1, 2): 2,
                         (2, 2): 1}

        walls_example = [(0, 0), (1, 0),
                         (1, 0), (1, 1)]

        create_wall(board_example, walls_example)

        expected = {(0, 0): 'H',
                    (0, 1): 4,
                    (0, 2): 2,
                    (1, 0): '+',  # wall joint
                    (1, 1): 'V',
                    (1, 2): 2,
                    (2, 0): 3,
                    (2, 1): 't',
                    (2, 2): 1}

        self.assertEqual(expected, board_example)
