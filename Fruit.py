from EatableEntity import EatableEntity


# Esto nose , tal vez conviene lo de las clases para cada tipo de fruta...
class Fruit(EatableEntity):
    def __init__(self, type):
        self.type = type
