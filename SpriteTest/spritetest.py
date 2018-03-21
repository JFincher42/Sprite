import os

import pygame  # pylint: disable=E1101

import sprite, imagesheet

pygame.init()           # pylint: disable=E1101
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

dragon_sheet = sprite.imagesheet.ImageSheet(os.path.join(".", "dragonflying.png"), 4, 6)
dragon = sprite.Sprite(dragon_sheet, 0, 0)
dragon.scale = .7
dragon.image_animation_rate = 45

puffin_sheet = imagesheet.ImageSheet(os.path.join(".", "puffinflysheet.png"), 5, 6)
puffin = sprite.Sprite(puffin_sheet, 0, 0)

background = sprite.Sprite(os.path.join(".", "skyscrolling.jpg"), 0, 0)

scalefact = -0.1
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # pylint: disable=E1101
            drawing = False

    x, y = pygame.mouse.get_pos()

    background.center_x -= .1 * c.get_time()
    if background.center_x < 0:
        background.center_x = 1018
    background.draw()

    puffin.center = (x,y)
    puffin.update(c.get_time())
    puffin.draw()

    pygame.display.flip()
    c.tick(30)
