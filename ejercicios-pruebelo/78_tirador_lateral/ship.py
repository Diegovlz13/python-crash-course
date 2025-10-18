import pygame

class Ship:
    """Una clase para gestionar la nave."""
    
    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, -90) # Gira la imagen 90 grados a la derecha
        self.rect = self.image.get_rect()
        
        # Coloca inicialmente cada nave nueva en el centro de la parte izquierda de la pantalla
        self.rect.midleft = self.screen_rect.midleft
        
        # Banderas de movimiento; empiezan con una bandera que no se mueve
        self.moving_up = False
        self.moving_down = False
        
        # Guarda un valor decimal para la posición vertical exacta de la nave
        self.y = float(self.rect.y)
        
        
    def update(self):
        """Actualiza la posición de la nave en función de las banderas de movimiento."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Actualiza la posición del rect
        self.rect.y = self.y
        
    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)