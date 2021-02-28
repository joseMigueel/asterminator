import pygame 
import sys
from modules import nave
from modules import asteroide
from modules import juego
from modules import planeta
import random




fps = 15
grados = 0
cantidad = 5
arrgobj = []
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
