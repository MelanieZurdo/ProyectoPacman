from .DynamicEntity import DynamicEntity


class Ghost(DynamicEntity):
    def __init__(self, color,direction):
        self.color = color
        self.direction=direction

    def can_eat_eatable_entity(self):
        return False

    def is_obstacle(self):
        return False

    def __str__(self):
        return "&"
