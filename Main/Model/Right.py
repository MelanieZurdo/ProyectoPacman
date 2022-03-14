from .Direction import Direction

class Right(Direction):
    
    def new_position(self,position):
        return position.increased_column()