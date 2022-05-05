import unittest
from Main.Model.Board import Board
from Main.Model.Direction import Direction
from Main.Model.FixedDirectionStrategy import FixedDirectionStrategy
from Main.Model.Ghost import Ghost
from Main.Model.Position import Position
from Main.Model.Pacman import Pacman
from Main.Model.PowerPellet import PowerPellet
from Main.Model.Square import Square
from Main.Model.PacDot import PacDot
from Main.Model.Wall import Wall


class TestBoard(unittest.TestCase):
    def test_put_pacman(self):
        board = Board(5, 5)
        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        pacman_position = Position(1, 1)
        pacdot = PacDot()
        pacdot_position = Position(1, 2)
        board.place_entity(pacdot_position, pacdot)
        board.place_entity(pacman_position, pacman)
        board.move_entity(pacman)
        self.assertIn(pacman, board.get_entities(pacdot_position))

    def test_wall_is_obstacle(self):
        board = Board(5, 5)
        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        pacman_position = Position(1, 1)
        wall = Wall()
        wall_position = Position(1, 2)
        board.place_entity(wall_position, wall)
        board.place_entity(pacman_position, pacman)
        board.move_entity(pacman)
        self.assertIn(pacman, board.get_entities(pacman_position))

    def test_two_entities_in_square(self):
        board = Board(5, 5)
        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        pacman_position = Position(1, 1)

        pacdot = PacDot()
        pacdot_position = Position(1, 2)

        power_pellet = PowerPellet()
        power_pellet_position = Position(1, 2)

        board.place_entity(pacdot_position, pacdot)
        board.place_entity(power_pellet_position, power_pellet)
        board.place_entity(pacman_position, pacman)

        board.move_entity(pacman)
        self.assertIn(pacman, board.get_entities(pacdot_position))
        self.assertNotIn(pacdot, board.get_entities(pacdot_position))


if __name__ == '__main__':
    unittest.main()
