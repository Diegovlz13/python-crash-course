class Empleado:
    """Clase que simula a un empleado."""
    
    def __init__(self, nombre, apellido, salario_anual):
        """Inicializa los atributos de la clase empleado."""
        self.nombre = nombre
        self.apellido = apellido
        self.salario_anual = salario_anual
        
    def dar_aumento(self, aumento=5_000):
        """
        Incrementa el salario anual de acuerdo a lo recibido, si no recibe nada lo
        aumenta en 5000 euros.
        """
        self.salario_anual += aumento