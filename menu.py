import pygame
import pygame_menu

pygame.init()

surface = pygame.display.set_mode((600,300))


def start_game():
    import main


def set_dificultad(value, dificultad):
    pass

tema = pygame_menu.themes.THEME_GREEN
tema.widget_font = pygame_menu.font.FONT_8BIT

menu = pygame_menu.Menu(300,600,'Asterminator',theme=tema)
menu.add_text_input('nombre: ',default='')

menu.add_selector('dificultad: ',[('Dificil',1),('Facil',2)], onchange=set_dificultad )
menu.add_button('inicio',start_game)
menu.add_button('salir',pygame_menu.events.EXIT)
menu.mainloop(surface)