from Main.Model.StaticEntity import StaticEntity

from ..Controler.Game import Game


class PowerPellet(StaticEntity):
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
    
    #New change
    def die(self):
        Game().power_pellet_eaten()
