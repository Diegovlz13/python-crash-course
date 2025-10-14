class Restaurante:
    """Clase que simula un restaurante."""
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos nombre_restaurante y tipo_oficina."""
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        self.numero_servido = 0
        
    def describir_restaurante(self):
        """Muestra la información acerca del restaurante."""
        print("Información acerca del restaurante:")
        print(f"El nombre del restaurante es {self.nombre_restaurante} y el tipo de cocina es {self.tipo_cocina}.")
    
    def abrir_restaurante(self):
        """Muestra cuándo el restaurante está abierto."""
        print(f"El restaurante {self.nombre_restaurante} está abierto.")
        
    def establecer_numero_servido(self, numero):
        """Actualiza el número servido de clientes."""
        self.numero_servido = numero
        
    def incrementar_numero_servido(self, incremento):
        """Incrementa el numero de clientes servidos."""
        self.numero_servido += incremento


class CarritoDeHelados(Restaurante):
    """Simula un carrito de helados."""
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        """Inicializa los atributos de la clase base."""
        super().__init__(nombre_restaurante, tipo_cocina)
        self.sabores = ['chocolate', 'fresa', 'vainilla', 'galleta', 'chicle']
        
    def mostrar_sabores(self):
        """Muestra los sabores disponibles."""
        print(f"Sabores disponibles:")
        for sabor in self.sabores:
            print(f"- {sabor}.")
            
carito_helados = CarritoDeHelados('Helados bobo', 'heladería')
carito_helados.describir_restaurante()
carito_helados.mostrar_sabores()