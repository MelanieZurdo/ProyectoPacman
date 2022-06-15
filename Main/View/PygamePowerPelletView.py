from .PygameView import PygameView
from Main.View.constants import *
import pygame     


class PygamePowerPelletView(PygameView):
    def draw(self,center_x,center_y):
        pygame.draw.circle(self.surface,WHITE,(center_x,center_y),7)