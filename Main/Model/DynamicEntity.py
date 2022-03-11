from abc import ABC,abstractmethod

class DynamicEntity(ABC):
    @abstractmethod
    def move(self):
        pass
