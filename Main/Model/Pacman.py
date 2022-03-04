from Directions import Direction
from Position import Position


class Pacman():

    def move(self, board, direction):
        position = board.get_position(self)
        if direction is Direction.UP:
            row=position.decrease_row()
            position_new = Position(row, position.get_column())
            board.clear_entity(position)
            board.place_entity(position_new, self)            
            return board
        if direction is Direction.DOWN:
            row = position.increase_row()
            position_new = Position(row, position.get_column())
            board.clear_entity(position)
            board.place_entity(position_new, self)
            return board
        if direction is Direction.RIGHT:
            column = position.increase_column()
            position_new = Position(position.get_row(), column)
            board.clear_entity(position)
            board.place_entity(position_new, self)
            return board
        if direction is Direction.LEFT:
            column = position.decrease_column()
            position_new = Position(position.get_row(), column)
            board.clear_entity(position)
            board.place_entity(position_new, self)
            return board

    def __str__(self):
        return "[@]"
