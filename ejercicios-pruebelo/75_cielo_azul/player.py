import pygame

class Mario:
    """Una clase para gestionar el personaje Mario."""
    
    def __init__(self, ai_game):
        """Inicializa el personaje y configura su posición inicial."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/mario.bmp')
        self.rect = self.image.get_rect()
        
        # Coloca inicialmente cada nave nueva en el crentro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)