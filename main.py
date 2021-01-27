import pygame 
import sys
from modules import nave
from modules import asteroide
import random

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
cantidad = 5
arrgobj = []
ban = False
for x in range(cantidad):
    objasteroide = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
    arrgobj.append(objasteroide)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    rectangulo = objnave.manejador_eventos(event)

    screen.blit(background,[0,0])
    screen.blit(objnave.image,objnave.rect)
    for x in arrgobj:
        rotar = pygame.transform.rotate(x.image,grados)
        screen.blit(rotar,x.rect)
        grados += 5
        x.rect.x -= 5
        if x.rect.x < 0:
            x.rect.x = pantalla_x - 80
            x.rect.y = random.randint(1,300)
        if grados > 360:
            grados = 0
    if ban:
        screen.blit(objnave.misilimage,objnave.misilrect)
        objnave.misilrect.x += 10

    if rectangulo != 0:
        objnave.misilrect.center = rectangulo.center
        ban = True
    

    #screen.blit(objasteroide.image,objasteroide.rect)
    #objasteroide.rotar()
    pygame.display.flip()
    clock.tick(fps)