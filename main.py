import pygame

pygame.init()
width = 800
height = 600
FPS = 60

window = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
run = True

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()