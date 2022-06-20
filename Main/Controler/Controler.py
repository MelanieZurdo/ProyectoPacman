import sys
import time
import pygame
from Main.Model.Direction import Direction
from Main.Model.HumanStrategy import HumanStrategy
from Main.Model.LevelFactory import LevelFactory
from Main.View.PygameViewFactory import PygameViewFactory
from Main.Model.User import User
from Main.Controler.Game import Game


class Controler:

    

    def main(self):
        level_factory = LevelFactory(PygameViewFactory())
        level_one = level_factory.get_level_one()
        user = User()
        game = Game(level_one)

        while level_one.pacman.is_alive():                        
            self.show_and_wait(level_one)
            user.apply_input(level_one)
            game.clock_tick()
        self.show_and_wait(level_one)

    def show_and_wait(self, level_one):
        level_one.board.get_view().draw()
        time.sleep(0.5)


if __name__ == '__main__':
    controler = Controler()
    controler.main()
