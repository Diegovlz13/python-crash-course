dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Las tuplas son inmutables
#dimensions[0] = 150

# Recorriendo una tupla
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
# Se puede modificar todo el contenido de una tupla
dimensions = (400, 10)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
