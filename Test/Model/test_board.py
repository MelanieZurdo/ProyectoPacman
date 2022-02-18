import unittest

from Main.Model.Board import Board
from Main.Model.Pacman import Pacman
from Main.Model.Position import Position


class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_insert_entity(self):
        board = Board(2, 2)
        pacman = Pacman
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))
        print("caca")


if __name__ == '__main__':
    unittest.main()
