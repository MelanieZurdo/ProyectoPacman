import unittest
import time
from Main.Model.PacDot import PacDot
from Main.Model.FixedDirectionStrategy import FixedDirectionStrategy
from Main.Model.Direction import Direction
from Main.Model.Board import Board
from Main.Model.Position import Position
from Main.Model.Pacman import Pacman
from Main.View.Console.BoardView import BoardView


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(10, 10)
        self.pacman = Pacman(FixedDirectionStrategy(Direction.up()))

    def tearDown(self):
        pass

    def test_insert_entity(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.up()))
        pacman_position = Position(0, 0)
        self.board.place_entity(pacman_position, pacman)
        self.assertIn(self.pacman, board.get_entities(pacman_position))

    def test_getrows(self):
        self.assertEqual(3, self.board.get_rows())

    def test_getcolumns(self):
        test_board = Board(3, 2)
        self.assertEqual(2, test_board.get_columns())

    def test_move_pacman_up(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.up()))
        pacman_position = Position(2, 1)
        board_view = BoardView(board)
        board_view.show()
        time.sleep(1)
        board.place_entity(pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, board.get_entities(Position(1, 1)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_down(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.down()))
        pacman_position = Position(7, 0)
        board_view = BoardView(board)
        board_view.show()
        time.sleep(1)
        board.place_entity(pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, board.get_entities(Position(8, 0)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_right(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        pacman_position = Position(5, 0)
        board_view = BoardView(board)
        board_view.show()
        time.sleep(1)
        board.place_entity(pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, board.get_entities(Position(5, 1)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_right(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.left()))
        pacman_position = Position(4, 1)
        board_view = BoardView(board)
        board_view.show()
        time.sleep(1)
        board.place_entity(pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, board.get_entities(Position(4, 0)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_capture_eatable_entity(self):
        board = Board(10, 10)
        pacman = Pacman(FixedDirectionStrategy(Direction.left()))
        pacman_position = Position(4, 1)
        board_view = BoardView(board)
        board_view.show()
        time.sleep(1)
        board.place_entity(pacman_position, pacman)
        pacdot = PacDot()
        pacdot_position = Position(4, 0)
        board.place_entity(pacdot_position, pacdot)
        board_view.show()
        time.sleep(1)
        board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, board.get_entities(Position(4, 0)))
        self.assertNotIn(pacdot, board.get_entities(Position(4, 0)))


if __name__ == '__main__':
    unittest.main()
