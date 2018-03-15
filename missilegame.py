##
## Missile Game
##

import sprite
import imagesheet
import pygame           # pylint: disable=E1101
import os

pygame.init()           # pylint: disable=E1101
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

ship = sprite.Sprite(os.path.join(".", "small ship right.png"), 0, 0)
#missile = sprite.Sprite(os.path.join(".", "missile right.png"), 0, 0)

impactsheet = imagesheet.ImageSheet(os.path.join(".", "impactspritesheet.png"), 5, 6)
incomingsheet = imagesheet.ImageSheet(os.path.join(".", "roundshipspin.png"), 5, 6)
#impact = sprite.Sprite(impactsheet, 0, 0)
#incoming = sprite.Sprite(incomingsheet, 0, 0)

ship.center = (75, 265)
ship_speed = 0.2
missile_speed = 0.5
background_speed = 0.1
enemy_speed = 0.2
enemy_time = 1200

background = sprite.Sprite(os.path.join(".", "skyscrolling.jpg"), 0, 0)
missiles = []
incoming = []

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # pylint: disable=E1101
            drawing = False
        elif event.type == pygame.KEYDOWN:      # pylint: disable=E1101
            if event.key == pygame.K_SPACE:     # pylint: disable=E1101
                missiles.append(sprite.Sprite(os.path.join(".", "missile right.png"), ship_x+40, ship_y))

    pygame.event.pump()
    ship_x, ship_y = ship.center
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:                       # pylint: disable=E1101
        ship_y-=ship_speed*c.get_time()
        if ship_y<50:
            ship_y=50
    elif keys[pygame.K_DOWN]:                   # pylint: disable=E1101
        ship_y+=ship_speed*c.get_time()
        if ship_y>520:
            ship_y=520

    ship.center_y = ship_y

    enemy_time -= c.get_time()
    if enemy_time <= 0:
        enemy_time = random.randint(1000,1500)
        incoming.append(sprite.Sprite(incomingsheet, 1050, random.randint(50,450)))

    background.center_x -= background_speed * c.get_time()
    if background.center_x < 0:
        background.center_x = 1018
    background.draw()

    ship.draw()

    missiles_gone = []
    for missile in missiles:
        missile.center_x += missile_speed * c.get_time()
        if missile.x > 1018:
            missiles_gone.append(missile)
        else:
            missile.draw()
    
    for missile in missiles_gone:
        missiles.remove(missile)

    pygame.display.flip()
    c.tick(30)
