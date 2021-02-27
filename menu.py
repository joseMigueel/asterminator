import pygame
import pygame_menu
from modules import base_de_datos

pygame.init()

surface = pygame.display.set_mode((600,300))


def start_game():
    db = base_de_datos.DB()
    db.insert_score((100,"jose"))
    import main


def set_dificultad(value, dificultad):
    pass

def start_p():
    import puntos
    

tema = pygame_menu.themes.THEME_GREEN
tema.widget_font = pygame_menu.font.FONT_8BIT

menu = pygame_menu.Menu(300,600,'Asterminator',theme=tema)
menu.add_text_input('nombre: ',default='')
menu.add_button("ver puntuacion",start_p)
menu.add_button('inicio',start_game)
menu.add_button('salir',pygame_menu.events.EXIT)
menu.mainloop(surface)