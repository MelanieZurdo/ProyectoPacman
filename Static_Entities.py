from abc import ABC, abstractmethod

class Static_Entitie(ABC):
    def __init__(self,status,position_r,position_c,score):    
        self.status=status 
        self.position_r=position_r
        self.position_c=position_c 
        self.score=score    
    
    def get_status(self):
        return self.status
    
    def get_position(self):
        return [self.position_r][self.position_c]

    def get_score(self):
        return self.score
    
    