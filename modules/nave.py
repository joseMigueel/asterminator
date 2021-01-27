import pygame

class Nave():

    def __init__(self,position):

        self.sheet = pygame.image.load('img/nave.png')

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.rect = self.image.get_rect()
        