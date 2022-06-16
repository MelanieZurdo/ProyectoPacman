from .Direction import Direction
from .MovementStrategy import MovementStrategy


class  FixedDirectionStrategy(MovementStrategy):
    def __init__(self,direction):
        self.direction=direction
        
    def get_direction(self):
        return self.direction
