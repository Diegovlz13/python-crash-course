class Car:
    """Clase que intenta simular un carro."""
    
    def __init__(self, make, model, year):
        """Inicializa los atributos de clase base."""
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
        
    def fill_gas_tank(self):
        """Imprime una frase mencionando que se esta llenando el tanque de gas."""
        print("Se ha llenado el tanque de gas.")
    

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

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_describe_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
