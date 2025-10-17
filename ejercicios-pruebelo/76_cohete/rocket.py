import pygame

class Rocket:
    """Una clase para gestionar el cohete."""
    
    def __init__(self, space_game):
        """Inicializa el cohete y configura su posición inicial."""
        self.screen = space_game.screen
        self.settings = space_game.settings
        self.screen_rect = space_game.screen.get_rect()
        
        # Carga la imagen del cohete y obtiene su rect
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        
        # Coloca inicialmente cada cohete nuevo en el centro de la pantalla
        self.rect.center = self.screen_rect.center
        
        # Banderas de movimiento; empiezan con una bandera que no se mueve
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        # Guarda un valor decimal para la posición horizontal y vertical exacta del cohete
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        """Actualiza la posición de la nave en función de la bandera de moviento."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        elif self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
            
        # Actualiza los objetos rect self.x y self.y
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Dibuja la nave en su ubicación actual."""
        self.screen.blit(self.image, self.rect)