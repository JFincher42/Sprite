import pygame
import imagesheet
# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):
    '''
    Defines a sprite as the following:
    - a subclass of pygame.sprite.Sprite, 
    - containing either:
        - a single image to display, or
        - a set of images to animate
    - with the following R/W attributes
        - an x,y position of the upper left corner of the image
        - an x,y position of the center of the image
        - 
    '''

    # Center properties
    @property
    def center(self):
        '''
        Returns the center of the sprite as an (x,y) tuple.
        '''
        #return (self.rect.x+self.width/2, self.rect.y+self.height/2)
        return self.rect.center
    
    @center.setter
    def center(self, new_center):
        '''
        Sets the sprites location so the center aligns with the provided new_center tuple.
        '''
        #self.__center_x, self.__center_y = new_center
        #self.rect.x = self.__center_x - self.width/2
        #self.rect.y = self.__center_y - self.height/2
        self.rect.center = new_center

    @property
    def center_x(self):
        #return self.__center_x
        return self.rect.center_x
    @property
    def center_y(self):
        #return self.__center_y
        return self.center_y

    @center_x.setter
    def center_x(self, new_center_x):
        #self.__center_x = new_center_x
        #self.rect.x = self.__center_x - self.width/2
        self.rect.center_x = new_center_x
    @center_y.setter
    def center_y(self, new_center_y):
        #self.__center_y = new_center_y
        #self.rect.y = self.__center_y - self.height/2
        self.rect.center_y = new_center_y
    
    # X and Y properties
    @property
    def x(self):
        return self.rect.x
    @property
    def y(self):
        return self.rect.y

    @x.setter
    def x(self, new_x):
        self.rect.x = new_x
    @y.setter
    def y(self, new_y):
        self.rect.y = new_y

    # Flip along each axis - true or false value
    @property
    def flip_x(self):
        return self.__flip_x
    @property
    def flip_y(self):
        return self.__flip_y

    @flip_x.setter
    def flip_x(self, new_flip_x):
        self.__flip_x = new_flip_x
    @flip_y.setter
    def flip_y(self, new_flip_y):
        self.__flip_y = new_flip_y

    # Has this sprite been destroyed?
    # Set by the destroy() function
    @property
    def destroyed(self):
        return self.__destroyed

    def __init__(self, image, xpos, ypos):
        # Call the super init first
        pygame.sprite.Sprite.__init__(self)

        self.image_list = []

        # Were we given a single image, or an object?
        if type(image) is str:
            # Single image - load it into our image list
            # Load the image we're given,set transparency, and get the bounding rectangle
            self.image_list.append(pygame.image.load(image).convert_alpha())

        elif type(image) is imagesheet.ImageSheet:
            # We were given an ImageSheet, so we can use that instead
            self.image_list = list(image.sprite_list)
            self.current_sprite = 0

        self.rect = self.image_list[0].get_rect()
        self.image_list[0].set_colorkey(WHITE)
        self.width = self.rect.width
        self.height = self.rect.height

        # Set the position of the item
        self.rect.x = xpos
        self.rect.y = ypos
        self.position = (xpos, ypos)
        self.center = (xpos+self.width/2, ypos+self.height/2)

        self.__flip_x = False
        self.__flip_y = False

        # Add this to it's own group for rendering
        self.mygroup = pygame.sprite.GroupSingle(self)

    # Draws the sprite onto the provided surface
    def draw(self, surf):
        # If it's a single image, grab it.  Else, grab the next one in line
        if len(self.image_list) == 1:
            self.image = self.image_list[0]
        else:
            self.image = self.image_list[self.current_sprite]
        
        # Flip if necessary
        self.image = pygame.transform.flip(self.image, self.__flip_x, self.__flip_y)
        
        # Draw it
        self.mygroup.draw(surf)

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.image_list):
            self.current_sprite = 0
        self.image = self.image_list[self.current_sprite]
