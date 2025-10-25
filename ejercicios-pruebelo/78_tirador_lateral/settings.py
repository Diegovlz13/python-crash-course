class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""
    
    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # Gris claro
        
        # Configuración de la nave
        self.ship_speed = 3.5
        
        # Configuración de las balas
        self.bullet_speed = 4.0
        self.bullet_width = 15
        self.bullet_height = 6
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Configuraciones de alien
        # Frecuencia con la que aparece un alien
        self.alien_frequency = 0.008 # Max = 1.0
        self.alien_speed = 1.5