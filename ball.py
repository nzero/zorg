import sys, pygame
pygame.init()

size = width, height = 600, 595
vector = [2, 2]
red = 250, 0, 0

screen = pygame.display.set_mode(size)

zorg = pygame.image.load("zorg.png")
zorgrect = zorg.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    zorgrect = zorgrect.move(vector)
    if zorgrect.left < 0 or zorgrect.right > width:
        vector[0] = -vector[0]
    if zorgrect.top < 0 or zorgrect.bottom > height:
        vector[1] = -vector[1]

    screen.fill(red)
    screen.blit(zorg, zorgrect)
    pygame.display.flip()
