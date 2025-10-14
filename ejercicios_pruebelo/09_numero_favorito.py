numeros_favoritos = {
    'naomi': [7, 25, 31],
    'diego': [13, 31, 4],
    'carlos': [20, 3, 56]
}

for nombre, numeros in numeros_favoritos.items():
    print(f"{nombre.title()}, tus numeros favoritos son:", end=" ")
    for numero in numeros:
        print(f"{numero}", end=" ")
    print("")