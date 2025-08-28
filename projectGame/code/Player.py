from code.Entity import Entity
import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 5

    def move(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed

        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += self.speed

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
        
            self.rect.x -= self.speed

        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed