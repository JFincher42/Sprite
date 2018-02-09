import sprite
import pygame

pygame.init()
w = pygame.display.set_mode([400, 400])

spaceship = sprite.Sprite("spaceship_sprite.png", 200, 200)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.TYPE == pygame.QUIT:
            drawing = False

    spaceship.draw()
    pygame.display.flip()
