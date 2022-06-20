from .DynamicEntity import DynamicEntity
from .Afraid import Afraid
from .Unafraid import Unafraid


class Ghost(DynamicEntity):
    def __init__(self, movement_strategy):
        DynamicEntity.__init__(self, movement_strategy, Unafraid())

    def can_eat_static_entity(self):
        return False
    
    def can_eat_ghost(self):
        return False
        

    
    def is_eatable_by(self, entity):
        return super().is_eatable_by(entity) and entity.can_eat_ghost()

    def accept(self, visitor):
        visitor.visitGhost(self)
    


    def __str__(self):
        return "&"
