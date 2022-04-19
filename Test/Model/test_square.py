import unittest
from Main.Model.Board import Board
from Main.Model.Direction import Direction
from Main.Model.Ghost import Ghost
from Main.Model.Position import Position
from Main.Model.Pacman import Pacman
from Main.Model.Square import Square
from Main.Model.PacDot import PacDot


class TestBoard(unittest.TestCase):
    def test_put_pacman(self):
        board = Board(5, 5)
        pacman = Pacman()
        pacman_position = Position(1, 1)
        pacdot = PacDot()
        pacdot_position = Position(1, 2)
        board.put_entitie_in_board(pacdot_position, pacdot)
        board.put_entitie_in_board(pacman_position, pacman)
        board.move_entity(pacman, Direction.right())
        self.assertEqual(pacman, board.get_entity(pacdot_position))
        self.assertEqual(100, pacman.pacman_score)


if __name__ == '__main__':
    unittest.main()
