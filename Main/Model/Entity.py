from abc import ABC, abstractmethod
from Main.Model.Visitable import Visitable
from .Printable import Printable


class Entity(ABC,Printable,Visitable):

    
    def is_eatable_by(self,entity):
        return False

    
    def eat(self,entity):
        pass

   
    def can_eat_eatable_entity(self):
        return False
    
    def can_eat_pacman(self):
        return False
    
   
    def is_dynamic(self):
        return False
    
