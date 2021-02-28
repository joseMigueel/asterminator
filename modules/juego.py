import pygame 
import sys
from modules import nave
from modules import asteroide
from modules import base_de_datos
from modules import planeta
import random
import pygame_menu
from menu import deploy_menu



def proceso_principal(cantidad,vidas,puntos,grados,ban,fps,nivel):

    pygame.init()
    pantalla_x = 600
    pantalla_y = 400
    clock = pygame.time.Clock()
    pygame.display.set_caption('ASTERMINATOR')
    size =(pantalla_x,pantalla_y)
    screen = pygame.display.set_mode(size)
    background = pygame.image.load('img//background_tierra.jpg').convert()
    background2 = pygame.image.load('img//background_espacio.jpg').convert()
    background3 = pygame.image.load('img//youwin.jpg').convert()
    objnave = nave.Nave(position =(0,pantalla_y//2-25),border_limits=size)
    objasteroide = asteroide.Asteroide((pantalla_x - 80,0))
    objplaneta = planeta.Planeta((600,50))
    arrgobj = []
    color_blanco = (255,255,255)
    font = pygame.font.Font(None,30)
    screen_rect = screen.get_rect()
    sonido_inicio = pygame.mixer.Sound('music/background.ogg')
    sonido_perdiste = pygame.mixer.Sound('music/perdiste.ogg')
    sonido_colision = pygame.mixer.Sound('music/explosion.ogg')

    for x in range(cantidad):
        objasteroide = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
        arrgobj.append(objasteroide)

    sonido_inicio.play()
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        
        rectangulo = objnave.manejador_eventos(event)

        if puntos > 25: 
            if nivel < 2:
                nivel += 1
            screen.blit(background2,[0,0])
            if nivel < 2:
                nivel += 1

        else:
            screen.blit(background,[0,0])

        if puntos > 100:
            objnave.rect.y = pantalla_y//2-25
            arrgobj.clear()
            screen.blit(objplaneta.image,objplaneta.rect)
            if objplaneta.rect.x > 400:
                objplaneta.rect.x -= 3
        
            if objnave.rect.x < 400:
                objnave.rect.x += 3
            else:
                objnave.rect.y = pantalla_y//2 - 75
                rotar = pygame.transform.rotate(objnave.image,objnave.grados)
                screen.blit(rotar,objnave.rect)
                if objnave.grados < 90:
                    objnave.grados += 5
                else:
                    
                    pygame.time.delay(3 * 1000) # 1 second == 1000 milliseconds
                    screen.blit(background3,[0,0])
                    pygame.display.update()
                    pygame.time.delay(3 * 1000)
                    
                    # Guardmos partida
                    db = base_de_datos.DB()
                    #print('INSERT INTO puntuacion(puntuacion, fecha)VALUES(1,now())')
                    #self.cur.execute('create table puntuaciones(id,puntos,nombre)')
                    datos = (puntos, 'jugador1')
                    db.insert_score(datos)


                    deploy_menu()
                #objnave.rotar()
        
        if vidas > 0:

            if objnave.rect.x < 400:
                screen.blit(objnave.image,objnave.rect)
            texto_marcador = font.render('Vidas:'+str(vidas)+' Puntos:'+str(puntos)+' Nivel: '+str(nivel),True,color_blanco)
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
                    puntos += 5
                if grados > 360:
                    grados = 0

            for x in arrgobj:
                if objnave.rect.colliderect(x.rect):
                    x.rect.x -= pantalla_x - 80
                    screen.blit(objnave.bumimage,objnave.rect)
                    vidas -= 1 
                    print(vidas)               
                    sonido_colision.play()
                    
            if ban:
                screen.blit(objnave.misilimage,objnave.misilrect)
                objnave.misilrect.x += 10
                for x in arrgobj:
                    if objnave.misilrect.colliderect(x.rect):
                        arrgobj.remove(x)
                        objnave.misilrect.x = pantalla_x + 10
                        puntos += 10
                        obj = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
                        arrgobj.append(obj)
                        fps += 1
            if rectangulo != 0:
                objnave.misilrect.center = rectangulo.center
                ban = True
        else:
            texto_final = font.render('GAME OVER  puntos:'+str(puntos)+'\n Si desea seguir jugando haga click:',True,color_blanco) 
            objnave.reiniciar()
            texto_final_rect = texto_final.get_rect()
            texto_final_rect.center = screen_rect.center
            screen.blit(texto_final,texto_final_rect)
            sonido_perdiste.set_volume(.1)
            sonido_perdiste.play(loops= 1)
            sonido_inicio.stop()
            pygame.event.clear()
            deploy_menu()

            #menu.mainloop(screen)
            
        #screen.blit(objasteroide.image,objasteroide.rect)
        #objasteroide.rotar()
        pygame.display.flip()
        clock.tick(fps)