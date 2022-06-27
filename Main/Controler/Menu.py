import pygame 
from Main.View.constants import *
from Main.View.PygameViewFactory import PygameViewFactory

class Menu(PygameViewFactory): 
    def __init__(self,controler):
        super().__init__()
        self.controler=controler
      

    def create_menu(self):
              
        pygame.display.set_caption("Menu")
        text_color=WHITE
        button_color=RED
        buttton_over_color=DARKORANGE
        button_width=100
        button_height=50
        x=self.surface.get_width()/2-button_width/2
        y=self.surface.get_height()/2-button_height/2
        button_rect=[x,y,button_width,button_height]
        button_font=pygame.font.SysFont('Arial',20)
        button_text=button_font.render("PLAY",True,text_color)
        self.surface.fill((BLACK))
        menu=True
        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    menu=False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if(button_rect[0]<=x<=button_rect[0]+button_rect[2] and button_rect[1]<=y<=button_rect[1]+button_rect[3]):
                        menu=False
                        self.controler.play()
            
            pygame.draw.rect(self.surface,button_color,button_rect)
            self.surface.blit(button_text,(button_rect[0]+(button_width-button_text.get_width())/2,button_rect[1]+(button_height-button_text.get_height())/2))
            pygame.display.update()