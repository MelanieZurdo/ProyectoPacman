import time
from Main.Model.Direction import Direction
from Main.Model.LevelFactory import LevelFactory
from Main.View.Console.BoardView import BoardView


class Controler:    

    def main(self):        
        level_factory=LevelFactory()
        level_one=level_factory.get_level_one()        
        board_view=BoardView(level_one.board)
        board_view.show()
        while True:
            time.sleep(1)
            for ghost in level_one.ghosts:
                level_one.board.move_entity(ghost,ghost.direction)
         
            level_one.board.move_entity(level_one.pacman,level_one.pacman.direction) 
            board_view.show()       
           
            

       


if __name__ == '__main__':
    controler=Controler()
    controler.main()