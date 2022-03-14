from abc import ABC, abstractmethod
class Direction(ABC):

    @abstractmethod
    def new_position(self):
        pass
    