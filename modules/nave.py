import pygame

class Nave():

    def __init__(self,position):

        self.sheet = pygame.image.load('img/nave.png')

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.ban = True
        self.respuesta = 0
        self.misil = pygame.image.load('img/misil.png')
        self.misilimage = self.misil.subsurface(self.misil.get_clip())
        self.misilrect = self.misilimage.get_rect()

    def disparar(self):
        self.respuesta = self.rect
    
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
            if event.type == pygame.K_SPACE:
                self.ban = True
                self.respuesta = 0
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
            if event.key == pygame.K_SPACE:
                self.ban = True
                self.disparar()

        return(self.respuesta)