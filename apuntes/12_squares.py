# ** Sirve para elevar un numero y tu le indicas la potencia
squares = []
for square in range(1, 11):
    squares.append(square ** 2)
    
print(squares)

# Listas por comprension
cubes = [cube ** 3 for cube in range(1, 11)]
print(cubes)