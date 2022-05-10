from shutil import move
from .DynamicEntity import DynamicEntity


class Pacman(DynamicEntity):
    def __init__(self,movement_strategy):
        DynamicEntity.__init__(self,movement_strategy)
        self.pacman_score=0

    def can_eat_eatable_entity(self):
        return True

    def eat(self, entity):
        self.pacman_score += entity.score

    def is_obstacle(self):
        return False

    def __str__(self):
        return " @ "
