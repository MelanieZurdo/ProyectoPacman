import random

from Main.Model.RandomStrategy import RandomStartegy
from .Ghost import Ghost
from .PacDot import PacDot
from .Wall import Wall
from .Board import Board
from .Level import Level
from .Pacman import Pacman
from .Position import Position
from .PowerPellet import PowerPellet


class LevelFactory:
    def __init__(self):
        self.level_one = None

    def get_level_one(self):
        if self.level_one:
            return self.level_one

        board = Board(10, 10)
        movement_strategy_pacman=RandomStartegy()
        pacman = Pacman(movement_strategy_pacman.get_direction())
        movement_strategy_ghost=RandomStartegy()
        ghosts = [Ghost("Blinky",movement_strategy_ghost.get_direction()), Ghost("Pinky",movement_strategy_ghost.get_direction()),Ghost("Inky",movement_strategy_ghost.get_direction()), Ghost("Clyde",movement_strategy_ghost.get_direction())]
        self.add_walls(board)
        self.add_pacman(board, pacman)
        self.add_ghosts(board, ghosts)
        self.add_power_pellets(board)
        self.fill_empty_with_pacdot(board)

        self.level_one = Level(board, pacman, ghosts)
        return self.level_one

    def add_walls(self, board):
        rows = board.get_rows()
        for i in range(1, rows-1):
            board.place_entity(Position(0, i), Wall())
            board.place_entity(Position(rows-1, i), Wall())
        columns = board.get_columns()
        for i in range(columns):
            board.place_entity(Position(i, 0), Wall())
            board.place_entity(Position(i, columns-1), Wall())

    def add_pacman(self, board, pacman):
        board.place_entity(Position(6, 4), pacman)

    def add_ghosts(self, board, ghosts):
        row = (((board.get_rows())//2)-1)
        column = (((board.get_columns())//2)-1)
        box_ghosts = [Position(row, column), Position(row, column+1), Position(row+1, column), Position(row+1, column+1)]
        for position, ghost in zip(box_ghosts, ghosts):
            board.place_entity(position, ghost)

    def add_power_pellets(self, board):
        power_pellets = [PowerPellet(), PowerPellet(), PowerPellet()]
        board.place_entity(Position(1, 1), power_pellets[0])
        board.place_entity(Position(8, 7), power_pellets[0])
        board.place_entity(Position(1, 6), power_pellets[0])

    def fill_empty_with_pacdot(self, board):
        for i in range(board.get_rows()):
            for j in range(board.get_columns()):
                position = Position(i, j)
                if board.is_empty(position):
                    board.place_entity(Position(i, j), PacDot())
