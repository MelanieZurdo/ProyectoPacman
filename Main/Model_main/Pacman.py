class Pacman():
    def __init__(self):
        self.shape="@"
    
    def move(self,position):
        self.position=position
        return self.position
        
    def __str__(self):
     return  "["+str(self.shape)+"]"
