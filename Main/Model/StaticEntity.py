from abc import ABC, abstractmethod

from Main.Model.Entity import Entity


class StaticEntity(Entity, ABC):
    @abstractmethod
    def is_obstacle(self):
        pass

    def can_eat_ghost(self):
        return False

    def is_eatable_by(self, entity):
        return entity.can_eat_static_entity() and not self.is_obstacle()
