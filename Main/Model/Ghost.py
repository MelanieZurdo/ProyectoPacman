from .DynamicEntity import DynamicEntity


class Ghost(DynamicEntity):
    def __init__(self,movement_strategy,color):
        DynamicEntity.__init__(self,movement_strategy)
        self.color = color

    def eat(self,entity):
        entity.kill()      

    def get_direction(self):
        return self.get_strategy()

    def get_strategy(self):
        return self.movement_strategy.get_direction()

    def can_eat_eatable_entity(self):
        return False
    
    def can_eat_pacman(self):
        return True

    def is_obstacle(self):
        return False
    
    def visit(self,visitor):
        visitor.visitGhost(self)

    def __str__(self):
        return "&"
