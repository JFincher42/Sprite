import pygame

# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, xpos, ypos):
        # Call the super init first
        pygame.sprite.Sprite.__init__(self)

        # Load the image we're given,set transparency, and get the bounding rectangle
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.center = (xpos+self.width/2, ypos+self.height/2)

        # Set the position of the item
        self.rect.x = xpos
        self.rect.y = ypos
        self.position = (xpos, ypos)

        # Add this to it's own group for rendering
        self.mygroup = pygame.sprite.GroupSingle(self)

    # Draws the sprite onto the provided surface
    def draw(self, surf):
        self.mygroup.draw(surf)
