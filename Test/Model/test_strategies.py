import unittest
from Main.Model.Direction import Direction
from Main.Model.RandomStrategy import RandomStartegy


class TestBoard(unittest.TestCase):
    def test_random_strategy(self):
        strategy = RandomStartegy()
        self.assertIn(strategy.get_direction(),[Direction.up(),Direction.down(),Direction.left(),Direction.right()])
        


if __name__ == '__main__':
    unittest.main()
