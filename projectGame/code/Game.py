import pygame
from code.Menu import Menu
from code.const import WIN_HEIGHT
from code.const import WIN_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.windom = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))
    def run(self):

        while True:
            menu = Menu(self.windom)
            menu.run()
            pass

