class Board:
    def __init__(self,number_rows,number_columns):
        self.number_rows=number_rows
        self.number_columns=number_columns
        self.board=[]


    def create_board(self):
        for i in range(self.number_rows):
            self.board.append([])
            for j in range(self.number_columns):
                self.board[i].append(0)
        return self.board
    
    
    
        
        

    

            
    
        




