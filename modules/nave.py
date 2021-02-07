import pygame

class Nave():

    def __init__(self,position,border_limits):

        self.limit_x,self.limit_y = border_limits
        self.nave_size_x,self.nave_size_y = 90, 51
        self.sheet = pygame.image.load('img/nave.png')

        self.image = self.sheet.subsurface(self.sheet.get_clip())

        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.ban = True
        self.respuesta = 0
        self.misil = pygame.image.load('img/misil.png')
        self.misilimage = self.misil.subsurface(self.misil.get_clip())
        self.misilrect = self.misilimage.get_rect()
        self.sheetbum = pygame.image.load('img/bum.png')
        self.bumimage = self.sheetbum.subsurface(self.sheetbum.get_clip())
        self.bumrect = self.bumimage.get_rect()

    def disparar(self):
        self.respuesta = self.rect
    
    def update(self,direccion):
        if (direccion == 'left') and (self.rect.x > 0): 
            self.rect.x -= 5
        if (direccion == 'right') and (self.rect.x < (self.limit_x- self.nave_size_x)):
            self.rect.x += 5
        if (direccion == 'up') and (self.rect.y > 0):
            self.rect.y -= 5
        if (direccion == 'down') and (self.rect.y < (self.limit_y - self.nave_size_y)):
            self.rect.y += 5
            
        self.image == self.sheet.subsurface(self.sheet.get_clip())
        print('Nave position:')
        print(self.rect.x,self.rect.y)

    def manejador_eventos(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.ban = False
                self.respuesta = 0
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                self.update('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                self.update('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                self.update('up')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                self.update('down')
            if event.key == pygame.K_SPACE:
                self.ban = True
                self.disparar()

        return(self.respuesta)