# Creando y mostrando 1_000_000 de numeros 1, 2, 3, ..., 1_000_000
numbers = list(range(1, 1_000_001))
#for number in numbers:
#    print(number)
    
# Calculando el minimo y el maximo
print("El menor es:", min(numbers))
print("El mayor es:", max(numbers))

# Sumando todos los valores
print("La suma total de cada numero es:", sum(numbers))

# Imprimiendo los tres primeros elementos
print("Estos son los tres primeros elementos de la lista:", numbers[:3])
print("Estos son los tres ultimos elementos de la lista:", numbers[-3:])

