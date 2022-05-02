from abc import ABC, abstractmethod
from Main.Model.Entity import Entity

class DynamicEntity(Entity,ABC):

   @abstractmethod
   def is_obstacle(self):
      pass  

