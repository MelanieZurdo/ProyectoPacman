from abc import ABC
from Main.Model.Entity import Entity


class EatableEntity(Entity,ABC):    

    def is_eatable_by(self,entity):
        return entity.can_eat_eatable_entity()
