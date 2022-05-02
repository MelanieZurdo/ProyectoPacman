from abc import ABC, abstractmethod

class MovementStrategy(ABC):
    @abstractmethod
    def get_direction(self):
        pass


