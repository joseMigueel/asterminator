import pygame

class Music():

    def __intit__(self):
        self.fondo = 'music/background.ogg'
        self.rotate = 'music/jump.ogg'

    def disparar(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.disparar)
        pygame.mixer.music.play(1)

    def inicio (self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.inicio)
        pygame.mixer.music.set_volume(.3)
        pygame.mixer.music.play()