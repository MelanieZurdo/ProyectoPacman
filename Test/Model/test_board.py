import unittest
from Main.Model.Board import Board
from Main.Model.Direction import Direction
from Main.Model.Position import Position
from Main.Model.Pacman import Pacman
from Main.Model.Square import Square
from Main.Model.Up import Up
from Main.Model.Down import Down
from Main.Model.Right import Right
from Main.Model.Left import Left



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

    def test_move_pacman_up(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(1,0)
        board.place_entity(pacman_position,pacman)      
        up=Up()
        board.move_entity(pacman,up)        
        self.assertEqual(pacman, board.get_entity(Position(0,0)))
        self.assertEqual(None,board.get_entity(pacman_position))
    
    def test_move_pacman_down(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(3,0)
        board.place_entity(pacman_position,pacman)      
        down=Down()
        board.move_entity(pacman,down)        
        self.assertEqual(pacman, board.get_entity(Position(4,0)))
        self.assertEqual(None,board.get_entity(pacman_position))

    def test_move_pacman_rigt(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(0,3)
        board.place_entity(pacman_position,pacman)      
        right=Right()
        board.move_entity(pacman,right)        
        self.assertEqual(pacman, board.get_entity(Position(0,4)))
        self.assertEqual(None,board.get_entity(pacman_position))

    def test_move_pacman_left(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(0,1)
        board.place_entity(pacman_position,pacman)      
        left=Left()
        board.move_entity(pacman,left)        
        self.assertEqual(pacman, board.get_entity(Position(0,0)))
        self.assertEqual(None,board.get_entity(pacman_position))

    
    
          
        
    

        



if __name__ == '__main__':
    unittest.main()
