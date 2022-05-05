from abc import ABC, abstractmethod
from .Entity import Entity

class DynamicEntity(Entity,ABC):
   def __init__(self):
      pass
      

   @abstractmethod
   def is_obstacle(self):
      pass 
   @abstractmethod
   def get_direction(self):
      pass 

