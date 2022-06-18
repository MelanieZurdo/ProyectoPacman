from Main.Model.StaticEntity import StaticEntity
from .EatableEntity import EatableEntity


class PowerPellet(EatableEntity):
    def __init__(self):
        self.score = 200

    def is_obstacle(self):
        return False

    def can_eat_eatable_entity(self):
        return False

    def accept(self, visitor):
        visitor.visitPowerPellet(self)

    def __str__(self):
        return " # "
