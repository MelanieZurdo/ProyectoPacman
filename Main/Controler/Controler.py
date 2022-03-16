import sys
import pygame
from pygame.locals import *

def main():
    pygame.init()
    # La clase o función principal que crea o ejecuta el juego
    # Contiene principalmente loop del juego (el alma de este)
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("tutorial pygame parte 2")
    

    while True:
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass
                elif event.key == K_ESCAPE:
                    sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == K_UP:
                    pass
                elif event.key == K_DOWN:
                    pass


if __name__ == "__main__":
    main()
 
 

        