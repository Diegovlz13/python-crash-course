motocycles = ["honda", "yamaha", "suzuki"]
print(motocycles)

# Modificando el primer elemento
motocycles[0] = "ducati"
print(motocycles)

# Añadiendo de nuevo, pero al final, honda
motocycles.append("honda")
print(motocycles)

# Añadiendo mas elementos con append()
motocycles.append("italica")
motocycles.append("vento")
motocycles.append("kawazaki")
print(motocycles)

# Insertando un elemento en una posicion especifica
motocycles.insert(0, "bmw")
print(motocycles)

# Eliminando un elemento especifico 
del motocycles[0]
print(motocycles)

# Eliminar el ultimo elemento de la lista (pila)
last_owned = motocycles.pop() # Lo puedo guardar y trabajar con el
print(motocycles)
print(f"The last motorcycle I owned was a {last_owned.title()}")

# pop() tambien sirve para obtener un elemento de una posicion especifica
first_owned = motocycles.pop(0)
print(motocycles)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Eliminar por valor cuando no sabemos el indice
motocycles.remove("italica")
print(motocycles)