# partir una lista (slide) funciona con indice 0
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
# Si se omite el primer valor, comienza desde el primero
print(players[:3])
# Si omitimos el segundo valor, termina hasta el final
print(players[2:])
# Podemos hacer uso de los negativos para mostrar los ultimos
print(players[-3:])
# Si agregamos el tercer valor, le decimos de cuanto en cuanto ir
print(players[0:4:3])

# Recorrer un slide con un for
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())