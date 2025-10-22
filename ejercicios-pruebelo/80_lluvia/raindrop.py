import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """Representa una sola gota de lluvia."""

    def __init__(self, ai_game):
        """Inicializa la gota y establece su posición inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Carga la imagen de la gota y obtiene su rectángulo.
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Coloca la gota cerca de la esquina superior izquierda.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Guarda posiciones exactas (float) para movimiento suave.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la gota hacia abajo y la recicla arriba cuando sale de pantalla."""
        # Avanza verticalmente con velocidad decimal para movimiento suave
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

        # Si la gota salió por la parte inferior, reaparece arriba
        if self.rect.top >= self.settings.screen_height:
            # Reaparece justo por encima del borde superior
            self.y = -self.rect.height
            self.rect.y = self.y

