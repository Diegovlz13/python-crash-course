import sys
from random import random
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """Clase general para gestionar los recursos y comportamientos del juego."""
    
    def __init__(self):
        """Inicializa el juego y crea recursos."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
    def run_game(self):
        """Inicializa el bucle principal para el juego."""
        while True:
            self._check_events()
            self._create_alien()

            self.ship.update()
            self.bullets.update()
            self.aliens.update()  # 🔹 se agrego para mover los aliens

            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien."""
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            
    def _create_alien(self):
        """Crea un alien si la condición se cumple."""
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
                
    def _update_screen(self):
        """Actualiza las imágenes en la pantalla."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)  # 🔹 asegura que los aliens se dibujen

        pygame.display.flip()
        

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
