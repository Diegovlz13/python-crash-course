class Dog:
    """Un simple intento de modelar un perro."""
    
    def __init__(self, name, age):
        """Inicializa los atributos de nombre y edad."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simula un perro sentándose en respuesta a una orden."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simular hacer la croqueta en respuesta a una orden."""
        print(f"{self.name} rolled over!")
        
my_dog = Dog('Africa', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()