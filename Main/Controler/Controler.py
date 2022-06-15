import sys
import time
import pygame
from Main.Model.Direction import Direction
from Main.Model.HumanStrategy import HumanStrategy
from Main.Model.LevelFactory import LevelFactory
from Main.View.PygameViewFactory import PygameViewFactory



class Controler:    

    def main(self):               
        level_factory=LevelFactory(PygameViewFactory())
        level_one=level_factory.get_level_one()
        

        while level_one.pacman.alive:
            time.sleep(1)
            self.user_input(level_one)
            level_one.board.move_entity(level_one.pacman)

            for ghost in level_one.ghosts:
                level_one.board.move_entity(ghost)            
             
            
            level_one.board.get_view().draw()
            # print(level_one.board) 
            
      
        

    def user_input(self,level_one):
         for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN:   
                if event.key==pygame.K_UP: 
                    movement_strategy=level_one.pacman.get_movement_strategy()
                    movement_strategy.update(Direction.up())
           
                if event.key==pygame.K_DOWN: 
                    movement_strategy=level_one.pacman.get_movement_strategy()
                    movement_strategy.update(Direction.down())
           
                if event.key==pygame.K_RIGHT: 
                    movement_strategy=level_one.pacman.get_movement_strategy()
                    movement_strategy.update(Direction.right())

                if event.key==pygame.K_LEFT:
                    movement_strategy=level_one.pacman.get_movement_strategy()
                    movement_strategy.update(Direction.left())         
                                
    
            

       


if __name__ == '__main__':
    controler=Controler()
    controler.main()