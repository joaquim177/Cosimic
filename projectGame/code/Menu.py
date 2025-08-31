import pygame
from code.const import WIN_WIDTH
from code.const import WIN_HEIGHT


class Menu:
    def __init__(self, windom):
        self.windom = windom
        self.surf = pygame.image.load('./assets/1.png')
        self.rect  = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.windom.blit(text_surf, text_rect)

        

    def run(self):
        self.menu_option = 0

        self.options = (['Play', (255,255,255), 150],  ['Quit', (255,255,255), 180] )
        pygame.mixer.music.load('./assets/menu.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.05)
        while True:
            self.windom.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=70, text='Cosmic', text_color=(255, 128, 0), text_center_pos=(WIN_WIDTH/2, 40) )

            for i, opt in enumerate(self.options):
                color = (255,222,33) if i == self.menu_option else opt[1]
                self.menu_text(
                    text_size=30,
                    text=opt[0],
                    text_color=color,
                    text_center_pos=(WIN_WIDTH/2, opt[2])
                )

            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_DOWN):
                        if((len(self.options) - 2) < self.menu_option):
                            self.menu_option = 0
                        else:
                            self.menu_option +=1

                    elif(event.key == pygame.K_UP):
                        if(self.menu_option < 1):
                            self.menu_option = 2
                        else:
                            self.menu_option -=1
                    
                    elif(event.key == pygame.K_RETURN):
                        res = self.options[self.menu_option][0]
                        return res
                        
                    else:
                        print("botao nao reconhecido")
                
