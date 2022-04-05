from abc import ABC,abstractmethod


class EatableEntity(ABC):
    @abstractmethod
    def __init__(self, score):
        self.score = score
    def list_eatable_entity(self):
        list_eatable_entity=list()
        list_eatable_entity.append(self)
        return list_eatable_entity
