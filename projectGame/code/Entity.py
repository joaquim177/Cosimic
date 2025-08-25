from abc import ABC, abstractmethod
import pygame


class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.position = position
        self.surf = pygame.image.load('./assets/'+name+'.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        pass
    
    @abstractmethod 
    def move():
        pass