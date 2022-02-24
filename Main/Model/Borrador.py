from Board import Board
from Square import Square
from PacDot import PacDot
from Position import Position

board=Board(5,5)
list_pacdot=list()
for i in range(5):
    new_pacdot=PacDot()
    list_pacdot.append(new_pacdot)


for i,pacdot in enumerate(list_pacdot):
    board.place_entity(Position(0,i),pacdot)
    board.place_entity(Position(1,i),pacdot)
print(board)




 


    




  





   


