from .Direction import Direction

class Left(Direction):
    
    def validate_position(self,position,board):
        if position.get_column()==board.limit_case_left():
            return False    
        else:
            return True

    def new_position(self,position):
        return position.decreased_column()