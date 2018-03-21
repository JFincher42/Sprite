##
## Missile Game
## Testing Sprite and Imagesheet libraries
##

# Library imports
import os
import random

import pygame           # pylint: disable=E1101

import sprite           # Sprite library should be in PYTHONPATH
import imagesheet

# Helper functions

# get_key_pressed
# Param:  keypress - pygame constant for the keypress (i.e. pygame.K_SPACE)
# Return: Boolean value whether the key was pressed or not
def get_key_pressed(keypress):
    keys = pygame.key.get_pressed()
    return keys[keypress]       # pylint: disable=E1101

# Initialize pygame stuff
pygame.init()           # pylint: disable=E1101
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Setup sprite strings
ship_string =       os.path.join(".", "MissileGame", "small ship right.png")
impact_string =     os.path.join(".", "MissileGame", "impactspritesheet.png")
incoming_string =   os.path.join(".", "MissileGame", "roundshipspin.png")
missile_string =    os.path.join(".", "MissileGame", "missile right.png")
background_string = os.path.join(".", "MissileGame", "skyscrolling.jpg")

# Setup sprites
ship = sprite.Sprite(ship_string, 0, 0)         # pylint: disable=E1102
ship_x, ship_y = 75, 265
ship.center = (ship_x, ship_y)
ship_speed = 0.2
ship_min_y = 50
ship_max_y = 520

impactsheet = imagesheet.ImageSheet(impact_string, 5, 6)
incomingsheet = imagesheet.ImageSheet(incoming_string, 5, 6)

missile_speed = 0.5
background_speed = 0.1

enemy_speed = 0.2
enemy_time = 2500

background = sprite.Sprite(background_string, 0, 0)         # pylint: disable=E1102
missiles = []
incoming = []
impacts = []

# Setup drawing loop
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # pylint: disable=E1101
            drawing = False

        # Check for space bar - fire missile
        elif event.type == pygame.KEYDOWN:      # pylint: disable=E1101
            if event.key == pygame.K_SPACE:     # pylint: disable=E1101
                missiles.append(sprite.Sprite(missile_string, ship_x+40, ship_y))       # pylint: disable=E1102

    # Clear the event pump
    pygame.event.pump()

    # Move the ship
    ship_x, ship_y = ship.center
    if get_key_pressed(pygame.K_UP):                       # pylint: disable=E1101
        ship_y-=ship_speed*c.get_time()
        if ship_y<ship_min_y:
            ship_y=ship_min_y
    elif get_key_pressed(pygame.K_DOWN):                   # pylint: disable=E1101
        ship_y+=ship_speed*c.get_time()
        if ship_y>ship_max_y:
            ship_y=ship_max_y
    ship.center_y = ship_y

    # Move the missiles
    for missile in missiles:
        missile.center_x += missile_speed * c.get_time()
        for enemy in incoming:
            if pygame.sprite.collide_rect(missile, enemy):
                # Add a collision animation
                x,y = pygame.sprite.collide_mask(missile, enemy)
                impacts.append(sprite.Sprite(impactsheet, x, y))

    
    # Check if we should spawn a new enemy
    enemy_time -= c.get_time()
    if enemy_time <= 0:
        # Pick a new random time for the next enemy, and create a new one
        enemy_time = random.randint(1500,2000)
        incoming.append(sprite.Sprite(incomingsheet, 1050, random.randint(50,450)))     # pylint: disable=E1102

    # Scroll the background
    background.center_x -= background_speed * c.get_time()
    if background.center_x < 0:
        background.center_x = 1018

    # Draw the background and ship
    background.draw()
    ship.draw()

    # Figure out if a missile is off screen
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

