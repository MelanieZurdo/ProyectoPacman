from .Ghost import Ghost
from .PacDot import PacDot
from .Wall import Wall
from .Board import Board
from .Level import Level
from .Pacman import Pacman
from .Position import Position
from .PowerPellet import PowerPellet


class LevelFactory:
    def __init__(self):
       self.level_one=None

    def get_level_one(self):
        if self.level_one:
            return self.level_one
   

        board=Board(5,5) 
        pacman=Pacman()
        board.place_entity(Position(1,1),pacman)               
        ghosts=[Ghost("blue"),Ghost("red"),Ghost("pink")]
        board.place_entity(Position(1,2),ghosts[0])        
        board.place_entity(Position(1,3),ghosts[1])        
        board.place_entity(Position(3,3),ghosts[2])        
        board.place_entity(Position(3,3),PowerPellet())
        board.place_entity(Position(2,3),PowerPellet())
        board.place_entity(Position(3,1),PowerPellet())

        for i in range(1,4):
            board.place_entity(Position(0,i),Wall())
            board.place_entity(Position(i,0),Wall())
            board.place_entity(Position(4,i),Wall())
            board.place_entity(Position(i,4),Wall())
        board.place_entity(Position(0,0),Wall())
        board.place_entity(Position(0,4),Wall())
        board.place_entity(Position(4,0),Wall())
        board.place_entity(Position(4,4),Wall())

        self.fill_empty_with_pacdot(board)
        self.level_one=Level(board,pacman,ghosts)
        return self.level_one
        
    def fill_empty_with_pacdot(self,board):
        for i in range(5):
            for j in range(5):
                position=Position(i,j)
                if board.is_empty(position):
                    board.place_entity(Position(i,j),PacDot())
            


        


