class Settings:
    """Una clase para guardar toda la configuración de GameSpace."""
    
    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 68, 106) # Azul
        
        # Configuración de la nave
        self.rocket_speed = 3.5