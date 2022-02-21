from Square import Square
from Position import Position
from Pacman import Pacman
from PacDot import PacDot


class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.create_board()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def create_board(self):
        self.board = list()
        for i in range(self.get_rows()):
            self.board.append([])
            for j in range(self.get_columns()):
                self.board[i].append(Square())

    def place_entity(self, position, entity):
        square = self.board[position.get_row()][position.get_column()]
        square.put(entity)

    def get_entity(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.entity 

    def clean_entity(self,position):
        square = self.board[position.get_row()][position.get_column()]
        return square.delete()       
        

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
    









