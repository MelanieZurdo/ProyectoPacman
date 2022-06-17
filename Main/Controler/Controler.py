import sys
import time
import pygame
from Main.Model.Direction import Direction
from Main.Model.HumanStrategy import HumanStrategy
from Main.Model.LevelFactory import LevelFactory
from Main.View.PygameViewFactory import PygameViewFactory
from Main.Model.User import User


class Controler:

    def main(self):
        level_factory = LevelFactory(PygameViewFactory())
        level_one = level_factory.get_level_one()
        level_one.board.get_view().draw()
        time.sleep(2)
        while level_one.pacman.alive:
            time.sleep(0.5)
            user = User()
            user.apply_input(level_one)
            level_one.move()
            level_one.board.get_view().draw()


if __name__ == '__main__':
    controler = Controler()
    controler.main()
