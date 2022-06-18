from .StaticEntity import StaticEntity


class Wall(StaticEntity):

      def accept(self,visitor):
        visitor.visitWall(self)

      def is_obstacle(self):
          return True  

      def __str__(self):
        return " | "
