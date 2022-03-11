from .Direction import Direction

class Right(Direction):
    
    def validate_position(self,position,board):
        if position.get_column()==board.limit_case_right():
            return False  
        else:
            return True
            
    def new_position(self,position):
        return position.increased_column()