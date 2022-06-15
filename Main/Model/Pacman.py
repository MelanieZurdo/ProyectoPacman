from .Printable import Printable
from .Visitable import Visitable
from .DynamicEntity import DynamicEntity


class Pacman(DynamicEntity):
    def __init__(self, movement_strategy):
        DynamicEntity.__init__(self, movement_strategy)
        self.pacman_score = 0
        self.life = 3
        self.alive=True
       
    def kill(self):
        self.alive=False

    def can_eat_eatable_entity(self):
        return True

    def eat(self, entity):
        self.pacman_score += entity.score

    def is_obstacle(self):
        return False

    def is_eatable_by(self, entity):
        return entity.can_eat_pacman()

    def visit(self, visitor):
        visitor.visitPacman(self)
    
    def get_movement_strategy(self):
        return self.movement_strategy

    def __str__(self):
        return " @ "
