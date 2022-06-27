import time
import pygame
from Main.Model.LevelFactory import LevelFactory
from Main.View.PygameViewFactory import PygameViewFactory
from Main.Model.User import User
from Main.Controler.Game import Game
from Main.View.constants import *
from Menu import Menu



class Controler:     

    def main(self,controler):
        menu=Menu(controler)
        menu.create_menu()
        
    
    def play(self):
        level_factory = LevelFactory(PygameViewFactory())
        level_one = level_factory.get_level_one()
        user = User()
        game = Game(level_one)
        sound = pygame.mixer.Sound("pacman_chomp.wav")

        while level_one.pacman.is_alive():
            sound.play()
            self.show_and_wait(level_one)
            user.apply_input(level_one)
            game.clock_tick()
        self.show_and_wait(level_one)

    def show_and_wait(self, level_one):
            level_one.board.get_view().draw()
            time.sleep(0.5)


if __name__ == '__main__':
    controler = Controler()
    controler.main(controler)

    
