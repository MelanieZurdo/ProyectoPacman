from .PacDot import PacDot
from .Square import Square
from .Position import Position
from .Wall import Wall
from .Direction import Direction



class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.create_board()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def in_board(self, position):
        return position.get_row() in range(0, self.get_rows()) and position.get_column() in range(0, self.get_columns())

    def create_board(self):
        self.board = list()
        for i in range(self.get_rows()):
            self.board.append([])
            for j in range(self.get_columns()):
                self.board[i].append(Square())

    def place_entity(self, position, entity):
        square = self.board[position.get_row()][position.get_column()]
        square.put(entity)

    def get_position(self, entity):
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if self.board[i][j].get_entity() == entity:
                    return Position(i, j)

    def get_entity(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.get_entity()

    def clear_entity(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.delete()

    def move_entity(self, entity, direction):
        position_entity = self.get_position(entity)
        new_position = direction.new_position(position_entity)
        if self.in_board(new_position) and self.is_not_wall(new_position) is not True:
            self.clear_entity(position_entity)
            self.place_entity(new_position, entity)

    def append_wall(self):
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if i == 0 or j == 0 or i == self.get_rows()-1 or j == self.get_columns()-1:
                    self.board[i][j].put(Wall())

    def is_not_wall(self,position):
       row=position.get_row()
       column=position.get_column()
       return row== 0 or column == 0 or row == self.get_rows()-1 or column == self.get_columns()-1
            
    def append_pacdot(self):
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if self.board[i][j].is_empty():
                    self.board[i][j].put(PacDot())

    def fill_board(self):
        self.append_wall()
        self.append_pacdot()

    def __str__(self):
        return '\n'+'\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])+'\n'
