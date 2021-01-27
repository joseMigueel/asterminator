import pygame

class Nave():

    def __init__(self,position):

        self.sheet = pygame.image.load('img/nave.png')

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.rect = self.image.get_rect()
    
    def update(self,direccion):
        if direccion == 'left':
            self.rect.x -= 5
        if direccion == 'right':
            self.rect.x += 5
        if direccion == 'up':
            self.rect.y -= 5
        if direccion == 'down':
            self.rect.y += 5
        self.image == self.sheet.subsurface(self.sheet.get_clip())
    
    def manejador_eventos(self, event):
        if event.type == pygame.KEYUP:
            pass

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')