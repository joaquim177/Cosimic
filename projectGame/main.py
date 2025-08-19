import pygame


pygame.init()

windom = pygame.display.set_mode(size=(600,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
