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

    def setUp(self):
        self.board = Board(10,10)
        self.pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        self.pacman_position = Position(4, 4)
        self.pacdot = PacDot()
        self.pacdot_position = Position(4,5)
        self.wall = Wall()
        self.wall_position = Position(4,5)
        self.power_pellet = PowerPellet()
        self.power_pellet_position = Position(1,2)

    def test_put_pacman(self):
        
        self.board.place_entity(self.pacdot_position, self.pacdot)
        self.board.place_entity(self.pacman_position, self.pacman)
        self.board.move_entity(self.pacman)
        self.assertIn(self.pacman, self.board.get_entities(self.pacdot_position))

    def test_wall_is_obstacle(self):
                
        self.board.place_entity(self.wall_position, self.wall)
        self.board.place_entity(self.pacman_position, self.pacman)
        self.board.move_entity(self.pacman)
        self.assertIn(self.pacman, self.board.get_entities(self.pacman_position))

    def test_two_entities_in_square(self):

        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        self.board.place_entity(self.pacdot_position, self.pacdot)
        self.board.place_entity(self.power_pellet_position, self.power_pellet)
        self.board.place_entity(self.pacman_position, pacman)

        self.board.move_entity(pacman)
        self.assertIn(pacman,self.board.get_entities(self.pacdot_position))
        self.assertNotIn(self.pacdot, self.board.get_entities(self.pacdot_position))


if __name__ == '__main__':
    unittest.main()
