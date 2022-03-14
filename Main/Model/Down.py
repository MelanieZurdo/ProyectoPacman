from .Direction import Direction

class Down(Direction):
    
    def new_position(self,position):
        return position.increased_row()
        