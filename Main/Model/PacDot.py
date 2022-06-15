from Main.Model.StaticEntity import StaticEntity
from .EatableEntity import EatableEntity


class PacDot(EatableEntity):
    def __init__(self):
        self.score=100

    def is_obstacle(self):
        return False 

    def can_eat_eatable_entity(self):
        return False
    
    def visit(self,visitor):
        visitor.visitPacDot(self)
        
    def __str__(self):
        return " · "
