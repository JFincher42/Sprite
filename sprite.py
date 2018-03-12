import pygame
import imagesheet
# Define some constants
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)


class Sprite(pygame.sprite.Sprite):
    '''
    Defines a sprite as the following:
    - a subclass of pygame.sprite.Sprite, 
    - a subclass of pygame.sprite.Sprite,
    - containing either:
        - a single image to display, or
        - a set of images to animate
    - with the following R/W attributes
        - an x,y position of the upper left corner of the image
        - an x,y position of the center of the image
        - 
        -

    R/W Fields:
      __image_list      - list of images in the sprite
                          a single image is in __image_list[0]
      __current_cell    - which image are we displaying?

      center            - center of the image rect
                          includes center_x and center_y
      x,y               - x and y coordinates of the upper left corner
                          of the image rect
      __flip_x,         - do we flip the image on the X...
      __flip_y            or the Y axis?  Uses pygame.transform
      __angle           - to what angle do we rotate the image?
      __scale           - do we scale the image up?

    R/O Fields:
      __destroyed       - have we destroyed this sprite?

    Methods
      draw              - draws the sprite at the current location
                          with the current flip, angle, and scale
      update            - for sprites with multiple images, change to the next image
    '''

    # Center properties
    @property
    def center(self):
        '''
        Returns the center of the sprite as an (x,y) tuple.
        '''
        # return (self.rect.x+self.width/2, self.rect.y+self.height/2)
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
        '''
        Returns the center_x property from the image rect
        '''
        return self.rect.center_x

    @property
    def center_y(self):
        '''
        Returns the center_y property from the image rect
        '''
        return self.center_y
        return self.rect.center_y

    @center_x.setter
    def center_x(self, new_center_x):
        '''
        Sets the center_x property of the image rect to the provided new_center_x
        '''
        self.rect.center_x = new_center_x

    @center_y.setter
    def center_y(self, new_center_y):
        '''
        Sets the center_y property of the image rect to the provided new_center_y
        '''
        self.rect.center_y = new_center_y

    # X and Y properties
    @property
    def x(self):
        '''
        Returns the x coordinate of the upper left corner of the image rect
        '''
        return self.rect.x

    @property
    def y(self):
        '''
        Returns the y coordinate of the upper left corner of the image rect
        '''
        return self.rect.y

    @x.setter
    def x(self, new_x):
        '''
        Sets the x coordinate of the upper left corner of the image rect
        to the provided new_x
        '''
        self.rect.x = new_x

    @y.setter
    def y(self, new_y):
        '''
        Sets the y coordinate of the upper left corner of the image rect
        to the provided new_y
        '''
        self.rect.y = new_y

    # Flip along each axis - true or false value
    @property
    def flip_x(self):
        '''
        Returns the value of the flip_x setting
        '''
        return self.__flip_x

    @property
    def flip_y(self):
        '''
        Returns the value of the flip_y setting
        '''
        return self.__flip_y

    @flip_x.setter
    def flip_x(self, new_flip_x):
        '''
        Sets the value of the flip_x setting to the provided new_flip_x
        '''
        self.__flip_x = new_flip_x

    @flip_y.setter
    def flip_y(self, new_flip_y):
        '''
        Sets the value of the flip_y setting to the provided new_flip_y
        '''
        self.__flip_y = new_flip_y

    # Scale the image larger or smaller
    @property
    def scale(self):
        '''
        Returns the scale at which we display the image
        '''
        return self.__scale

    @scale.setter
    def scale(self, new_scale):
        '''
        Sets the scale at which we display the image
        '''
        self.__scale = new_scale

    # Angle to which the image should be rotated
    @property
    def angle(self):
        '''
        Returns the angle at which we display the image
        '''
        return self.__angle

    @angle.setter
    def angle(self, new_angle):
        '''
        Sets the angle at which we display the image
        '''
        self.__angle = new_angle

    # Has this sprite been destroyed?
    # Set by the destroy() function
    @property
    def destroyed(self):
        '''
        Returns the value of the __destroyed setting
        '''
        return self.__destroyed

    def __init__(self, image, xpos, ypos):
        '''
        Initializes the Sprite object by:
        - setting the image to either
          - a specific image as a String or
          - an ImageSheet object,
        - the X and Y coordinate of the upper left corner of the image

        It also sets the following items to default values:
        - flip_x and flip_y to False
        - scale to 1.0
        - angle to 0
        '''
        # Call the super init first
        pygame.sprite.Sprite.__init__(self)

        self.image_list = []
        self.__image_list = []

        # Were we given a single image, or an object?
        if type(image) is str:
            # Single image - load it into our image list
            # Load the image we're given,set transparency, and get the bounding rectangle
            self.image_list.append(pygame.image.load(image).convert_alpha())
            self.__image_list.append(pygame.image.load(image).convert_alpha())

        elif type(image) is imagesheet.ImageSheet:
            # We were given an ImageSheet, so we can use that instead
            self.image_list = list(image.sprite_list)
            self.current_sprite = 0
            self.__image_list = list(image.sprite_list)
            self.__current_cell = 0

        self.rect = self.image_list[0].get_rect()
        self.image_list[0].set_colorkey(WHITE)
        self.rect = self.__image_list[0].get_rect()
        self.__image_list[0].set_colorkey(WHITE)
        self.width = self.rect.width
        self.height = self.rect.height

        # Set the position of the item
        self.rect.x = xpos
        self.rect.y = ypos
        self.position = (xpos, ypos)
        self.center = (xpos+self.width/2, ypos+self.height/2)
        # self.position = (xpos, ypos)
        # self.center = (xpos+self.width/2, ypos+self.height/2)

        self.__flip_x = False
        self.__flip_y = False

        self.__scale = 1.0
        self.__angle = 0.0

        # Add this to it's own group for rendering
        self.mygroup = pygame.sprite.GroupSingle(self)

<<<<<<< HEAD
    # Draws the sprite onto the current surface
    def draw(self):
=======
    # Draws the sprite onto the provided surface
    def draw(self):
        '''
        Draw the current sprite at it's current location
        Scale and rotate as necessary
        '''
>>>>>>> c9f2863386223ea03eafe4550548c36d9e4f29cd
        # If it's a single image, grab it.  Else, grab the next one in line
        if len(self.image_list) == 1:
            self.image = self.image_list[0]
        if len(self.__image_list) == 1:
            self.image = self.__image_list[0]
        else:
            self.image = self.image_list[self.current_sprite]
            self.image = self.__image_list[self.__current_cell]

        # Flip if necessary
        self.image = pygame.transform.flip(self.image, self.__flip_x, self.__flip_y)

        # Rotate and scale
        self.image = pygame.transform.rotozoom(
            self.image, self.__angle, self.__scale)
        # TODO: Rotation looks wierd, might want to try something different

        # Draw it
        self.mygroup.draw(pygame.display.get_surface())

    def update(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self.image_list):
            self.current_sprite = 0
        self.image = self.image_list[self.current_sprite]
        self.__current_cell += 1
        if self.__current_cell >= len(self.image_list):
            self.__current_cell = 0
        self.image = self.image_list[self.__current_cell]
