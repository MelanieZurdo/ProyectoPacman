from .EatableEntity import EatableEntity
from .Board import Board
class Pacman():

    def capture_eatable_entity(self,board,position):
        entity=board.get_entity(position)
        if entity in (entity.list_eatable_entity()):
            board.clear_entity(position)

    def __str__(self):
        return "[@]"
