import pygame
from Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.windom = pygame.display.set_mode(size=(600,400))
    def run(self):
        while True:
            menu = Menu(self.windom)
