from Main.Model_main.EatableEntity import EatableEntity


#TODO: Maybe is better to have a children class for each fruit
class Fruit(EatableEntity):
    def __init__(self, type):
        self.type = type
