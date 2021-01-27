import pygame 
import sys
from modules import nave
from modules import asteroide

pygame.init()
pantalla_x = 600
pantalla_y = 400
pygame.display.set_caption('ASTERMINATOR')
size =(pantalla_x,pantalla_y)
screen = pygame.display.set_mode(size)

background = pygame.image.load('img//background_tierra.jpg').convert()
objnave = nave.Nave((pantalla_x//2,pantalla_y//2))
objasteroide = asteroide.Asteroide((pantalla_x - 80,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        objnave.manejador_eventos(event)

    screen.blit(background,[0,0])
    screen.blit(objnave.image,objnave.rect)
    screen.blit(objasteroide.image,objasteroide.rect)
    pygame.display.flip()