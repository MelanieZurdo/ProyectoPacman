from Directions import Direction
from Position import Position
from Board import Board


class Pacman():

    def move(self, board, direction):
        position = board.get_position(self)
        if direction is Direction.UP:
            check_position = (position.get_row(), position.get_column())
            if check_position in (board.limit_cases_up()):
                pass
            else:
                row = position.decrease_row()
                position_new = Position(row, position.get_column())
                board.clear_entity(position)
                board.place_entity(position_new, self)
                return board

        if direction is Direction.DOWN:
            check_position = (position.get_row(), position.get_column())
            if check_position in (board.limit_cases_down()):
                pass
            else:
                row = position.increase_row()
                position_new = Position(row, position.get_column())
                board.clear_entity(position)
                board.place_entity(position_new, self)
                return board

        if direction is Direction.RIGHT:
            check_position = (position.get_row(), position.get_column())
            if check_position in (board.limit_cases_right()):
                pass
            else:
                column = position.increase_column()
                position_new = Position(position.get_row(), column)
                board.clear_entity(position)
                board.place_entity(position_new, self)
                return board

        if direction is Direction.LEFT:
            check_position = (position.get_row(), position.get_column())
            if check_position in (board.limit_cases_left()):
                pass
            else:
                column = position.decrease_column()
                position_new = Position(position.get_row(), column)
                board.clear_entity(position)
                board.place_entity(position_new, self)
                return board

    def __str__(self):
        return "[@]"
