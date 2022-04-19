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
        return position.get_row() in range(1, self.get_rows()-1) and position.get_column() in range(1, self.get_columns()-1)

    def create_board(self):
        self.board = list()
        for i in range(self.get_rows()):
            self.board.append([])
            for j in range(self.get_columns()):
                self.board[i].append(Square())

    def place_entity(self, position, entity):
        square = self.board[position.get_row()][position.get_column()]
        square.put(entity)

    def put_entity_in_board(self, position, static_entity):
        square = self.board[position.get_row()][position.get_column()]
        square.put_entitie_in_square(static_entity)

    def get_position(self, entity):
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if entity in self.board[i][j].get_entities():
                    return Position(i, j)

    def get_entities(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.get_entities()
    def get_entity(self,position):
        square = self.board[position.get_row()][position.get_column()]
        return square.get_entity()


    def clear_entity(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.delete()

    def move_entity(self, entity, direction):
        position_entity = self.get_position(entity)
        square = self.board[position_entity.get_row()][position_entity.get_column()]
        new_position = direction.new_position(position_entity)
        if self.in_board(new_position):
            self.place_entity(new_position, entity)

    def __str__(self):
        return '\n'+'\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])+'\n'
