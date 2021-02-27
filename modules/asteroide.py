import pygame
from random import randrange 

class Asteroide():

    def __init__(self,position):
        self.sheet = pygame.image.load('img/asteroide.png')
        self.imageaux = self.sheet.subsurface(self.sheet.get_clip())
        bandera = randrange(10) 
        if bandera % 2:
            #self.sheet = self.imageauxiliar
            self.image = self.imageaux
            #self.imagemin = pygame.transform.scale(self.image,(40,40) )
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.grados = 0
        else: 
            #self.sheet = pygame.transform.scale(self.image,(40,40) 
            self.image = pygame.transform.scale(self.imageaux,(40,40) )
            #self.imagemin = pygame.transform.scale(self.image,(40,40) )
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.grados = 0
    def rotar(self):

        rotar = pygame.transform.rotate(self.sheet,self.grados)
        rect = rotar.get_rect()
        self.rect.center = rect.center 
        self.grados += 5
        if self.grados > 360:
            self.grados = 0