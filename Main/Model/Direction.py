from abc import ABC, abstractmethod
class Direction(ABC):

    @abstractmethod
    def validate_position(self):
        pass
    @abstractmethod
    def new_position(self):
        pass