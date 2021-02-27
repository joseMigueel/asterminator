import pygame
import pygame_menu
from modules import base_de_datos

pygame.init()

surface = pygame.display.set_mode((600,300))


def start_game():
    import main


def set_dificultad(value, dificultad):
    pass

def start_p():
    import puntos

def regresar ():
    import menu
    pygame_menu.events.EXIT


tema = pygame_menu.themes.THEME_GREEN
tema.widget_font = pygame_menu.font.FONT_8BIT

menu = pygame_menu.Menu(300,600,'Puntuaciones',theme=tema)
db = base_de_datos.DB()
db.cur.execute('SELECT * from puntuaciones')
rows = db.cur.fetchall()
for row in rows:
    print(row)
    menu.add_label(str(row[1])+"pt "+ str(row[2]))


menu.add_button('Regresar',regresar)

menu.mainloop(surface)