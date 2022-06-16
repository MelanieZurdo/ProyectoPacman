from .Printable import Printable
from .Host import Host
from .DynamicEntity import DynamicEntity


class Pacman(DynamicEntity):
    def __init__(self, movement_strategy):
        DynamicEntity.__init__(self, movement_strategy)
        self.alive = True

    def die(self):
        self.alive = False

    def can_eat_eatable_entity(self):
        return True

    def is_obstacle(self):
        return False

    def is_eatable_by(self, entity):
        return entity.can_eat_pacman()

    def accept(self, visitor):
        visitor.visitPacman(self)

    def __str__(self):
        return " @ "
