from .State import State

class Afraid(State):

    def is_afraid(self):
        return True
    
    def can_eat_entity(self):
        return False