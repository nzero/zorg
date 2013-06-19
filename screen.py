#!/usr/bin env python

#Creating a screen
import sys, pygame
pygame.init()

size = width, height = 600, 500

screen = pygame.display.set_mode(size)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
