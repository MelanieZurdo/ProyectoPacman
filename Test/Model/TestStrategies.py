import unittest
from Main.Model.Direction import Direction
from Main.Model.RandomStrategy import RandomStrategy


class TestBoard(unittest.TestCase):
    def test_random_strategy(self):
        strategy_set=set()
        for i in range(500):
         strategy = RandomStrategy()
         strategy_set.add(strategy.get_direction())  
        self.assertIn(Direction.up(),strategy_set)
        self.assertIn(Direction.down(),strategy_set)
        self.assertIn(Direction.right(),strategy_set)
        self.assertIn(Direction.left(),strategy_set)
        


if __name__ == '__main__':
    unittest.main()
