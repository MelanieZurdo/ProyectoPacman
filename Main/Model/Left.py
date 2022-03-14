from .Direction import Direction

class Left(Direction):   
    
    def new_position(self,position):
        return position.decreased_column()