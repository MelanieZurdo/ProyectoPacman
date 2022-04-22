from abc import ABC,abstractmethod


class StaticEntity(ABC):
    @abstractmethod
    def is_obstacle(self):
        pass
