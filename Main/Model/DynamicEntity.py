from abc import ABC, abstractmethod
from .Entity import Entity
from .Afraid import Afraid
from .Unafraid import Unafraid


class DynamicEntity(Entity, ABC):
    def __init__(self, movement_strategy, state):
        self.movement_strategy = movement_strategy
        self.state = state
        self.alive = True
    
    def die(self):
        self.alive = False

    def is_obstacle(self):
        False

    def get_direction(self):
        return self.movement_strategy.get_direction()

    def is_dynamic(self):
        return True

    def eat(self, entity):
        entity.die()

    def calm(self):
        self.state = Unafraid()

    def scare(self):
        self.state = Afraid()

    def is_afraid(self):
        return self.state.is_afraid()

    def can_eat_static_entity(self):
        pass

    def is_eatable_by(self, entity):
        return self.state.is_afraid() and entity.is_dynamic()
    
    def is_alive(self):
        return self.alive
