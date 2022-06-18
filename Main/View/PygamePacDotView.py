from .PygameView import PygameView
from Main.View.constants import *
import pygame


class PygamePacDotView(PygameView):
     def draw(self,center_x,center_y):
        pygame.draw.circle(self.surface,RED,(center_x,center_y),5)