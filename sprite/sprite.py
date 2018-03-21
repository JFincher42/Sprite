import pygame

from sprite import imagesheet

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

    R/W Fields:
      __image_list      - list of images in the sprite
                          a single image is in __image_list[0]
      __current_cell    - which image are we displaying?

      center            - center of the image rect as a tuple
                          includes center_x and center_y
      x,y               - x and y coordinates of the upper left corner
                          of the image rect
      __flip_x,         - do we flip the image on the X...
      __flip_y            or the Y axis?  Uses pygame.transform
      __angle           - to what angle do we rotate the image?
      __scale           - do we scale the image up?

    R/O Fields:
      __destroyed       - have we destroyed this sprite?

    Internal fields:
      __last_update     - when did we last update the sprite?

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
        return self.rect.center

    @center.setter
    def center(self, new_center):
        '''
        Sets the sprites location so the center aligns with the provided new_center tuple.
        '''
        self.rect.center = new_center

    @property
    def center_x(self):
        '''
        Returns the center_x property from the image rect
        '''
        return self.rect.centerx

    @property
    def center_y(self):
        '''
        Returns the center_y property from the image rect
        '''
        return self.rect.centery

    @center_x.setter
    def center_x(self, new_center_x):
        '''
        Sets the center_x property of the image rect to the provided new_center_x
        '''
        self.rect.centerx = new_center_x

    @center_y.setter
    def center_y(self, new_center_y):
        '''
        Sets the center_y property of the image rect to the provided new_center_y
        '''
        self.rect.centery = new_center_y

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

        # Change the bounding rectangle as well
        self.rect.width = self.__orig_rect.width * new_scale
        self.rect.height = self.__orig_rect.height * new_scale
        #TODO: Update the __image_list and self.rect fields when the scale is updated
        #TODO: Can we do this multiple times?

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
        # TODO: When setting the angle, apply it to every image
        # TODO: Can we do this multiple times?

    @property
    def image_animation_rate(self):
        '''
        Returns the current image animation rate
        '''
        return self.__image_animation_rate

    @image_animation_rate.setter
    def image_animation_rate(self, new_iar):
        self.__image_animation_rate = new_iar

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, new_visible):
        self.__visible = new_visible

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
        - visible to True
        - destroyed to False
        '''
        # Call the super init first
        pygame.sprite.Sprite.__init__(self)

        # Setup the time
        self.__last_time = pygame.time.get_ticks()

        # Blank the image list
        self.__image_list = []

        # Were we given a single image, or an object?
        if type(image) is str:
            # Single image - load it into our image list
            # Load the image we're given,set transparency, and get the bounding rectangle
            self.__image_list.append(pygame.image.load(image).convert_alpha())
            self.image = self.__image_list[0]
            self.__current_cell = 0

        elif type(image) is imagesheet.ImageSheet:
            # We were given an ImageSheet, so we can use that instead
            self.__image_list = list(image.sprite_list)
            self.image = self.__image_list[0]
            self.__current_cell = 0
            self.__image_animation_rate = 30

        # Set the bounding rectangle, and the original rectangle
        # Use the original rectangle for scaling purposes
        self.rect = self.image.get_rect()
        self.__orig_rect = self.rect.copy()
        self.__image_list[0].set_colorkey(WHITE)
        #self.width = self.rect.width
        #self.height = self.rect.height

        # Set the position of the item
        self.rect.x = xpos
        self.rect.y = ypos
        # self.position = (xpos, ypos)
        # self.center = (xpos+self.width/2, ypos+self.height/2)

        self.__flip_x = False
        self.__flip_y = False

        self.__scale = 1.0
        self.__angle = 0.0
        self.__visible = True
        self.__destroyed = False

        # Add this to it's own group for rendering
        self.__mygroup = pygame.sprite.GroupSingle(self)

    # Draws the sprite onto the provided surface
    def draw(self):
        '''
        Draw the current sprite at it's current location
        Scale and rotate as necessary
        '''

        # If it's not visible, we're done
        if not self.__visible:
            return

        # If it's a single image, grab it.  Else, grab the next one in line
        if len(self.__image_list) == 1:
            self.image = self.__image_list[0]
        else:
            self.image = self.__image_list[self.__current_cell]

        # Flip if necessary
        self.image = pygame.transform.flip(
            self.image, self.__flip_x, self.__flip_y)

        # Rotate and scale
        #self.image = pygame.transform.rotozoom(
        #    self.image, self.__angle, self.__scale)
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.image = pygame.transform.rotate(self.image, self.__angle)
        #self.rect.width *= self.__scale
        #self.rect.height *= self.__scale

        #TODO: Inspect this code closely and rewrite
        '''
        width = int(self.image.get_width() * self.__scale)
        height = int(self.image.get_height() * self.__scale)
        newimage = pygame.transform.scale(self.image, (width, height))
        self.image = pygame.Surface((width, height), pygame.SRCALPHA, newimage)
        #self.image.blit(newimage, (0,0))
        self.image = pygame.transform.rotate(self.image, self.__angle)
        self.rect = self.image.get_rect()
        '''
        # TODO: Rotation looks wierd, might want to try something different

        # Draw it onto the display surface
        self.__mygroup.draw(pygame.display.get_surface())

    def update(self, ticks):
        '''
        Updates an animated sprite to the next image, using the timer provided
        Calculates the number of milliseconds to wait, and checks to see if
        that much time has passed.  If so, we change to the next image.
        Otherwise, we don't.
        param: ticks the number of milliseconds that has passed so far
        '''

        # First, if there's only one image, we're done
        if len(self.__image_list) == 1:
            return

        # Adjust the time to be aware of the animation rate set
        # Normal framerate is 30, so we need to scale ticks accordingly
        ticks /= (self.__image_animation_rate/30)
        elapsed = pygame.time.get_ticks() - self.__last_time

        # Has enough time passed?
        if elapsed > ticks:
            # Reset the timer
            self.__last_time = pygame.time.get_ticks()

            # Pick the next image, wrap around if necessary
            self.__current_cell += 1
            if self.__current_cell >= len(self.__image_list):
                self.__current_cell = 0
            self.image = self.__image_list[self.__current_cell]
