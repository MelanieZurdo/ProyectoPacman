import unittest
from Board import Board
from Main.Model.PacDot import PacDot
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
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))

    def test_move_pacman(self):
        board = Board(2, 2)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        board.place_entity((pacman.move(Position(0, 0))), (board.get_entity(pacman_position)))
        board.clean_entity(pacman_position)
        self.assertEqual(pacman, board.get_entity(
        (pacman.move(Position(0, 0)))))
        self.assertNotEqual(pacman, board.get_entity(pacman_position))

    def test_set_complete_board(self):
        board=Board(2,2)
        pacman=Pacman()
        pacman_position = Position(0,0)
        for i,j in enumerate(board):
            if board[i][j].is_empty():
                board[i][j].put(PacDot())
            




if __name__ == '__main__':
    unittest.main()
