import sys
import pygame

class Teclas:
    """Clase general para probar los eventos pygame."""
    
    def __init__(self):
        """Inicializa la clase y crea recursos."""
        pygame.init()
        self.bg_color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Prueba teclas")
        
    def run_test(self):
        """Inicializa el bucle principal para la prueba."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
    def _check_keydown_events(self, event):
        """Responde a las pulsaciones de teclas."""
        if event.key == pygame.K_RIGHT:
            print("Se presiono la flecha derecha.")
        elif event.key == pygame.K_LEFT:
            print("Se presiono la flecha izquierda.")
        if event.key == pygame.K_UP:
            print("Se presiono la flecha hacia arriba.")
        elif event.key == pygame.K_DOWN:
            print("Se presiono la flecha hacia abajo.")
        elif event.key == pygame.K_q:
            print("Se presiono 'q' que indicar salir.")
            sys.exit()
                
    def _update_screen(self):
        """Actualiza la pantalla nueva."""
        self.screen.fill(self.bg_color)
        pygame.display.flip()
        
        
if __name__ == '__main__':
    # Hace una instancia de la prueba y la ejecuta
    t = Teclas()
    t.run_test()