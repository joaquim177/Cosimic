from abc import ABC, abstractmethod
import pygame

from code.const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.position = position
        self.surf = pygame.image.load('./assets/'+name+'.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        
        if(self.name == 'cometa' or self.name == 'player'):
            print(self.name, ENTITY_HEALTH[self.name])
            self.health = ENTITY_HEALTH[self.name]
        pass
    
    @abstractmethod 
    def move():
        pass