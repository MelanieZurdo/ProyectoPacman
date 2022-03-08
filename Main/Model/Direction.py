from abc import ABC, abstractmethod
class Direction(ABC):

    @abstractmethod
    def validate_position(self):
        pass