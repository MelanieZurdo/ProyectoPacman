class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column
    
    def decreased_row(self):
        return Position(self.get_row()-1,self.get_column())

    def increased_row(self):
        return Position(self.get_row()+1,self.get_column())
    
    def decreased_column(self):
        return Position(self.get_row(),self.get_column()-1)

    def increased_column(self):
        return Position(self.get_row(),self.get_column()+1)

