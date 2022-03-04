import unittest
from Board import Board
from Directions import Direction
from Position import Position
from Pacman import Pacman
from Wall import Wall


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
        board = Board(2, 2)
        pacman = Pacman()
        pacman_position = Position(0, 0)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))

    def test_move_pacman(self):
        board = Board(2, 2)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)        
        pacman.move(board, Direction.DOWN)
        self.assertEqual(pacman, board.get_entity(Position(0,1)))


if __name__ == '__main__':
    unittest.main()
