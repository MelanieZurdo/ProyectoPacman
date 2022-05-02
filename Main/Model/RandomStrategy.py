from Main.Model.ComputerStrategy import ComputerStrategy
from Main.Model.Direction import Direction
import random


class RandomStartegy(ComputerStrategy):
    def get_direction(self):
        directions=[Direction.up(),Direction.down(),Direction.left(),Direction.right()]
        return random.choice(directions)