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
puntos = 5
vidas = 3
color_blanco = (255,255,255)
font = pygame.font.Font(None,30)
screen_rect = screen.get_rect()

for x in range(cantidad):
    objasteroide = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
    arrgobj.append(objasteroide)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    rectangulo = objnave.manejador_eventos(event)

    screen.blit(background,[0,0])
    
    if vidas > 0:
        screen.blit(objnave.image,objnave.rect)
        texto_marcador = font.render('Vidas:'+str(vidas)+' Puntos:'+str(puntos),True,color_blanco)
        texto_marcador_rect = texto_marcador.get_rect()
        texto_marcador_rect.center = screen_rect.center
        text_x = texto_marcador_rect[0]
        print(texto_marcador_rect)
        screen.blit(texto_marcador,[text_x,0,176,21])
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

        for x in arrgobj:
            if objnave.rect.colliderect(x.rect):
                x.rect.x -= pantalla_x - 80
                screen.blit(objnave.bumimage,objnave.rect)
                vidas -= 1 
                print(vidas)

        if ban:
            screen.blit(objnave.misilimage,objnave.misilrect)
            objnave.misilrect.x += 10
            for x in arrgobj:
                if objnave.misilrect.colliderect(x.rect):
                    arrgobj.remove(x)
                    objnave.misilrect.x = pantalla_x + 10
                    puntos += 5
                    obj = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
                    arrgobj.append(obj)
                    fps += 1
        if rectangulo != 0:
            objnave.misilrect.center = rectangulo.center
            ban = True
    else:
        texto_final = font.render('GAME OVER  puntos:'+str(puntos),True,color_blanco)
        texto_final_rect = texto_final.get_rect()
        texto_final_rect.center = screen_rect.center
        screen.blit(texto_final,texto_final_rect)

    #screen.blit(objasteroide.image,objasteroide.rect)
    #objasteroide.rotar()
    pygame.display.flip()
    clock.tick(fps)