""" def game_loop(surface,board):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        draw_board(surface,board)
        draw_grid(surface)
        


def initialize_game():
    pygame.init()
   
    return surface


def main():
    surface = initialize_game()
    game_loop(surface, BOARD)


if __name__ == "__main__":
    main()




     myrect = pygame.Rect(i*self.block_width, j*self.block_height,self.block_width,self.block_height)
    center_x = (i*self.block_width)+(self.block_width/2)
    center_y = (j*self.block_height)+(self.block_height/2)
    entities = self.printable.get_entities(position)
    if len(entities) == 0:
        pygame.draw.rect(self.surface, constants.BLACK, myrect)
    for entity in entities:
        entity.get_view() 

    board_view=BoardView(level_one.board)
        board_view.show()


 
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit() 

if self.printable.color=="Inky":
            ghost=pygame.image.load('C:/Users/Melanie/Desktop/ProyectoPacman/Main/Controler/img/redghost.png')
         if self.printable.color=="Blinky":
            ghost=pygame.image.load('C:/Users/Melanie/Desktop/ProyectoPacman/Main/Controler/img/orangeghost.png')
         if self.printable.color=="Pinky":
            ghost=pygame.image.load('C:/Users/Melanie/Desktop/ProyectoPacman/Main/Controler/img/pinkghost.png')
         if self.printable.color=="Clyde":
            ghost=pygame.image.load('C:/Users/Melanie/Desktop/ProyectoPacman/Main/Controler/img/blueghost.png')

                  
         ghost = pygame.transform.scale(ghost,[block_width,block_height])            
         self.surface.blit(ghost, [center_x-(block_width/2),center_y-(block_height/2)])  """

class MiClas():
    x=5


p1=MiClas()

print(Miclas().x)