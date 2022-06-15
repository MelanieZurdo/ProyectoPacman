from .PygameView import PygameView
from Main.View.constants import *
import pygame 

class PygameWallView(PygameView):
     def draw(self,center_x,center_y):
        pygame.draw.circle(self.surface,UGLY_PINK,(center_x,center_y),5)