from EatableEntity import EatableEntity


class PacDot(EatableEntity):
    def __init__(self):
        self.score = 100
        self.shape="*"
    
    def __str__(self):
        return "["+str(self.shape)+"]"
    
     
            
            



