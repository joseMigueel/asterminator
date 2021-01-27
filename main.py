import pygame 
import sys
import random

pygame.init()

pantalla_x = 600
pantalla_y = 400
pygame.display.set_caption('ASTERMINATOR')
size =(pantalla_x,pantalla_y)
screen = pygame.display.set_mode(size)
background = pygame.image.load('img/backgroun_espacio').convert()
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()