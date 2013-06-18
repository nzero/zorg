import sys, pygame #we need to import our module
pygame.init() #we need to initialize our pygame
               #or it won't do stuff

size = width, height = 400, 400 #set up a screen size
red = 250, 0, 0      #tell python what color red is...it's not too bright

screen = pygame.display.set_mode(size)   #set our display up
zorg = pygame.image.load("zorg.png")    #bring in zorg from the folder
zorgrect = zorg.get_rect()    #use the rect class on zorg, because he's a rectangle

while 1:    #make a loop to handle shutting down if we just hit "close"
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        screen.fill(red)    #fill the screen with red
        screen.blit(zorg, zorgrect)   #blit zorg to our screen
        pygame.display.flip()          #display all of this to the user
