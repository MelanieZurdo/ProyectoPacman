import unittest
import time
import curses
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
        pacman = Pacman()
        pacman_position = Position(0, 0)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))



    def test_move_pacman_up(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(2,1)
        stdscr = curses.initscr()
        board.fill_board()
        print_start(stdscr,board)  
        board.place_entity(pacman_position,pacman)
        print_start(stdscr,board) 
        board.move_entity(pacman,Direction.up()) 
        print_start(stdscr,board) 
        self.assertEqual(pacman, board.get_entity(Position(1,1)))
        self.assertEqual(None,board.get_entity(pacman_position))
    
    def test_move_pacman_down(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(2,0)
        board.place_entity(pacman_position,pacman)         
        board.move_entity(pacman,Direction.down())        
        self.assertEqual(pacman, board.get_entity(Position(3,0)))
        self.assertEqual(None,board.get_entity(pacman_position))

    def test_move_pacman_rigt(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(0,2)
        board.place_entity(pacman_position,pacman)            
        board.move_entity(pacman,Direction.right())        
        self.assertEqual(pacman, board.get_entity(Position(0,3)))
        self.assertEqual(None,board.get_entity(pacman_position))

    def test_move_pacman_left(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(0,2)
        board.place_entity(pacman_position,pacman)    
        board.move_entity(pacman,Direction.left())        
        self.assertEqual(pacman, board.get_entity(Position(0,1)))
        self.assertEqual(None,board.get_entity(pacman_position))
    
    

    def test_capture_eatable_entity(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(0,1)
        board.place_entity(pacman_position,pacman) 
        board.fill_board()
        board.move_entity(pacman,Direction.up())

        

        
    
if __name__ == '__main__':
    unittest.main()
