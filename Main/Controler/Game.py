from Main.Controler.game_constants import *



def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Game():
    
    def __init__(self, level):
        self.level = level        
        self.power_pellet_counter=-1
    
    def clock_tick(self):
        self.level.move()
        self.power_pellet_counter-=1
        if self.power_pellet_counter==0:                 
            self.power_pellet_mode_off()

    def power_pellet_eaten(self):                     
        self.power_pellet_mode_on()

    def power_pellet_mode_off(self):
        self.level.pacman.scare()
        for ghost in self.level.ghosts:
            ghost.calm()

    def power_pellet_mode_on(self):        
        
        self.power_pellet_counter=POWER_PELLET_TICKS_AMOUNT
        self.level.pacman.calm()
        for ghost in self.level.ghosts:
            ghost.scare()
       
        

        


        
