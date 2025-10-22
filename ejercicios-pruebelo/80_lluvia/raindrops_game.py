import sys
import pygame

from settings import Settings
from raindrop import Raindrop

class RaindropsGame:
    """Gestiona los recursos y el comportamiento del juego de lluvia."""

    def __init__(self):
        """Inicializa el juego y crea los recursos."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Crea la ventana según la configuración.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Lluvia de gotas")

        # Grupo de gotas.
        self.raindrops = pygame.sprite.Group()

        # Crea la cuadrícula de gotas.
        self._create_drops()

    def run_game(self):
        """Inicia el bucle principal del juego."""
        while True:
            self._check_events()
            self.raindrops.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responde a eventos del sistema y del teclado."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Responde a las teclas presionadas."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        """Crea un ‘cielo’ lleno de gotas con separación uniforme."""
        # Gota de referencia para medir ancho/alto.
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        # Empezamos con un margen de 1 gota y separamos 1 gota entre cada una.
        current_x, current_y = drop_width, drop_height
        while current_y < (self.settings.screen_height - 2 * drop_height):
            while current_x < (self.settings.screen_width - 2 * drop_width):
                self._create_drop(current_x, current_y)
                current_x += 2 * drop_width
            # Fila terminada; reinicia X y baja a la siguiente fila.
            current_x = drop_width
            current_y += 2 * drop_height

    def _create_drop(self, x_position, y_position):
        """Crea una gota y la coloca en la cuadrícula."""
        new_drop = Raindrop(self)
        new_drop.rect.x = x_position
        new_drop.rect.y = y_position
        # Mantén sincronizada la coordenada flotante para el movimiento.
        new_drop.y = float(y_position)
        self.raindrops.add(new_drop)

    def _update_screen(self):
        """Dibuja todo y actualiza la pantalla."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    juego = RaindropsGame()
    juego.run_game()
