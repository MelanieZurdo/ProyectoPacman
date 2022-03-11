from .Direction import Direction

class Down(Direction):
    
    def validate_position(self,position,board):
        if position.get_row()==board.limit_case_down():
            return False  
        else:
            return True
            
    def new_position(self,position):
        return position.increased_row()