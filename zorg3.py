import pygame
import os

white = (255, 255, 255)
# I'm going to start using classes in examples
# so that Frost won't yell at me.
class Zorg(object):  # represents Zorg,
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load("zorg.png")
        # the zorgs's position
        self.x = 0
        self.y = 0

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1 # Make this number larger to see Zorg hustle
        if key[pygame.K_DOWN]: # down key
            self.y += dist # move down by our "dist" multiplier
        elif key[pygame.K_UP]: # up key
            self.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.x -= dist # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit Zorg at his current position
        surface.blit(self.image, (self.x, self.y))


pygame.init()
screen = pygame.display.set_mode((640, 400))

zorg = Zorg() # create an instance
clock = pygame.time.Clock()

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    zorg.handle_keys() # handle the keys

    screen.fill(white) # fill the screen with white after EVERY draw
    zorg.draw(screen) # draw Zorg, this isn't rocket science
    pygame.display.flip() # show the user everything we drew

    clock.tick(60)
