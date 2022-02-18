import unittest
from Main.Model_main import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_createboard(self):
        self.assertEqual()

    def test_getrows(self):
        self.assertEqual(3, self.test_board.get_rows())

    def test_getcolumns(self):
        self.assertEqual(2, self.test_board.get_columns())

    def insert_entity(self):
        board = Model_main.Board(2, 2)
        pacman = Pacman
        pacman_position = Position(1, 1)
        board.place_entity(pacman_position, pacman)
        self.assertEqual(pacman, board.get_entity(pacman_position))


if __name__ == '__main__':
    unittest.main()
