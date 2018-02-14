'''
Image Sheet class
'''

import pygame


class ImageSheet:

    def __init__(self, image, row, col):
        '''
        Initializes an Image Sheet.  It breaks a larger image
        into a list of smaller images.

        param: image is the sprite sheet
        param: row is the number of rows of images
        param: col is the numbers of columns of images
        '''
        sheet = pygame.image.load(image).convert_alpha()
        image_rect = sheet.get_rect()
        sprite_width = image_rect.get_width()/col
        sprite_height = image_rect.get_height()/row
        for y in range(0, image_rect.get_height(), sprite_height):
            for x in range(0, image_rect.get_width(), sprite_width):
