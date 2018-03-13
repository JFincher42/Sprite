import sprite
import imagesheet
import pygame           # pylint: disable=E1101
import os

pygame.init()           # pylint: disable=E1101
w = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

xpos = 100
ypos = 100
sheet = imagesheet.ImageSheet(os.path.join(".", "spaceship_sprite.png"), 2, 2)
spaceship = sprite.Sprite(os.path.join(".", "spaceship_sprite.png"), xpos, ypos)

bullwinkle_sheet = imagesheet.ImageSheet(os.path.join(".", "Bullwinkle_Sprites.png"), 1, 6)
bullwinkle = sprite.Sprite(bullwinkle_sheet, xpos, ypos)

dragon_sheet = imagesheet.ImageSheet(os.path.join(".", "dragonflying.png"), 4, 6)
dragon = sprite.Sprite(dragon_sheet, xpos, ypos)
dragon.scale = 1
dragon.image_animation_rate = 45
print("Width=" + str(dragon.rect.width) + ", Height=" + str(dragon.rect.height))

#spaceship = sprite.Sprite(sheet, xpos, ypos)
#spaceship.current_sprite = 2

scalefact = -0.1
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # pylint: disable=E1101
            drawing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dragon.scale <= 0.5 or dragon.scale >= 1.5:
                scalefact *= -1
            dragon.scale = dragon.scale + scalefact

    w.fill((128, 128, 128))
    x, y = pygame.mouse.get_pos()
    #spaceship.center = (x, y)
    #spaceship.flip_y = True
    #spaceship.angle += 1
    #spaceship.draw()

    #bullwinkle.center = (x,y)
    #bullwinkle.update(c.get_time())
    #bullwinkle.draw()



    dragon.center = (x,y)
    dragon.update(c.get_time())
    dragon.draw()

    pygame.draw.rect(w, (255,255,255), dragon.rect, 1)

    pygame.display.flip()
    c.tick(30)
