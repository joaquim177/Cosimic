import pygame
from code.Menu import Menu
from code.Level import Level
from code.const import WIN_HEIGHT
from code.const import WIN_WIDTH

class Game:
    def __init__(self):
        pygame.init()
        self.windom = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))
    def run(self):

        while True:
            menu = Menu(self.windom)

            menu_return = menu.run()
            if(menu_return == 'Play'):
                level = Level(self.windom, 'level1')
                level_return = level.run()
            elif(menu_return == 'Quit'):
                pygame.quit()
                quit()

            pass

