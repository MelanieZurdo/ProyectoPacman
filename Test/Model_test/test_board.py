import unittest
import sys

sys.path.insert(0,'/path/to/Main')

from Main.Model_main.Board import Board
from Main.Model_main.Position import Position
from Main.Model_main.Pacman import Pacman
from Main.Model_main.PacDot import PacDot




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
        board = Board(2,2)
        pacman = Pacman()
        pacman_position = Position(1, 1)       
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman,board.get_entity(pacman_position))
    
    def test_set_board(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(1,1)        
        for i in range(board.get_rows()):            
            for j in range(board.get_columns()):
                if board[i][j]==[1][1]:
                    continue
                board[i].append(PacDot())




if __name__ == '__main__':
    unittest.main()

