class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
    
    def decrease_row(self):
        return Position(self.get_row()-1,self.get_column())

    def increase_row(self):
        return Position(self.get_row()+1,self.get_column())
    
    def decrease_column(self):
        return Position(self.get_row(),self.get_column-1)

    def increase_column(self):
        return Position(self.get_row(),self.get_column+1)

