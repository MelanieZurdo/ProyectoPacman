from Main.Model.MovementStrategy import MovementStrategy
from Main.Model.Direction import Direction
import pygame


class HumanStrategy(MovementStrategy):
    def __init__(self):
        self.direction = Direction.right()

    def update(self, direction):
        self.direction = direction
        return self.direction

    def get_direction(self):
        return self.direction
