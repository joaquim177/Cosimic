from code.Entity import Entity
import pygame
pygame.mixer.init()
from code.PlayerShot import PlayerShot
from code.const import WIN_HEIGHT, WIN_WIDTH


class Player(Entity):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.speed = 5
        self.shot_delay = 7

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

    def shoot(self):
        shoot_sound = pygame.mixer.Sound("./assets/tiro.mp3")
        shoot_sound.set_volume(0.1)
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = 10
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_KP_ENTER]:
                shoot_sound.play()
                return PlayerShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))
