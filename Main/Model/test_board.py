import unittest
from Board import Board
from Directions import Direction
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
        board = Board(2, 2)
        pacman = Pacman()
        pacman_position = Position(0, 0)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))

    def test_move_pacman_UP(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.UP)
        self.assertEqual(pacman, board.get_entity(Position(0, 1)))

    def test_move_pacman_DOWN(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.DOWN)
        self.assertEqual(pacman, board.get_entity(Position(2, 1)))

    def test_move_pacman_RIGHT(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.RIGHT)
        self.assertEqual(pacman, board.get_entity(Position(1, 2)))

    def test_move_pacman_LEFT(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.LEFT)
        self.assertEqual(pacman, board.get_entity(Position(1, 0)))

    def test_move_pacman_up_limit_case(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(0, 0)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.UP)
        self.assertEqual(pacman, board.get_entity(Position(0, 0)))

    def test_move_pacman_down_limit_case(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(4, 0)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.DOWN)
        self.assertEqual(pacman, board.get_entity(Position(4, 0)))

    def test_move_pacman_right_limit_case(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(0, 4)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.RIGHT)
        self.assertEqual(pacman, board.get_entity(Position(0, 4)))

    def test_move_pacman_left_limit_case(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 0)
        board.place_entity(pacman_position, pacman)
        pacman.move(board, Direction.LEFT)
        self.assertEqual(pacman, board.get_entity(Position(1, 0)))


if __name__ == '__main__':
    unittest.main()
