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
        
# Instancia de la clase restaurante
restaurante = Restaurante('QUIN', 'comida china')
print(restaurante.numero_servido)

# Estableciendo un valor
restaurante.establecer_numero_servido(10)
print(restaurante.numero_servido)

# Incrementando ese valor en 5 
restaurante.incrementar_numero_servido(5)
print(restaurante.numero_servido)
