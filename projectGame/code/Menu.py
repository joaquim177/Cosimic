import pygame
from code.const import WIN_WIDTH
from code.const import WIN_HEIGHT


class Menu:
    def __init__(self, windom):
        self.windom = windom
        self.surf = pygame.image.load('./assets/1.png')
        self.rect  = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Cria a fonte
        text_font = pygame.font.SysFont("lucida Sans Typewriter", text_size)
        
        # Renderiza o texto
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        
        # Cria o retângulo do texto centrado na posição
        text_rect = text_surf.get_rect(center=text_center_pos)
        
        # Desenha o texto na janela
        self.windom.blit(text_surf, text_rect)

        

    def run(self):
        pygame.mixer.music.load('./assets/fase1.mp3')
        pygame.mixer.music.play(-1)

        while True:
            self.windom.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=70, text='Cosmic', text_color=(255, 128, 0), text_center_pos=(WIN_WIDTH/2, 40) )
            self.menu_text(text_size=30, text='Play', text_color=(255,255,255), text_center_pos=(WIN_WIDTH/2, 150))
            self.menu_text(text_size=30, text='Score', text_color=(255,255,255), text_center_pos=(WIN_WIDTH/2, 180))
            self.menu_text(text_size=30, text='Quit', text_color=(255,255,255), text_center_pos=(WIN_WIDTH/2, 210))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
     
