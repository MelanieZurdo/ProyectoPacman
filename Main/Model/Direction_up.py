from .Direction import Direction

class Direction_Up(Direction):
    
    def validate_position(self,position):
        if position.get_row()==0:
            return position
        else:
             return position.decrease_row()
         
    
            



 