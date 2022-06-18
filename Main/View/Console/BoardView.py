import curses
import time


class BoardView():
    def __init__(self,board):
        self.board=board
        self.stdscr = curses.initscr()
    
    def show(self):
        self.stdscr.addstr(0, 0, str(self.board))        
        self.stdscr.refresh()
        

    

