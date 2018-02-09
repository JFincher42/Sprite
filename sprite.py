import pygame

# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.image.set_colorkey(WHITE)
        self.position = (xpos, ypos)
        width = self.image.get_width()
        height = self.image.get_height()
        self.center = (xpos+width/2, ypos+height/2)

        self.mygroup = pygame.sprite.GroupSingle(self)

    def draw(self, surf):
        self.mygroup.draw(surf)
