import pygame

class Asteroide():

    def __init__(self,position):

        self.sheet = pygame.image.load('img/asteroide.png')
        self.image = self.sheet.subsurface(self.sheet.get_clip())
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