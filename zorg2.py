import sys, pygame
pygame.init()

size = width, height = 600, 595
vector = [0, 1]
red = 250, 0, 0

screen = pygame.display.set_mode(size)

zorg = pygame.image.load("zorg.png")
zorgrect = zorg.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

	zorgrect = zorgrect.move(vector)
	if zorgrect.bottom > height: #check to see if the bottom of Zorg is > the screen height
		vector[1] = -vector[1]  #remember how we flipped strings. let's do that with his
								#Y-axis position.  Should turn him around.
    

    screen.fill(red)
    screen.blit(zorg, zorgrect)
    pygame.display.flip()
