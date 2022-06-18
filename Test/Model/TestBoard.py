import unittest
import time
from Main.Model.Ghost import Ghost
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
        self.pacman_position = Position(4,4)
        self.pacdot = PacDot()
        self.pacdot_position = Position(4,3)        
        self.ghost_position = Position(3,4)


    def test_insert_entity(self):        
        pacman = Pacman(FixedDirectionStrategy(Direction.up()))
        ghost=Ghost(FixedDirectionStrategy(Direction.up()),"RED")        
        self.board.place_entity(self.pacman_position, pacman)
        self.board.place_entity(self.ghost_position,ghost)

        self.assertIn(pacman, self.board.get_entities(self.pacman_position))
        self.assertIn(ghost,self.board.get_entities(self.ghost_position))

    def test_move_pacman_up(self):
        pacman = Pacman(FixedDirectionStrategy(Direction.up()))        
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, self.board.get_entities(Position(3,4)))
        self.assertNotIn(pacman, self.board.get_entities(self.pacman_position))

    def test_move_pacman_down(self):    
        pacman = Pacman(FixedDirectionStrategy(Direction.down()))       
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, self.board.get_entities(Position(5,4)))
        self.assertNotIn(pacman, self.board.get_entities(self.pacman_position))

    def test_move_pacman_right(self):        
        pacman = Pacman(FixedDirectionStrategy(Direction.right()))
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, self.board.get_entities(Position(4,5)))
        self.assertNotIn(pacman, self.board.get_entities(self.pacman_position))

    def test_move_pacman_right(self):       
        pacman = Pacman(FixedDirectionStrategy(Direction.left()))       
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman,self.board.get_entities(Position(4,3)))
        self.assertNotIn(pacman, self.board.get_entities(self.pacman_position))

    def test_move_ghost_up(self):
        ghost=Ghost(FixedDirectionStrategy(Direction.up()),"RED") 
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.ghost_position, ghost)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(ghost)
        board_view.show()
        time.sleep(1)
        self.assertIn(ghost, self.board.get_entities(Position(2,4)))
        self.assertNotIn(ghost,self.board.get_entities(self.ghost_position))

    def test_ghost_eat_pacman(self):
        pacman = Pacman(FixedDirectionStrategy(Direction.up()))
        ghost=Ghost(FixedDirectionStrategy(Direction.down()),"RED") 
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)
        self.board.place_entity(self.ghost_position, ghost)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)    
       

        self.assertNotIn(pacman, self.board.get_entities(self.pacman_position))


    def test_capture_eatable_entity(self):        
        pacman = Pacman(FixedDirectionStrategy(Direction.left()))        
        board_view = BoardView(self.board)
        board_view.show()
        time.sleep(1)
        self.board.place_entity(self.pacman_position, pacman)          
        self.board.place_entity(self.pacdot_position, self.pacdot)
        board_view.show()
        time.sleep(1)
        self.board.move_entity(pacman)
        board_view.show()
        time.sleep(1)
        self.assertIn(pacman, self.board.get_entities(Position(4,3)))
        self.assertNotIn(self.pacdot, self.board.get_entities(Position(4,3)))


if __name__ == '__main__':
    unittest.main()
