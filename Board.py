from Nivel import Nivel
from Pacman import Pacman
from Position import Position

class Board(Nivel):#Si bien me funciona, no me convence a nivel teorico, un tablero es un nivel?
    def __init__(self,rows,columns):
        super().__init__(rows,columns)
        self.board=self.create_board()
        
    
    
    def create_board(self):
        board=[]
        for i in range(self.rows):
            board.append([])   
            print()                
            for j in range(self.columns):                
                board[i].append(None)                       
        return board

    
    def place_character(self,*args):
        for i,value in enumerate(args):
            if i==0:
                character=value
            elif i==1:
                x,y=value
                self.board[x][y]=character
        


pacman=Pacman
pacman_place=Position(1,2)
tablero=Board(5,5)
tablero.place_character(pacman,pacman_place.position)
print(tablero.board)
        
        
       
        
        
        
        








      
    







        







    
        



    
    
        
    
    
        
        

    

            
    
        




