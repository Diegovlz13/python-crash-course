import sys
import pygame

from settings import Settings
from estrella import Estrella
from random import randint

class Cielo:
    """Clase general para gestionar los recursos y comportamientos de un cielo."""
    
    def __init__(self):
        """Inicializa el cielo y crea recursos."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Cielo Estrellado")
        
        self.estrellas = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_sky(self):
        """Inicializa el bucle principal para el cielo."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
    def _update_screen(self):
        """Actualiza las imagenes en la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        self.estrellas.draw(self.screen)
        
        pygame.display.flip()
        
    def _create_fleet(self):
        """Crea la flota de estrellas."""
        estrella = Estrella(self)
        
        i = 0
        while i < 100:
            current_x = randint(0, self.settings.screen_width)
            current_y = randint(0, self.settings.screen_height)
            self._create_estrella(current_x, current_y)
            i += 1
            
    def _create_estrella(self, x_position, y_position):
        """Crea una estrella y la coloca en la fila."""
        new_estrella = Estrella(self)
        new_estrella.x = x_position
        new_estrella.rect.x = x_position
        new_estrella.rect.y = y_position
        self.estrellas.add(new_estrella)
        
        
if __name__ == '__main__':
    # Hace una instancia del cielo y lo ejecuta
    ce = Cielo()
    ce.run_sky()