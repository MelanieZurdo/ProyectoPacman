from numpy import character
from Square import Square
from Position import Position
from Pacman import Pacman


class Board():
    def __init__(self, rows, columns, square):
        self.rows = rows
        self.columns = columns
        self.square = square
        self.create_board()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def create_board(self):
        self.board = []
        for i in range(self.get_rows()):
            self.board.append([])
            for j in range(self.get_columns()):
                self.board[i].append(self.square)
        return self.board

    def place_entity(self, entity, position):
        self.board[position.get_row()][position.get_column()] = entity
        return self.board

    def __str__(self):
        return f"{self.create_board()}"
