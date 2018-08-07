'''
Test cases for the sprite class

Jon Fincher, July 2018
'''
import os
import unittest
import pygame
import sprite
import imagesheet

class TestSprite(unittest.TestCase):

    def setUp(self):
        pygame.init()           # pylint: disable=E1101
        w = pygame.display.set_mode([500,500])
        # Single image sheet
        self.spaceship_sheet = sprite.imagesheet.ImageSheet(os.path.join("SpriteDemo", "spaceship_sprite.png"),1,1)
        # Mutli-image sheet
        self.dragon_sheet = sprite.imagesheet.ImageSheet(os.path.join("SpriteDemo", "dragonflying.png"), 4, 6)

    '''
    test_new_single_sprite - tests whether we can create a new sprite with a single image
    '''
    def test_new_sprite(self):
        single_sprite = sprite.Sprite(os.path.join("SpriteDemo", "spaceship_sprite.png"),250,250)
        self.assertEqual("<class 'sprite.Sprite'>", str(type(single_sprite)), "ERROR: New sprite not created")
    
    '''
    test_new_single_image_sheet - tests creating a new sprite from a single image sheet
    '''
    def test_new_single_image_sheet(self):
        single_sprite = sprite.Sprite(self.spaceship_sheet,250,250)
        self.assertEqual("<class 'sprite.Sprite'>", str(type(single_sprite)), "ERROR: Single image sprite not created")

    '''
    test_new_multi_image_sheet - tests creating a new sprite from a multi image sheet
    '''
    def test_new_multi_image_sheet(self):
        multi_sprite = sprite.Sprite(self.dragon_sheet,250,250)
        self.assertEqual("<class 'sprite.Sprite'>", str(type(multi_sprite)), "ERROR: Mutli image sprite not created")
