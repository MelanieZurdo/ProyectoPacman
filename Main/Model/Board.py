from .Square import Square
from .Position import Position
from .Direction import Direction
from .Up import Up


class Board():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.create_board()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def in_board(self,position):
        if position.get_row() in range(0,5) and position.get_column() in range(0,5):
            return True
        else:
            return False     

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
        check_position=self.in_board(new_position)
        if check_position:
            self.clear_entity(position_entity)
            self.place_entity(new_position,entity)

        

    def fill_board(self):
        pass

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
