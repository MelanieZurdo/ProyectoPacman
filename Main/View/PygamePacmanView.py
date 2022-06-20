import pygame
from Main.Model.Afraid import Afraid
from Main.View.constants import*
from .PygameView import PygameView


class PygamePacmanView(PygameView):

    def draw(self, center_x, center_y):
        if self.get_printable().is_afraid():
            pygame.draw.circle(self.surface, GOLD, (center_x, center_y), 10)
        else:
            pygame.draw.circle(self.surface, GREEN, (center_x, center_y), 10)
