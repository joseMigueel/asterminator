import pygame
from random import randrange 

class Planeta:

    def __init__(self,position):
        self.sheet = pygame.image.load('img//planeta3.png')
        #self.sheet = self.imageauxiliar
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        #self.imagemin = pygame.transform.scale(self.image,(40,40) )
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.grados = 0