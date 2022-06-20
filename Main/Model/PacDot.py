from Main.Model.StaticEntity import StaticEntity


class PacDot(StaticEntity):
    def __init__(self):
        self.score = 100

    def is_obstacle(self):
        return False

    def can_eat_eatable_entity(self):
        return False

    def accept(self, visitor):
        visitor.visitPacDot(self)

    def __str__(self):
        return " · "
