from Main.View.constants import *
from .PygameView import PygameView
import pygame


class PygameGhostView(PygameView):
      def draw(self,center_x,center_y):
        pygame.draw.circle(self.surface,BLUE,(center_x,center_y),10)

        
         
         