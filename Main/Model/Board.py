from Main.Model.Visitable import Visitable
from .Printable import Printable
from .Square import Square
from .Position import Position
from .Wall import Wall



class Board(Printable,Visitable):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.create_board()

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def in_board(self, position):
        return position.get_row() in range(0, self.get_rows()-1) and position.get_column() in range(0, self.get_columns()-1)

    def is_obstacle(self,existing_entity):
        return existing_entity.is_obstacle()

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
                if entity in self.board[i][j].get_entities():
                    return Position(i, j)

    def get_entities(self, position):
        square = self.board[position.get_row()][position.get_column()]
        return square.get_entities()

    def clear_entity(self, position,entity):
        square = self.board[position.get_row()][position.get_column()]
        return square.delete_entity(entity)

    def move_entity(self,entity):        
        position_entity = self.get_position(entity)       
        direction=entity.get_direction()
        new_position=direction.new_position(position_entity)
        
        new_square=self.board[new_position.get_row()][new_position.get_column()]
        
        for existing_entity in new_square.get_entities():
            if self.is_obstacle(existing_entity):
                return False  

        if self.in_board(new_position):
            self.clear_entity(position_entity,entity)                   
            self.place_entity(new_position, entity)
            
    def is_empty(self,position):
        return self.board[position.get_row()][position.get_column()].is_empty()
    
    def visit(self,visitor):
        visitor.visitBoard(self)

    def __str__(self):
        return '\n'+'\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.board])+'\n'
