"""Una clase que se puede usar para representar un coche."""

class Car:
    """Clase que intenta simular un carro."""
    
    def __init__(self, make, model, year):
        """Inicializa los atributos de clase Car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    
    def get_describe_name(self):
        """Devuelve el nombre descriptivo con un formato adecuado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """Imprime una oración con el kilometraje del carro."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Actualiza el kilometraje del carro.
        Se rechaza el cambio si disminuye en vez de aumentar el kilometraje.
        """
        if self.odometer_reading < mileage:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Añade la cantidad de millas a la lectura del kilometraje."""
        self.odometer_reading += miles
