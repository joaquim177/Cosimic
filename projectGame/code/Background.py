import pygame
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name:str, position:tuple):
        super().__init__(name,position)
        pass

    def move(self):
        pass