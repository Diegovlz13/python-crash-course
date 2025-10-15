class Settings:
    """Una clase para guardar toda la configuración de Blue Sky Game."""
    
    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255) # Blanco