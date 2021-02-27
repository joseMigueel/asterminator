import pygame 
import sys
from modules import nave
from modules import asteroide
from modules import base_de_datos
import random
import pygame_menu

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
background2 = pygame.image.load('img//background_espacio.jpg').convert()
objnave = nave.Nave(position =(0,pantalla_y//2-25),border_limits=size)
objasteroide = asteroide.Asteroide((pantalla_x - 80,0))
cantidad = 5
arrgobj = []
ban = False
puntos = 5
vidas = 3
color_blanco = (255,255,255)
font = pygame.font.Font(None,30)
screen_rect = screen.get_rect()
#pygame.mixer.music.load('music/background.ogg')
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(.3)
sonido_inicio = pygame.mixer.Sound('music/background.ogg')
sonido_perdiste = pygame.mixer.Sound('music/perdiste.ogg')
sonido_colision = pygame.mixer.Sound('music/explosion.ogg')



def set_dificultad(value, dificultad):
    pass

def start_game():
    pygame.init()
    pantalla_x = 600
    pantalla_y = 400
    clock = pygame.time.Clock()
    fps = 15
    grados = 0
    pygame.display.set_caption('ASTERMINATOR')
    size =(pantalla_x,pantalla_y)   
    bscreen = pygame.display.set_mode(size)
    background = pygame.image.load('img//background_tierra.jpg').convert()
    background2 = pygame.image.load('img//background_espacio.jpg').convert()
    objnave = nave.Nave(position =(0,pantalla_y//2-25),border_limits=size)
    objasteroide = asteroide.Asteroide((pantalla_x - 80,0))
    cantidad = 5
    arrgobj = []
    ban = False
    puntos = 5
    vidas = 3
    color_blanco = (255,255,255)
    font = pygame.font.Font(None,30)
    screen_rect = screen.get_rect()
    #pygame.mixer.music.load('music/background.ogg')
    #pygame.mixer.music.play(-1)
    #pygame.mixer.music.set_volume(.3)
    sonido_inicio = pygame.mixer.Sound('music/background.ogg')
    sonido_perdiste = pygame.mixer.Sound('music/perdiste.ogg')
    sonido_colision = pygame.mixer.Sound('music/explosion.ogg')
    proceso_principal(0,3,5,0,False,15)


tema = pygame_menu.themes.THEME_GREEN
tema.widget_font = pygame_menu.font.FONT_8BIT

menu = pygame_menu.Menu(300,600,'jugador: '+str(puntos)+" pt",theme=tema)
menu.add_text_input('Cambiar nombre: ',default='')
menu.add_button('reiniciar',start_game)
menu.add_button('salir',pygame_menu.events.EXIT)



def proceso_principal(cantidad,vidas,puntos,grados,ban,fps):


    


    for x in range(cantidad):
        objasteroide = asteroide.Asteroide((pantalla_x - 80,random.randint(1,300)))
        arrgobj.append(objasteroide)

    sonido_inicio.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                db = base_de_datos.DB()
                print('INSERT INTO puntuacion(puntuacion, fecha)VALUES(1,now())')
                #self.cur.execute('create table puntuaciones(id,puntos,nombre)')
                datos = (puntos, 'jugador1')
                db.insert_score(datos)
                vidas = 3
                puntos = 0
                sonido_perdiste.stop()
                sonido_inicio.play()
                for x in arrgobj:
                    x.rect.x -= pantalla_x - 80
            

                surface = pygame.display.set_mode((600,400))





            

        rectangulo = objnave.manejador_eventos(event)

        if puntos > 25: 
            screen.blit(background2,[0,0])
        else:
            screen.blit(background,[0,0])

        if puntos > 100:
            objnave.rect.x += 3
            arrgobj.clear()

        
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
                    sonido_colision.play()
                    
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
            texto_final = font.render('GAME OVER  puntos:'+str(puntos)+'\n Si desea seguir jugando haga click:',True,color_blanco) 
            objnave.reiniciar()
            texto_final_rect = texto_final.get_rect()
            texto_final_rect.center = screen_rect.center
            screen.blit(texto_final,texto_final_rect)
            sonido_perdiste.set_volume(.1)
            sonido_perdiste.play(loops= 1)
            sonido_inicio.stop()
            #menu.mainloop(screen)
            
        #screen.blit(objasteroide.image,objasteroide.rect)
        #objasteroide.rotar()
        pygame.display.flip()
        clock.tick(fps)