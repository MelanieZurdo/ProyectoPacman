class Level:
    def __init__(self, board, pacman, ghosts):
        self.board = board
        self.pacman = pacman
        self.ghosts = ghosts

    def move(self):
        self.board.move_entity(self.pacman)
        for ghost in self.ghosts:
            self.board.move_entity(ghost)
