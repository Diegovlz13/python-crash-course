from settings import Settings
from player import Mario

import sys
import pygame


class BlueSkyGame:
    """Clase general para gestionar los recursos y comportamientos del juego."""
    
    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky Game")
        
        self.mario = Mario(self)
        
    def run_game(self):
        """Inicializa el bucle principal para el juego."""
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
        self.mario.blitme()
        
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = BlueSkyGame()
    ai.run_game()
    