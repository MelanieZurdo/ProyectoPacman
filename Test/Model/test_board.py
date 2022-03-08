import unittest
from Main.Model.Board import Board
from Main.Model.Direction import Direction
from Main.Model.Direction_up import Direction_Up
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

    def test_move_pacman_UP(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(1,0)
        board.place_entity(pacman_position,pacman)      
        UP=Direction_Up()
        board.move_entity(pacman,UP)        
        self.assertEqual(pacman, board.get_entity(Position(0,0)))
    
    def test_pacman_really_move(self):
        board=Board(5,5)
        pacman=Pacman()
        pacman_position=Position(1,0)
        board.place_entity(pacman_position,pacman)      
        UP=Direction_Up()
        board.move_entity(pacman,UP)        
        self.assertEqual(None,board.get_entity(pacman_position))
    

        



if __name__ == '__main__':
    unittest.main()
