import sprite
import pygame
import os

pygame.init()
w = pygame.display.set_mode([400, 400])

spaceship = sprite.Sprite(os.path.join(".", "spaceship_sprite.png"), 100, 100)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    spaceship.draw(w)
    pygame.display.flip()
