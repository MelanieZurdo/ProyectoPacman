from abc import ABC, abstractmethod


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


class Direction(ABC):

    @abstractmethod
    def new_position(self):
        pass

    def up():
        return Up()

    def down():
        return Down()

    def right():
        return Right()

    def left():
        return Left()


@singleton
class Up(Direction):
    def new_position(self, position):
        return position.decreased_row()


@singleton
class Down(Direction):
    def new_position(self, position):
        return position.increased_row()


@singleton
class Right(Direction):
    def new_position(self, position):
        return position.increased_column()


@singleton
class Left(Direction):
    def new_position(self, position):
        return position.decreased_column()
