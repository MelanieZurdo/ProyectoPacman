from abc import ABC, abstractmethod

class Move_Entitie(ABC):
    def __init__(self,status,position_r,position_c):    
        self.status=status 
        self.position_r=position_r
        self.position_c=position_c      
    
    def get_status(self):
        return self.status
    
    def get_position(self):
        return [self.position_r][self.position_c]
    
    @abstractmethod
    def move_entitie():
        pass









