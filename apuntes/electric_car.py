"""Un conjunto de clases que sirven para representar coches eléctricos."""

from car import Car

class ElectricCar(Car):
    """Representa aspectos de un coche propios de los vehículos eléctricos."""
    
    def __init__(self, make, model, year):
        """Inicializa los atributos de la clase base."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def fill_gas_tank(self):
        """Los coches eléctricos no tienen depósito de combustible."""
        print("This car doesn't need a gas tank!")
        

class Battery:
    """Un simple intento de modelar una bateria para un coche eléctrico."""
    
    def __init__(self, battery_size=75):
        """Inicializa los atributos de la batería."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Imprime una frase que describe el tamaño de la bateria."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Imprime una frase sobre la autonomía que ofrece esta batería."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        """Establece la capacidad en 100 si no esta ya así."""
        if self.battery_size != 100:
            self.battery_size = 100