from abc import ABC, abstractmethod
from Main.Model.Entity import Entity


class EatableEntity(Entity,ABC):  
    @abstractmethod
    def is_obstacle(self):
        pass  

    def is_eatable_by(self,entity):
        return entity.can_eat_eatable_entity()
    
    

