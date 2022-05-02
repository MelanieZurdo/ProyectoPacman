from abc import ABC, abstractmethod
from .Entity import Entity

class DynamicEntity(Entity,ABC):
   def __init__(self,movement_strategy):
      self.movement_strategy=movement_strategy

   @abstractmethod
   def is_obstacle(self):
      pass  

