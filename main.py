import pygame 
import sys
from modules import nave
from modules import asteroide

pygame.init()
pantalla_x = 600
pantalla_y = 400
clock = pygame.time.Clock()
fps = 15
grados = 0
pygame.display.set_caption('ASTERMINATOR')
size =(pantalla_x,pantalla_y)
screen = pygame.display.set_mode(size)

background = pygame.image.load('img//background_tierra.jpg').convert()
objnave = nave.Nave((0,pantalla_y//2-25))
objasteroide = asteroide.Asteroide((pantalla_x - 80,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        objnave.manejador_eventos(event)

    screen.blit(background,[0,0])
    screen.blit(objnave.image,objnave.rect)
    rotar = pygame.transform.rotate(objasteroide.image,grados)
    grados += 5
    if grados > 360:
        grados = 0
    screen.blit(rotar,objasteroide.rect)
    #screen.blit(objasteroide.image,objasteroide.rect)
    #objasteroide.rotar()
    pygame.display.flip()
    clock.tick(fps)