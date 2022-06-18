import pygame
from Main.View.constants import *
from Main.Model.Visitor import Visitor
from Main.Model.Position import Position
from Main.View.PygameBoardView import PygameBoardView
from Main.View.PygamePacmanView import PygamePacmanView
from Main.View.PygameGhostView import PygameGhostView
from Main.View.PygamePacDotView import PygamePacDotView
from Main.View.PygamePowerPelletView import PygamePowerPelletView
from Main.View.PygameWallView import PygameWallView



class PygameViewFactory(Visitor):    
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.surface.fill(BLACK)

    def visitBoard(self,board):
        board.set_view(PygameBoardView(self.surface))
        for i in range(board.get_rows()):
            for j in range(board.get_columns()): 
                entities=board.get_entities(Position(i,j))
                for entity in entities:
                    entity.accept(self)   
   

    def visitPacman(self,pacman):
        pacman.set_view(PygamePacmanView(self.surface))
    
    def visitGhost(self,ghost):
        ghost.set_view(PygameGhostView(self.surface))
    
    def visitPacDot(self,pacdot):
        pacdot.set_view(PygamePacDotView(self.surface))
    
    def visitPowerPellet(self,powerpellet):
        powerpellet.set_view(PygamePowerPelletView(self.surface))
    
    def visitWall(self,wall):
        wall.set_view(PygameWallView(self.surface))

