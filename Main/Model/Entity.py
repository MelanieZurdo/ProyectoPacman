from abc import ABC, abstractmethod
from Main.Model.Host import Host
from .Printable import Printable


class Entity(ABC, Printable, Host):

    @abstractmethod
    def is_obstacle(self):
        pass

    @abstractmethod
    def is_eatable_by(self, entity):
        pass

    @abstractmethod
    def can_eat_ghost(self):
        pass

    def eat(self, entity):
        pass

    def can_eat_pacman(self):
        return False

    def is_dynamic(self):
        return False

    def die(self):
        pass
