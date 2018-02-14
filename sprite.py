import pygame

# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, image, xpos, ypos):
        # Call the super init first
        pygame.sprite.Sprite.__init__(self)

        self.image_list = []

        # Were we given a single image, or an object?
        if type(image) is str:
            # Single image - load it into our image list
            # Load the image we're given,set transparency, and get the bounding rectangle
            self.image_list.append(pygame.image.load(image).convert_alpha())
            self.rect = self.image[0].get_rect()
            self.image[0].set_colorkey(WHITE)
            self.width = self.image[0].get_width()
            self.height = self.image[0].get_height()
            self.center = (xpos+self.width/2, ypos+self.height/2)

        else:
            # We were given a list, so we can use that instead
            pass

        # Set the position of the item
        self.rect.x = xpos
        self.rect.y = ypos
        self.position = (xpos, ypos)

        # Add this to it's own group for rendering
        self.mygroup = pygame.sprite.GroupSingle(self)

    # Draws the sprite onto the provided surface
    def draw(self, surf):
        self.mygroup.draw(surf)
