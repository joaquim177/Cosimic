import pygame
from code.Entity import Entity
from code.const import WIN_WIDTH



class Enimy(Entity):
    def __init__(self, name, position):

        super().__init__(name, position)
        
    def move(self):
        self.rect.centerx  -= 5
        if(self.rect.right <= 0):
            self.rect.left = WIN_WIDTH