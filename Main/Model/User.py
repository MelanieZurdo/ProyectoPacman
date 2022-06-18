import pygame
from .Direction import Direction


class User:
    def apply_input(self, level_one):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    movement_strategy = level_one.pacman.movement_strategy
                    movement_strategy.update(Direction.up())

                if event.key == pygame.K_DOWN:
                    movement_strategy = level_one.pacman.movement_strategy
                    movement_strategy.update(Direction.down())

                if event.key == pygame.K_RIGHT:
                    movement_strategy = level_one.pacman.movement_strategy
                    movement_strategy.update(Direction.right())

                if event.key == pygame.K_LEFT:
                    movement_strategy = level_one.pacman.movement_strategy
                    movement_strategy.update(Direction.left())
