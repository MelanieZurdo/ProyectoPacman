from Move_Entities import Move_Entitie
from Board import Board

class Ghost(Move_Entitie):    
    def __init__(self,status,position_r,position_c,color_ghost):                       
        super().__init__(status,position_r,position_c)
        self.color_ghost=color_ghost

    def get_color_ghost(self):
        return self.color_ghost
    
    def move_entitie():
        pass