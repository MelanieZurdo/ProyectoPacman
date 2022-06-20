from Main.View.constants import *
from .PygameView import PygameView
import pygame


class PygameGhostView(PygameView):
      def draw(self,center_x,center_y):   
        if self.get_printable().is_afraid():
              pygame.draw.circle(self.surface,DARKGREY,(center_x,center_y),10)
        else:
              pygame.draw.circle(self.surface,BLUE,(center_x,center_y),10)

        
         
         