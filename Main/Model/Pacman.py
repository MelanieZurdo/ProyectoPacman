from .DynamicEntity import DynamicEntity

class Pacman(DynamicEntity):

    def capture_eatable_entity(self,board,position):
        entity=board.get_entity(position)
        if entity in (entity.list_eatable_entity()):
            board.clear_entity(position)

    def __str__(self):
        return "[@]"
