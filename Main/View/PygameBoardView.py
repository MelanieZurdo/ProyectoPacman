import pygame
from Main.View.EntitiesComparator import EntitiesComparator
from Main.Model.Position import Position
from .PygameView import PygameView
from Main.View.constants import *
from functools import cmp_to_key



class PygameBoardView(PygameView):
    def __init__(self, surface):
        PygameView.__init__(self, surface)
        self.block_height = None
        self.block_width = None

    def inicialize_parameters(self):
        if not self.block_height:
            self.block_height = round(SCREEN_HEIGHT/self.get_printable().get_rows())
            self.block_width = round(SCREEN_WIDTH/self.get_printable().get_columns())

    def draw(self):
        self.inicialize_parameters()
        

        for i in range(self.get_printable().get_rows()):
            for j in range(self.get_printable().get_columns()):
                entities = list(self.get_printable().get_entities(Position(i, j)))                
                entities.sort(key=cmp_to_key(EntitiesComparator.compare))
                

                center_x = (i*self.block_width)+(self.block_width/2)
                center_y = (j*self.block_height)+(self.block_height/2)
                self.draw_grid()
                myrect = pygame.Rect(
                    j*self.block_width, i*self.block_height, self.block_width, self.block_height)
                pygame.draw.rect(self.surface, BLACK, myrect)
                for entity in entities:
                    entity.get_view().draw(center_y, center_x)
        pygame.display.update()

    def draw_grid(self):
        for i in range(self.get_printable().get_rows()):
            new_height = round((i * self.block_height))
            new_width = round((i * self.block_width))
            pygame.draw.line(self.surface, WHITE, (0, new_height),(SCREEN_WIDTH, new_height), 2)
            pygame.draw.line(self.surface, WHITE, (new_width, 0),(new_width, SCREEN_HEIGHT), 2)
