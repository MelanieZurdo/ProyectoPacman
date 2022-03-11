from abc import ABC,abstractmethod


class EatableEntity(ABC):
    @abstractmethod
    def __init__(self, score):
        self.score = score
