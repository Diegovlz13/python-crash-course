# Ordenar lista de forma permanente sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Ordenar de forma inversa reverse = True
cars.sort(reverse=True)
print(cars)

# Ordenar de forma temporal con la función sorted()
print("Here is the original list:")
print(cars)
print("Here is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse=True)) # Tambien acepta el orden inverso

# Invertir una lista sin ordenar, de forma permanente
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Lista original:")
print(cars)
print("Lista invertida:")
cars.reverse()
print(cars)

# Contar los elementos de una lista
longitud = len(cars)
print(f"La lista cars tiene {longitud} elementos")






