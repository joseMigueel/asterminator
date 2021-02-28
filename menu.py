import pygame
import pygame_menu
from modules import base_de_datos
import random


def start_game():
    from modules import nave, asteroide, juego, planeta

    fps = 15
    grados = 0
    cantidad = 5
    ban = False
    puntos = 0
    vidas = 3
    nivel = 1

    juego.proceso_principal(cantidad=cantidad,
                            vidas=vidas,
                            grados=grados,
                            puntos=puntos,
                            ban=ban,
                            fps=fps,
                            nivel=1)


def show_scores():
    # Desplegamos el menu
    surface = pygame.display.set_mode((600,300))
    tema = pygame_menu.themes.THEME_GREEN
    tema.widget_font = pygame_menu.font.FONT_8BIT
    menu = pygame_menu.Menu(300,600,'Puntuaciones',theme=tema)
    
    # Obtenemos puntuaciones de la base de datos
    db = base_de_datos.DB()
    db.cur.execute('SELECT * from puntuaciones')
    rows = db.cur.fetchall()
    
    # Iteramos sobre las puntuaciones y las mostramos en el menu
    for row in rows:
        print(row)
        menu.add_label(str(row[1])+"pt "+ str(row[2]))

    menu.add_button('Regresar', deploy_menu)
    # Ejecutamos el menu
    menu.mainloop(surface)



def deploy_menu():

    pygame.init()
    surface = pygame.display.set_mode((600,300))
    tema = pygame_menu.themes.THEME_GREEN
    tema.widget_font = pygame_menu.font.FONT_8BIT

    menu = pygame_menu.Menu(300,600,'Asterminator',theme=tema)
    menu.add_text_input('nombre ',default='aaa', maxchar=3)
    menu.add_button("ver puntuacion", show_scores)
    menu.add_button('inicio', start_game)
    menu.add_button('salir', pygame_menu.events.EXIT)
    menu.mainloop(surface)


if __name__ == "__main__":
    deploy_menu()
