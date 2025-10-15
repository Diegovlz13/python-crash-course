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
        
    
class Admin(Usuario):
    """Clase que representa un administrador."""
    
    def __init__(self, nombre, apellido, edad, correo):
        super().__init__(nombre, apellido, edad, correo)
        self.privilegios = Privilegios()
        
            
class Privilegios:
    """Simula los privilegios de un admistrador."""
    
    def __init__(self):
        """Inicializa los atributos de la clase."""
        self.privilegios = ['puede añadir comentario', 'puede borrar comentario', 'puede vetar usuarios']
        
    def show_privileges(self):
        """Muestra los privilegios que tiene un administrador."""
        print("Privilegios disponibles para un admin:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}.")
        

admin = Admin('diego', 'velazquez', 22, 'iseare13@gmail.com')
admin.privilegios.show_privileges()