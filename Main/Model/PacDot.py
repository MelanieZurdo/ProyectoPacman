from .EatableEntity import EatableEntity


class PacDot(EatableEntity):
    def __init__(self):
        self.score=100
        
    def __str__(self):
        return "[·]"
