from usuario import Usuario

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