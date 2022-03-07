from .Square import Square
from .Position import Position


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

    def limit_cases_up(self):
        limit_cases_up = list()
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if i == 0:
                    limit_cases_up.append((i, j))
        return limit_cases_up

    def limit_cases_down(self):
        limit_cases_down = list()
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if i == self.get_rows()-1:
                    limit_cases_down.append((i, j))
        return limit_cases_down

    def limit_cases_right(self):
        limit_cases_right = list()
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if j == self.get_columns()-1:
                    limit_cases_right.append((i, j))
        return limit_cases_right

    def limit_cases_left(self):
        limit_cases_left = list()
        for i in range(self.get_rows()):
            for j in range(self.get_columns()):
                if j == 0:
                    limit_cases_left.append((i, j))
        return limit_cases_left

    def fill_board(self):
        pass

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])
