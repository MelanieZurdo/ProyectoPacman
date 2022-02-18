from abc import ABC


class EatableEntity(ABC):
    def __init__(self, score):
        self.score = score
