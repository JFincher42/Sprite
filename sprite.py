import pygame

# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, xpos, ypos):
        super.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.image.set_colorkey(WHITE)
        self.position = (xpos, ypos)
        width = self.image.width
        height = self.image.height
        self.center = (xpos+width/2, ypos+height/2)
