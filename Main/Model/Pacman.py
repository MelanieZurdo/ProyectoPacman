from .DynamicEntity import DynamicEntity


class Pacman(DynamicEntity):
    def __init__(self, movement_strategy):
        self.pacman_score = 0
        self.movement_strategy = movement_strategy

    def can_eat_eatable_entity(self):
        return True

    def get_strategy(self):
        return self.movement_strategy

    def eat(self, entity):
        self.pacman_score += entity.score

    def is_obstacle(self):
        return False

    def __str__(self):
        return " @ "
