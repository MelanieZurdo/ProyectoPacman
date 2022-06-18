from Main.Model.ComputerStrategy import ComputerStrategy
from Main.Model.Direction import Direction
import random


class RandomStrategy(ComputerStrategy):  
    def __init__(self): 
        self.directions=[Direction.up(),Direction.down(),Direction.left(),Direction.right()]

    def get_direction(self):        
        return random.choice(self.directions)