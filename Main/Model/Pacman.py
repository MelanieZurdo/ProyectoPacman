from pickle import TRUE
from .Unafraid import Unafraid
from .Afraid import Afraid
from .Printable import Printable
from .Host import Host
from .DynamicEntity import DynamicEntity


class Pacman(DynamicEntity):
    def __init__(self, movement_strategy):
        DynamicEntity.__init__(self, movement_strategy, Afraid())
       
    
    def can_eat_ghost(self):
        return True

   

    def can_eat_static_entity(self):
        return True
  

    def accept(self, visitor):
        visitor.visitPacman(self)

    def __str__(self):
        return " @ "
