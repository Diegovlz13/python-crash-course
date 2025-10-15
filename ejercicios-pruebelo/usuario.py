class Usuario:
    """clase que representa un usuario."""
    
    def __init__(self, nombre, apellido, edad, correo):
        """Inicializa los atributos de clase Usuario."""
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.intentos_inicio = 0
    
    def describir_usuario(self):
        """Muestra la información acerca del usuario."""
        print("Información acerca del usuario:")
        print(f"- Nombre completo: {self.nombre} {self.apellido}.")
        print(f"- Edad: {self.edad}.")
        print(f"- Correo: {self.correo}")
    
    def saludar_usuario(self):
        """Simula un saludo hacia el usuario."""
        print(f"Hola, {self.nombre} {self.apellido}, ¡un gusto verte por aquí de nuevo!")
        
    def incrementar_intentos_inicio(self):
        """Incrementa los inicios de sesión en 1."""
        self.intentos_inicio += 1
        
    def restablecer_intentos_inicio(self):
        """Restablece los inicios de sesión a 0."""
        self.intentos_inicio = 0