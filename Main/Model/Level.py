class Level:
    def __init__(self, board, pacman, ghosts):
        self.board = board
        self.pacman = pacman
        self.ghosts = ghosts
        self.dynamic_entities=[self.pacman]
        self.dynamic_entities.extend(self.ghosts)

    def move(self):        
        for entity in self.dynamic_entities:
            if entity.is_alive():
                self.board.move_entity(entity)

