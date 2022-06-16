from .DynamicEntity import DynamicEntity


class Ghost(DynamicEntity):
    def __init__(self, movement_strategy, color):
        DynamicEntity.__init__(self, movement_strategy)
        self.color = color    

    def can_eat_eatable_entity(self):
        return False

    def can_eat_pacman(self):
        return True

    def is_obstacle(self):
        return False

    def accept(self, visitor):
        visitor.visitGhost(self)

    def __str__(self):
        return "&"
