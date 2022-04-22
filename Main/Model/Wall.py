from .StaticEntity import StaticEntity


class Wall(StaticEntity):

      def is_obstacle(self):
          return True  

      def __str__(self):
        return "[-]"
