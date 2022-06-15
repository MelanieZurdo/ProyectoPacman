from abc import ABC


class Visitor(ABC):
    def visitBoard(self,board):
       pass    
   
    def visitPacman(self,pacman):
        pass
    
    def visitGhost(self,ghost):
        pass
    
    def visitPacDot(self,pacdot):
        pass
    
    def visitPowerPellet(self,powerpellet):
        pass
    
    def visitWall(self,wall):
        pass