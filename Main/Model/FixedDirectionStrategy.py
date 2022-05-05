from .Direction import Direction


class  FixedDirectionStrategy():
    def __init__(self,direction):
        self.direction=direction
        
    def get_direction(self):
        return self.direction
