'''
Test cases for the imagesheet class

Jon Fincher, July 2018
'''
import os
import unittest
import sprite
import imagesheet

class TestImageSheet(unittest.TestCase):

    def setUp(self):

        self.spaceship_sheet = sprite.imagesheet.ImageSheet(os.path.join("SpriteDemo", "spaceship_sprite.png"),1,1)
        self.dragon_sheet = sprite.imagesheet.ImageSheet(os.path.join("SpriteDemo", "dragonflying.png"), 4, 6)

    '''
    test_single_image - tests whether imagesheet can load a single image successfully
    '''
    def test_single_image(self):
        self.assertEqual(self.spaceship_sheet.SPRITECOUNT, 1, "Did not load single sprite image properly.")

    '''
    test_animated_image - tests whether imagesheet can load an animated image successfully
    '''
    def test_animated_image(self):
        self.assertEqual(self.dragon_sheet.SPRITECOUNT, 24, "Did not load animated sprite image properly.")
        self.assertEqual(self.dragon_sheet.sprite_list.count, 24, "Sprite list count doesn't match SPRITE_COUNT")
