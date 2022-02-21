from EatableEntity import EatableEntity

class PacDot(EatableEntity):
    def __init__(self):
        self.shape="*"
    def __str__(self):
        return "["+str(self.shape)+"]"
