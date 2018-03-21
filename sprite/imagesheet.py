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

        # Initialize the list of sprites and the current sprite
        self.sprite_list = []

        # Load the sheet as an image, and get the extents
        sheet = pygame.image.load(image).convert_alpha()
        sheet_width = sheet.get_rect().width
        sheet_height = sheet.get_rect().height

        # Calculate the height and width of each sprite
        sprite_width = sheet_width//col
        sprite_height = sheet_height//row

        # Now loop through the sheet sprite by sprite
        for rows in range(row):
            y = rows * sprite_height
            for cols in range(col):
                x = cols * sprite_width
                # At this point, x,y is the upper left corner of the sprite
                # So we can set the image clip to a rectangle starting there
                # with width and height set to sprite_width and sprite_height
                sheet.set_clip(pygame.Rect(x, y, sprite_width, sprite_height))
                self.sprite_list.append(sheet.subsurface(sheet.get_clip()))

        self.SPRITECOUNT = len(self.sprite_list)
