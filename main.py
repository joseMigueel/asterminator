import pygame 
import sys
from modules import nave
from modules import asteroide
from modules import juego
import random

pygame.init()


fps = 15
grados = 0
cantidad = 5
arrgobj = []
ban = False
puntos = 5
vidas = 3

juego.proceso_principal(cantidad=cantidad,
                        vidas=vidas,
                        grados=grados,
                        puntos=puntos,
                        ban=ban,
                        fps=fps)