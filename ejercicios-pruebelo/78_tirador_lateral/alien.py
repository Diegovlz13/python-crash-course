from random import randint

import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """Una clase para representar un solo alienígena en la flota."""

    def __init__(self, ss_game):
        """Inicializa el alien y establece su posición inicial."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Carga la imagen del alien y establece su atributo rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nuevo alien en una posición aleatoria en el lado derecho
        #    de la pantalla.
        self.rect.left = self.screen.get_rect().right
        # El punto más bajo en la pantalla donde colocaremos el alien es la altura
        #    de la pantalla, menos la altura del alien.
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)

        # Almacena la posición horizontal exacta del alien.
        self.x = float(self.rect.x)

    def update(self):
        """Mueve el alien constantemente hacia la izquierda."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x