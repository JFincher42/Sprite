import pygame

# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, xpos, ypos):
        super.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.rect
        self.image.set_colorkey(WHITE)
        self.position = (xpos, ypos)
        width = self.image.width
        height = self.image.height
        self.center = (xpos+width/2, ypos+height/2)

        self.mygroup = pygame.sprite.GroupSingle(self)

    def draw(self):
        self.mygroup.draw()
