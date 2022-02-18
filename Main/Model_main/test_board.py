import unittest
from Board import Board
from Position import Position
from Pacman import Pacman


class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getrows(self):
        test_board = Board(3, 2)
        self.assertEqual(3, test_board.get_rows())

    def test_getcolumns(self):
        test_board = Board(3, 2)
        self.assertEqual(2, test_board.get_columns())

    def test_insert_entity(self):
        board = Board(2,2)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman.__str__(),board.get_entity(pacman_position))


if __name__ == '__main__':
    unittest.main()
