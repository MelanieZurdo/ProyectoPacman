from abc import ABC, abstractmethod


class Entity(ABC):
    
    def is_eatable_by(self,entity):
        pass

    
    def eat(self,entity):
        pass

   
    def can_eat_eatable_entity():
        return False
