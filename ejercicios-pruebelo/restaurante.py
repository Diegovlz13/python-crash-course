"""Una clase que se puede utilizar para representar un restaurante."""

class Restaurante:
    """Clase que simula un restaurante."""
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos nombre_restaurante y tipo_oficina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        
    def describir_restaurante(self):
        """Muestra la información acerca del restaurante."""
        print("Información acerca del restaurante:")
        print(f"El nombre del restaurante es {self.nombre_restaurante} y el tipo de cocina es {self.tipo_cocina}.")
    
    def abrir_restaurante(self):
        """Muestra cuándo el restaurante está abierto."""
        print(f"El restaurante {self.nombre_restaurante} está abierto.")