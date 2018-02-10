import sprite
import pygame
import os

pygame.init()
w = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

xpos=100
ypos=100
spaceship = sprite.Sprite(os.path.join(".", "spaceship_sprite.png"), xpos, ypos)

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    w.fill((128,128,128))
    xpos+=2
    if xpos>400:
        xpos=0
    spaceship.rect.x = xpos
    spaceship.draw(w)
    pygame.display.flip()
    c.tick(30)
