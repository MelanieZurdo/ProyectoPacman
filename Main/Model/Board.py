from .Square import Square
from .Position import Position
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

    def limit_case_up(self):
        return self.get_rows()-self.get_rows()

    def limit_case_down(self):
        return self.get_rows()-1

    def limit_case_right(self):
        return self.get_columns()-1

    def limit_case_left(self):
        return self.get_columns()-self.get_columns()

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
        check_position = direction.validate_position(position_entity,self)
        if check_position is False:
            pass
        else:
            new_position = direction.new_position(position_entity)
            self.clear_entity(position_entity)
            self.place_entity(new_position, entity)

    def fill_board(self):
        pass

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
