import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory
import time
class Level:
    def __init__(self, windom, name):
        self.windom = windom
        self.name = name 
        self.event_enemy = pygame.USEREVENT +1
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.getEntity('level1'))
        self.entity_list.append(EntityFactory.getEntity('player'))
        self.start_time = pygame.time.get_ticks()
        pygame.time.set_timer(self.event_enemy, 4000)
        pass

    def cronometro(self):
        while True:
            time.sleep(1)
            self.time += 1

    def run(self):
        pygame.mixer_music.load('./assets/'+self.name+'.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            timer = (pygame.time.get_ticks() - self.start_time) / 1000  


            for ent in self.entity_list:
                if hasattr(ent, "move"):
                    ent.move()
                self.windom.blit(ent.surf, ent.rect)
            
            self.level_text(14, f'Proteja o planeta terra!! - Timer: {timer}', (255,255,255), (200,10) )    
            self.level_text(14, f'Fps: {clock.get_fps() :.0f}', (255,255,255), (30, 320) )    
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == self.event_enemy:
                    self.entity_list.append(EntityFactory.getEntity('cometa'))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.windom.blit(text_surf, text_rect)