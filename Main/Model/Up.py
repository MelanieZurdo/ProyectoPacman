from .Direction import Direction

class Up(Direction):
    
    def validate_position(self,position,board):
        if position.get_row()==board.limit_case_up():
            return False    
        else:
            return True

    def new_position(self,position):
        return position.decreased_row()

        

            
    

        
         
    
            



 