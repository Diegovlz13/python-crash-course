import pygame
from pygame.sprite import Sprite
from random import randint

class Estrella(Sprite):
    """Una clase para representar una sola estrella en la flota."""
    
    def __init__(self, ce):
        """Inicializa la estrella y establece su posición inicial."""
        super().__init__()
        self.screen = ce.screen
        
        # Carga la imagen de la estrella y configura su atributo rect
        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()
        
        # Inicia una nueva estrella cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Guarda la posición horizontal exacta de la estrella
        self.x = float(self.rect.x)