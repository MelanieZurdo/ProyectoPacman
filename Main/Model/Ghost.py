from .DynamicEntity import DynamicEntity


class Ghost(DynamicEntity):
    def __init__(self, color,movement_strategy ):
        self.color = color
        self.movement_strategy=movement_strategy 

    def get_strategy(self):
        return self.movement_strategy        

    def can_eat_eatable_entity(self):
        return False

    def is_obstacle(self):
        return False

    def __str__(self):
        return "&"
