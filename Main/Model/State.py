from abc import ABC, abstractmethod
class State(ABC):
    
    def is_afraid(self):
        pass

    def can_eat_entity(self):
        pass