import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, windom, name):
        self.windom = windom
        self.name = name    
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.getEntity('level1'))
        print("Level: "+name)
        pass

    def run(self):
        while True:
            for ent in self.entity_list:
                self.windom.blit(source=ent.surf, dest= ent.rect)
            pygame.display.flip()
        