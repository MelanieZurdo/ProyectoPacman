import unittest
import time
import curses
from Main.Model.LevelFactory import LevelFactory
from Main.Model.PacDot import PacDot
from Main.Model.StrategyChoseDirection import ChoseDirection
from Main.Model.Direction import Direction
from Main.Model.Board import Board
from Main.Model.Direction import Up
from Main.Model.Ghost import Ghost
from Main.Model.Position import Position
from Main.Model.Pacman import Pacman
from Main.Model.Square import Square


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
        pacman = Pacman(ChoseDirection(Direction.up()))
        pacman_position = Position(0, 0)
        board.place_entity(pacman_position, pacman)
        self.assertIn(pacman, board.get_entities(pacman_position))

    def print_start(stdscr, object):
        stdscr.addstr(0, 0, str(object))
        stdscr.refresh()
        time.sleep(1)

    def test_move_pacman_up(self):
        board = Board(10, 10)
        pacman = Pacman(ChoseDirection(Direction.up()))
        pacman_position = Position(2, 1)
        stdscr = curses.initscr()
        TestBoard.print_start(stdscr, board)
        board.place_entity(pacman_position, pacman)
        TestBoard.print_start(stdscr, board)
        board.move_entity(pacman)
        TestBoard.print_start(stdscr, board)
        self.assertIn(pacman, board.get_entities(Position(1, 1)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_down(self):
        board = Board(10, 10)
        pacman = Pacman(ChoseDirection(Direction.down()))
        pacman_position = Position(7,0)
        stdscr = curses.initscr()
        TestBoard.print_start(stdscr, board)
        board.place_entity(pacman_position, pacman)
        TestBoard.print_start(stdscr, board)
        board.move_entity(pacman)
        TestBoard.print_start(stdscr, board)
        self.assertIn(pacman, board.get_entities(Position(8,0)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_right(self):
        board = Board(10, 10)
        pacman = Pacman(ChoseDirection(Direction.right()))
        pacman_position = Position(5,0)
        stdscr = curses.initscr()
        TestBoard.print_start(stdscr, board)
        board.place_entity(pacman_position, pacman)
        TestBoard.print_start(stdscr, board)
        board.move_entity(pacman)
        TestBoard.print_start(stdscr, board)
        self.assertIn(pacman, board.get_entities(Position(5,1)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_move_pacman_right(self):
        board = Board(10, 10)
        pacman = Pacman(ChoseDirection(Direction.left()))
        pacman_position = Position(4,1)
        stdscr = curses.initscr()
        TestBoard.print_start(stdscr, board)
        board.place_entity(pacman_position, pacman)
        TestBoard.print_start(stdscr, board)
        board.move_entity(pacman)
        TestBoard.print_start(stdscr, board)
        self.assertIn(pacman, board.get_entities(Position(4,0)))
        self.assertNotIn(pacman, board.get_entities(pacman_position))

    def test_capture_eatable_entity(self):
        board = Board(10, 10)
        pacman = Pacman(ChoseDirection(Direction.left()))
        pacman_position = Position(4,1)
        stdscr = curses.initscr()
        TestBoard.print_start(stdscr, board)
        board.place_entity(pacman_position,pacman)
        pacdot=PacDot()
        pacdot_position = Position(4,0)
        board.place_entity(pacdot_position,pacdot)
        TestBoard.print_start(stdscr, board)
        board.move_entity(pacman)
        TestBoard.print_start(stdscr, board)
        self.assertIn(pacman, board.get_entities(Position(4,0)))
        self.assertNotIn(pacdot, board.get_entities(Position(4,0)))




       


if __name__ == '__main__':
    unittest.main()
