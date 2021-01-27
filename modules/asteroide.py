import pygame

class Asteroide():

    def __init__(self,position):

        self.sheet = pygame.image.load('img/asteroide.png')
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position