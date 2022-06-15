import pygame
from Main.View.constants import*
from .PygameView import PygameView


class PygamePacmanView(PygameView):     

    def draw(self,center_x,center_y):
        pygame.draw.circle(self.surface,GOLD,(center_x,center_y),10)  

    """ def draw(self,center_x,center_y,block_width,block_height):    
        pacman_picture= pygame.image.load('C:/Users/Melanie/Desktop/ProyectoPacman/Main/Controler/img/pacman.png')
        pacman_picture = pygame.transform.scale(pacman_picture,[block_width,block_height])
        pacman_picture.set_colorkey(WHITE)
        self.surface.blit(pacman_picture, [center_x-(block_width/2),center_y-(block_height/2)])"""
        
       

   

    
